"""Extract exact Hallmark CSS theme tokens from pinned upstream (no assets copied)."""
import argparse
import json
import pathlib
import re
import subprocess

PIN = "04977e15f3dfd6ee4b74c887dac3eb52665d6c92"
ROOT = pathlib.Path(__file__).resolve().parents[1]
DEST = ROOT / "catalog/entries/hallmark-themes.json"
TOKEN = re.compile(r"(--[a-zA-Z0-9_-]+)\s*:\s*([^;]+);")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--upstream-root", type=pathlib.Path, required=True)
    args = p.parse_args()
    source = args.upstream_root.resolve()
    revision = subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip()
    if revision != PIN:
        raise SystemExit(f"Unexpected upstream revision {revision}")
    rows = json.loads(DEST.read_text(encoding="utf-8"))
    if len(rows) != 50:
        raise SystemExit(f"Expected 50 themes; got {len(rows)}")
    for entry in rows:
        if entry["source_ref"] != PIN:
            raise SystemExit(f"Unexpected source ref {entry['catalog_id']}")
        slug = entry["catalog_id"].split(":")[-1]
        if not re.fullmatch(r"[a-z0-9-]+", slug):
            raise SystemExit(f"Unsafe theme slug {slug}")
        path = source / "site" / "themes" / slug / "tokens.css"
        if not path.is_file():
            raise SystemExit(f"No token file for {slug}")
        text = path.read_text(encoding="utf-8")
        values = {name: value.strip() for name, value in TOKEN.findall(text)}
        if not values:
            raise SystemExit(f"No CSS custom properties in {slug}")
        entry["design_tokens"] = values
        entry["review_notes"] = (
            f"CSS tokens extracted verbatim from {PIN}:site/themes/{slug}/tokens.css; "
            "theme images/photos/fonts and redistributed CSS remain separately license-gated."
        )
        entry["evidence_status"] = "source_inspected"
    DEST.write_text(json.dumps(rows, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Extracted pinned CSS token values for {len(rows)} Hallmark themes")

if __name__ == "__main__":
    main()
