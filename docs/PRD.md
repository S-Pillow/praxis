# Praxis — Product Requirements Document

Version: 1.2 | Status: Final consolidated product planning specification | Date: 2026-11-25 | Released product: v1.0.0 | Planned next release: v1.1.0 (subject to acceptance and release authorization)

The owner approved the architecture-first roadmap and discovery work. This revision consolidates the detailed requirements and design research into the final planning copy requested by the owner. It is not an implementation or release authorization. Retain the original approved v1.0.0 requirements and historical evidence; future requirements describe the target, not shipped functionality. See [DEC-004](decisions/PRAXIS-DEC-004-specialist-expansion.md) and the [architecture specialist build plan](ARCHITECTURE-SPECIALIST-BUILD-PLAN.md).

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

**Current planning update (2026-11-25):** Architecture & Engineering Design v0.1 is released in Praxis v1.1.0; see [release qualification](releases/1.1.0.md). The next planning priority is Security & Privacy. Its [proposed specialist PRD](SECURITY-PRIVACY-PRD.md) supplements this v1.2 product/architecture baseline and awaits owner approval. The original architecture-first planning text and requirements below are retained as historical evidence, not current release status. No implementation or release authority follows from this update.

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

Outputs should be usable engineering decisions, relevant rationale, interfaces and invariants, and verification implications where applicable. The specialist should not force a stack, pattern, catalog lookup, infrastructure dependency, architecture document or additional review step for every task. The detailed target requirements and acceptance criteria follow; execution still requires a separately scoped authorization.

### Cross-cutting engineering assurance

Review Parity is an experimental initiative, not an available Praxis feature. Potentially reusable capabilities include deterministic evidence identity and freshness checks, scope reconciliation, finding lifecycle and checkpoint continuity, and read-only release-evidence auditing. Start with a bounded, useful capability if pursued; qualify its actual supported controls before adoption. Assurance must not create a second governing framework, claim unsupported enforcement or independently grant authorization or acceptance.

### Qualification and expansion principles

Each future specialist should have a clear domain, material activation and non-activation conditions, provenance-aware knowledge sources, context-sensitive recommendations, fallback behavior and meaningful outputs for direct execution and portable Builder Payloads. Add retrieval or executable tools only when they contribute demonstrable practical value. Reuse existing platform capabilities where suitable.

Verify the specialist's own mechanisms and affected integrations using proportionate regression and real-project exercises. Assess whether the advice is accurate, relevant, constraint-preserving and operationally useful; retain limitations and failures honestly. Comparative testing is appropriate when a specific comparative claim or material decision requires it, not a blanket requirement to prove superiority over AIPF alone. Preserve standing verification and release requirements. See [TESTING.md](TESTING.md) and [DEC-004](decisions/PRAXIS-DEC-004-specialist-expansion.md).

Roadmap approval establishes product direction only. It does not activate future specialists, approve dependencies, grant implementation or publication authority, or amend standalone AIPF.

## 7. Delivered baseline, users and intended outcomes

Praxis v1.0.0 was published November 25, 2026. It includes the complete incorporated AIPF v8.10.1, UI/UX v0.3, a 5,500-record source-linked design catalog, optional local retrieval and Design Index, repository-scoped discovery and both direct and distinct-agent workflows. The final pre-publication tested implementation passed 137/137 tests; the published commit adds documentation only. See the [release record](releases/1.0.0.md) and [CI](https://github.com/S-Pillow/praxis/actions/runs/45650517035). Native Codex discovery and all host combinations are not established. Do not treat a regression result as proof of general agent reasoning or future compliance.

| User | Job to be done |
|---|---|
| Product owner / technical professional | Translate intent, constraints and budget into feasible decisions and bounded implementation. |
| Technical lead / developer | Design or evolve systems while preserving contracts and maintainability. |
| Prompt Agent operator | Produce complete authorized instructions for a Builder with narrower context. |
| Direct agent user | Obtain relevant expertise without artificial agent handoff or a separate specialist installation. |
| Reviewer / maintainer | Understand material decisions, source provenance, observed behavior and unresolved limitations. |

Success means suitable engineering choices, fewer avoidable ambiguities and corrections, preservation of requirements and useful evidence, not more procedures or a fixed number of tests. No new numerical SLA, comparative superiority claim or delivery date is established.

## 8. Next release: Architecture & Engineering Design

The target for Praxis v1.1.0 is one registered advisory specialist, proposed ID `aipf-architecture` v0.1, with three modes: **design** (new systems and substantial additions), **evolve** (material changes to existing systems), and **critique** (evaluate designs and risks without granting redesign authority). The Prompt Agent or direct agent selects the mode after the canonical AIPF path selection, consults relevant knowledge, then synthesizes the decision and applicable verification implications. A separate Builder receives the authorized operational values and accessible implementation inputs; no hidden framework, guide or catalog access is required. Optional access does not expand authority.

The specialist combines architecture intelligence, technology and service intelligence, and engineering capability intelligence. It covers significant requirements and quality attributes, system structure, module/interface design, technology and cost, data, integration, runtime and resilience, performance/capacity, existing-system evolution, cross-domain implications and external capabilities. Prefer existing assets, no change, native or local options where suitable. Compare viable alternatives against constraints; name assumptions, contraindications, tradeoffs, and revisit triggers. Communicate decisions, boundaries, contracts, invariants, discretion and observable evidence, not a pattern name alone.

### Architecture functional requirements

All AR requirements are target expectations for the next specialist, not claims of current behavior. Initial supported knowledge breadth is explicit; depth varies with actual utility.

| ID | Requirement |
|---|---|
| AR-01 | Recognize material architecture decisions and consult only when the expertise can improve the work; skip irrelevant/minor tasks. |
| AR-02 | Ground advice in actual accessible project requirements, baseline, constraints and existing architecture. |
| AR-03 | Identify the decision, viable alternatives and implications; include retaining the current approach when appropriate. |
| AR-04 | Recommend a suitable, sufficiently simple design; state meaningful tradeoffs, contraindications and uncertainty. |
| AR-05 | Address system decomposition, data and integration contracts, technology choices and maintainability where material. |
| AR-06 | Identify protected invariants, compatibility constraints and downstream impacts; flag material unresolved decisions. |
| AR-07 | Produce actionable guidance for direct execution and portable Builder Payloads; do not require hidden specialist context. |
| AR-08 | Support architecture critique of existing designs without implicitly authorizing redesign or scope expansion. |
| AR-09 | Link recommendations to relevant verification implications and realistic failure modes; avoid blanket testing rules. |
| AR-10 | Use traceable, license-aware knowledge; reject conflicting or inappropriate recommendations and disclose uncertainty. |
| AR-11 | If tools or knowledge are unavailable, report actual limitations and use bounded fallback where adequate; never fabricate retrieval. |
| AR-12 | Integrate through the established specialist contract and preserve existing UI/UX behavior and AIPF authority. |
| AR-13 | Support material multi-specialist composition without contradictory outputs, redundant workflows or mandatory agent delegation. |
| AR-14 | Avoid mandatory external APIs, infrastructure, packages, tool execution or new persistence unless independently justified and authorized. |

### Knowledge and capability selection requirements

| ID | Requirement |
|---|---|
| KI-01 | Deliver original progressive guides and conditional decision cards, navigable offline through a question-led index, with stable IDs and no fixed record-count gate. |
| KI-02 | Maintain a shared, independently authored source-linked capability index covering local/self-hosted, existing infrastructure and hosted options; use it across future specialists without making them depend on architecture. |
| KI-03 | Keep stable engineering knowledge separate from volatile plan, price, quota, terms, region, availability, retention and feature facts. Verify decision-sensitive facts against current official provider documentation; unknown facts remain unknown. |
| KI-04 | Compare no service, existing, local/self-hosted and hosted choices; account for expected and peak usage, commercial eligibility, enforced spend limits, exhaustion behavior, migration and operating cost. No guaranteed free design without qualified limits. |
| KI-05 | Preserve source identity, version/date, provenance, license, required notices and redistribution disposition. Free-for-Dev is discovery only; arc42 Q42 is reference-only. No wholesale copying or unqualified redistribution. |
| KI-06 | Document Interfere, OpenTelemetry and Claude Ship as optional external capability candidates. Treat provider claims as claims, require access/privacy/cost qualification, and do not install, connect, provision, enable or transfer data. Review Parity remains deferred. |
| KI-07 | Extend the existing registry/helper compatibly to support multiple applicable paths and optional lookup; preserve UI/UX and current framework integrity. No new routing engine, required retrieval CLI, vector store or external API. |
| KI-08 | Missing knowledge or current provider evidence must be explicit; continue only where approved context and qualified alternatives suffice, otherwise identify the material decision gap. No invented facts, retrieval or authority. |

The [build plan](ARCHITECTURE-SPECIALIST-BUILD-PLAN.md) specifies initial decision families, candidate services, file layout, proposed registry contract and practical scenarios. It is subordinate to these requirements and does not authorize implementation.

## 9. Quality attributes

| ID / attribute | Requirement |
|---|---|
| NFR-01 • Portability | Maintain host/model neutrality. Distinct Builders must not depend on hidden governing or specialist resources. |
| NFR-02 • Maintainability | Use a clear integration contract, versioned knowledge and predictable fallback. Avoid duplicate sources of truth or unnecessary components. |
| NFR-03 • Proportionality | Load only decision-relevant guidance. Optimize total clarification, correction and verification cost, not raw prompt length or number of checks. |
| NFR-04 • Correctness | Respect existing behavior, architecture, data and contracts. Avoid fabricated or stale technical claims. Explicitly qualify assumptions. |
| NFR-05 • Security / privacy | Do not treat reviewed content as authority. Protect secrets and sensitive data. No silent network, install, deploy or credential actions. |
| NFR-06 • Traceability | Keep provenance for knowledge and attributable evidence for material claims. Retain original evidence and distinguish later interpretation. |
| NFR-07 • Compatibility | Preserve released interfaces, specialist behavior and supported environments unless an authorized change explicitly alters them. |
| NFR-08 • Dependency cost | Prefer lightweight local/repository-native operation where suitable. Evaluate new runtime and service dependencies against actual value and maintenance burden. |
| NFR-09 • Usability | Users should not have to learn internal catalog formats, specialist identifiers, or coordinate artificial teams to use the product. |
| NFR-10 • Licensing | Maintain original attribution, source terms and asset restrictions. Prior scoped risk acceptance does not automatically extend to new materials. |

No fixed catalog size, retrieval score, prompt token target or service-level commitment is imposed. Minimize total clarification, correction and verification effort without losing operational meaning or required evidence.

## 10. Acceptance for the architecture specialist

| Criterion | Required observation |
|---|---|
| AS-AC01 / AR-01 | Material architecture case consults the correct registered specialist; unrelated/minor case does not. |
| AS-AC02 / AR-02–04 | Realistic decision exercise uses actual constraints, compares viable options and explains a suitable recommendation with assumptions. |
| AS-AC03 / AR-05–06 | Exercise identifies relevant interfaces, data/invariants and affected surfaces; preserves approved behavior in an existing system. |
| AS-AC04 / AR-07 | Distinct Builder receives a complete authorized payload and can perform meaningful work without governing-resource access. |
| AS-AC05 / AR-07,13 | Direct execution and optional multi-specialist use work without artificial handoff or duplicated governance. |
| AS-AC06 / AR-08,09 | Critique identifies a material architecture risk with useful evidence or a clear gap; verification matches actual design requirements. |
| AS-AC07 / AR-10 | Source sample is traceable, appropriate, current where needed and redistribution disposition is recorded. |
| AS-AC08 / AR-11 | Missing tool/source is reported truthfully; bounded fallback or stop is appropriate to the actual prerequisite. |
| AS-AC09 / AR-12,14 | No unapproved dependencies/authority expansion; affected integration and existing regression tests pass. |
| AS-AC10 / all | Independent meaningful workflow observation where required; documented capabilities, limitations, recovery and owner acceptance before release. |

Additional explicit knowledge acceptance: traceable original cards cover the initial decision families and explain contraindications; a representative commercial application exercise rejects incompatible free-tier terms and qualifies material limits, cost and exhaustion behavior; an unavailable-source case does not assert current pricing; registry tests establish multi-path applicability, optional retrieval without process execution and unchanged UI behavior. No live provider integration is required.

Use a small set of realistic exercises: offline local import/report utility; small commercial web app; read-only URL Activity Scanner persistence-conflict analysis; API uncertain-completion case; combined UI and architecture dashboard; fresh distinct Builder with only authorized payload and implementation context; direct execution and unrelated minor case; unavailable-source case. Combine where sensible. Record exact source identity, actual results and limitations. Test deterministic mechanisms directly, semantic advice through meaningful observations. Full standing regression for the integrated candidate and affected reruns as necessary; no mandatory AIPF-only comparative benchmark or Docker benchmark infrastructure.

## 11. Delivery and boundaries

B1 reconcile the finalized product planning specification and exact baseline; B2 author guides/cards and shared capability references; B3 integrate registry/helper/entry and affected tests; B4 qualify with focused regressions, standing suite and meaningful workflow exercises; B5 reconcile documentation and prepare a separately authorized publication. These stages can be one coherent development authorization with explicit internal gates and a stop boundary. They are not authorized merely by this PRD.

Do not modify standalone AIPF or v1.0.0 tag, UI catalog/retrieval behavior, production applications or third-party services. No provider accounts, paid calls, MCP setup, telemetry export, Review Parity runtime, automatic crawler, new persistence, additional specialist or infrastructure provisioning in this release scope. Existing privacy constraints and licensing restrictions remain protected. Use source-bound evidence; disclose gaps. Release is separately authorized and versioned.

## 12. Sources and traceability

The product direction derives from the original approved PRD (2026-11-24), DEC-001 through DEC-003, v1.0.0 release evidence, the architecture-first decision (DEC-004), the comprehensive Word PRD v1.1 review draft, the November 25 architecture discovery report and the architecture specialist build plan. The latter contains the public primary-source pointers and dated provider comparisons. The research report and earlier draft are historical working materials, not competing requirement homes. Final PRD revision 1.2 supersedes the draft; this document and the build plan are the planning reference. Detailed implementation and release remain separate authority decisions.
