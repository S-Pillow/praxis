#!/usr/bin/env python3
"""Reproducible retrieval-quality benchmark for the UI/UX Specialist lookup.

Runs the existing retrieval commands unchanged as subprocesses, validates their
JSON output and scores it against frozen case judgments. Read-only: it never
modifies the catalog, the retrieval scripts or any project.
"""
import argparse
import hashlib
import json
import math
import pathlib
import platform
import re
import subprocess
import sys

if __package__:
    from .search_catalog import load_catalog
else:
    from search_catalog import load_catalog

ROOT = pathlib.Path(__file__).resolve().parents[1]
BENCH_DIR = ROOT / "research" / "evaluations" / "retrieval-benchmark"
CASES = BENCH_DIR / "cases.json"
POST_HOC = BENCH_DIR / "post-hoc-judgments.json"
TOOLS = {
    "recommend": ("scripts/recommend_design.py", "references"),
    "search": ("scripts/search_catalog.py", "results"),
}
SPLITS = ("historical", "development", "held_out")


def sha256_file(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def load_json(path):
    return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))


def catalog_identity(root=ROOT):
    """Hash of every production entry file, in load order (starter excluded)."""
    digest = hashlib.sha256()
    files = sorted(p for p in (root / "catalog" / "entries").glob("*.json") if p.name != "starter.json")
    records = 0
    for path in files:
        data = path.read_bytes()
        digest.update(path.name.encode() + b"\0" + data + b"\0")
        records += len(json.loads(data))
    return {"files": len(files), "records": records, "sha256": digest.hexdigest()}


def catalog_index(root=ROOT):
    return {entry["catalog_id"]: entry for entry in load_catalog(root / "catalog" / "entries")}


def git_revision(root=ROOT):
    try:
        rev = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, text=True,
                             capture_output=True, check=True).stdout.strip()
        tracked = subprocess.run(["git", "status", "--porcelain", "--untracked-files=no",
                                  "--", "scripts/recommend_design.py", "scripts/search_catalog.py", "catalog"],
                                 cwd=root, text=True, capture_output=True, check=True).stdout.strip()
        return {"head": rev, "retrieval_and_catalog_modified": bool(tracked)}
    except (OSError, subprocess.CalledProcessError):
        return {"head": None, "retrieval_and_catalog_modified": None}


def build_argv(case, python=sys.executable):
    script, _ = TOOLS[case["tool"]]
    return [python, script, case["query"], *case["args"]]


def run_command(case, root=ROOT, python=sys.executable, timeout=120):
    argv = build_argv(case, python)
    proc = subprocess.run(argv, cwd=root, capture_output=True, timeout=timeout)
    return {
        "argv": ["python3", *argv[1:]],
        "exit_code": proc.returncode,
        "stdout": proc.stdout.decode("utf-8", errors="replace"),
        "stderr": proc.stderr.decode("utf-8", errors="replace"),
    }


def parse_output(tool, raw):
    """Classify a run as ok, empty, command_failed or malformed.

    Only a zero exit with well-formed JSON whose result list contains valid
    items counts as a recommendation. Anything incomplete is malformed.
    """
    if raw["exit_code"] != 0:
        return "command_failed", [], [f"exit code {raw['exit_code']}"]
    try:
        data = json.loads(raw["stdout"])
    except (TypeError, ValueError) as exc:
        return "malformed", [], [f"invalid JSON: {exc}"]
    key = TOOLS[tool][1]
    if not isinstance(data, dict) or not isinstance(data.get(key), list):
        return "malformed", [], [f"missing list field '{key}'"]
    problems, items = [], []
    for position, item in enumerate(data[key], 1):
        if not isinstance(item, dict):
            problems.append(f"item {position} is not an object")
            continue
        cid, score = item.get("catalog_id"), item.get("relevance_score")
        if not isinstance(cid, str) or not cid:
            problems.append(f"item {position} has no catalog_id")
        if isinstance(score, bool) or not isinstance(score, (int, float)) or not math.isfinite(score):
            problems.append(f"item {position} has no numeric relevance_score")
        items.append(item)
    if problems:
        return "malformed", [], problems
    return ("ok" if items else "empty"), items, []


def rule_matches(rule, catalog_id, entry):
    if catalog_id in rule.get("ids", []):
        return True
    if entry is None:
        return False
    types = rule.get("entry_types")
    if types and entry.get("entry_type") not in types:
        return False
    name_re, text_re = rule.get("name_regex"), rule.get("text_regex")
    if not name_re and not text_re:
        return bool(types)
    name = str(entry.get("original_name", ""))
    text = " ".join([name, str(entry.get("description", "")),
                     " ".join(map(str, entry.get("compatibility_restrictions", [])))])
    return bool((name_re and re.search(name_re, name)) or (text_re and re.search(text_re, text)))


def grade_for(case, catalog_id, post_hoc):
    for grade, ids in case["judgments"].items():
        if catalog_id in ids:
            return int(grade), "frozen"
    extra = post_hoc.get(case["id"], {}).get(catalog_id)
    if extra is not None:
        return int(extra["grade"]), "post_hoc"
    return None, "unjudged"


def score_case(case, raw, rules, index, post_hoc):
    status, items, problems = parse_output(case["tool"], raw)
    results = []
    for rank, item in enumerate(items, 1):
        cid = item["catalog_id"]
        entry = index.get(cid)
        grade, source = grade_for(case, cid, post_hoc)
        conflicts = [name for name in case["conflict_rules"] if rule_matches(rules[name], cid, entry)]
        results.append({
            "rank": rank,
            "catalog_id": cid,
            "original_name": item.get("original_name"),
            "entry_type": item.get("entry_type"),
            "role": item.get("role"),
            "relevance_score": item["relevance_score"],
            "grade": grade,
            "grade_source": source,
            "conflicts": conflicts,
            "in_catalog": entry is not None,
            "evidence_status": item.get("evidence_status"),
            "redistribution_status": item.get("redistribution_status"),
            "asset_license_status": item.get("asset_license_status"),
        })
    graded = [r for r in results if r["grade"] is not None]
    actionable = [r["rank"] for r in graded if r["grade"] == 3]
    scored = {
        "id": case["id"],
        "origin": case["origin"],
        "split": case["split"],
        "role": case["role"],
        "tool": case["tool"],
        "argv": raw["argv"],
        "exit_code": raw["exit_code"],
        "stderr_bytes": len(raw["stderr"].encode()),
        "status": status,
        "problems": problems,
        "result_count": len(results),
        "results": results,
        "relevant_in_top3": sum(1 for r in graded if r["rank"] <= 3 and r["grade"] >= 2),
        "first_actionable_rank": min(actionable) if actionable else None,
        "conflict_count": sum(1 for r in results if r["conflicts"]),
        "useful": any(r["grade"] >= 2 for r in graded),
        "useful_frozen_only": any(r["grade"] >= 2 for r in graded if r["grade_source"] == "frozen"),
        "unjudged": sum(1 for r in results if r["grade_source"] == "unjudged"),
        "post_hoc": sum(1 for r in results if r["grade_source"] == "post_hoc"),
    }
    if case["expect_empty"]:
        scored["abstention"] = "correct" if status == "empty" else (
            "incorrect" if status == "ok" else "not_assessable")
    elif status == "empty":
        scored["abstention"] = "acceptable_empty" if case["empty_acceptable"] else "unacceptable_empty"
    else:
        scored["abstention"] = None
    retained = case.get("retained_output")
    if retained:
        expected = (BENCH_DIR / retained).read_text(encoding="utf-8")
        scored["matches_retained_output"] = raw["stdout"] == expected
    return scored


def summarize(scored):
    applicable = [s for s in scored if s["abstention"] not in ("correct", "incorrect", "not_assessable")]
    follow = [s for s in applicable if s["role"] == "follow_up"]
    ids = lambda rows: [s["id"] for s in rows]
    return {
        "cases": len(scored),
        "status": {k: ids([s for s in scored if s["status"] == k])
                   for k in ("ok", "empty", "command_failed", "malformed")},
        "relevant_in_top3": {
            "cases_with_at_least_one": ids([s for s in applicable if s["relevant_in_top3"]]),
            "denominator": len(applicable),
            "per_case": {s["id"]: s["relevant_in_top3"] for s in applicable},
        },
        "first_actionable_rank": {
            "per_case": {s["id"]: s["first_actionable_rank"] for s in applicable},
            "cases_with_actionable": len([s for s in applicable if s["first_actionable_rank"]]),
            "denominator": len(applicable),
        },
        "constraint_conflicts": {
            "conflicting_results": sum(s["conflict_count"] for s in scored),
            "returned_results": sum(s["result_count"] for s in scored),
            "per_case": {s["id"]: s["conflict_count"] for s in scored if s["conflict_count"]},
        },
        "useful_query_coverage": {
            "useful": ids([s for s in applicable if s["useful"]]),
            "not_useful": ids([s for s in applicable if not s["useful"]]),
            "useful_frozen_judgments_only": ids([s for s in applicable if s["useful_frozen_only"]]),
            "denominator": len(applicable),
        },
        "abstention": {
            "expected_empty": {s["id"]: s["abstention"] for s in scored if s["abstention"] in ("correct", "incorrect", "not_assessable")},
            "empty_results": {s["id"]: s["abstention"] for s in scored if s["abstention"] in ("acceptable_empty", "unacceptable_empty")},
        },
        "follow_up_usefulness": {
            "useful": ids([s for s in follow if s["useful"]]),
            "denominator": len(follow),
            "case_ids": ids(follow),
        },
        "judgment_coverage": {
            "returned_results": sum(s["result_count"] for s in scored),
            "frozen": sum(s["result_count"] - s["unjudged"] - s["post_hoc"] for s in scored),
            "post_hoc": sum(s["post_hoc"] for s in scored),
            "unjudged": sum(s["unjudged"] for s in scored),
        },
    }


def run_benchmark(cases_path=CASES, post_hoc_path=POST_HOC, splits=SPLITS, runner=run_command, root=ROOT):
    fixture = load_json(cases_path)
    post_hoc = load_json(post_hoc_path).get("judgments", {}) if pathlib.Path(post_hoc_path).exists() else {}
    index = catalog_index(root)
    cases = [c for c in fixture["cases"] if c["split"] in splits]
    scored = [score_case(c, runner(c), fixture["conflict_rules"], index, post_hoc) for c in cases]
    return {
        "benchmark": fixture["benchmark"],
        "cases_sha256": sha256_file(cases_path),
        "post_hoc_sha256": sha256_file(post_hoc_path) if pathlib.Path(post_hoc_path).exists() else None,
        "environment": {
            "repository": git_revision(root),
            "catalog": catalog_identity(root),
            "python": platform.python_version(),
            "retrieval_scripts_sha256": {name: sha256_file(root / path) for name, (path, _) in TOOLS.items()},
        },
        "summary": {split: summarize([s for s in scored if s["split"] == split]) for split in splits},
        "summary_all_non_held_out": summarize([s for s in scored if s["split"] != "held_out"]),
        "cases": scored,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--cases", default=str(CASES))
    ap.add_argument("--post-hoc", default=str(POST_HOC))
    ap.add_argument("--split", action="append", choices=SPLITS,
                    help="Restrict to a split (repeatable). Default: all splits.")
    ap.add_argument("--output", help="Write full results JSON to this path")
    ap.add_argument("--raw", action="store_true", help="Include raw stdout of every command in the output")
    ap.add_argument("--check-historical", action="store_true",
                    help="Exit 1 if any historical rerun differs from its retained output")
    args = ap.parse_args()
    raws = {}

    def recording_runner(case):
        raw = run_command(case)
        raws[case["id"]] = raw["stdout"]
        return raw

    result = run_benchmark(args.cases, args.post_hoc, tuple(args.split or SPLITS), recording_runner)
    if args.raw:
        result["raw_stdout"] = raws
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=False) + "\n"
    if args.output:
        pathlib.Path(args.output).write_text(text, encoding="utf-8")
    print(json.dumps({"cases_sha256": result["cases_sha256"], "summary": result["summary"]}, ensure_ascii=False, indent=2))
    drift = [c["id"] for c in result["cases"] if c.get("matches_retained_output") is False]
    if args.check_historical and drift:
        print(f"historical drift: {', '.join(drift)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
