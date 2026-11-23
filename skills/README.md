# AIPF Specialist Suite — prototype skills

## First usable prototype: UI/UX

`aipf-ui-ux/SKILL.md` is an optional, single-file design specialist. It helps a coding AI **design while building**, then **critique and audit** meaningful results. It does not replace AIPF v8.10.1, install dependencies, create a second project state, or publish anything.

When a coding assistant supports `SKILL.md` skills, point it to this file through that assistant's normal skill-loading mechanism. For catalog-backed recommendations, the assistant must also be able to read this repository and run `python scripts/search_catalog.py` from its root. The specialist still provides general, project-grounded design guidance when that search is unavailable; it must say that no catalog lookup was performed.

Example request: **"Use the AIPF UI/UX specialist to improve this dashboard's hierarchy and mobile layout without changing its functionality. Use the existing brand tokens and inspect the rendered result if tools are available."**

The catalog is reference-only: search results are recommendations, not permission to copy fonts, photos, brand assets or third-party code. No installation, runtime deployment, or independent visual-performance improvement is implied by this prototype.

Smoke checks: `python -m unittest discover -s tests -v`.
