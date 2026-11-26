# Integrated Praxis usage and validation

## Entry and routing

Select Praxis, not the separate standalone AIPF plugin. Load `skills/praxis/SKILL.md` from the actual pinned repository root. A Prompt Agent (or direct executing agent) follows the complete incorporated AIPF path selector and loads selected dependencies. Keep the project's approved PRD/requirements separate; a reference is usable only when the actor can actually read it. Consult a registered specialist for material work, using its actual instructions before retrieval. The specialist is guidance, not a second governing framework or an independent actor.

| Active task | Applicable framework paths (illustrative) | Specialist action |
|---|---|---|
| New user-facing application | 11 + 14 | UI/UX build |
| Substantial redesign preserving behavior | 12 + 14 | UI/UX build |
| Material visual/usability review | 14 + applicable companions | UI/UX critique |
| Technical interface accessibility checks | 14 + applicable companions | UI/UX audit |
| Minor text-only correction | 12 + 14 where applicable | None unless concrete benefit |
| Routine backend-only repair | 12 | None unless a material architecture decision is involved |
| New system or material design decision | 11 or 12 | Architecture design |
| Structural change or review | 12 | Architecture evolve or critique |

The agent selects paths and materiality under AIPF; the table is not a replacement Path Selector. The registry maps task type to a specialist and its existing mode. For future specialists extend the registry, entry guidance and integration tests together; do not register unavailable modules or allow them to introduce new authority. The v1.1.0 source registers UI/UX v0.3 and architecture v0.1; see [release qualification](docs/releases/1.1.0.md).

The optional read-only helper is for agents, not a user workflow:

```sh
python scripts/praxis_context.py --task ui-build --chapter 11 --chapter 14
# after reading the selected specialist, if execution and catalog are available:
python scripts/praxis_context.py --task ui-build --chapter 11 --chapter 14 --platform web --request 'Build a financial dashboard with readable tables'
```

The second invocation delegates unchanged to the existing `recommend_design.py` CLI. It does not interpret arbitrary natural-language task classification, select an AIPF path, install anything, or execute a build. A `consult` result identifies a specialist, not proof an agent read or applied it. `completed`, `empty`, `unavailable` lookup statuses describe the actual command result. If Chapter 14 is missing for a material UI classification, the helper requests path recheck; it does not authorize the path. Unavailable specialist/lookup can fall back to approved context and craft where sufficient; missing/corrupt governing framework content is a hard integrity failure, not permission to improvise governance. Preserve license restrictions, source evidence, existing design identity and scope.

In a two-agent workflow the Prompt Agent applies the [payload synthesis guidance](skills/praxis/references/builder-payload.md) and transports only the canonical authorized Builder Payload. Distill all necessary PRD, governance and specialist values so execution does not depend on Praxis, AIPF, catalogs or the PRD. Optional access is permitted but creates no additional authority. Verified accessible implementation inputs may be referenced under Chapter 21; stop if required operational meaning or access is missing. Distinct Builders do not choose subsequent work. For direct use, the executing agent follows AIPF directly, with no additional transport or handoff ceremony.

## Supported discovery

In a repository-aware agent, open the Praxis checkout (or make it readable from the target project), select Praxis, and use `AGENTS.md` / `.agents/skills/praxis/SKILL.md` to load `skills/praxis/SKILL.md`. If the host does not discover repository adapters, explicitly ask it to read that entry file. Cursor 3.31.15 validation reported repository-based activation; native skill-picker discovery was unavailable. No global installation or separate AIPF plugin is required. No native discovery claim is made for untested hosts. Use `python -X utf8` for manual Python CLI invocations on hosts with a non-UTF-8 default. Unknown helper task identifiers fail explicitly (exit 2); do not treat an error as non-activation.

## Validation

See [standing scenario regression strategy](docs/TESTING.md).

Run `python -m unittest discover -s tests -v` from the full Praxis repository. The integration tests cover complete canonical-projection integrity, routing to the existing specialist, skipping nonmaterial tasks, separate critique and audit modes, missing path, unavailable specialist, failed lookup, the existing live local Python catalog command, and entry-point/role instructions. A helper test is not a live host activation test; independent Prompt Agent and Builder testing remains separate from repository-level regression verification.

The canonical source is `Neutral_AIPF_v8_10_1.docx` with SHA-256 `8e66028c8ebf60ea87180be1c23933273d8a597c425d3a1595ae81d9a720b8e6`. The complete Markdown projection SHA-256 is `b11dfa2c12deb4d5b90833af4f10a02b5daf5e26d143469560b896fe9c85e0fd`; this is not the manifest-file digest. The actual `framework/projection-manifest.json` SHA-256 at the QUALITY-01 baseline is `f1c49a23f9157d3358e474c374e95cdb7cf65591504b79d498a202d44c1c58e1`. The manifest lists all contiguous partitions; none introduces normative changes.

## Architecture consultation (development candidate)

For a material architecture task, consult `skills/architecture/SKILL.md` and its index directly. An optional helper example is `python scripts/praxis_context.py --task architecture-design --chapter 11 --request "Design a local import and reporting utility"`. Use the actual selected chapter and mode. `lookup_status: not_applicable` means no lookup process, not proof of consultation. No Python is required to read the guides. The independently usable [capability index](knowledge/capabilities/INDEX.md) is not an approved dependency list.

## Security & Privacy consultation (development candidate)

For material security or privacy work, consult `skills/security-privacy/SKILL.md` after canonical routing and use design, harden or review. Example: `python scripts/praxis_context.py --task security-design --chapter 12 --chapter 15 --request "Design resource isolation for an authorized shared feature"`. Use the actual selected paths. No lookup subprocess; no guide consultation or security assurance inferred from helper output. Source-review boundaries, Builder independence and AIPF authority remain binding.
