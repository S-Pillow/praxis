# PRAXIS-DEC-001 — Scenario-based regression testing

Status: Owner approved (conversation, 2026-11-24, America/Kentucky/Louisville)
Product: Praxis v0.1
Applies to: Praxis development and release verification, not a modification of the standalone AIPF standard.

## Decision

Scenario-based regression testing is a permanent part of the Praxis regression strategy, alongside conventional unit and integration testing. The owner explicitly agreed with this proposal after PRAXIS-SELFTEST-01. Preserve the decision in the repository development baseline and testing documentation at the next authorized integration update.

## Required coverage

Cover materially affected natural-language task routing, overlapping AIPF paths and conditional controls, specialist activation and non-activation, authority and stop boundaries, invalid inputs and unavailable capabilities, and direct versus distinct-agent execution. Extend coverage when adding or changing specialists or governing integrations. Retain applicable existing scenarios and their expected behavior.

## Evidence approach

Use PRAXIS-SELFTEST-01 as the initial scenario corpus (14 walkthroughs, 13 helper checks, four actual catalog lookups and five fault cases). Keep reasoning walkthroughs, executable checks, and independent live-agent observations distinct. Do not claim blind testing, independent accuracy or observed runtime behavior from self-authored walkthroughs or helper calls. Preserve actual requests, expected/observed decisions, commands, outcomes and source identity. Include negative and failure cases, not only successful paths. Prefer focused regression additions tied to material changes; no mandatory repeated research or retrieval benchmark cycle.

## Validation reconciliation (2026-11-24)

Source: owner's pasted PRAXIS-VALIDATION-01 summary, not the full local Windows report. Reported candidate tree d2135148… and unchanged source. Full report in the private evidence store (local path omitted): `PRAXIS-VALIDATION-01/PRAXIS-VALIDATION-01-REPORT.md`; reported SHA-256 `b2bb3a9c494a55de2925899bde2f66d603739d0725f39666bfcbb4d91b024a17`. Full report not independently inspected.

- Regression: 111 ran, 4 failures and 2 errors; reported Windows symlink privilege and cp1252 decoding issues. AC-09 remains unmet on this host. Exact failing assertions and tracebacks need review.
- Unified activation: PARTIAL; repo AGENTS.md/skills loading and catalog use observed by Cursor; native Cursor discovery unavailable; screenshots missing.
- Context sensitivity: PASS as reported for all four subcases.
- Distinct agents: PARTIAL; separate Task agents, operational payload and preserved scope reported; live DOM evidence pending.
- Degradation: PASS as reported for unavailable catalog/specialist and missing governance.
- Self-test defect: unrecognized task identifiers return `not_needed`; correction proposed to reject invalid identifiers explicitly.

## Proposed next correction unit (not yet authorized by this decision)

Inspect the full validation report and affected files; correct demonstrated portability failures without weakening integrity assertions, use explicit UTF-8 for affected text I/O, reject unknown task identifiers, add focused regression coverage and incorporate this decision. Rerun affected tests and the full suite on Linux and Windows; close outstanding runtime/DOM/screenshot evidence and accurately document supported entry mechanisms. No requirement to implement native Cursor discovery if repository-based discovery meets the approved entry-point contract; evaluate any remaining portability acceptance gap explicitly. Preserve the validated candidate for comparison and avoid unrelated retrieval changes, new specialists, or standalone AIPF modifications.

Release status: not ready. Independent validation PARTIAL; AC-09 unmet and other evidence gaps remain. This note does not authorize remediation, shared repository mutations or release. The tested candidate and approved v0.1 documents remain unchanged in this step.
