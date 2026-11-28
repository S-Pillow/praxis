# Operational documentation and repository quality

Use only applicable cards. Examples are synthetic and unexecuted. Source IDs resolve through [SOURCES](../SOURCES.md); provider facts must be verified at use.

## DO-D32 — What runbook or README information actually helps?

**Applicability / context:** Material setup, operational guidance, release/change or incident documentation; use shared guidance even without DevOps activation.

**Decision and alternatives:** Choose audience/profile and actual first success; include prerequisites, supported versions, exact target/command, expected output and failure branches, secrets/cost/permission warnings, ownership and recovery when applicable. Distinguish illustrative commands from verified actual commands. Avoid empty boilerplate and duplicated canonical docs. For incident runbook include symptom/diagnosis, safe actions, stop and recovery; no automatic execute.

**Counterexample:** Copy-paste instructions point at production or put keys into source; README says every feature ready although release is older.

**Observable verification:** Clean applicable environment follows safe first action and actual outcome; compare claims and command to source and released state; verify labels/URLs and render if material.

**Sources and limits:** DO-S04–11, DO-S32–33; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D33 — How should documentation and release parity be checked?

**Applicability / context:** Material source/version/badge/index change or repository health review.

**Decision and alternatives:** Use shared [Repository Quality index](../../../knowledge/repository-quality/INDEX.md). Compare actual file/section and destination meaning, not link existence; verify fragments, paths, version history, release metadata and rendered content. Use native local checks first, optional Lychee external checks only with network/credential boundaries and timeout/redirect/cache interpretation; optional Actionlint for workflow grammar. Do not change repository policy or CI automatically. Preserve original qualifiers and accepted brand; small correction does not justify redesign.

**Counterexample:** A link returns 200 to the wrong product/version; workflow path filters skip docs-only changes while standing tests assert README version; scanner badge appears current but target stale.

**Observable verification:** Inspect exact semantic claims and actual rendered surface, first success, source/release identity, applicable workflow trigger; report unavailable observer and bounded next step.

**Sources and limits:** DO-S01, DO-S04–13, DO-S19–25, DO-S32–33; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.
