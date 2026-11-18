# Catalog inventory and verification — 2026-11-18

**Current scope:** five pinned upstream repositories, 19 main inventory files, **1,927 non-starter records**, plus nine earlier illustrative starter records that are **excluded** from production counts. The import represents an inventory snapshot, not production-ready bundled content.

| Source | Records | Verified depth |
|---|---:|---|
| Hallmark | 50 themes | Parsed theme index, material descriptions and preview references; CSS token files and individual asset rights not yet extracted/cleared |
| UI UX Pro Max | 1,116 rows from 12 CSVs | Parsed individual dataset rows (selected fields + source row identity); exact unselected columns remain referenced in pinned source |
| Open Design Agent Kit | 702 entries: 198 systems, 114 templates, 193 examples, 197 skills | Pinned Git tree path inventory; **individual token JSON and example/template bodies not yet extracted**. Treat as candidate records, not fully inspected content |
| MengTo Skills | 14 illustration stylecards | Parsed style.json, palette and example references; SVG example rights not independently cleared |
| Impeccable | 45 design-knowledge references | Pinned reference path inventory; selected critique/audit methods previously inspected, no wholesale adoption |
| **Total** | **1,927** | **Mixed evidence depth; review each entry state** |

Cross-source overlap: 8 normalized-name matches are recorded in `catalog/relations/overlaps.json` as **candidate** relationships; no entries have been deleted, merged or declared visually equivalent.

## How to validate

Run:
```bash
python -m unittest discover -s tests -v
```

The GitHub Actions workflow `Catalog validation` runs this command with read-only permissions. Passing checks demonstrate integrity of **catalog structure and source identity**; they do NOT establish visual performance, upstream content correctness, legal clearance or individual asset provenance.

## Human/agent workflow

See `research/prompt-agent-builder-interface.md`. AIPF Prompt Agent controls route, approvals, scope, and reconciliation. A distinct Builder executes only the transported, accessible operational payload, using selected catalog entries as non-authoritative guidance.

## Known follow-up gaps

- Enrich 198 Open Design design system token JSONs; review 114 template bodies, 193 example manifests and 197 skills for descriptions/references (some are non-UI).
- Extract Hallmark theme CSS token values and map local previews to specific originals/licenses.
- Preserve remaining UI UX Pro Max CSV columns during next normalization pass and verify per-font/icon licensing.
- Independently verify each external/photo/font/demo asset as needed for a redistribution proposal; block all bundles while not cleared.
- Review eight overlap candidates semantically/visually (not just name equivalence).
- Independently evaluate specialist methods against AIPF Chapter 14 with observed baseline tasks.
