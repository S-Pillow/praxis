# Praxis — Product Requirements Document

Version: 1.3 | Status: Owner-approved consolidated product requirements | Date: 2026-11-26 | Release target: Praxis v1.2.0 (accepted candidate; publication verified separately)

This is the single authoritative product PRD for Praxis. It consolidates [product PRD v1.2](https://github.com/S-Pillow/praxis/blob/c6393f6174e8d83e6760cf64bfbe889710d8919d/docs/PRD.md) and [Security & Privacy Specialist PRD v1.1](https://github.com/S-Pillow/praxis/blob/c6393f6174e8d83e6760cf64bfbe889710d8919d/docs/SECURITY-PRIVACY-PRD.md), preserving their approved requirements, stable identifiers, source/rights boundaries and history. The owner accepted the qualified security candidate and separately authorized B5 and consolidation on 2026-11-26. AIPF v8.10.1 governs execution; requirements approval does not grant execution authority. See [v1.2.0 qualification and release record](releases/1.2.0.md), [DEC-004](decisions/PRAXIS-DEC-004-specialist-expansion.md) and the [architecture specialist build plan](ARCHITECTURE-SPECIALIST-BUILD-PLAN.md).

**Document lifecycle:** Maintain one canonical product PRD. Temporary specialist PRDs may be developed and approved independently; consolidate their approved requirements at acceptance/release, preserve original approved revisions in immutable Git history, reconcile stable IDs and references, and keep supporting architecture, research, implementation plans and evidence separate. Future QA and DevOps requirements require their own discovery, approval and execution authority.

**Navigation:** [Product and roadmap](#1-product-vision) · [Architecture](#8-architecture--engineering-design) · [Quality attributes](#9-quality-attributes) · [Security & Privacy](#13-security-and-privacy-specialist).

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

**Current roadmap (2026-11-26):** UI/UX v0.3 and Architecture v0.1 are released in v1.1.0. Security & Privacy v0.1 is qualified and owner accepted for v1.2.0; see [Section 13](#13-security-and-privacy-specialist) and the [release record](releases/1.2.0.md). QA & Engineering Quality and DevOps & Reliability remain future; their detailed requirements and execution require separate approval. Review Parity remains deferred.

Historically the next specialist after v1.0.0 was **Software Architecture & Engineering Design**. This supersedes the earlier QA-first planning preference; it does not invalidate the QA research or change the accepted v1.0.0 requirements and evidence.

### Product direction

Specialists add domain expertise and useful techniques rather than a parallel development methodology. Prioritize knowledge that improves decisions before implementation, while retaining support for implementation guidance, diagnosis, critique and verification. AIPF remains authoritative for governance, authorization, proportionality and acceptance. Specialist advice must be evaluated against approved project intent, constraints and the actual implementation context.

In separate-agent workflows, the Prompt Agent consults relevant specialists and translates selected recommendations into concrete, operationally complete Builder Payload instructions. The Builder retains appropriate implementation discretion within the authorized scope and need not access Praxis or its specialist resources. The same capabilities support direct single-agent execution without artificial role separation or handoffs. Optional specialist access does not expand authority.

| Specialist | Roadmap status | Intended contribution |
|---|---|---|
| UI/UX & Design Intelligence | Available in v1.0.0 | Interface design, usability, accessibility and source-linked design knowledge |
| Software Architecture & Engineering Design | Released in v1.1.0 | Appropriate architectural patterns, technology tradeoffs, module boundaries, data modeling, integration contracts, resilience and maintainability; avoid unnecessary complexity |
| Security & Privacy | v0.1 accepted for v1.2.0; see Section 13 | Threat modeling, trust boundaries, authentication, authorization, secure design and data protection |
| QA & Engineering Quality | Future | Risk-based test design, effective assertions, diagnosis, regression strategy and behavioral verification |
| DevOps & Reliability | Future | Deployment strategies, infrastructure, observability, recovery and operational resilience |

The remaining specialist order is an indicative planning sequence, not a delivery schedule. The later priorities may change with actual needs and evidence.

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

## 8. Architecture & Engineering Design

The approved v1.1.0 requirements specify one registered advisory specialist, ID `aipf-architecture` v0.1, with three modes: **design** (new systems and substantial additions), **evolve** (material changes to existing systems), and **critique** (evaluate designs and risks without granting redesign authority). The Prompt Agent or direct agent selects the mode after the canonical AIPF path selection, consults relevant knowledge, then synthesizes the decision and applicable verification implications. A separate Builder receives the authorized operational values and accessible implementation inputs; no hidden framework, guide or catalog access is required. Optional access does not expand authority.

The specialist combines architecture intelligence, technology and service intelligence, and engineering capability intelligence. It covers significant requirements and quality attributes, system structure, module/interface design, technology and cost, data, integration, runtime and resilience, performance/capacity, existing-system evolution, cross-domain implications and external capabilities. Prefer existing assets, no change, native or local options where suitable. Compare viable alternatives against constraints; name assumptions, contraindications, tradeoffs, and revisit triggers. Communicate decisions, boundaries, contracts, invariants, discretion and observable evidence, not a pattern name alone.

### Architecture functional requirements

All AR requirements are retained as the approved architecture baseline; delivered evidence is in the [v1.1.0 release record](releases/1.1.0.md). Initial supported knowledge breadth is explicit; depth varies with actual utility.

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

The product direction derives from the original approved PRD (2026-11-24), DEC-001 through DEC-003, v1.0.0 release evidence, the architecture-first decision (DEC-004), the comprehensive Word PRD v1.1 review draft, the November 25 architecture discovery report and the architecture specialist build plan. The latter contains the public primary-source pointers and dated provider comparisons. The research report and earlier draft are historical working materials, not competing requirement homes. Final PRD revision 1.2 superseded the draft; revision 1.3 retains those requirements and consolidates the approved Security & Privacy requirements. The build plan remains a supporting reference. Detailed implementation and release remain separate authority decisions.


---

## 13. Security and Privacy Specialist

**Approved scope:** Security & Privacy v0.1, retained from the [approved specialist PRD v1.1](https://github.com/S-Pillow/praxis/blob/c6393f6174e8d83e6760cf64bfbe889710d8919d/docs/SECURITY-PRIVACY-PRD.md). All SP, SK, SN, AC, Q and SD identifiers remain unchanged. AC01–14 in this section are specialist-local and distinct from original product AC-01–12 and AS-AC01–10. Historical research, candidate options and planned exercises retain their original evidence and approval boundaries. Original specialist section numbers map to 13.x below.

### 13.0. Document control and inherited product baseline

| Item | Controlled meaning |
| --- | --- |
| Product | Praxis — Intelligence into action; vendor-neutral engineering decision support powered by AIPF. |
| Document | Consolidated product PRD v1.3, Section 13; retains approved specialist PRD v1.1. |
| Historical delivered baseline | v1.1.0: UI/UX v0.3 and Architecture & Engineering Design v0.1; AIPF v8.10.1. |
| Accepted target | Security & Privacy v0.1, Praxis v1.2.0; owner accepted qualified candidate and authorized B5. Publication is verified separately. |
| Requirements authority | Sections 1–12 for inherited PR/AR/KI/NFR and acceptance baseline; Section 13 for approved SP/SK/SN and AC01–14; AIPF governs execution. |
| Historical evidence | [v1.0.0](releases/1.0.0.md), [v1.1.0](releases/1.1.0.md), [architecture build plan](ARCHITECTURE-SPECIALIST-BUILD-PLAN.md). |
| Review status | Owner approved the specialist specification, B1–B4 development, qualified candidate and B5 release/consolidation. A qualified candidate, accepted candidate and published version are different states. |

#### Delivered capabilities and evidence to preserve

| Capability | Released baseline and qualification |
| --- | --- |
| Integrated entry | One repository entry with embedded AIPF projection; no separate framework installation or required orchestration service. |
| UI/UX | Three established modes; 5,500 source-linked design records, read-only search/recommendation and existing output contracts. |
| Architecture | Three established modes; 11 guides, 33 decision cards, 20 shared capability records in 10 families; independent capability index. |
| Registry and helper | Legacy singular chapter and additive chapters_any; optional retrieval; truthful unavailable/not-applicable states; no process execution for architecture lookup. |
| Qualification | 155/155 on Linux and native Windows on final prospective merge; 25/25 separate corrected independent Builder exercise; 155/155 post-merge Linux. [Final PR CI](https://github.com/S-Pillow/praxis/actions/runs/45727998534), [main CI](https://github.com/S-Pillow/praxis/actions/runs/45728139370). |
| Shared source and recovery | Protected main at baseline above; [published v1.1.0](https://github.com/S-Pillow/praxis/releases/tag/v1.1.0); v1.0.0 retained. No release asset/runtime package test or universal host discovery claim. |

Do not rerun historical exercises just to increase test counts. Carry evidence only while controlling source, configuration and environment remain relevant; prove preserved behavior and test the integrated candidate. Prior UI asset restrictions and rights decisions do not automatically cover new source materials. Independent workflow results establish meaningful portability, not a comparative performance claim.

#### Inherited functional and quality requirements

The original product requirements PR-01–14 are retained by reference in their authoritative product PRD. The following is a scope crosswalk, not a rewritten requirement home. Architecture AR-01–14, architecture knowledge KI-01–08 and AS-AC01–10 remain qualified at their prior surface; changes that could affect them require affected regression and the standing suite. New acceptance IDs in this document apply to Security & Privacy only.

| Product requirement family | Application in this proposal |
| --- | --- |
| PR-01–03: unified entry, included AIPF, accessible approved context | Preserve entry and projection; reviewed content and tool access never confer authority (SP-01,12,14). |
| PR-04–06: materiality-driven activation, UI/UX, knowledge/retrieval | Add only material security consultation; preserve existing modes/outputs; disclose unavailable knowledge (SP-01,11,14; SK-01,07). |
| PR-07–09: direct and distinct execution, evidence | No self-handoff; portable T1 payload; attributable review and correction (SP-10,12; AC09,11). |
| PR-10–11: extensibility and discovery | Compatible registration and explicit host fallback; no placeholder skill (SP-13,14). |
| PR-12: packaged plugin exploration | Future; no package or host-specific requirement. |
| PR-13: engineering specialist expansion | Security & Privacy is accepted for v1.2.0; preserve Architecture delivery and original direction decision. |
| PR-14: cross-cutting assurance | Review Parity remains deferred; findings are advisory and source-linked, not an independent approval mechanism. |

All ten product NFRs remain inherited: portability, maintainability, proportionality, correctness, security/privacy, traceability, compatibility, dependency cost, usability and licensing. SN-01–07 are additional specialist-specific constraints, not a replacement. In particular, ordinary users should not learn specialist IDs, query syntax or chapter numbering, and a longer prompt or larger security inventory is not a success metric. Optimize the total decision, clarification, implementation, correction and verification effort.

#### Navigation and precedence

Subsections 13.1–13.3 define outcomes, scope and requirements; 13.4–13.6 define knowledge, evidence and optional capabilities; 13.7–13.9 specify integration, acceptance and delivery; 13.10 is the source register; 13.11 records the stop boundary. Original specialist-local references to sections 0–11 refer to subsections 13.0–13.11, not product Sections 1–12. Original planning language, design questions and dated research are retained as historical requirements intent, not current execution authority or claims of runtime behavior. In a conflict with the accepted product PRD or governing AIPF, resolve the actual scope and owner decision before changing requirements. Do not silently rewrite an accepted invariant.

### 13.1. Product vision and outcomes

Praxis should give a Prompt Agent or direct executing agent practical security and privacy expertise at the point of decision, not only after code has been written. The specialist should help build the simplest sufficient controls for the actual assets, actors, data flows and risks, improve existing systems without avoidable behavioral changes, and distinguish source-backed findings from suspected weaknesses and optional hardening. AIPF remains the sole governing authority for execution, authorization, evidence, acceptance and release.

The product problem is not a shortage of security lists or scanning tools. It is the difficulty of selecting appropriate controls, recognizing material trust boundaries, translating security decisions into implementation requirements, and verifying what a control actually prevents. Privacy needs equivalent attention: avoiding unnecessary collection, limiting exposure, honoring retention and deletion, and evaluating third-party processing. A clean scan, a privacy-oriented brand or a checklist alone does not establish security or legal compliance.

| Outcome | Observable success |
| --- | --- |
| Prevent avoidable design flaws | Identify assets, principals, boundaries, abuse cases and context-appropriate controls before implementation; specify negative tests. |
| Reduce disclosure | Prefer no new collection or external transfer where sufficient; explicitly address logs, identifiers, exports, backups and agent context. |
| Make review actionable | Tie each material finding to evidence, expected behavior, impact, uncertainty and the smallest suitable remediation. |
| Preserve extensibility | Compose with Architecture and UI/UX without new governing rules, mandatory delegation or runtime services. |
| Improve portability | An independent Builder can implement a complete authorized payload without access to Praxis, the source catalog or the PRD. |

#### Users and representative jobs

- Product owners and technical leads: decide what protection is justified, assess residual risks and approve material tradeoffs.
- Prompt Agents and direct developers: choose controls, reason about data and trust boundaries, produce concrete implementation and verification instructions.
- Builders and reviewers: implement authorized controls, test negative cases, assess evidence, correct specific defects and disclose unresolved gaps.
- Operators: understand configuration, data flows, access, recovery and tool risks without having to become security specialists.

Success does not mean more controls, more scanners, more findings or more process. The first release must not claim penetration-testing coverage, universal protection, compliance certification, detection rates or comparative superiority.

### 13.2. Scope and operating modes

The initial component covers material security and privacy decisions in new and existing software. It supports local utilities, web applications, APIs, agents and service integrations; additional platforms are covered only to the extent that the relevant evidence and domain knowledge are available.

| Mode / proposed task ID | Expected behavior |
| --- | --- |
| Design / `security-design` | Establish threat and privacy context, select suitable controls and alternatives, define requirements and observable verification. |
| Harden / `security-harden` | Diagnose a material weakness or changed boundary, preserve approved behavior, select a bounded mitigation and regression tests. No silent fixes. |
| Review / `security-review` | Perform proportionate source-based assessment, distinguish observed evidence from unresolved leads and hardening, specify safe verification and recommendations. |

Activation requires a material security/privacy question or boundary change after canonical AIPF routing. Examples: new identity/session flow, resource authorization, untrusted file or URL handling, sensitive storage, telemetry/export, credential lifecycle, dependency selection, agent permissions or a requested security critique. Routine cosmetic edits, ordinary formatting and unrelated minor fixes do not activate it solely because a chapter applies. Existing specialist consultation remains available; one agent synthesizes recommendations rather than creating competing approvals.

A full audit, live probing, target-controlled execution, dependency installation, persistent audit outputs, credential use, access changes or external data transfer requires separately established authority and capability under AIPF. A request for guidance is not an audit authorization. Security work must remain defensive and scoped to authorized targets; use synthetic inputs and dummy identities for exercises. If execution safety cannot be enforced, do not execute and identify the precise evidence gap.

#### Activation examples and proportionality

| Request or change | Consultation and boundary |
| --- | --- |
| New offline single-user report generator | Design if files, sensitive data or network decisions are material; no mandatory login, service or persistent audit log. Architecture chooses storage; Security defines data and path constraints. |
| Add team sharing or administrative export | Design/evolve with Architecture and Security; define principal, resource, membership, revocation, export scope and negative tests before implementation. UI/UX clarifies sharing state without becoming the authorization control. |
| Existing API rejects valid users after a permission change | Harden: diagnose actual role/ownership/session behavior; do not weaken checks or redesign identity without evidence/authority. |
| User asks to assess an uploaded repository | Review source within approved scope. Clarify target/action/allowed evidence if material; do not infer permission to run code or contact its deployment. |
| New scanner or MCP integration | Design/review data transfers, trust and permissions; select no tool/existing/local alternative if adequate. No installation or connector activation from recommendation alone. |
| Rename a variable, format prose, adjust purely cosmetic style | No security activation unless the edit affects a real boundary (for example, disclosure or a privacy-sensitive UI affordance). Existing specialist routing stays intact. |

#### Decision and output contract

Start from actual intent, existing source and environment, asset sensitivity and actor/resource relationship, relevant trust boundary, externally visible behavior, operational capacity, legal/contract constraints supplied by the owner and what can actually be observed. Distinguish known facts, assumptions and owner decisions. Ask only decision-changing questions; do not assume a multi-tenant or regulated environment when none is established.

| Step | Useful output |
| --- | --- |
| Frame | What security/privacy decision is material; what behavior and data must remain unchanged; what is explicitly out of scope. |
| Establish context | Assets, actors, flows, trust/privilege boundaries and actual existing controls; note unavailable implementation facts. |
| Compare | Retain/no new collection or service, existing control, suitable local or managed alternative; identify applicability, usability, cost and failure tradeoffs. |
| Recommend | Explain simplest sufficient option, preconditions, contraindications and material unresolved choices. For hardening, identify the smallest effective delta. |
| Translate | Concrete invariants and permitted operations, interfaces/configuration assumptions and meaningful implementation discretion; negative as well as positive verification. |
| Reconcile | State evidence strength, observed behavior, residual uncertainty, owner decision or safe stop; no invented proof or automatic approval. |

Example (illustrative, not a test result): a CSV reporting utility for private local records does not need an account service or remote analytics. Choose local processing, user-selected input, bounded parsing, explicit output location, no implicit network/retention, and sanitized error messages. Verify accepted inputs, rejection without partial effects, repeated execution, preserved input and absence of forbidden writes/transfers within the observable test scope. Encryption at rest depends on the actual threat and storage environment; do not invent a custom scheme. The Builder may choose helpers and file layout within the stated constraints.

#### Explicit exclusions for the first release

- No embedded scanner, exploit catalog, autonomous pentest harness, mandatory multi-agent system, hosted audit service, secrets manager, telemetry, network crawler or new database.
- No automatic installation, account creation, external scanning, upload, remediation, production policy change or release action.
- No duplicated AIPF governance, Review Parity runtime or future QA/DevOps specialist implementation.
- No bulk source import, blanket license clearance, legal advice, compliance certification or mandatory framework-specific control on every project.

### 13.3. Functional requirements

All SP requirements are approved Must requirements for the first qualified candidate unless an explicit scope decision changes them. Acceptance IDs are in section 8. The specialist supplies advice and concrete requirements; only the active project authorization permits action.

| ID | Requirement and observable behavior | Acceptance |
| --- | --- | --- |
| SP-01 | Activate by material security/privacy intent after canonical AIPF routing. Support design, harden and review; skip unrelated work and disclose unavailable guidance. | AC01, AC02 |
| SP-02 | Map relevant assets, actors, data flows, entry points, trust boundaries and security/privacy objectives; use abuse cases and context-specific threat lenses (e.g., STRIDE or LINDDUN) when useful. | AC03 |
| SP-03 | Design identity, authentication, session and authorization controls appropriate to the system; distinguish authentication from resource-level permission, tenant isolation and least privilege. Avoid unnecessary accounts. | AC03, AC04 |
| SP-04 | Identify untrusted inputs, outputs, file/path, URL, protocol and service boundaries. Recommend validation, safe APIs, context-aware encoding, bounded processing and safe failures with negative tests. | AC04, AC05 |
| SP-05 | Advise on secret lifecycle, storage, rotation, revocation, vetted cryptography, transport and key ownership. Do not disclose real secret values or invent cryptographic schemes. | AC04, AC06 |
| SP-06 | Identify purposes, collection alternatives, data categories, identifiers, recipients, retention, deletion/export, logs and backups. Distinguish minimization, pseudonymization and anonymity; do not imply legal compliance. | AC06 |
| SP-07 | Assess dependency, package, build, CI and release trust, including provenance, vulnerability evidence, update/rollback and third-party terms; distinguish inventory from verified reachability or risk. | AC07 |
| SP-08 | Treat repo files, skills, prompts, model outputs and tool data as untrusted content rather than authority. Address agent permissions, MCP/tool access, sensitive context, output handling and approval boundaries. | AC08 |
| SP-09 | Recommend context-appropriate configuration, rate/resource bounds, error handling, abuse prevention and security-sensitive monitoring. Do not add services or data collection by default. | AC03, AC05, AC06 |
| SP-10 | Review actual source and available behavior; retain scope and coverage limits, classify findings truthfully, consider existing controls and counterevidence, and propose a proportionate correction. | AC05, AC09 |
| SP-11 | Qualify optional tools against existing/local/no-tool alternatives, rights, access, network/data transfer, cost, result limitations and current version; no unapproved integration or execution. | AC07, AC10 |
| SP-12 | Provide complete implementation constraints, permitted actions, negative tests, evidence expectations and unresolved assumptions in direct or distinct-Builder work. Preserve Builder independence from governing resources. | AC11 |
| SP-13 | Compose material Architecture, UI/UX and Security advice coherently; preserve original behavior and scope unless an authorized change is necessary. Surface conflicts for owner decision. | AC12 |
| SP-14 | Preserve AIPF v8.10.1, existing registry behavior, UI/UX catalog/retrieval, Architecture guides/capability records, released tags and standing regression baseline. | AC01, AC13 |

### 13.4. Knowledge architecture and curation

Use a small progressive guide set and original, source-linked decision records. Begin with a focused skill entry and index; load only relevant guides and cards. The following nine domains define coverage, not a quota for number of cards or a requirement to use all domains for each task. Each candidate topic must justify its value, source and verification implications before inclusion.

| Domain / suggested guide | Initial decision topics |
| --- | --- |
| Threat modeling & trust boundaries | Asset/principal inventory; data flow and boundary mapping; security versus privacy threats; abuse cases; existing controls; risk and proportionality. |
| Identity & access | No-account/local alternative; approved identity provider; credential and session lifecycle; permission checks; tenant isolation; administrative operations and recovery. |
| Secure interfaces & data handling | Input contracts, context-aware encoding, injection prevention, file/path/URL boundaries, webhooks, service trust, bounded parsing and error responses. |
| Secrets, crypto & communication | Secret classification, references not values, storage and rotation, vetted libraries, transport protection, key ownership, revocation and backup. |
| Privacy & lifecycle | Purpose and minimization, identifier correlation, telemetry, analytics, replay and masking, third-party transfer, retention, export/deletion, derived data, backup restoration. |
| Software supply chain | Package provenance, dependency inventory/SBOM, advisory freshness, reachability limits, lockfiles, CI least privilege, signing/update provenance, reproducible remediation. |
| AI agents & MCP | Untrusted content, tool permissions and side effects, delegated authority, context minimization, prompt injection, output validation, sandboxing and explicit external-transfer boundaries. |
| Deployment & abuse resistance | Secure defaults, configuration, network boundaries, availability/resource limits, admission controls, error/log redaction and security event handling. |
| Assessment & remediation | Scope and coverage, source evidence, existing mitigations, finding classification, independent verification when required, minimal correction, regression and residual risk. |

#### Initial decision-card inventory — build coverage, not a card-count quota

These 36 proposed decision questions make the nine-guide plan concrete. IDs are planning identifiers; B1 may consolidate or split records when there is a demonstrated reason, retaining a mapping so no decision coverage disappears. Each row identifies useful output and a verification or contraindication. No source text is incorporated verbatim. Source codes refer to section 10; exact primary clauses and rights remain B1/B2 work.

| ID / decision | Intended guidance and evidence |
| --- | --- |
| SD01 • Asset, actor and data-flow model | Identify protected resources, principals, sensitive flows, entry points and trust transitions; validate against actual context, not a generic diagram. PS-02. |
| SD02 • Threat and privacy risk lens | Choose STRIDE, LINDDUN or targeted abuse cases where useful; distinguish harm to people from system compromise. PS-02,04. |
| SD03 • Existing controls and residual risk | Identify controlling mitigation, defense in depth and owner risk decisions; avoid redesign where current control suffices. SR-06,07. |
| SD04 • Security requirements and trust contract | Convert risks into explicit allow/deny invariants, abuse cases and relevant observations; do not confuse a checklist with verification. PS-01,02. |
| SD05 • Identity need and trust source | Local/no-account, existing or approved identity service; identify identity proof and recovery constraints before proposing new accounts. PS-01. |
| SD06 • Authentication and credential lifecycle | Prefer vetted mechanisms, appropriate MFA/recovery/rate limits based on risk, test successful and failed login and revoked access. PS-01. |
| SD07 • Session and token lifecycle | Establish issuance, validation, audience/scope, expiry, rotation/revocation and safe storage; distinguish browser and machine credentials. PS-01. |
| SD08 • Resource and tenant authorization | Enforce server-side principal/resource/action permission, default deny where appropriate, test cross-tenant/role access and revoked membership. PS-01. |
| SD09 • Input and output contracts | Validate types, sizes and semantics at actual boundary; parameterized operations, context-aware rendering and safe error messages; test invalid and benign inputs. PS-01. |
| SD10 • Files, paths and uploads | Approved root, ownership, limits, parsing, storage and content type; safe reject/cleanup; avoid untrusted code execution and path assumptions. SR-07, PS-01. |
| SD11 • URLs, outbound requests and callbacks | Define allowed destination/service trust, redirect behavior, request authentication, replay and resource limits; verify bounded synthetic cases. SR-07, PS-01. |
| SD12 • Protocol, client and integration boundaries | CORS/CSRF, webhooks, serialization, message identity, cache and client-side state where applicable; do not treat UI hiding as enforcement. SR-06, PS-01. |
| SD13 • Secrets discovery, storage and access | Classify secrets, use references and approved storage, prevent exposure in source, logs, fixtures and agent context; no real values in evidence. PS-01,03. |
| SD14 • Key/credential rotation and recovery | Ownership, least privilege, revocation, rotation, expiration and recovery; define response without unauthorized credential changes. PS-01,06. |
| SD15 • Vetted crypto and transport | Match threat to vetted libraries/protocols and key lifecycle; distinguish password hashing, integrity and encryption; no bespoke crypto or unsupported numeric mandates. PS-01. |
| SD16 • Sensitive storage and backups | Map data-at-rest protection, access, backup/restore and failure tradeoffs; prove intended scope rather than promise encryption solves all risks. PS-01,04. |
| SD17 • Purpose, minimization and collection | Establish necessary fields/recipients and no-collection alternative; distinguish data subject harm, consent/notice needs and unresolved legal obligations. PS-04. |
| SD18 • Identifiers, analytics and session replay | Distinguish cookieless, pseudonymous and anonymous; examine event fields, correlation, masking, payloads and optional features. SR-04. |
| SD19 • Retention, deletion, export and derived data | Define authorized lifecycle across primary store, caches, logs, backups, exports and processors; specify verifiable deletion scope and exceptions. PS-04, SR-06. |
| SD20 • Local processing and external disclosure | Compare local versus cloud transformation; assess clipboard, extension trust, logs and public artifacts; verify actual disclosure boundary. SR-03,08. |
| SD21 • Dependency selection and provenance | Existing/no dependency first; inspect origin, version, lockfile, maintainership, rights and install/runtime permissions. PS-03. |
| SD22 • Advisory applicability and freshness | Distinguish version match, affected feature, reachable behavior, mitigation and unknown facts; absence of advisory is not assurance. SR-02, PS-03. |
| SD23 • SBOM and build/release integrity | Inventory exact artifact components, CI least privilege, provenance and update verification where material; no blanket SBOM compliance claim. PS-03,07. |
| SD24 • Targeted remediation and rollback | Verify recipe/patch applicability, license, preview and preserve contracts; test affected behavior and retain previous known-good state. SR-05, PS-03. |
| SD25 • Untrusted model/repository content | Treat prompts, tool responses, retrieved files and generated values as data; separate governing authority and real user consent. SR-01,06,07; PS-05. |
| SD26 • Agent tools, MCP and delegated access | Qualify permissions, side effects, resource/data scope, dependency trust and independent authorization; no implicit privilege expansion. SR-02, PS-05. |
| SD27 • Sensitive context and output | Minimize prompt/context disclosure, redact reports, validate model/tool output before use; test refusal to follow untrusted instructions. PS-05. |
| SD28 • Isolation and artifact trust | Separate authorized read-only inspection from sandboxed execution; scratch-only output and trusted promotion; report unobservable checks. SR-06. |
| SD29 • Secure runtime and configuration | Select secure defaults, approved roles, network ingress/egress and environment-specific configuration; avoid hidden infrastructure changes. PS-06. |
| SD30 • Resource and abuse limits | Identify admission, payload, queue, concurrency and quota boundaries; select graceful failure and tests with synthetic local load only. PS-01,06. |
| SD31 • Security events and operational signals | Identify actionable events, access, redaction, retention, release correlation and incident-owner escalation; no telemetry by default. PS-04,06. |
| SD32 • Change and recovery readiness | Config drift, restore, revocation and recovery of security controls; coordinate with Architecture and future DevOps without implementing their scope. PS-03,06. |
| SD33 • Scope, coverage and evidence plan | Map reviewed surfaces, revision/configuration, authorized observers and exclusions; never infer comprehensive audit coverage from source listing. SR-06. |
| SD34 • Finding classification and refutation | Evidence trace, affected principal/resource, existing mitigation, bounded outcome, disposition and counterevidence; no speculative severity. SR-06. |
| SD35 • Remediation and security regression | Smallest correction, preservation of intended behavior, negative/positive checks and independent verification when required; retain unresolved facts. SR-05,06,07. |
| SD36 • Responsible disclosure and residual risk | Restrict private findings, use owner-approved reporting channels, preserve uncertainty and track recheck conditions; no public disclosure or legal certification. PS-03,04. |

#### Curation workflow and selection decisions

Use the initial source register and source-level discovery map. Extract decision questions rather than copy catalogs or enforce an external skill's workflow. Compare primary sources when recommendations differ; choose applicability over numeric presets. For each included guide, review positive examples, contraindications, context and a safe check. For rights, distinguish the repository license from file-level licensing, code dependencies, linked training materials, images, standards and vendor terms. If reuse rights remain unclear, retain a source pointer or original synthesis only. Do not treat permission to link as permission to reproduce. Reject material with no practical decision value, unsupported assurances, mandatory third-party tooling or conflicting governance. Index only curated records that exist; no phantom entries. Preserve dated facts and recheck on meaningful source/terms changes rather than a blanket refresh schedule.

#### Knowledge and source requirements

| ID | Requirement |
| --- | --- |
| SK-01 | Maintain a navigable index of unique decision IDs, topic/trigger and canonical guide; verify all internal references and domain coverage. |
| SK-02 | Each decision record states context, decision question, alternatives (including no change), suitable/unsuitable conditions, risks and constraints, concrete guidance, verification, sources and known limits. |
| SK-03 | Record source identity, author/publisher, URL, edition or immutable revision, observation scope/date, rights disposition and claim supported. Distinguish original synthesis from excerpts, provider statements, direct observation and inference. |
| SK-04 | Prefer primary standards and official documentation; use community collections for discovery. Check conflicting guidance, applicability and current versions before using decision-sensitive facts. Do not universalize numeric thresholds. |
| SK-05 | Keep stable knowledge separate from volatile vendor features, plan terms, advisories and costs. Reverify material facts at point of use and report unavailable evidence rather than fabricate. |
| SK-06 | Preserve attribution, notices and file-level rights. No third-party code/text import until reuse rights are established. Reference-only or original synthesis is the default. |
| SK-07 | Extend the independently usable shared capability index; do not create a competing provider directory, mandatory retrieval engine or redundant copies of architecture guidance. |
| SK-08 | Include positive/negative examples and safe verification implications; reject irrelevant offensive scripts, certification dumps, tool install instructions and alternate authority models. |

#### Suggested decision record contract

Stable ID; domain; trigger and decision question; project context assumptions; alternatives and rationale; applicable/non-applicable conditions; implementation constraints; security/privacy tradeoff; negative/positive checks; unresolved facts and revisit trigger; primary reference(s), date/version and rights disposition. A card is advisory knowledge, not a finding, execution instruction or authorization. Knowledge examples must use dummy data.

### 13.5. Findings and verification integrity

A security review must distinguish evidence from a hypothesis. A source location or scanner warning does not by itself demonstrate an exploitable boundary failure. Identify the affected principal, protected resource, expected control, relevant source/configuration, counterevidence and observed result. Do not imply a stronger impact than evidence supports.

| Disposition | Required interpretation |
| --- | --- |
| Confirmed | Concrete boundary/control failure established by source and/or sufficient bounded observation; material claims independently verified when required by AIPF. Record exact verified surface and impact. |
| Needs validation | Plausible source-backed concern with an exact missing fact, environment, permission or observation. No definitive severity or success claim when evidence is insufficient. |
| Rejected | Evidence refutes the candidate or establishes an effective controlling mitigation. Preserve concise reason when material. |
| Hardening / design recommendation | Optional defense-in-depth or architectural improvement; do not report as a confirmed vulnerability solely because another layer could be added. |

These are security-domain interpretations of evidence, not a replacement for AIPF outcome or acceptance vocabularies. Use severity/likelihood and impact only at the strength supported by the available facts; identify methodology/version and assumptions. Report coverage as assessed surfaces and exclusions, not a percentage unless the denominator is defined and evidenced. Avoid equating no findings with a secure system.

#### Evidence contract and safe observation

For material findings, retain an ID/fingerprint, source revision, target/configuration, trace and relevant lines, expected control, evidence attribution, counterevidence, disposition, bounded impact, recommended correction, regression check, unresolved fact and recheck trigger. Redact sensitive values and avoid putting private findings in public issues or PRs. Revalidate affected evidence after source/configuration changes. Prior evidence transfers only for unchanged controlling conditions.

A scoped review is source-read-only by default. Actual execution of untrusted target code requires an authorized isolated environment with no external network, sanitized environment, read-only source/toolchain, scratch-only writes and bounded resources. Use dummy accounts and data, never live targets or real secrets; record inability to observe if required controls are missing. No automatic finding publication, broad scans or retention of sensitive artifacts. Independent verification is real, named and observable, not simulated by relabeling the same agent.

#### Coverage and evidence lifecycle

Use a lightweight review record where the review is consequential; simple guidance may need only a decision and stated limits. A proposed record is a conceptual contract, not a requirement to add JSON storage, validators or a new review runtime. Reviewers identify checked and unchecked surfaces, actual observed inputs, source/configuration identity, required controls, what was not executable, and which evidence would change the verdict. Consolidate duplicate candidates by root cause and preserve a stable finding identity if classification changes. Keep evidence and derived summaries aligned after correction; an earlier warning may be rejected, unresolved, corrected and revalidated, not simply deleted to obtain a clean report.

| Field group | Required information when material |
| --- | --- |
| Scope and authority | Authorized target/revision, purpose, explicit excluded systems/actions, data-handling boundary. |
| Finding identity | Stable ID, affected principal/resource, control and source trace; separate root cause from multiple symptoms. |
| Observation | Actual source/tool/operator evidence, source/config identity and attributable observer; observed result vs inference. |
| Counterevidence | Existing guard, assumptions, negative evidence, environment limitations; exact unresolved dependency if any. |
| Disposition | Confirmed, needs validation, rejected or hardening; bounded impact and rationale, severity only where justified. |
| Correction and continuity | Minimum suitable change, preserved invariant, regression/recovery evidence, owner and recheck trigger. |

Example: a scanner flags a database query construction. Source inspection shows an approved parameterized execution path and test evidence confirms untrusted values remain data. Record the actual check and reject the candidate where that control governs the reported path; if an alternate execution path remains unknown, preserve a separate unresolved concern. If an unrelated defense could be strengthened, report it as hardening. Do not use a scanner warning, test green status or absence of other warnings as a whole-system conclusion.

A full audit workflow is an optional future engagement pattern, not a first-release mandatory mode. Source-only review is still meaningful when runtime isolation or a separate verifier is absent. Required independent verification must be performed by an actual distinct observer or appropriate independent method under AIPF; otherwise report the observation as pending. The security specialist does not create its own audit approval, risk acceptance or release authority.

### 13.6. Shared capability intelligence

Use the existing `knowledge/capabilities/` index and `QUALIFICATION.md`. Candidate records are discovery aids, not approved dependencies. The proposed list is intentionally selective and may be pruned if a record adds no decision value. Qualify official documentation and terms for the exact version, deployment, plan and relevant rights before inclusion; actual executions require separate approval.

| Candidate | Role and qualification boundary |
| --- | --- |
| Safe Anything | Local pattern-based code, secrets, agent and configuration scanner; no data-flow guarantee; offline mode omits OSV queries. Confirm exclusions and redaction claims before use. |
| OSV-Scanner | Dependency advisory lookup; qualify online metadata transfer, offline database setup/freshness and unsupported ecosystems. |
| Semgrep / Gitleaks | Static analysis and secret detection candidates. Engine, rules, history scope, network and licensing must be qualified separately; no tool execution yet. |
| GitHub security features | Existing repository-native alternatives; distinguish availability, plan/visibility requirements, access and output disclosure. |
| CycloneDX / Dependency-Track | Inventory and component-risk management; SBOM contents may be sensitive, inventory is not vulnerability or compliance proof. |
| OpenRewrite | Targeted deterministic remediation; inspect module/recipe rights, preview exact delta, preserve behavior, test and review; no bulk automatic edits. |
| Umami | Analytics privacy case and optional capability; inspect collection, identifiers, replay, retention and self-hosted/cloud differences. |
| DevToys | Local developer processing candidate; consider clipboard, logs, extensions and third-party boundaries. |
| aeo.js | Cross-specialist public content generation candidate; inspect exported content, access boundaries and rights. No code reuse while revision/license unknown. |

Every qualified record should include the problem solved, supported environment, local/no-tool alternative, version/evidence, data entering/leaving the boundary, permissions, cost/limits where material, license, false-positive/false-negative or other constraints, failure/exit behavior, and authorized-use caveat. Prefer no new service when sufficient. No runtime dependency, account, credential, scanner integration, MCP activation or data export is part of this build.

#### Capability selection matrix and cost/data assessment

Use the existing capability index before considering new records. Each candidate below remains unqualified for operational use unless explicitly supported by the stated source observation. Product selection, configuration and execution are outside this PRD authorization. Do not turn a catalog into an install list.

| Decision family | First alternatives | Decision-critical questions |
| --- | --- | --- |
| Static source analysis | Manual scoped review; existing lint/CI; local Safe Anything or Semgrep | Language and rule coverage, source transfer, ignored/generated files, result sensitivity, rule rights, false positives/negatives. |
| Dependency advisories | Existing lockfile/native audit; OSV-Scanner or repository-native features | Offline database freshness, metadata transfer, ecosystems, transitive paths, reachability, update/rollback. |
| Secrets | Existing commit review or approved local scanner; Gitleaks/Safe Anything | History versus current tree, redaction, exclusions, false positives and safe credential-response ownership. |
| Inventory | Existing lockfile/build manifest; CycloneDX; Dependency-Track only if needed | Exact artifact coverage, identifiers, transitive dependencies, access to SBOM, retention and operating burden. |
| Remediation | Small reviewed patch; existing migration tooling; OpenRewrite | Recipe applicability/terms, preview, no mass changes by default, tests and recovery. |
| Analytics/privacy | No analytics, aggregate existing metrics, local processing; Umami if qualified | Purpose, event identifiers, replay, masking, access, retention/deletion, recipients, self-host/cloud and costs. |
| Local developer data | Standard library or existing local utility; DevToys | Sensitive input, clipboard, log persistence, update/extension trust, offline behavior. |
| Public artifact disclosure | Existing generated site checks; aeo.js if already justified | Generated text/metadata/indexes, intended public content, access protection, rights/version. |

For a candidate with costs or external calls, specify plan/edition, commercial eligibility, data residency/processor and retention, units/limits, expected and peak usage, failure or exhaustion, hard spend control and operational exit. Price-free or open-source does not mean zero cost, no disclosure or legal permission for all usage. Compare existing approved alternatives and confirm whether a materially required fact is knowable without installation or transfer. If not, explicitly leave the candidate unqualified; no speculative estimate substitutes for a required hard cap or legal/data-processing decision.

Concrete source-observed distinctions for the first release:

- Safe Anything documents a pattern-first engine, skipped paths/file sizes and no general data-flow guarantee. Its offline option omits the OSV dependency query, not just telemetry; record reduced coverage rather than assert equivalent offline results. The documented outbound metadata is package names, ecosystem and versions, not source contents. Runtime redaction/network behavior remains unobserved.
- Umami is a privacy-oriented architecture reference; inspected schema fields include distinct IDs, session links, event/query fields and replay configuration. A requirement forbidding linkable identifiers cannot be satisfied by a cookieless label. Compare no tracking, aggregate-only local counts and an explicitly approved event model. Do not infer a vulnerability from schema presence.
- DevToys documents local utilities and a privacy policy; extension terms explicitly introduce third-party trust. Qualify specific utility/extension data flows rather than promising the full application never communicates externally.
- OpenRewrite core root license and individual parser/recipe terms differ. Qualify exact component, code rights, project/environment compatibility and reviewed diff; the commercial platform is a separate decision.
- aeo.js generated content is a disclosure surface, not a security control. No code reuse while license/revision is unverified. It may remain reference-only if no meaningful capability record is justified.

No new scanner runs are required to qualify the advisory specialist's baseline. If a chosen record depends on a runtime claim that cannot be established from available authoritative documentation, record the limitation and obtain separate bounded execution authorization before asserting it. Use synthetic output to test finding interpretation without pretending it is a scan.

### 13.7. Integration and nonfunctional requirements

#### Logical design

Use the existing Praxis entry, registry and helper; AIPF chooses the applicable path first, the agent identifies material security/privacy intent, and optional specialist consultation returns advice. The agent reconciles domain contributions into one authorized execution decision or payload. Architecture owns structure and tradeoffs; Security owns risk, controls and privacy; UI/UX owns interaction/accessibility, including comprehensible privacy choices; QA owns broader behavioral verification; DevOps owns broader operational delivery; Review Parity remains deferred. Domain boundaries are advisory, not exclusive; cross-domain issues should be synthesized, not duplicated.

Proposed paths: `skills/security-privacy/SKILL.md`, `INDEX.md`, `SOURCES.md`, nine progressive guides, additive `knowledge/capabilities/` entries, `skills/specialists.json` registration, narrowly affected entry/helper/tests/docs. Exact path naming and applicability representation are B1 design decisions. Security can be relevant across more than Chapters 11/12; do not restrict it solely to one application type or introduce a new AIPF chapter. Determine the smallest compatible representation after inspecting the existing registry/helper and canonical routing; no unconditional activation by chapter alone. Existing UI singular `chapter` and architecture `chapters_any`, optional lookup semantics and serialized legacy outputs must remain compatible.

#### Proposed integration surfaces and compatibility gates

| Surface | Expected implementation boundary (B1 to confirm) |
| --- | --- |
| `skills/security-privacy/` | One authoritative skill, index, sources and nine progressive guides; source-linked decision IDs, mode guidance, truthful fallback. |
| `knowledge/capabilities/` | Extend existing index/sources and relevant family files, preserving all 20 existing records and their identities; new security categories only if justified. |
| `skills/specialists.json` | Add one real entry for three material task IDs; preserve existing schema and entries. Confirm appropriate canonical path applicability rather than presume Chapter 11/12 only. |
| `skills/praxis/SKILL.md` and discovery | Integrate materiality selection and synthesis; existing adapters and canonical path selection remain controlling. No new host dependency or mandatory specialist loading by Builder. |
| `scripts/praxis_context.py` | Reuse registry semantics where possible. If an additive compatibility change is necessary, prove existing status/output equivalence, unsupported/invalid mode behavior and no process invocation for a no-tool specialist. |
| CI, tests and docs | Focused routing, source/ID/link, fallback and preservation tests; verify workflow path coverage for actual changed locations. Keep native Linux/Windows regression and historical fixtures. No unapproved network/tool installation. |

Exact released code should be inspected at B1 before fixing registry chapter representation or helper deltas; this is proposed architecture, not a claim of tested integration. Preserve the existing product and framework paths, full catalog/rights, search and recommendation scripts, published tags, tests and historical evidence unless separately authorized. Where a shared interface changes, compare legacy serialized results, not just new tests. Where a candidate has no retrieval script, a request for optional lookup must return an accurate not-applicable/unavailable result as appropriate to the established contract and perform no process or network action.

#### Role and portability contract

| Responsibility | Direct mode | Distinct Builder mode |
| --- | --- | --- |
| Intent and scope | One executing agent applies AIPF and owner-approved context. | Prompt Agent derives authorized unit and retains reasoning; owner decisions remain explicit. |
| Domain advice | Load only relevant security/architecture/UI guidance. | Prompt Agent selects and reconciles relevant knowledge; Builder need not load it. |
| Implementation | Act within confirmed target, authority and safety boundary. | Current T1 payload contains target, accessible inputs, requirements, permitted/forbidden effects, constraints, negative tests, evidence and stop. |
| Validation | Observe actual evidence; independent observer where required. | Builder reports actual changes/results, no invented tests; Prompt Agent independently reconciles, arranges required observations and decides disposition within authority. |

For example, a Builder tasked with a disposable ownership-checked local resource function receives the dummy actor/resource contract, authorized read/update behavior, default-deny and error rules, forbidden networking or real data, tests for owner/non-owner/unknown actor and stop condition. It does not need the PRD, source register or specialist guide. Avoid prescribing every internal helper when the invariant is sufficient. Distinct Builder access to optional governing resources cannot expand permissions. A direct agent executes without a manufactured self-handoff.

Security & Privacy has no authority to force technology choices over Architecture or mandate a user-facing design over UI/UX. If a proposed convenience weakens a material resource check, preserve the boundary and consider simpler safe UX. If privacy requirements preclude analytics, Architecture must not add an event store by default. Where the owner must choose an intended tradeoff, disclose the conflict and stop only dependent work. Future QA and DevOps will share verification and operational knowledge; Review Parity remains a separate potential assurance mechanism. No proof receipt, automated approval, audit platform or generalized workflow extension is added here.

#### Performance and usability expectations

Security consultation should be discoverable through natural language, not require manual catalog browsing or an explicit command for every task. Keep the initial entry concise; read only decision-relevant guides. A longer checklist is not a measure of security. Favor the fewest tools and least access that establish needed evidence, while preserving correctness, coverage and risk-appropriate review. No promised latency, token savings or detection-rate improvement without an explicit measurement plan and actual observations.

| ID | Quality constraint |
| --- | --- |
| SN-01 | Preserve AIPF authority, existing product/version boundaries and explicit scope. Neither source material nor scanner finding grants action authority. |
| SN-02 | No new mandatory runtime, external dependency, storage, telemetry, paid quota or provider integration. Prefer bounded, progressive loading and existing helper mechanisms. |
| SN-03 | Privacy by default: minimize collection/retention, no real secrets in output/fixtures, no silent network or target execution; sanitized evidence and scope-safe storage. |
| SN-04 | Portability: direct mode and independent Builder payload; no hidden governing context, unavailable capabilities or mandatory separate agent. |
| SN-05 | Reproducibility: pinned source and exact test identity, cross-platform UTF-8/path handling, deterministic local fixtures, raw statuses and truthful limitations. |
| SN-06 | Maintainability: unique IDs, links, source rights, small original knowledge, clear separation of stable vs volatile information; do not duplicate AIPF or prior specialist content. |
| SN-07 | Security/availability claims proportionate to evidence; no guarantees, certification, universal detection or benchmark superiority without separately authorized evidence. |

### 13.8. Acceptance and qualification

The following criteria are approved release-candidate gates, not themselves completed evidence. See the [qualification and release record](releases/1.2.0.md) for observations. The candidate must satisfy each applicable criterion, with exact source identity, actual results, evidence ownership, limitations and recovery anchors. A blocked required observation is not a pass. Any owner acceptance and publication decision remains separate.

| ID | Acceptance criterion and evidence |
| --- | --- |
| AC01 | Positive material task activation in all three modes and negative unrelated/minor cases; existing UI and Architecture behavior unchanged. Deterministic registry/helper and integration tests. |
| AC02 | Missing guide/tool/source or unsupported host produces truthful fallback or explicit decision gap; no fabricated references, results or subprocess. Negative tests and actual guidance observation. |
| AC03 | New-system scenario maps assets, actors, data flows and risks; selects suitable controls including no new service/account where appropriate; explains tradeoffs and negative checks. Observed design output. |
| AC04 | Disposable identity/resource scenario tests authorized and unauthorized access with dummy principals, session/credential boundaries and no real secrets. Positive/negative behavior observed. |
| AC05 | Existing-source critique or safe fixture traces an actual boundary, evaluates controls and selects minimal remediation preserving approved behavior. No live probes. Regression demonstrates correction where implemented. |
| AC06 | Privacy scenario evaluates identifiers, retention, log/export, analytics/replay and deletion/backup behavior; rejects unnecessary collection; does not equate cookie absence with anonymity. Source-grounded decision and synthetic verification. |
| AC07 | Supply-chain/remediation exercise distinguishes inventory, advisory freshness, applicability and actual evidence; qualified tool alternatives and targeted diff/test plan; no unapproved installation. |
| AC08 | Agent/MCP scenario treats malicious-looking untrusted content as data; rejects authority expansion, secret disclosure and unapproved network/privileged actions. Observable negative behavior. |
| AC09 | Review exercise produces distinct confirmed, needs-validation, rejected and hardening records with trace, counterevidence and limited impact; real independent observation where required, no fabricated sandbox or severity. |
| AC10 | Point-of-use sample capability qualification records source/version, rights, data transfer, access, limitations and no-tool alternative; unavailable/unsafe options remain unselected. |
| AC11 | Fresh independent Builder implements a complete bounded security/privacy payload without Praxis/AIPF/PRD access; reviewer executes returned code/tests and independent negative checks, reconciles findings and corrections. Direct mode separately observed. |
| AC12 | Combined Architecture + Security + UI/UX design/review yields coherent requirements, resolves conflicts or escalates material choices, preserves approved scope. No duplicated governance. |
| AC13 | Full standing suite (155 at v1.1.0) plus new focused checks passes on exact integrated candidate; Linux and native Windows at pre-release. Protected source/behavior verified; no unapproved dependency or network operation. |
| AC14 | Source provenance, rights, knowledge coverage, documented usage, limitations, recovery and independent evidence reconciled against SP/SK/SN criteria; owner accepts before merge/publication. |

#### Representative exercise set

Combine scenarios where sensible, without substituting one kind of evidence for another. A realistic small API with dummy users and resources can cover tenant isolation, input validation, negative tests and portable Builder handoff. A local-only utility can test no unnecessary network or persistence, secret-safe logs and fallback. A privacy-oriented dashboard can exercise retention, telemetry minimization and combined UI/Architecture/Security consultation. A controlled source-only review of an existing app can assess trust boundaries and findings without contacting deployed services. A deliberately untrusted agent-input fixture can test permissions and non-disclosure. A scanner result can be represented by a synthetic fixture; real scanning is not mandatory and requires separately authorized capability. Include failure/correction and reopening where material.

Evidence types: deterministic tests for mechanisms, observed semantic decisions for advisory quality, source references for claims, actual independent handoff for portability, and hosted CI on exact release-bound source for cross-platform regression. Record commands, raw exit/status, environment, commit/tree, observer and limitations. Do not count disposable exercise tests as product regression tests. No mandatory comparative benchmark or new audit infrastructure.

#### Detailed qualification matrix

This matrix elaborates the existing AC01–14 gates rather than adding an unrelated benchmark. B1 selects 2–3 combined practical exercises plus focused deterministic/negative checks as needed, keeping every criterion traceable. Proposed scenarios use disposable data, source-only inspection and explicit capabilities. No production access, real user data or scanner installation is required.

| Case and requirement mapping | Required observable result and failure condition |
| --- | --- |
| Q01 — Material activation (AC01/02; SP-01,14) | All three proposed modes resolve for appropriate canonical paths; formatting or irrelevant chapter presence does not activate. Unavailable guide/tool reports truthful fallback. Fail on placeholder registration, fabricated lookup, unexpected subprocess, changed UI/Architecture output. |
| Q02 — New minimal design (AC03; SP-02,03,09) | Given actual constraints, compare no-account/no service, existing and suitable control options; map principal/resource boundaries, state tradeoff and test. Fail on unjustified new service, missing authorization decision or claims unsupported by inputs. |
| Q03 — Resource isolation (AC04; SP-03,04,05) | Disposable two-actor resource fixture: authorized action succeeds, other actor and unknown actor denied without data leak or write; appropriate credential/session failure cases when present. Test boundary rather than UI visibility. |
| Q04 — Safe inputs and regression (AC05; SP-04,09,10) | Actual source trace or local fixture identifies an invalid input/control issue; bounded correction rejects invalid and preserves valid operations, error/cleanup behavior and prior data. Source review alone cannot claim runtime success. |
| Q05 — Privacy-first dashboard (AC06/12; SP-06,09,13) | Compare no analytics, minimal local counts and permitted analytics option; identify IDs, replay/log/export, retention/deletion/backup, recipient and usability. Reject incompatible collection; reconcile Architecture and UI choices. Verify selected synthetic behavior where implemented. |
| Q06 — Supply-chain evidence (AC07/10; SP-07,11) | Synthetic inventory/advisory records distinguish exact version match, applicability, mitigation and missing freshness. Local/existing alternatives and bounded remediation diff/test plan; no external advisory request unless authorized. Fail on blanket security/compliance or free-use claim. |
| Q07 — Agent/tool boundary (AC08; SP-08) | Treat untrusted fixture instructions as data; demonstrate no unauthorized tool call, context disclosure, credential access or state change. Missing OS sandbox produces source-only result, not fabricated execution. |
| Q08 — Finding lifecycle (AC09; SP-10) | Source-linked examples produce confirmed, unresolved, rejected and hardening dispositions with counterevidence; duplicate root cause reconciled, no inflated severity or coverage. Independent confirmation where required or explicit unresolved gate. |
| Q09 — Qualified optional capability (AC10; SP-11; SK-03–07) | Trace a selected source to exact release/docs/rights and data transfer/cost/coverage limitations; verify meaningful alternatives. Unknown or incompatible provider facts result in unselected candidate, not inferred capability. |
| Q10 — Independent Builder (AC11; SP-12) | Fresh Builder receives only bounded payload and accessible target/fixture; actual meaningful implementation, authored tests and independent reviewer checks with original/corrected source retained; no governing-resource dependency. |
| Q11 — Direct/composed consultation (AC11/12; SP-12,13) | Direct agent uses relevant existing and new expertise, reconciles privacy/UX/architecture decisions and produces one coherent bounded output; no self-transport or overlapping approval. |
| Q12 — Integrated release candidate (AC13/14; SP-14; all SK/SN) | Run standing and new tests, verify exact source identity, protected trees and legacy outputs, trace every requirement to observed or carried evidence, preserve limits and recovery. Native Windows and hosted Linux before release; failure blocks affected transition. |

Use existing-system read-only critique to establish whether an agent can preserve accepted behavior while identifying a specific boundary and recommending verifiable remediation; do not claim a third-party vulnerability from a hypothetical fixture. Direct semantic observation is separate from deterministic helper output. For the independent Builder, use a fresh agent where required and available, not an imitation of independence. If the initial handoff fails, retain original code/results and request a targeted correction. Carry unaffected prior observations only where source/controls remain relevant.

#### Practical metrics and comparison boundary

Track meaningful metrics: requirements with sufficient evidence or an explicit gap; preserved legacy behavior; positive/negative routing and fallback outcomes; actual negative and positive application checks; distinct-Builder portability and corrections; source/rights and link integrity; test terminal status per platform. Count test cases separately from advisory observations. Test count, card count, number of warnings or a perfect checklist is not a measure of overall security. Any comparative claim about security effectiveness, false-negative rates, agent quality, time or token savings needs a separately justified evaluation with a defined dataset, baselines and observation limits; it is not mandatory for this candidate.

### 13.9. Delivery, milestones and risk

The following B1–B5 sequence is a proposed delivery plan aligned to the prior Architecture build; it is not additional AIPF governance and does not grant execution authority.

| Stage | Scope / exit |
| --- | --- |
| B1 – Baseline and design | Reconcile owner-approved PRD, exact released source, implementation surfaces, activation strategy, source/rights gaps and acceptance matrix. Exit: bounded authorized build and exact protected invariants. |
| B2 – Knowledge and capabilities | Curate original guides/cards and selective shared records; verify sources/rights, decision coverage and link integrity. Exit: source-linked knowledge, honest limits and no mandatory tools. |
| B3 – Integration | Add compatible registry/entry/help changes, relevant tests, direct and portable output behavior; preserve existing specialists and AIPF. Exit: deterministic focused integration passes. |
| B4 – Candidate qualification | Run full regression, meaningful practical and independent Builder exercises, reconcile every requirement and limitation; preserve exact candidate and evidence. Stop at qualified candidate. |
| B5 – Delivery and release | Separate owner authorization: pre-release documentation, protected PR, native Linux/Windows CI, source reconciliation, owner acceptance, merge and publication only when explicitly authorized. |

#### Stage-level deliverables and stop conditions

| Stage | Required outputs, evidence and boundary |
| --- | --- |
| B1 | Approved revision and exact released/planning base; inspect current registry/helper/CI and canonical integration path; map SP/SK/SN to acceptance, decide guide/record granularity and rights treatment. Resolve decision-blocking inputs before dependent implementation. No implied later phase authority. |
| B2 | Original guide/index/source register and selected independent capability records, sample source/claim/rights verification; unique IDs and links, actual decision coverage, transparent unknowns, no wholesale import or executable tool prerequisite. Stop on material rights/authority conflict. |
| B3 | Compatible integration with existing entries/outputs, missing-tool behavior, composed advice and focused deterministic tests; inspect changed paths against B1 allowed/forbidden surfaces. Do not add broad orchestration or external provider actions. |
| B4 | Exact candidate source manifest and tree, focused and full standing regression, meaningful direct and distinct-Builder observations, source-only existing-system critique and synthetic privacy/finding cases. Retain raw outcomes, corrections, owner/observer attribution and requirement-level ledger. Stop at qualified candidate; do not merge or publish. |
| B5 | Separate authorization for preparation, cross-platform CI and final source/docs/rights reconciliation. Owner acceptance and explicit integration/publication authority before consequential transitions. Verify merged identity, tag and release; preserve recovery anchor. |

Expected verification ownership: executing agent observes exact local source/tests and direct guidance; named separate Builder returns independent implementation where required; reviewer observes returned artifacts and additional checks; hosted CI observes native Windows/Linux; product owner accepts material risk and release. If a necessary environment or independent observer is unavailable, mark the affected gate blocked or unresolved, not passed. Retain private evidence outside the public repository unless publication is authorized and sanitized. Record exact source identities and relevant result links, not a stale green report. Recovery before integration is isolated candidate/branch and retained baseline; after release, prior verified tag remains selectable. Revert or replace only under later authorization.

#### Decisions still to establish in B1

- Determine the smallest compatible cross-path applicability representation and any helper change after inspecting actual released source; retain existing interface semantics.
- Confirm precise card/file organization, source clauses and rights; use original synthesis/reference-only and preserve the planning inventory mapping if consolidated.
- Select only decision-useful optional capability records; verify exact versions, local/offline/hosted and cost/data/license constraints. No tool installation or service integration follows.
- Choose practical fixtures and independent observation method based on actual capability; clarify if any required observation cannot be performed. Keep known limitations and release gates separate.
- Confirm documentation updates and publication artifact scope at B5, not during B1–B4. Version labels remain proposals until owner approval.

#### Principal risks and mitigation

| Risk | Mitigation / revisit trigger |
| --- | --- |
| Over-activation or second governance model | Task materiality, canonical AIPF routing, negative routing tests; review any new authority language. |
| False confidence or false positives | Evidence classifications, existing-control analysis, safe negative tests, bounded claims; recheck on source/config changes. |
| Sensitive data exposure | No real credentials or private findings in public artifacts; explicit data flow and offline alternatives; recheck when tools/telemetry change. |
| Untrusted code or prompt execution | Read-only discovery, authorized sandbox checks, no hidden privileges or mandatory tools; block execution when isolation absent. |
| Stale guidance or mixed rights | Pinned sources, file-level rights, current primary references for material facts; recheck editions/terms at point of use. |
| Scope creep and review duplication | Original selective records, shared index, no Review Parity or other specialist implementation; defer nonessential tools. |

#### Historical decisions for owner review (resolved for this release)

- Approve or adjust the proposed first-release scope, three operating modes and nine knowledge domains. Proposed release labels (specialist 0.1 / Praxis v1.2.0) are not commitments.
- Confirm acceptable reference-only reuse, source-backed original synthesis and optional tool records; resolve any desired source imports individually.
- Authorize B1–B4 separately after PRD review; B5 preparation and merge/publication remain separately controlled. No implied changes to live apps, provider settings or licenses.

### 13.10. Source register and traceability

The seven GitHub repository root licenses were inspected at pinned revisions during Research Checkpoint 01 (2026-11-25). Selected documentation, tree listings and limited source samples were read. This is not a comprehensive code audit, tool execution, performance validation or redistribution clearance. The PRD is original synthesis; it does not incorporate source code or copied third-party guides. Exact license blob IDs and selected source observations are recorded below; individual third-party content and recipe rights remain separate.

#### Research sources (SR)

**SR-01 — [H4cker](https://github.com/The-Art-of-Hacking/h4cker/tree/72e3da0fa1411ef754a5d61b59cb0f58bf64f5f4).** MIT; LICENSE `e87b7062645d6f36a5f71a908b039b4c5533bfb9`. README, 720-file tree, application-security, AI-security and ethics/privacy/governance landing pages. Discovery only; verify original references individually. Exclude irrelevant training/exploit artifacts.

**SR-02 — [Safe Anything](https://github.com/erkamyaman/safe-anything/tree/09a7269eac49000f6cee64af2f94d2ce05da64be).** MIT; LICENSE `c98b47c040b56fcb3bd9a460aae26fa4fee684e8`. README; docs/privacy.md; docs/STATUS.md; docs/adr/0001-patterns-first.md. Candidate optional scanner. Upstream test claims, not locally reproduced. No data-flow guarantee; offline mode omits OSV dependency checks. Default advisory query sends package names, ecosystems and versions according to docs.

**SR-03 — [DevToys](https://github.com/DevToys-app/DevToys/tree/2dbbc8aa594978d11165a0e8112243c96a277dbc).** MIT; LICENSE.md `a9a469ec012931f7ff027cdfa52c3de917af33df`. README, PRIVACY-POLICY.md (dated 2021), EXTENSIONS-TERM-AND-CONDITIONS.md. Local processing reference; extension trust, clipboard and log boundaries warrant separate assessment. Policy claims not verified at runtime.

**SR-04 — [Umami](https://github.com/umami-software/umami/tree/dbb8d606fbd4e99220fb83bcb4abad3e0f97f42a).** MIT; LICENSE `eff41369347b0c5e88a96bd00c9266343b758e7a`. README, 2,163-file tree, selected prisma/schema.prisma fields (blob `ba94dbceaab7617b8554450a119f3716703a1dff`), collection pixel route (blob `d7fc2416709a903ea5d0dfedabc688539a06f3b2`). Session IDs, event data, distinct IDs and replay configuration make this a useful privacy-design case, not an assertion of anonymization or a product vulnerability. [Replay docs](https://docs.umami.is/docs/replays) describe masking.

**SR-05 — [OpenRewrite](https://github.com/openrewrite/rewrite/tree/4d2110dbbf7098a3185b6eb0e94c7f5f55a20d35).** Apache-2.0 root; LICENSE `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`. README and root tree; [official licensing](https://docs.openrewrite.org/licensing/openrewrite-licensing). Individual modules/recipes have differing terms. Optional targeted remediation, not autonomous bulk source mutation.

**SR-06 — [Cloudflare Security Audit Skill](https://github.com/cloudflare/security-audit-skill/tree/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8).** MIT; LICENSE `6dbc9ecb3a5b9080e95b962869e8c7ab16cfdc20`. README, 22-file tree, selected SKILL.md, VALIDATION-AND-REPORTING.md and report-schema.json. Source-first review, coverage tracking, candidate refutation, outcome distinctions, real independence, sandbox boundary. Do not adopt six-phase workflow as parallel governance or claim fresh verifier without capability. No audit run.

**SR-07 — [Agent Skills](https://github.com/addyosmani/agent-skills/tree/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74).** MIT; LICENSE `d67778ada6b9cda6227e9130da182c13e73c8b2e`. README, 280-file tree, selected security-and-hardening/SKILL.md, references/security-checklist.md and evals/cases/security-and-hardening.json. Secure-design guidance and positive/negative activation tests; no imported authority model or rigid universal thresholds.

**SR-08 — [aeo.js](https://aeojs.org/getting-started/introduction/).** Unverified. Introduction and [configuration](https://aeojs.org/reference/configuration/). Generated full text, raw Markdown, index and robots configuration. Review actual generated disclosure, distinguish crawler guidance from access control. Cross-specialist discovery; do not import code yet.

#### Primary standards and reference candidates (PS)

The following official references were inspected during initial discovery, not exhaustively extracted. Validate exact clauses, edition status and rights during B1/B2. No certification claim or mandatory control set is inferred.

- PS-01: [OWASP ASVS 5.0.0](https://owasp.org/projects/asvs) — application security requirements and verification.
- PS-02: [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) — assets, boundaries, STRIDE and privacy threat analysis.
- PS-03: [NIST SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) — secure development practices; [1.2 draft](https://csrc.nist.gov/pubs/sp/800/218/r1/ipd) is not a final baseline.
- PS-04: [NIST Privacy Framework](https://www.nist.gov/privacy-framework) — privacy risk management; [version 1.1 draft](https://www.nist.gov/privacy-framework/new-projects/privacy-framework-version-11) must not be confused with final guidance.
- PS-05: [OWASP Agentic Applications 2026](https://genai.owasp.org/top-10-for-agentic-applications-2026/) — agent and tool risk; relevant LLM security sources to be selected and version-qualified.
- PS-06: [CIS Controls v8.1](https://www.cisecurity.org/controls/v8-1) — selective operational safeguards.
- PS-07: [CycloneDX](https://owasp.org/projects/cyclonedx) — software supply-chain inventory standard.

| Requirement cluster | Research basis | Primary-source foundation |
| --- | --- | --- |
| SP-02–04, SP-09 | SR-01, SR-06, SR-07 | PS-01, PS-02, PS-06 |
| SP-05–06 | SR-01, SR-03, SR-04, SR-08 | PS-01, PS-04 |
| SP-07, SP-11 | SR-02, SR-05, SR-07 | PS-03, PS-07 |
| SP-08 | SR-01, SR-02, SR-06, SR-07 | PS-05, PS-03 |
| SP-10 | SR-06, SR-07 | PS-01, PS-02 |
| SP-01, SP-12–14 | Product PRD v1.2; v1.1.0 integration and qualification | AIPF v8.10.1 (sole governing authority) |

**Verification stamp:** source discovery observed 2026-11-25; this PRD consolidates that evidence. No runtime scanner behavior, exhaustive upstream rights check or live privacy/security verification was performed. Current vendor facts, aeo.js immutable revision/license and unqualified candidate tool terms remain open before any dependent use.

#### Completeness reconciliation against the consolidated product PRD v1.2

The 28-page product PRD combined general product context, established v1.0.0 requirements, Architecture Specialist requirements, knowledge/capability design, review-parity research and delivery details. The original 11-page Security & Privacy PRD covered a narrower subject; this expanded revision supplies comparable specialist-level depth without copying accepted architecture requirements into a competing home. Both Markdown and Word carry the full expanded specialist requirements. The product PRD and historical build plan remain linked in GitHub.

| Prior consolidated coverage | Where addressed here |
| --- | --- |
| Document control, product vision, users and jobs, baseline and product principles | Sections 0–2; inherited core PR/NFR crosswalk, released v1.1.0 evidence and status distinctions. |
| Execution models, integration architecture, specialist roadmap | Sections 0, 2 and 7; direct/distinct roles, concrete surface contract, materiality and compatibility. |
| Domain scope, decisions and outputs, progressive knowledge design, retrieval | Sections 2–4; explicit decision procedure, 36 candidate decision topics, record contract and source selection. |
| Functional, knowledge and quality requirements | Sections 3, 4 and 7; existing SP-01–14, SK-01–08 and SN-01–07 preserved, inherited product controls explicit. |
| Capability records, service selection and costs | Section 6; decision-family alternatives, source-observed limitations, network/data/cost/rights and operating constraints. |
| Review Parity and other external engineering capabilities | Sections 5–7; source-bound evidence and independent verification, cross-cutting runtime remains deferred. |
| Acceptance, practical scenarios, metrics and comparative claims | Section 8; AC01–14 preserved, explicit Q01–12 checks, evidence types and comparison boundary. |
| Build, risks, unresolved decisions, traceability, final authority | Sections 9–11; B1–B5 deliverables, risk/rights gaps, source register, rollback and release authority. |

This is coverage reconciliation, not proof that all potential security topics or upstream files have been inspected. No implementation, scanner execution, new primary-source verification or legal clearance is inferred from this expansion. The original research observation date remains unchanged. The revised document is ready for requirements review, not candidate acceptance.

### 13.11. Final scope and authorization boundary

This section is the approved Security & Privacy requirements baseline for Praxis v1.2.0. Preserve the v1.1.0 recovery anchor, AIPF v8.10.1, existing UI/UX and Architecture behavior, catalog/rights, source history and prior acceptance evidence. The owner authorized B1–B4 development, accepted the qualified candidate, and separately authorized B5 and consolidation. No live-target audit, provider action, additional specialist implementation, future release or unrelated change follows from this document. Publication is verified by the reconciled GitHub tag and release metadata.
