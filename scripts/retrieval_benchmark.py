#!/usr/bin/env python3
"""Reproducible retrieval-quality benchmark for the UI/UX Specialist lookup.

Runs a retrieval implementation as subprocesses, validates its JSON output and
scores it against frozen case judgments. Read-only: it never modifies the
catalog, the retrieval scripts or any project.

Implementations: ``working-tree`` (scripts/ in this checkout), ``v0.2`` (the
pinned copies in research/evaluations/retrieval-benchmark/reference-v0.2),
``specialist-uiux-02`` or ``specialist-uiux-03`` (the pinned experiment copies
in reference-specialist-uiux-02 and reference-specialist-uiux-03), each run
against this checkout's catalog.
"""
import argparse
import hashlib
import json
import math
import pathlib
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter

if __package__:
    from .search_catalog import load_catalog
else:
    from search_catalog import load_catalog

ROOT = pathlib.Path(__file__).resolve().parents[1]
BENCH_DIR = ROOT / "research" / "evaluations" / "retrieval-benchmark"
CASES = BENCH_DIR / "cases.json"
POST_HOC = BENCH_DIR / "post-hoc-judgments.json"
REFERENCE_V02 = BENCH_DIR / "reference-v0.2"
REFERENCE_UIUX02 = BENCH_DIR / "reference-specialist-uiux-02"
REFERENCE_UIUX03 = BENCH_DIR / "reference-specialist-uiux-03"
PINNED = {"v0.2": REFERENCE_V02, "specialist-uiux-02": REFERENCE_UIUX02, "specialist-uiux-03": REFERENCE_UIUX03}
TOOLS = {
    "recommend": ("scripts/recommend_design.py", "references"),
    "search": ("scripts/search_catalog.py", "results"),
}
SPLITS = ("historical", "development", "held_out")
IMPLEMENTATIONS = ("working-tree", *PINNED)
REPRODUCTION_IGNORED = {("environment", "repository"), ("environment", "python")}


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


class Implementation:
    """A directory containing scripts/ and catalog/ that commands run from."""

    def __init__(self, name, root=ROOT, scripts_dir=None):
        if name not in IMPLEMENTATIONS and scripts_dir is None:
            raise ValueError(f"unknown implementation {name!r}")
        self.name, self.root, self._tmp = name, root, None
        self.source = pathlib.Path(scripts_dir) if scripts_dir else PINNED.get(name)
        self.workdir = root

    def __enter__(self):
        if self.source is not None:
            self._tmp = tempfile.TemporaryDirectory(prefix="retrieval-impl-")
            work = pathlib.Path(self._tmp.name)
            (work / "scripts").mkdir()
            for script, _ in TOOLS.values():
                shutil.copyfile(self.source / pathlib.Path(script).name, work / script)
            (work / "catalog").symlink_to(self.root / "catalog", target_is_directory=True)
            self.workdir = work
        return self

    def __exit__(self, *exc):
        if self._tmp:
            self._tmp.cleanup()
        self.workdir = self.root

    def scripts_sha256(self):
        return {name: sha256_file(self.workdir / path) for name, (path, _) in TOOLS.items()}


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


def load_judgment_sets(post_hoc_path=POST_HOC, extra_paths=()):
    """Ordered (label, judgments) pairs consulted after the frozen judgments."""
    sets = []
    if post_hoc_path and pathlib.Path(post_hoc_path).exists():
        sets.append(("post_hoc", load_json(post_hoc_path).get("judgments", {})))
    for path in extra_paths:
        data = load_json(path)
        sets.append((data["label"], data.get("judgments", {})))
    return sets


def grade_for(case, catalog_id, judgment_sets):
    for grade, ids in case["judgments"].items():
        if catalog_id in ids:
            return int(grade), "frozen"
    for label, judgments in judgment_sets:
        extra = judgments.get(case["id"], {}).get(catalog_id)
        if extra is not None:
            return int(extra["grade"]), label
    return None, "unjudged"


def score_case(case, raw, rules, index, judgment_sets):
    if isinstance(judgment_sets, dict):
        judgment_sets = [("post_hoc", judgment_sets)]
    status, items, problems = parse_output(case["tool"], raw)
    results = []
    for rank, item in enumerate(items, 1):
        cid = item["catalog_id"]
        entry = index.get(cid)
        grade, source = grade_for(case, cid, judgment_sets)
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
    frozen = [r for r in graded if r["grade_source"] == "frozen"]
    actionable = [r["rank"] for r in graded if r["grade"] == 3]
    actionable_frozen = [r["rank"] for r in frozen if r["grade"] == 3]
    sources = Counter(r["grade_source"] for r in results)
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
        "useful_frozen_only": any(r["grade"] >= 2 for r in frozen),
        "unjudged": sources.get("unjudged", 0),
        "post_hoc": sources.get("post_hoc", 0),
        "relevant_returned": sum(1 for r in graded if r["grade"] >= 2),
        "relevant_returned_frozen_only": sum(1 for r in frozen if r["grade"] >= 2),
        "first_actionable_rank_frozen_only": min(actionable_frozen) if actionable_frozen else None,
        "grade_sources": dict(sorted(sources.items())),
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
    returned = sum(s["result_count"] for s in scored)
    conflicting = sum(s["conflict_count"] for s in scored)
    sources = Counter()
    for s in scored:
        sources.update(s["grade_sources"])
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
            "per_case_frozen_only": {s["id"]: s["first_actionable_rank_frozen_only"] for s in applicable},
        },
        "constraint_conflicts": {
            "conflicting_results": conflicting,
            "returned_results": returned,
            "per_case": {s["id"]: s["conflict_count"] for s in scored if s["conflict_count"]},
            "rate": round(conflicting / returned, 4) if returned else None,
            "cases_with_conflict": ids([s for s in scored if s["conflict_count"]]),
        },
        "useful_query_coverage": {
            "useful": ids([s for s in applicable if s["useful"]]),
            "not_useful": ids([s for s in applicable if not s["useful"]]),
            "useful_frozen_judgments_only": ids([s for s in applicable if s["useful_frozen_only"]]),
            "denominator": len(applicable),
            "excluded_expected_empty": ids([s for s in scored if s not in applicable]),
        },
        "relevant_returned": {
            "total": sum(s["relevant_returned"] for s in applicable),
            "total_frozen_only": sum(s["relevant_returned_frozen_only"] for s in applicable),
            "returned_in_scored_cases": sum(s["result_count"] for s in applicable),
            "per_case": {s["id"]: s["relevant_returned"] for s in applicable},
        },
        "returned_per_case": {s["id"]: s["result_count"] for s in scored},
        "abstention": {
            "expected_empty": {s["id"]: s["abstention"] for s in scored if s["abstention"] in ("correct", "incorrect", "not_assessable")},
            "empty_results": {s["id"]: s["abstention"] for s in scored if s["abstention"] in ("acceptable_empty", "unacceptable_empty")},
        },
        "follow_up_usefulness": {
            "useful": ids([s for s in follow if s["useful"]]),
            "denominator": len(follow),
            "case_ids": ids(follow),
            "useful_frozen_judgments_only": ids([s for s in follow if s["useful_frozen_only"]]),
        },
        "judgment_coverage": {
            "returned_results": returned,
            "frozen": sources.get("frozen", 0),
            "post_hoc": sources.get("post_hoc", 0),
            "unjudged": sources.get("unjudged", 0),
            "by_source": dict(sorted(sources.items())),
        },
    }


def run_benchmark(cases_path=CASES, post_hoc_path=POST_HOC, splits=SPLITS, runner=None, root=ROOT,
                  implementation="working-tree", extra_judgments=(), raw_stdout=False, scripts_dir=None):
    fixture = load_json(cases_path)
    judgment_sets = load_judgment_sets(post_hoc_path, extra_judgments)
    index = catalog_index(root)
    cases = [c for c in fixture["cases"] if c["split"] in splits]
    raws = {}
    with Implementation(implementation, root, scripts_dir) as impl:
        run = runner or (lambda case: run_command(case, impl.workdir))
        scored = []
        for case in cases:
            raw = run(case)
            raws[case["id"]] = raw["stdout"]
            scored.append(score_case(case, raw, fixture["conflict_rules"], index, judgment_sets))
        scripts = impl.scripts_sha256()
    result = {
        "benchmark": fixture["benchmark"],
        "cases_sha256": sha256_file(cases_path),
        "post_hoc_sha256": sha256_file(post_hoc_path) if post_hoc_path and pathlib.Path(post_hoc_path).exists() else None,
        "environment": {
            "repository": git_revision(root),
            "catalog": catalog_identity(root),
            "python": platform.python_version(),
            "retrieval_scripts_sha256": scripts,
            "implementation": implementation,
        },
        "summary": {split: summarize([s for s in scored if s["split"] == split]) for split in splits},
        "summary_all_non_held_out": summarize([s for s in scored if s["split"] != "held_out"]),
        "cases": scored,
    }
    if extra_judgments:
        result["additional_judgments"] = [
            {"label": label, "path": str(pathlib.Path(path).resolve().relative_to(root)), "sha256": sha256_file(path)}
            for (label, _), path in zip(judgment_sets[-len(extra_judgments):], extra_judgments)
        ]
    if raw_stdout:
        result["raw_stdout"] = raws
    return result


def reproduction_differences(expected, actual, path=()):
    """Paths where ``actual`` does not reproduce every field of ``expected``.

    New fields in ``actual`` are allowed; the recorded checkout revision and
    Python patch version are informational and ignored.
    """
    if path in REPRODUCTION_IGNORED:
        return []
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            return [path]
        diffs = []
        for key, value in expected.items():
            if key not in actual:
                diffs.append(path + (key,))
            else:
                diffs.extend(reproduction_differences(value, actual[key], path + (key,)))
        return diffs
    if isinstance(expected, list):
        if not isinstance(actual, list) or len(expected) != len(actual):
            return [path]
        diffs = []
        for i, (a, b) in enumerate(zip(expected, actual)):
            diffs.extend(reproduction_differences(a, b, path + (i,)))
        return diffs
    return [] if expected == actual else [path]


def _case_view(case):
    return {
        "status": case["status"],
        "returned": [r["catalog_id"] for r in case["results"]],
        "grades": [r["grade"] for r in case["results"]],
        "useful": case["useful"],
        "useful_frozen_only": case["useful_frozen_only"],
        "relevant_returned": case.get("relevant_returned", sum(1 for r in case["results"] if (r["grade"] or 0) >= 2)),
        "first_actionable_rank": case["first_actionable_rank"],
        "conflict_count": case["conflict_count"],
        "conflicting_ids": [r["catalog_id"] for r in case["results"] if r["conflicts"]],
        "abstention": case["abstention"],
    }


def compare(base, candidate):
    """Case-level and split-level differences between two benchmark runs."""
    base_cases = {c["id"]: c for c in base["cases"]}
    rows, newly_useful, regressed = [], [], []
    for case in candidate["cases"]:
        if case["id"] not in base_cases:
            continue
        before, after = _case_view(base_cases[case["id"]]), _case_view(case)
        reasons = []
        if before["useful"] and not after["useful"]:
            reasons.append("lost usefulness")
        if after["conflict_count"] > before["conflict_count"]:
            reasons.append("more conflicts")
        if before["first_actionable_rank"] and (not after["first_actionable_rank"]
                                                or after["first_actionable_rank"] > before["first_actionable_rank"]):
            reasons.append("first actionable result lost or lower")
        if before["abstention"] == "correct" and after["abstention"] != "correct":
            reasons.append("abstention lost")
        if before["status"] in ("ok", "empty") and after["status"] not in ("ok", "empty"):
            reasons.append("command failed or malformed")
        improvements = []
        if after["useful"] and not before["useful"]:
            improvements.append("newly useful")
        if after["conflict_count"] < before["conflict_count"]:
            improvements.append("fewer conflicts")
        if after["first_actionable_rank"] and (not before["first_actionable_rank"]
                                               or after["first_actionable_rank"] < before["first_actionable_rank"]):
            improvements.append("first actionable result gained or higher")
        if after["abstention"] == "correct" and before["abstention"] != "correct":
            improvements.append("abstention gained")
        if "newly useful" in improvements:
            newly_useful.append(case["id"])
        if reasons:
            regressed.append(case["id"])
        rows.append({"id": case["id"], "split": case["split"], "before": before, "after": after,
                     "improvements": improvements, "regressions": reasons})
    splits = [s for s in SPLITS if s in candidate["summary"] and s in base["summary"]]
    metrics = {}
    for split in splits:
        b, a = base["summary"][split], candidate["summary"][split]
        view = lambda s: {
            "useful": f"{len(s['useful_query_coverage']['useful'])}/{s['useful_query_coverage']['denominator']}",
            "useful_frozen_only": f"{len(s['useful_query_coverage']['useful_frozen_judgments_only'])}/{s['useful_query_coverage']['denominator']}",
            "cases_with_relevant_in_top3": f"{len(s['relevant_in_top3']['cases_with_at_least_one'])}/{s['relevant_in_top3']['denominator']}",
            "cases_with_actionable": f"{s['first_actionable_rank']['cases_with_actionable']}/{s['first_actionable_rank']['denominator']}",
            "conflicting_results": f"{s['constraint_conflicts']['conflicting_results']}/{s['constraint_conflicts']['returned_results']}",
            "returned_results": s["constraint_conflicts"]["returned_results"],
            "abstention": s["abstention"],
            "follow_up_useful": f"{len(s['follow_up_usefulness']['useful'])}/{s['follow_up_usefulness']['denominator']}",
        }
        metrics[split] = {"before": view(b), "after": view(a)}
        for side, run in (("before", base), ("after", candidate)):
            cases = [c for c in run["cases"] if c["split"] == split and c["abstention"] not in ("correct", "incorrect", "not_assessable")]
            metrics[split][side]["relevant_returned"] = sum(_case_view(c)["relevant_returned"] for c in cases)
            metrics[split][side]["relevant_returned_frozen_only"] = sum(
                1 for c in cases for r in c["results"] if r["grade_source"] == "frozen" and r["grade"] >= 2)
    return {
        "before": {"implementation": base["environment"].get("implementation", "v0.2"),
                   "retrieval_scripts_sha256": base["environment"]["retrieval_scripts_sha256"]},
        "after": {"implementation": candidate["environment"].get("implementation"),
                  "retrieval_scripts_sha256": candidate["environment"]["retrieval_scripts_sha256"]},
        "catalog": candidate["environment"]["catalog"],
        "same_catalog": base["environment"]["catalog"] == candidate["environment"]["catalog"],
        "cases_sha256": candidate["cases_sha256"],
        "by_split": metrics,
        "newly_useful": newly_useful,
        "regressed": regressed,
        "cases": rows,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--cases", default=str(CASES))
    ap.add_argument("--post-hoc", default=str(POST_HOC))
    ap.add_argument("--judgments", action="append", default=[],
                    help="Additional labelled judgment file consulted after post-hoc judgments (repeatable)")
    ap.add_argument("--implementation", default="working-tree",
                    help="working-tree, a pinned implementation (" + ", ".join(PINNED) + "), or a label for --scripts-dir")
    ap.add_argument("--scripts-dir", help="Run recommend_design.py and search_catalog.py copied from this directory")
    ap.add_argument("--split", action="append", choices=SPLITS,
                    help="Restrict to a split (repeatable). Default: all splits.")
    ap.add_argument("--output", help="Write full results JSON to this path")
    ap.add_argument("--raw", action="store_true", help="Include raw stdout of every command in the output")
    ap.add_argument("--check-historical", action="store_true",
                    help="Exit 1 if any historical rerun differs from its retained output")
    ap.add_argument("--compare", nargs=2, metavar=("BEFORE", "AFTER"),
                    help="Compare two results files instead of running; writes to --output")
    args = ap.parse_args()
    if args.compare:
        text = json.dumps(compare(load_json(args.compare[0]), load_json(args.compare[1])), ensure_ascii=False, indent=2) + "\n"
        if args.output:
            pathlib.Path(args.output).write_text(text, encoding="utf-8")
        else:
            print(text, end="")
        return 0
    result = run_benchmark(args.cases, args.post_hoc, tuple(args.split or SPLITS),
                           implementation=args.implementation, extra_judgments=args.judgments,
                           raw_stdout=args.raw, scripts_dir=args.scripts_dir)
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
