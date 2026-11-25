# Praxis — Product Requirements Document

Version: 0.2 | Status: Owner-approved product baseline and roadmap direction | Original baseline: 2026-11-24 | Roadmap revision: 2026-11-25 ([DEC-004](decisions/PRAXIS-DEC-004-specialist-expansion.md))

**Intelligence into action.**

## 1. Product vision

Praxis is an extensible, AI-powered software development system that combines structured development governance, specialist expertise, curated knowledge and engineering capabilities into a unified agent experience. Its purpose is to improve the quality, consistency and reliability of AI-assisted software development without requiring users to manually coordinate multiple independent tools, skills or frameworks.

One entry point. The right expertise. Governed execution.

Praxis has its own product identity, powered by AIPF and developed by ForgeForward. AIPF remains an independent standalone framework with its own lifecycle. Praxis incorporates AIPF alongside specialist capabilities, catalogs and development tools. Neither product requires separate installation of the other. Repository: `S-Pillow/praxis`, preserving the existing specialist-suite repository history. Praxis v1.0.0 has been published; the original planning and release evidence remains recorded separately.

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
| PR-13 | Additional engineering specialists, prioritized by their contribution to material engineering decisions and practical execution; see section 6 | Future |
| PR-14 | Optional cross-cutting engineering assurance, potentially reusing Review Parity mechanisms; subject to separate qualification and implementation approval | Future |

## 4. Non-functional requirements

Praxis must remain lightweight, portable, maintainable and transparent. Avoid unnecessary dependencies on specific AI models, agent vendors, external APIs or hosting environments. Preserve AIPF governing principles; distinguish verified evidence from assumptions; respect project authorization boundaries; avoid silent scope expansion. Specialist recommendations remain subordinate to approved requirements and governing constraints. Prompt synthesis prioritizes product quality, correctness, operational completeness and clarity over token savings. See [DEC-002](decisions/PRAXIS-DEC-002-builder-context-independence.md) and [DEC-003](decisions/PRAXIS-DEC-003-quality-first-prompts.md).

## 5. Initial release acceptance criteria

At the time of this approved requirements baseline, all were pending validation for the integrated Praxis product; existing component evidence was not integrated acceptance. For the later criterion-by-criterion disposition, see [v1.0.0 release record](releases/1.0.0.md).

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

## 6. Specialist expansion roadmap

The next planned specialist is **Software Architecture & Engineering Design**. This supersedes the earlier QA-first planning preference; it does not invalidate the QA research or change the accepted v1.0.0 requirements and evidence.

### Product direction

Specialists add domain expertise and useful techniques rather than a parallel development methodology. Prioritize knowledge that improves decisions before implementation, while retaining support for implementation guidance, diagnosis, critique and verification. AIPF remains authoritative for governance, authorization, proportionality and acceptance. Specialist advice must be evaluated against approved project intent, constraints and the actual implementation context.

In separate-agent workflows, the Prompt Agent consults relevant specialists and translates selected recommendations into concrete, operationally complete Builder Payload instructions. The Builder retains appropriate implementation discretion within the authorized scope and need not access Praxis or its specialist resources. The same capabilities support direct single-agent execution without artificial role separation or handoffs. Optional specialist access does not expand authority.

| Specialist | Roadmap status | Intended contribution |
|---|---|---|
| UI/UX & Design Intelligence | Available in v1.0.0 | Interface design, usability, accessibility and source-linked design knowledge |
| Software Architecture & Engineering Design | Next planned | Appropriate architectural patterns, technology tradeoffs, module boundaries, data modeling, integration contracts, resilience and maintainability; avoid unnecessary complexity |
| Security & Privacy | Future | Threat modeling, trust boundaries, authentication, authorization, secure design and data protection |
| QA & Engineering Quality | Future | Risk-based test design, effective assertions, diagnosis, regression strategy and behavioral verification |
| DevOps & Reliability | Future | Deployment strategies, infrastructure, observability, recovery and operational resilience |

The order beyond the next specialist is an indicative planning sequence, not a delivery schedule. The later priorities may change with actual needs and evidence.

### Architecture specialist: intended capability boundary

The specialist should support both new-system design and material changes to existing systems. It should help the agent evaluate suitable options against requirements, expected scale, existing constraints, security and operational needs, skills, costs and maintainability; explicitly identify tradeoffs, contraindications and assumptions; preserve appropriate existing architecture; and recommend the simplest sufficient design.

Outputs should be usable engineering decisions, relevant rationale, interfaces and invariants, and verification implications where applicable. The specialist should not force a stack, pattern, catalog lookup, infrastructure dependency, architecture document or additional review step for every task. Implementation, registration, knowledge-source selection and detailed acceptance criteria require a separately scoped development unit.

### Cross-cutting engineering assurance

Review Parity is an experimental initiative, not an available Praxis feature. Potentially reusable capabilities include deterministic evidence identity and freshness checks, scope reconciliation, finding lifecycle and checkpoint continuity, and read-only release-evidence auditing. Start with a bounded, useful capability if pursued; qualify its actual supported controls before adoption. Assurance must not create a second governing framework, claim unsupported enforcement or independently grant authorization or acceptance.

### Qualification and expansion principles

Each future specialist should have a clear domain, material activation and non-activation conditions, provenance-aware knowledge sources, context-sensitive recommendations, fallback behavior and meaningful outputs for direct execution and portable Builder Payloads. Add retrieval or executable tools only when they contribute demonstrable practical value. Reuse existing platform capabilities where suitable.

Verify the specialist's own mechanisms and affected integrations using proportionate regression and real-project exercises. Assess whether the advice is accurate, relevant, constraint-preserving and operationally useful; retain limitations and failures honestly. Comparative testing is appropriate when a specific comparative claim or material decision requires it, not a blanket requirement to prove superiority over AIPF alone. Preserve standing verification and release requirements. See [TESTING.md](TESTING.md) and [DEC-004](decisions/PRAXIS-DEC-004-specialist-expansion.md).

Roadmap approval establishes product direction only. It does not activate future specialists, approve dependencies, grant implementation or publication authority, or amend standalone AIPF.
