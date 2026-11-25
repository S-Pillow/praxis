# Praxis — Product Requirements Document

Version: 0.1 | Status: Owner approved | Approval: 2026-11-24 (conversation: “Approved”)

**Intelligence into action.**

## 1. Product vision

Praxis is an extensible, AI-powered software development system that combines structured development governance, specialist expertise, curated knowledge and engineering capabilities into a unified agent experience. Its purpose is to improve the quality, consistency and reliability of AI-assisted software development without requiring users to manually coordinate multiple independent tools, skills or frameworks.

One entry point. The right expertise. Governed execution.

Praxis has its own product identity, powered by AIPF and developed by ForgeForward. AIPF remains an independent standalone framework with its own lifecycle. Praxis incorporates AIPF alongside specialist capabilities, catalogs and development tools. Neither product requires separate installation of the other. Proposed repository identity: `S-Pillow/praxis`, preserving the existing specialist-suite repository history; no rename has yet been performed.

## 2. Target users

Developers, technical professionals, product owners and AI-assisted builders who want reliable software without sacrificing engineering discipline. Support experienced developers and users communicating primarily in natural language.

## 3. Functional requirements

| ID | Requirement | Priority |
|---|---|---|
| PR-01 | Single entry point for the complete system | Required |
| PR-02 | Self-contained AIPF framework | Required |
| PR-03 | Project context and requirements management | Required |
| PR-04 | Context-aware specialist activation | Required |
| PR-05 | Integrated UI/UX specialist | Required |
| PR-06 | Specialist knowledge and catalog retrieval | Required |
| PR-07 | Direct single-agent development | Required |
| PR-08 | Separate Prompt Agent and Builder Agent workflows; portable payloads independent of Builder access to Praxis, AIPF, specialists, catalogs or PRD | Required |
| PR-09 | Evidence-based verification and regression testing | Required |
| PR-10 | Extensible specialist registration | Required |
| PR-11 | Portable agent discovery adapters | Required |
| PR-12 | Plugin distribution | Future |
| PR-13 | Additional engineering specialists | Future |

## 4. Non-functional requirements

Praxis must remain lightweight, portable, maintainable and transparent. Avoid unnecessary dependencies on specific AI models, agent vendors, external APIs or hosting environments. Preserve AIPF governing principles; distinguish verified evidence from assumptions; respect project authorization boundaries; avoid silent scope expansion. Specialist recommendations remain subordinate to approved requirements and governing constraints. Prompt synthesis prioritizes product quality, correctness, operational completeness and clarity over token savings. See [DEC-002](decisions/PRAXIS-DEC-002-builder-context-independence.md) and [DEC-003](decisions/PRAXIS-DEC-003-quality-first-prompts.md).

## 5. Initial release acceptance criteria

At the time of this approved requirements baseline, all were pending validation for the integrated Praxis product; existing component evidence was not integrated acceptance. For the later criterion-by-criterion disposition, see [v1.0.0 release preparation](releases/1.0.0.md).

- [ ] AC-01: A single entry point activates the incorporated framework.
- [ ] AC-02: No separate AIPF installation is required.
- [ ] AC-03: Relevant UI/UX work activates the specialist.
- [ ] AC-04: Unrelated work does not unnecessarily activate specialists.
- [ ] AC-05: Existing catalog and retrieval capabilities remain functional.
- [ ] AC-06: Both single-agent and separate-agent workflows are supported. A distinct Builder can execute a complete payload without access to Praxis, AIPF, specialists, catalogs or PRD; optional access does not expand authority. Verify meaningful execution, evidence and reconciliation; no mandatory extra handoff for direct mode.
- [ ] AC-07: Framework governance and authorization boundaries are preserved, including current T1 derivation and issuance, operational completeness, explicit scope, and quality-first prompt review (no material ambiguity or missing required controls).
- [ ] AC-08: Unavailable specialist capabilities are handled transparently.
- [ ] AC-09: All existing and new regression tests pass.
- [ ] AC-10: Independent real-world agent testing confirms the intended workflow.
- [ ] AC-11: Installation and usage are documented.
- [ ] AC-12: The product owner approves the release.

See [architecture](ARCHITECTURE.md) and [development baseline](DEVELOPMENT-BASELINE.md). Product baseline approval is not release approval.
