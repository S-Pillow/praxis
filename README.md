# AIPF Specialist Suite

**Current continuation handoff:** [2026-11-23 AIPF Specialist Suite handoff](research/handoffs/2026-11-23-aipf-specialist-suite.md) — verified repository state, Prompt Agent/Builder Agent execution-model clarification, accepted decisions, experiment evidence, limitations, and next real-project comparison gate.

**Status: research/prototype; not released or installed.** This repository investigates optional specialist knowledge and reusable design catalogs that help an AI **do better work while building** and **critique/audit the result before completion**. The governing standard remains **AIPF v8.10.1**; no specialist replaces or revises its authority.

## Current workstreams

1. **Unified Design Catalog** — independent inventory of styles, themes, templates, palettes, typography, systems, examples, and reusable UI craft knowledge. Preserve original names, source paths, token values, preview references, compatibility constraints, and per-entry provenance. Keep overlapping source entries distinct while linking equivalences.
2. **Specialist Evaluation** — assess individual sources and techniques (UI build, design critique, technical audit, QA/debugging). No wholesale import of competing governance.
3. **Licensing and provenance** — treat repository license and asset/file rights separately. No third-party media/fonts/screenshots/examples bundled until reviewed.

## Decisions to preserve

- **Primary benefit:** teach the AI better practical techniques **during implementation**; also inspect/verify before completion.
- **Anti-generic diagnostics:** optional and context-sensitive, never global aesthetic prohibitions.
- **Brand truth:** extract verified approved brand tokens/values from accessible canonical sources where feasible; do not guess or overwrite an existing design system.
- **Critique vs audit:** separate aesthetic/usability critique from verifiable technical checks.
- **No additional mandatory “degraded review” disclosure** requested; report only real evidence and capabilities without falsely claiming independent review.
- **Catalog first:** metadata and source links before copying media/assets. An upstream source is not a governing rule.
- No amendment to AIPF v8.10.1; potential improvements must be discussed before a separate canonical framework change.

## Layout

- `catalog/schema/` — normalized entry schema
- `catalog/entries/` — 5,500 source-linked production entries plus an illustrative starter file
- `catalog/mappings/` — source-specific mapping and extraction notes
- `research/` — workstream scope and source evaluation record
- `research/licensing/` — rights review and redistribution gates
- `research/decisions/` — accepted boundaries
- `skills/` — optional prototype specialists; currently one UI/UX skill
- `tests/` — reserved for schema and catalog checks

## First usable UI/UX specialist (prototype v0.2)

The optional [UI/UX skill](skills/aipf-ui-ux/SKILL.md) now automatically requests a short, read-only set of relevant references from the existing [unified catalog](catalog/SEARCH.md) when the coding AI can access this repository and run Python. Users provide a normal UI request; they do not need to run catalog searches or copy prompts. The AI uses candidates to **design during implementation** and then performs separate design critique and technical UI audit. It is one `SKILL.md` file with no additional runtime dependencies or required ceremonies; for use see [skills/README.md](skills/README.md). It is not installed or released and has not yet been proven to improve rendered design outcomes.

## Real catalog interface (local prototype)

The [Design Index](ui/catalog-explorer/README.md) is a local-only, read-only browser of the existing 5,500-entry unified catalog. It offers search, category filters, incremental browsing, real source details and locally saved references without any new data store or third-party runtime. It is not a deployed site or a replacement for the optional UI/UX specialist.

## Current source set

- [Hallmark](https://github.com/Nutlope/hallmark)
- [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- [Open Design Agent Kit](https://github.com/feimacode/open-design-agent-kit)
- [Impeccable](https://github.com/pbakaus/impeccable)
- [MengTo Skills](https://github.com/MengTo/Skills)

See [field map](catalog/mappings/source-field-map.md), [license review](research/licensing/source-license-register.md), and [catalog starter](catalog/entries/starter.json).

### Boundaries

**This is not a redistributed bundle of upstream assets.** Catalog entries initially represent source-derived metadata/observations and extraction examples. Source licenses are recorded provisionally and third-party/embedded rights must be checked per entry before republishing source content or assets. No claimed visual test, runtime compliance, or quantitative performance improvement without execution evidence.
