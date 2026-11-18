"""Enrich source-path inventory with exact upstream descriptions (no binary assets).

Uses a pinned local checkout of feimacode/open-design-agent-kit. Does not copy
HTML demo bodies, images, fonts, screenshots, scripts, or sample binary assets.
"""
import argparse
import json
import pathlib
import re
import subprocess

EXPECTED = "1b3832c3452720f028a96b1bdab805ecc1aa3213"
ROOT = pathlib.Path(__file__).resolve().parents[1]
GROUPS = {
    "templates": ("catalog/entries/open-design-templates.json", 114),
    "examples": ("catalog/entries/open-design-examples.json", 193),
    "skills": ("catalog/entries/open-design-skills.json", 197),
}

def parse_skill(text):
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    front = match.group(1) if match else ""
    fields = {}
    for field in ("name", "description"):
        found = re.search(rf"(?m)^{field}:\s*(.+)$", front)
        if found:
            fields[field] = found.group(1).strip().strip('"').strip("'")
    body = text[match.end():] if match else text
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", body)]
    for para in paras:
        if para and not para.startswith(("#", "`", "---", "|", "![", "<")) and len(para) >= 25:
            fields.setdefault("description", para[:900])
            break
    return fields

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--upstream-root", type=pathlib.Path, required=True)
    args = ap.parse_args()
    root = args.upstream_root.resolve()
    actual = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    if actual != EXPECTED:
        raise SystemExit(f"Incorrect upstream commit {actual}; expected {EXPECTED}")
    total = 0
    for group, (local_path, expected_count) in GROUPS.items():
        dest = ROOT / local_path
        rows = json.loads(dest.read_text(encoding="utf-8"))
        if len(rows) != expected_count:
            raise SystemExit(f"{group}: expected {expected_count}, found {len(rows)}")
        for e in rows:
            if e["source_ref"] != EXPECTED:
                raise SystemExit(f"Unpinned entry {e['catalog_id']}")
            relative = pathlib.PurePosixPath(e["source_path_or_key"])
            if relative.is_absolute() or ".." in relative.parts:
                raise SystemExit(f"Unsafe source path {relative}")
            path = (root / str(relative)).resolve()
            if not path.is_relative_to(root) or not path.is_file():
                raise SystemExit(f"Missing upstream source {relative}")
            if group == "examples":
                source = json.loads(path.read_text(encoding="utf-8"))
                e["original_name"] = source.get("title") or source.get("name") or e["original_name"]
                q = source.get("od", {}).get("useCase", {}).get("query", {})
                example = (q.get("en", "") if isinstance(q, dict) else "") or ""
                e["description"] = source.get("description") or example or e["original_name"]
                e["preview_reference"] = (
                    f"https://github.com/feimacode/open-design-agent-kit/blob/{EXPECTED}/"
                    f"{str(relative.parent)}/example.html"
                ) if (path.parent / "example.html").exists() else None
                e["review_notes"] = "Pinned open-design.json read; example is reference only, no HTML/assets copied. Embedded third-party assets remain unreviewed."
            else:
                skill = parse_skill(path.read_text(encoding="utf-8"))
                e["original_name"] = skill.get("name") or e["original_name"]
                e["description"] = skill.get("description") or e["original_name"]
                e["review_notes"] = "Pinned SKILL.md description extracted; skill code, dependent scripts, demos and media NOT bundled; not a runnable AIPF specialist."
            e["normalized_name"] = e["original_name"]
            e["evidence_status"] = "source_inspected"
            e["compatibility_restrictions"] = [
                c for c in e.get("compatibility_restrictions", [])
                if c != "Source detail not yet extracted"
            ]
            e["redistribution_status"] = "reference_only"
            total += 1
        dest.write_text(json.dumps(rows, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
        print(f"{group}: enriched {len(rows)}")
    print(f"Source descriptions enriched: {total}, upstream={actual}")

if __name__ == "__main__":
    main()
