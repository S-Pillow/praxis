#!/usr/bin/env python3
"""Read-only, dependency-free catalog retrieval for AIPF-governed work.

This utility retrieves source-backed design knowledge. It does NOT authorize
changes, select an AIPF path, install skills, grant asset rights, or certify quality.
A Prompt Agent must select approved guidance and transport required operational
values into an accessible Builder Payload when a distinct Builder exists.
"""
import argparse
import json
import math
import pathlib
import re
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
ENTRIES_DIR = ROOT / "catalog" / "entries"
TOKEN_PATTERN = re.compile(r"[a-z0-9]+")
STOP = {"the", "and", "for", "with", "that", "this", "from", "into", "like", "use", "a", "an", "of", "in", "on", "to", "ui", "ux", "design"}

def terms(text):
    return [term for term in TOKEN_PATTERN.findall(str(text).lower()) if term not in STOP]

def load_catalog(directory=ENTRIES_DIR):
    """Load all production entry files; starter is illustrative, not canonical."""
    result = []
    for path in sorted(pathlib.Path(directory).glob("*.json")):
        if path.name == "starter.json":
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            raise ValueError(f"Entry file must be a JSON list: {path}")
        result.extend(data)
    ids = [entry["catalog_id"] for entry in result]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate catalog IDs detected")
    return result

def entry_fields(entry):
    """Token weights emphasize original name and type over free-text matches."""
    return (
        terms(entry["original_name"]) * 8
        + terms(entry["entry_type"]) * 3
        + [t for keyword in entry.get("keywords", []) for t in terms(keyword)] * 2
        + terms(entry.get("description", ""))
        + terms(" ".join(entry.get("compatibility_restrictions", [])))
    )

def rank_entries(query, entries, limit=5, entry_type=None, source=None, specialist_use=None):
    q = list(dict.fromkeys(terms(query)))
    if not q:
        return []
    filtered = [
        e for e in entries
        if (entry_type is None or e["entry_type"] == entry_type)
        and (source is None or e["source_repo"].lower() == source.lower())
        and (specialist_use is None or e["specialist_use"] in {specialist_use, "multiple"})
    ]
    if not filtered:
        return []
    docs = [Counter(entry_fields(e)) for e in filtered]
    df = Counter(term for document in docs for term in document)
    avg_length = sum(sum(d.values()) for d in docs) / len(docs)
    k1, b = 1.2, 0.75
    ranked = []
    for entry, doc in zip(filtered, docs):
        score = 0.0
        for term in q:
            tf = doc[term]
            if not tf:
                continue
            idf = math.log(1 + (len(filtered) - df[term] + 0.5) / (df[term] + 0.5))
            denom = tf + k1 * (1 - b + b * sum(doc.values()) / (avg_length or 1))
            score += idf * (tf * (k1 + 1)) / denom
        if score:
            ranked.append((round(score, 6), entry))
    ranked.sort(key=lambda pair: (-pair[0], pair[1]["catalog_id"]))
    return ranked[:max(0, limit)]

def reference(entry, score, include_tokens=False):
    """Operational summary for a Prompt Agent; never implies Builder access."""
    fields = [
        "catalog_id", "entry_type", "original_name", "description",
        "source_repo", "source_url", "source_ref", "source_path_or_key",
        "evidence_status", "source_license", "asset_license_status",
        "redistribution_status", "preview_reference", "compatibility_restrictions",
        "platforms", "specialist_use",
    ]
    result = {field: entry.get(field) for field in fields}
    result["relevance_score"] = score
    if include_tokens:
        result["design_tokens"] = entry.get("design_tokens")
    return result

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("query", help="Search for a product, visual style, palette, font, pattern, etc.")
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--type", choices=[
        "theme", "style", "template", "palette", "font_pairing",
        "font_family", "design_system", "example", "guideline",
        "anti_pattern", "motion_preset", "chart_type", "illustration_style",
        "design_knowledge", "brand_reference",
    ])
    ap.add_argument("--source", help="Exact owner/repository name")
    ap.add_argument("--specialist-use", choices=["build", "critique", "audit", "reference"])
    ap.add_argument("--include-tokens", action="store_true", help="Include actual source tokens, if imported")
    args = ap.parse_args()
    matches = rank_entries(
        args.query, load_catalog(), limit=args.limit,
        entry_type=args.type, source=args.source, specialist_use=args.specialist_use
    )
    output = {
        "query": args.query,
        "results": [reference(item, score, args.include_tokens) for score, item in matches],
        "scope_note": (
            "Catalog results are non-authoritative references. Prompt Agent must verify "
            "approved requirements, source provenance, Builder accessibility, license "
            "boundaries and the relevant AIPF authorization unit. This search performs "
            "no build, deployment, asset bundling or visual validation."
        ),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
