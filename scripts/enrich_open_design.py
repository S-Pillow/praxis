"""Deterministically enrich catalog entries from a locally checked-out pinned upstream.

No network calls. No third-party binaries/previews copied. This script requires
the pinned upstream checkout and modifies only the catalog JSON file.
"""
import argparse
import json
import pathlib
import subprocess

EXPECTED_COMMIT = "1b3832c3452720f028a96b1bdab805ecc1aa3213"
ROOT = pathlib.Path(__file__).resolve().parents[1]
ENTRIES = ROOT / "catalog/entries/open-design-design-systems.json"

def named_tokens(section):
    if not isinstance(section, dict):
        return {}
    result = {}
    for entry in section.get("tokens", []):
        if isinstance(entry, dict) and entry.get("name") and "value" in entry:
            result[entry["name"]] = entry["value"]
    return result

def extract_tokens(source):
    type_data = source.get("type", {})
    grouped = {}
    for group in type_data.get("groups", []):
        name = group.get("name", "unnamed")
        grouped[name] = {
            style["name"]: {k: v for k, v in style.items() if k != "name"}
            for style in group.get("styles", []) if style.get("name")
        }
    data = {
        "color": named_tokens(source.get("color", {})),
        "font_families": type_data.get("families", {}),
        "typography": grouped,
        "spacing": named_tokens(source.get("spacing", {})),
        "radius": named_tokens(source.get("radius", {})),
        "shadow": named_tokens(source.get("shadow", {})),
        "type_metrics": named_tokens(source.get("typeMetrics", {})),
    }
    return data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--upstream-root", type=pathlib.Path, required=True)
    args = parser.parse_args()
    base = args.upstream_root.resolve()
    actual = subprocess.check_output(["git", "-C", str(base), "rev-parse", "HEAD"], text=True).strip()
    if actual != EXPECTED_COMMIT:
        raise SystemExit(f"Incorrect upstream commit: {actual}, expected {EXPECTED_COMMIT}")
    rows = json.loads(ENTRIES.read_text(encoding="utf-8"))
    if len(rows) != 198:
        raise SystemExit(f"Unexpected source inventory size {len(rows)}; expected 198")
    enriched = 0
    for row in rows:
        if row["source_ref"] != EXPECTED_COMMIT:
            raise SystemExit(f"Wrong pinned source for {row['catalog_id']}")
        rel = pathlib.PurePosixPath(row["source_path_or_key"])
        if rel.parts[:1] != ("claude-design-systems",) or rel.name != "tokens.json" or ".." in rel.parts:
            raise SystemExit(f"Unexpected upstream file path {rel}")
        path = (base / str(rel)).resolve()
        if not path.is_relative_to(base) or not path.is_file():
            raise SystemExit(f"Missing pinned source file {rel}")
        raw = json.loads(path.read_text(encoding="utf-8"))
        name = raw.get("name")
        if not name:
            raise SystemExit(f"Missing system name at {rel}")
        tokens = extract_tokens(raw)
        if not tokens["color"] or not tokens["font_families"]:
            raise SystemExit(f"Missing material design tokens at {rel}")
        row["original_name"] = name
        row["normalized_name"] = name
        row["description"] = f"Design system {name}; verified color, typography, spacing and shape guidance from pinned upstream token JSON."
        row["design_tokens"] = tokens
        row["review_notes"] = (
            f"Exact token values extracted from {EXPECTED_COMMIT}:{rel}; "
            f"upstream metadata {json.dumps(raw.get('meta', {}), sort_keys=True)}; "
            "brand/trademark/asset rights remain unresolved; no preview content copied."
        )
        row["evidence_status"] = "source_inspected"
        enriched += 1
    ENTRIES.write_text(json.dumps(rows, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Enriched {enriched}/{len(rows)} design systems from {actual}")

if __name__ == "__main__":
    main()
