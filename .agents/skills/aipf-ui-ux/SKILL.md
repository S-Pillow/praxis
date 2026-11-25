---
name: aipf-ui-ux
description: "Use for material UI/UX tasks in this repository: create, improve, critique, or audit web/mobile/desktop interfaces using the AIPF UI/UX specialist and optional source-linked design catalog lookup. Do not use for unrelated coding."
---

# Repository-discoverable AIPF UI/UX specialist (v0.3)

This is a **discovery adapter** for coding agents; the full, single source of truth is `skills/aipf-ui-ux/SKILL.md` at the repository root. **Read that file and follow it before designing or editing a UI.** Do not treat this loader as a separate rule set or a replacement for AIPF v8.10.1.

When material catalog knowledge would help and the repository's command runner is accessible, **run the lookup yourself** from this repository root, with the user's actual UI request:

```bash
python scripts/recommend_design.py "Build an accessible financial dashboard" --mode build --platform web
```

Choose `build`, `critique`, or `audit` according to the task; do not invent a platform. The command returns a short **unapproved** shortlist from the existing catalog. Critically assess relevance and provenance, preserve current project/brand requirements, and do not copy third-party assets without clearance. Never ask the end user to run Python or open the catalog for an otherwise feasible task. Do not claim catalog retrieval or rendered validation if those tools were unavailable.

**Scope:** This adapter is discovered when the coding agent runs within this repository or a subfolder; it is **not** a global install and is not automatically available inside unrelated application repositories.
