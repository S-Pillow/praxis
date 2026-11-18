"""Pinned MengTo SKILL.md metadata extractor; never copies runnable skills/assets."""
import argparse
import json
import pathlib
import re
import subprocess

SHA = "3cc93458c4949c39a04e938ea7892a1d6d3d40bf"
ROOT = pathlib.Path(__file__).resolve().parents[1]
DEST = ROOT / "catalog/entries/mengto-design-knowledge.json"

def parse(text):
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    front = match.group(1) if match else ""
    fields = {}
    for key in ("name", "description"):
        m = re.search(rf"(?m)^{key}:\s*(.+)$", front)
        if m:
            fields[key] = m.group(1).strip().strip('"').strip("'")
    body = text[match.end():] if match else text
    for line in body.splitlines():
        line = line.strip()
        if len(line) > 32 and not line.startswith(("#", "!", "|", "`", "<", "-")):
            fields.setdefault("description", line[:1000])
            break
    return fields

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--upstream-root", type=pathlib.Path, required=True)
    args = p.parse_args()
    root = args.upstream_root.resolve()
    rev = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    if rev != SHA:
        raise SystemExit(f"Unexpected source SHA {rev}")
    data = json.loads(DEST.read_text(encoding="utf-8"))
    if len(data) != 123:
        raise SystemExit("Expected 123 selected MengTo knowledge records")
    for entry in data:
        if entry["source_ref"] != SHA:
            raise SystemExit("Source ref mismatch")
        rel = pathlib.PurePosixPath(entry["source_path_or_key"])
        if rel.is_absolute() or ".." in rel.parts or rel.name != "SKILL.md":
            raise SystemExit(f"Unsafe source path {rel}")
        path = (root / str(rel)).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise SystemExit(f"Missing skill source {rel}")
        fields = parse(path.read_text(encoding="utf-8"))
        entry["original_name"] = fields.get("name") or entry["original_name"]
        entry["description"] = (fields.get("description") or entry["original_name"])[:1000]
        entry["normalized_name"] = entry["original_name"]
        entry["evidence_status"] = "source_inspected"
        entry["review_notes"] = (
            f"Pinned SKILL.md description extracted from {SHA}:{rel}; "
            "original runnable skill, previews and third-party demos NOT imported; "
            "tool and distribution compatibility need individual review."
        )
    DEST.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print("Enriched 123 MengTo source-skill knowledge references")

if __name__ == "__main__":
    main()
