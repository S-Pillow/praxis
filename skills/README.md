# Praxis — skills

For integrated governed development, select [Praxis](praxis/SKILL.md). Its framework selects the path before consulting the specialist below. The original UI/UX skill remains independently usable.

## UI/UX specialist (v0.3)

`aipf-ui-ux/SKILL.md` is an optional, single-file design specialist. It helps a coding AI **design while building**, then **critique and audit** meaningful results. It does not replace AIPF v8.10.1, install dependencies, create a second project state, or publish anything.

When a coding assistant supports `SKILL.md` skills, point it to this file through that assistant's normal skill-loading mechanism. When the assistant has access to the repository and can run commands, **it automatically calls** `python scripts/recommend_design.py "<normal user UI request>" --mode build` from the repository root. This performs a short read-only lookup of the full catalog. The user does **not** run Python, launch the Design Index, choose templates, or copy a prompt. The assistant interprets the retrieved candidates and does the authorized UI work; no independent skill execution or silent background service is implied.

If the catalog or command runner is unavailable, the assistant works from accessible approved project context and must not claim a lookup occurred. The Design Index and its copy-prompt button remain optional for browsing and manual handoffs.

Example request: **"Use the AIPF UI/UX specialist to improve this dashboard's hierarchy and mobile layout without changing its functionality. Use the existing brand tokens and inspect the rendered result if tools are available."**

The catalog is reference-only: search results are recommendations, not permission to copy fonts, photos, brand assets or third-party code. No installation, runtime deployment, or independent visual-performance improvement is implied by this release. See [CHANGELOG.md](../CHANGELOG.md) for v0.3 changes and known limitations.

Smoke checks: `python -m unittest discover -s tests -v`.

## Codex repository discovery (no manual catalog setup)

Codex discovers skills from `.agents/skills` in the repository hierarchy. This repository includes `.agents/skills/aipf-ui-ux/SKILL.md`, a **short adapter** that loads the single authoritative specialist at `skills/aipf-ui-ux/SKILL.md`; `AGENTS.md` scopes its intended use to material UI tasks. A coding agent launched inside this repository can choose the specialist from a normal user request and run the read-only catalog lookup itself.

**Boundary:** This is a **repository-local** discovery setup, not a system-wide installation or a guarantee that every AI tool will automatically activate it. To use the specialist from a different application repository, the target coding agent must be given access to this specialist and catalog through its supported skill/plugin mechanism. The full catalog remains in this repo and should not be copied into every target app by default.

These checks validate file discovery layout and executable retrieval, **not** whether a live Codex runtime selected and used the skill. That final activation test requires a Codex session with this checkout open.

## Architecture v0.1 (development candidate)

Use the integrated Praxis entry for material architecture decisions after canonical routing. See [architecture skill](architecture/SKILL.md), [decision index](architecture/INDEX.md) and the independent [capability index](../knowledge/capabilities/INDEX.md). No standalone installation or lookup command is required. Local B4 qualification is complete; [pre-release validation and release authorization remain pending](../docs/releases/1.1.0-pre-release.md).
