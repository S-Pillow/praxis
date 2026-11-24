# AIPF Specialist Suite — prototype skills

## First usable prototype: UI/UX

`aipf-ui-ux/SKILL.md` is an optional, single-file design specialist. It helps a coding AI **design while building**, then **critique and audit** meaningful results. It does not replace AIPF v8.10.1, install dependencies, create a second project state, or publish anything.

When a coding assistant supports `SKILL.md` skills, point it to this file through that assistant's normal skill-loading mechanism. When the assistant has access to the repository and can run commands, **it automatically calls** `python scripts/recommend_design.py "<normal user UI request>" --mode build` from the repository root. This performs a short read-only lookup of the full catalog. The user does **not** run Python, launch the Design Index, choose templates, or copy a prompt. The assistant interprets the retrieved candidates and does the authorized UI work; no independent skill execution or silent background service is implied.

If the catalog or command runner is unavailable, the assistant works from accessible approved project context and must not claim a lookup occurred. The Design Index and its copy-prompt button remain optional for browsing and manual handoffs.

Example request: **"Use the AIPF UI/UX specialist to improve this dashboard's hierarchy and mobile layout without changing its functionality. Use the existing brand tokens and inspect the rendered result if tools are available."**

The catalog is reference-only: search results are recommendations, not permission to copy fonts, photos, brand assets or third-party code. No installation, runtime deployment, or independent visual-performance improvement is implied by this prototype.

Smoke checks: `python -m unittest discover -s tests -v`.
