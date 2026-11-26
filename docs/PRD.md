# Praxis — Product Requirements Document

Version: 1.4 | Status: Owner-approved consolidated product requirements | Date: 2026-11-26 | Release target: Praxis v1.3.0 (accepted candidate; publication verified separately)

This is the single authoritative product PRD for Praxis. It consolidates [product PRD v1.2](https://github.com/S-Pillow/praxis/blob/c6393f6174e8d83e6760cf64bfbe889710d8919d/docs/PRD.md) and [Security & Privacy Specialist PRD v1.1](https://github.com/S-Pillow/praxis/blob/c6393f6174e8d83e6760cf64bfbe889710d8919d/docs/SECURITY-PRIVACY-PRD.md), preserving their approved requirements, stable identifiers, source/rights boundaries and history. The owner accepted the qualified security candidate and separately authorized B5 and consolidation on 2026-11-26. AIPF v8.10.1 governs execution; requirements approval does not grant execution authority. See [v1.2.0 qualification and release record](releases/1.2.0.md), [DEC-004](decisions/PRAXIS-DEC-004-specialist-expansion.md) and the [architecture specialist build plan](ARCHITECTURE-SPECIALIST-BUILD-PLAN.md).

The owner accepted the qualified QA & Engineering Quality v0.1 candidate and separately authorized B5 and consolidation on 2026-11-26. Revision 1.4 preserves [product PRD v1.3](https://github.com/S-Pillow/praxis/blob/93da10c375b11d4f1172d9cb248b76a0fd2487d4/docs/PRD.md) and incorporates the [approved QA PRD v1.0](https://github.com/S-Pillow/praxis/blob/9ca1a283af3e09d0411c069a47a3cbc4e8892413/docs/QA-ENGINEERING-QUALITY-PRD.md) as Section 14. See [v1.3.0 qualification and release record](releases/1.3.0.md). Prior consolidation and release statements below are retained as historical scope and provenance. No future specialist implementation is authorized.

**Document lifecycle:** Maintain one canonical product PRD. Temporary specialist PRDs may be developed and approved independently; consolidate their approved requirements at acceptance/release, preserve original approved revisions in immutable Git history, reconcile stable IDs and references, and keep supporting architecture, research, implementation plans and evidence separate. Future DevOps requirements require their own discovery, approval and execution authority; the approved QA requirements are now consolidated below.

**Navigation:** [Product and roadmap](#1-product-vision) · [Architecture](#8-architecture--engineering-design) · [Quality attributes](#9-quality-attributes) · [Security & Privacy](#13-security-and-privacy-specialist) · [QA & Engineering Quality](#14-qa--engineering-quality-specialist).

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

**Current roadmap (2026-11-26):** UI/UX v0.3 and Architecture v0.1 are released in v1.1.0; Security & Privacy v0.1 is released in v1.2.0. QA & Engineering Quality v0.1 is technically qualified and owner accepted for v1.3.0; see [Section 14](#14-qa--engineering-quality-specialist) and [release record](releases/1.3.0.md). DevOps & Reliability remains future; its detailed requirements and execution require separate approval. Review Parity remains deferred.

Historically the next specialist after v1.0.0 was **Software Architecture & Engineering Design**. This supersedes the earlier QA-first planning preference; it does not invalidate the QA research or change the accepted v1.0.0 requirements and evidence.

### Product direction

Specialists add domain expertise and useful techniques rather than a parallel development methodology. Prioritize knowledge that improves decisions before implementation, while retaining support for implementation guidance, diagnosis, critique and verification. AIPF remains authoritative for governance, authorization, proportionality and acceptance. Specialist advice must be evaluated against approved project intent, constraints and the actual implementation context.

In separate-agent workflows, the Prompt Agent consults relevant specialists and translates selected recommendations into concrete, operationally complete Builder Payload instructions. The Builder retains appropriate implementation discretion within the authorized scope and need not access Praxis or its specialist resources. The same capabilities support direct single-agent execution without artificial role separation or handoffs. Optional specialist access does not expand authority.

| Specialist | Roadmap status | Intended contribution |
|---|---|---|
| UI/UX & Design Intelligence | Available in v1.0.0 | Interface design, usability, accessibility and source-linked design knowledge |
| Software Architecture & Engineering Design | Released in v1.1.0 | Appropriate architectural patterns, technology tradeoffs, module boundaries, data modeling, integration contracts, resilience and maintainability; avoid unnecessary complexity |
| Security & Privacy | Released in v1.2.0; see Section 13 | Threat modeling, trust boundaries, authentication, authorization, secure design and data protection |
| QA & Engineering Quality | v0.1 accepted for v1.3.0; see Section 14 | Risk-based test design, effective assertions, diagnosis, regression strategy and behavioral verification |
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

---

## 14. QA & Engineering Quality Specialist

**Approved scope:** QA v0.1. Original [approved QA PRD v1.0](https://github.com/S-Pillow/praxis/blob/9ca1a283af3e09d0411c069a47a3cbc4e8892413/docs/QA-ENGINEERING-QUALITY-PRD.md) (blob `a4f87d7a1e7834f9fe8b9e52200abd1b07721b29`) remains immutable. All 42 QA-F/K/N requirements, 18 QA-AC criteria, QD01–12 exercises and individual traceability rows are retained. Historical proposal language and sample cases remain specification intent, not proof of current behavior or additional authority. Actual qualification is documented separately.

### 14.0. Document control and governing baseline

| Item | Identity / status |
|---|---|
| Product baseline | Praxis v1.2.0, released commit `93da10c375b11d4f1172d9cb248b76a0fd2487d4`, tree `fdeba1d234c4825dab8b9a210910657bdcb65c20` (factual erratum recorded in B1; approved original retained) |
| Requirements authority | [Historical canonical product PRD v1.3](https://github.com/S-Pillow/praxis/blob/93da10c375b11d4f1172d9cb248b76a0fd2487d4/docs/PRD.md), blob `4509b8e4c3d9dbe16f7386f8be682727fd63c85a`; all existing PR/AR/KI/NFR/SP/SK/SN requirements retained |
| AIPF | v8.10.1. Canonical DOCX SHA-256 `8e66028c8ebf60ea87180be1c23933273d8a597c425d3a1595ae81d9a720b8e6`; full Markdown projection SHA-256 `b11dfa2c12deb4d5b90833af4f10a02b5daf5e26d143469560b896fe9c85e0fd`; neither is manifest-file digest |
| Released modules | UI/UX v0.3, Architecture v0.1, Security & Privacy v0.1; 24 shared capability records; 163 standing regression tests on Linux and native Windows for the v1.2.0 qualified release tree. [Release evidence](releases/1.2.0.md) |
| Discovery | `b0f9fd6d3b19fb1e9a363c1a2320a0662710db48`; [Discovery report](../research/qa-engineering-quality/QA-ENGINEERING-QUALITY-DISCOVERY-01.md), [source register](../research/qa-engineering-quality/QA-SOURCE-REGISTER-01.md), [cross-specialist research register](../research/CROSS-SPECIALIST-RESEARCH-REGISTER.md) |
| Owner decision | Owner approved QA PRD v1.0 and B1–B4, accepted the qualified candidate, and separately authorized B5 and consolidation on 2026-11-26. AIPF governs all execution. |
| Lifecycle | Consolidated canonical PRD v1.4, Section 14; original approved specialist PRD v1.0 retained at immutable revision. Preserve approved IDs, wording, original history, provenance and evidence. Retire separate active PRD only after reconciliation. |

QA-F, QA-K, QA-N and QA-AC identifiers extend the existing product requirements without renumbering them. QD01–QD12 are representative exercise families retained from discovery, not product test counts. The owner approved these requirements and accepted the qualified candidate. The requirements, planned exercises and original decision tables below remain the approved specification and historical planning intent, not execution evidence. Actual observations and limits are in the [v1.3.0 release record](releases/1.3.0.md). Original QA-local references to Sections 0–14 refer to subsections 14.0–14.14, not the earlier product sections.

**Navigation:** [Vision](#141-vision-and-problem) · [Scope](#142-users-and-scope) · [Requirements](#143-functional-requirements) · [Knowledge](#144-knowledge-architecture) · [Integration](#145-integration-and-consultation) · [Methods](#146-verification-diagnosis-and-test-effectiveness) · [AI evaluation](#147-ai-agent-and-instruction-evaluation) · [Capabilities](#148-capability-and-source-qualification) · [Quality attributes](#149-non-functional-requirements) · [Acceptance](#1410-acceptance-criteria) · [Exercises](#1411-representative-qualification-exercises) · [Delivery](#1412-delivery-and-release) · [Traceability](#1413-traceability) · [Owner decisions](#1414-owner-review-and-stop-boundary).

### 14.1. Vision and problem

Praxis brings material engineering intelligence into decisions, operational prompts and direct implementation. QA & Engineering Quality supplies expertise in determining whether software actually behaves correctly, how to detect meaningful failures, how to diagnose their causes, and how to prove a correction preserves approved behavior. It should contribute before, during and after implementation, not become a mandatory final sign-off department or autonomous test platform. AIPF already governs scope, authority, evidence, acceptance and release.

#### 14.1.1 Problem statements

- Green tests can be irrelevant, circular, mock-only or insensitive to the defect. The v1.2.0 independent Builder's original 15 tests passed, yet its reviewer identified four findings; corrected v2 passed independent checks. That bounded historical result illustrates test blind spots, not a claim about general defect rates or the future QA specialist.
- Material regressions occur in unchanged callers, coupled contracts, state, migrations, failure paths, asynchronous ordering and platform differences.
- AI-generated code may look correct but silently discard zero/false/empty, violate trust boundaries, add needless dependencies, use misleading assertions or report evidence never obtained.
- A screenshot, HTTP success status, coverage percentage or test count can create false confidence if actual effect, recovery and independent oracles remain unobserved.
- Agents can solve a problem through different valid paths. Exact trace equality is not correctness; unauthorized effects are unacceptable even if the response looks correct.
- Distributed execution requires explicit source/fixture/environment/observer identity, separate reports and observed results, and preservation of failures and corrections.

#### 14.1.2 Outcomes and success

The specialist must help translate requirements and risk into observable tests; select the right verification layer and feasible observer; reproduce and diagnose failures with falsifiable hypotheses; assess test effectiveness; verify corrections and preserve existing behavior; supply applicable AI and data evaluation expertise; and synthesize material guidance into one direct action or portable Builder Payload.

Success means sufficient technical evidence for representative use and the integrated regression, not a target number of cards/tests/tools, code reduction, universal host support, certification, accuracy/coverage SLA, or comparative superiority over AIPF alone. Additional comparisons require a decision or claim that depends on them.

### 14.2. Users and scope

| Actor | Job to be done | QA contribution |
|---|---|---|
| Product owner | Understand what works, what remains unverified and which decision is needed | Concrete observed outcomes, impact and limitations in usable language; no specialist IDs required |
| Prompt Agent | Turn requirements into precise, executable verification | Risk-selected tests, acceptance oracles, negative effects, environment, authority and stop in T1 |
| Direct executing agent | Design/perform authorized tests or repair | Suitable methods, bounded diagnosis and actual verification, without self-handoff |
| Distinct Builder | Execute complete authorized work without governing context | Portable instructions and accessible inputs, raw test evidence and stop |
| Independent reviewer | Detect blind spots and verify correction | Source identity, independently authored checks, counterevidence, original/corrected history |
| Maintainer | Keep meaningful regression and avoid overengineering | Causal findings, focused corrections, reliable tests and proportionate coverage |

#### 14.2.1 In scope

Risk and impact, test design and oracles, unit/property/state, contracts/integration, browser and UX verification, controlled failure and concurrency, reproduction/regression, flakiness, test strength, maintainability, data quality and AI/agent evaluation. Deliver original progressive knowledge, a question-led index, source/rights records, selected shared capability records, compatible additive integration, focused tests, representative direct and independent exercises and full cross-platform standing regression.

#### 14.2.2 Out of scope

No second governance, status vocabulary, evidence lifecycle or acceptance authority; no autonomous test daemon, orchestrator, crawler, scanner, trace database, telemetry platform, benchmark service or automatic instruction optimization. No mandatory Playwright/EvalView/Promptfoo/etc., dependency installs, paid calls, accounts, production fault injection, live security probing, customer-data export or infrastructure provisioning. No AIPF change, DevOps or Review Parity implementation, replacement of released retrieval/catalog behavior, broad refactor, certification or automatic AI authorship claims. No new hosting, packaging or release through this planning document.

#### 14.2.3 Domain boundaries

| Domain | QA contribution | Protected boundary |
|---|---|---|
| UI/UX | Observable user flows, render/interaction, accessibility and adverse states | UI/UX defines design/usability intent; QA cannot redesign to make tests pass |
| Architecture | Structural contract, consistency, integration/test seams and change impact | Architecture owns design/technology tradeoffs; no speculative refactor for tests |
| Security & Privacy | Negative auth, no disclosure/mutation, safe inputs and data lifecycle verification | Security supplies trust/control requirements; QA grants no live probing or risk acceptance |
| Future DevOps | Application recovery and CI evidence | Infrastructure, live operations and delivery expertise remain separate |
| Review Parity (deferred) | Source-bound claim/evidence sufficiency | No independent approval/signature/provenance runtime |
| AIPF | Engineering techniques and concrete observables | Canonical governance, routing, readiness, evidence, status, correction, acceptance and release remain authoritative |

Compose relevant expertise into one coherent decision or instruction. Do not duplicate reports or create separate approvals merely because domains overlap.

### 14.3. Functional requirements

All 22 are proposed Must requirements, applied conditionally to material work and approved constraints, not a checklist for every task.

| ID | Requirement | Observable fulfillment / limits |
| --- | --- | --- |
| QA-F01 | Material activation | Consult QA after canonical AIPF path selection for material verification, diagnosis or engineering-quality decisions. Select plan/diagnose/review; skip minor or unrelated work without concrete benefit. No mandatory extra consultation for routine AIPF verification. |
| QA-F02 | Risk and impact strategy | Identify intended behaviors, changed and coupled surfaces, high-impact invariants, failure modes, actual environment and feasible observations. Prioritize decision-changing tests over blanket coverage; history is a lead, not proof. |
| QA-F03 | Requirements-to-oracle mapping | Translate approved requirements into explicit preconditions, stimuli, expected results, negative effects and observable checks. Resolve material ambiguity through AIPF; distinguish requirement, assumption, suggestion and unknown. |
| QA-F04 | Test level and isolation | Select smallest sufficient unit, component, property, contract, integration, system or exploratory method. Distinguish mock, synthetic fixture, actual provider and observed runtime; retain meaningful integration coverage. No test pyramid quota. |
| QA-F05 | Boundary, property and state testing | Use relevant equivalence classes, limits, missing/null/zero/false/empty, invariants, invalid states and action sequences. Use reproducible generated counterexamples; protect unrelated behavior. |
| QA-F06 | Contracts and integration | Verify consumer/provider expectations, schema/serialization, error semantics, compatible versus breaking changes, dependency assumptions and actual interaction when required. Mock success is not provider proof. |
| QA-F07 | User-facing quality | Derive observable user outcomes, actual mutations, keyboard/focus and accessible semantics, loading/error/empty and responsive/long-text behavior as material. Distinguish computed contrast, static checks and observed rendering. |
| QA-F08 | Controlled failure and concurrency | Design bounded deterministic delay, timeout, duplicate, stale/out-of-order response, cancellation and partial failure scenarios. Verify recovery, idempotency and no extra writes or silent loss. No live chaos testing without separate authority. |
| QA-F09 | Diagnosis and reproduction | Capture exact failing stimulus, source, environment, expected/observed, causal hypothesis and next discriminating observation. Distinguish code/test/data/timing/dependency/configuration/infrastructure faults; honor AIPF diagnostic breakpoint. |
| QA-F10 | Correction and regression | Preserve original failure identity and reason; demonstrate material fail-before/pass-after where required/feasible; verify affected and unrelated invariants. Changed oracle, silent skip or unrelated environment repair is not a demonstrated fix. |
| QA-F11 | Differential verification | Pin baseline and candidate plus parity inputs when comparison changes a decision; judge absolute acceptance independently; classify improved, regressed, equivalent valid/invalid, approved intentional change or incomparable. Unchanged failure is not a pass. |
| QA-F12 | Test effectiveness | Assess assertion sensitivity, oracle independence, defect detection and coverage gaps; target meaningful mutant/counterexample. Distinguish killed, surviving, equivalent, invalid and untested mutations; no arbitrary score target. |
| QA-F13 | Flakiness and reliability | Separate deterministic failure, nondeterministic behavior and environment noise; control clock, random seed, state, order and readiness when suitable; retain intermittent failures and retries. No silent quarantine, retries or weakened checks to get green. |
| QA-F14 | Maintainability and critique | Identify actual duplication, unused logic, excessive complexity, suspicious imports, misleading tests and unnecessary abstractions. Inspect real use and counterevidence; prefer smallest complete correction, existing mechanisms or no change. No AI authorship judgment or LOC quota. |
| QA-F15 | Data and transformation quality | Verify relevant schema, types, units, missing/zero, duplicate/order, totals, reconciliation, rejection, round-trip/migration and partial writes. Distinguish data/model quality and drift; use authorized synthetic data. |
| QA-F16 | AI and agent evaluation | Assess outcome, constraints, tool permissions/target/arguments, causal prerequisites, contract drift, retrieval versus answer correctness and multi-turn behavior. Accept valid alternate paths; unauthorized action fails regardless of final text. |
| QA-F17 | Evaluation validity | Freeze material cases and gates; use reliable oracle or calibrated domain/model judge, disagreement/abstention, independent/held-out cases and repetition where warranted. Control model/config/task parity, report failures/denominators/uncertainty. No automatic prompt optimization or required comparative benchmark without a specific claim. |
| QA-F18 | Findings and evidence | Trace material finding to requirement, exact source or runtime, observation, impact and counterevidence. Distinguish confirmed defect, unresolved observation, rejected suspicion and optional improvement; propose proportionate next check/correction under existing AIPF evidence and status controls. |
| QA-F19 | Capability qualification and fallback | Compare no new tool, existing, local/self-hosted and hosted alternatives; qualify actual version/platform, rights, access, data, costs/limits and failure behavior. Missing guide/runner/observer remains explicit; do not fabricate or downgrade required evidence. |
| QA-F20 | Direct and distinct workflows | Direct agent uses current operational boundary without self-handoff. Prompt Agent distills material verification into canonical T1 payload with accessible inputs, no required governing-resource access for Builder; preserve evidence ownership and stop boundary. |
| QA-F21 | Multi-specialist composition | Synthesize material QA, Architecture, UI/UX and Security expertise once. Preserve requirements and trust/design boundaries; resolve material conflicts through AIPF, no duplicate governance or approvals. |
| QA-F22 | Compatible integration | Extend entry, registry, optional helper and shared knowledge index additively. Preserve three existing entries, versions/modes/results, framework bytes, catalog/retrieval, standing suite and recovery anchor. No new routing engine or required executable. |

#### 14.3.1 Activation examples

| Actual request | Expected material consultation |
|---|---|
| Plan local CSV reconciliation with invalid and duplicate rows | Plan: data oracles, rejection, counts, protected output |
| Intermittent stale autocomplete after rapid input | Diagnose: causal order, deterministic reproduction, minimal correction |
| Candidate tests green but ownership or other negative effect untested | Review: assertion strength, counterexample and source-bound evidence |
| AI app with several legitimate tool paths | Plan/review: material constraints, actual action/target and causal gates |
| Substantial privacy-first dashboard redesign | Plan/review with UI/UX, Architecture, Security where material |
| Typo-only docs change or unrelated routine backend edit | Normally none; AIPF verification still applies |
| Missing required browser or reviewer | Disclose pending observation and request authorized feasible alternative, not qualification |

### 14.4. Knowledge architecture

#### 14.4.1 Knowledge requirements

| ID | Requirement | Observable fulfillment / limits |
| --- | --- | --- |
| QA-K01 | Navigable original knowledge | Question-led offline index, stable decision IDs, progressive loading and working guide links. |
| QA-K02 | Conditional decisions | Each decision card gives actual question, applicability/exclusions, context, alternatives including no change, tradeoffs, counterexample, observables and source pointers. |
| QA-K03 | Coverage | All twelve decision families in Section 4.2 are covered with positive and negative guidance. Guide/card count is design discretion. |
| QA-K04 | Provenance | Author/project, URL, revision/edition or date, file/section, supported claim, rights and limits. Pin repository sources where possible. |
| QA-K05 | Primary sources | Verify decision-sensitive facts against authoritative source/docs; inspect implementation when necessary. Separate observed source from author benchmarks and runtime evidence. |
| QA-K06 | Volatile versus stable | Separate stable methods from versions, supported hosts, plans, prices, terms, features, retention and quotas; recheck at point of use. |
| QA-K07 | Rights and originality | Original synthesis; no wholesale imported third-party skills, prompts, code, fixtures, data or assets. Preserve notices and verify rights before reuse; unknown rights reference-only. |
| QA-K08 | Shared capabilities | Add only useful, qualified discovery records to existing independent capability index; preserve 24 existing entries and avoid duplicates or new tool directory/runtime. |
| QA-K09 | Examples and limitations | Show meaningful correct and faulty cases, false confidence, unavailable resources, counterevidence and interpretation limits. Label illustrations unexecuted. |
| QA-K10 | Deferred research continuity | Preserve 29 source IDs and 14 XR leads in pinned research; add later dispositions only under separate authorized decision. No backlog-to-requirement conversion. |

#### 14.4.2 Decision families

All 12 families must be navigable; proposed filenames can be grouped or revised during design, without a fixed file/card count.

| Family | Candidate guide | Questions for decision cards | Discovery anchors |
| --- | --- | --- | --- |
| Risk and impact | risk-impact.md | Which changed and coupled contracts matter? What high-risk unchanged caller is affected? How use churn/co-change and handle shallow history? What can safely be omitted? | QA-S01,03,07 |
| Test design and oracles | test-design.md | Independent expected result, equivalence/boundary classes, decision tables, metamorphic relations, negative effects, intended failure reason and fixture validity. | QA-S03,24–26 |
| Unit, property and state | unit-property-state.md | Example versus generated invariant, explicit zero/false/empty, state transitions and sequences, deterministic clock/seed and counterexample minimization. | QA-S24,03 |
| Contracts and integration | contracts-integration.md | Consumer/provider, actual vs stub, serialization, schema evolution, dependency substitution, round-trip/migration and error semantics. | QA-S26,02,03 |
| Browser and UX | browser-ux.md | User journeys, semantic locators, readiness, keyboard/focus, actual rendering, accessibility, screenshots/DOM/network/state and responsive stress. | QA-S12,27,05,20,22 |
| Failure and resilience | failure-resilience.md | Timeout, partial completion, stale responses, duplicate events, cancellation, retry/idempotency, deterministic injection and cleanup. | QA-S05,03,24 |
| Diagnosis and regression | diagnosis-regression.md | Reproduction, causal hypothesis, minimal correction, fail-before/pass-after, differential parity, intermittent failure and stale evidence. | QA-S03,01,27 |
| Maintainability | maintainability.md | Actual duplication, complexity, unused paths, false-positive leads, smallest complete change, useful test seams and protected constraints. | QA-S06,07,09 |
| Data quality | data-quality.md | Schema/types/units, missingness, duplicates, totals/reconciliation, migration, model/data drift, privacy-preserving fixtures. | QA-S16,24,26 |
| AI and agent quality | ai-agent-quality.md | Outcome/authority gates, parameters, causal order, alternate valid paths, MCP drift, retrieval/answer, multi-turn state and evaluator validity. | QA-S02,04,08–11,13–15,28 |
| Test-suite effectiveness | test-effectiveness.md | Detect meaningful defect, independently authored oracle, weak and known-good suite, mutation classifications, flake, coverage limitations. | QA-S03,25,06 |
| Capability selection | capability-selection.md | No new tool/existing/local/hosted alternatives, version/platform/rights, actual costs/data access, failure and fallback. | QA-S02,04,12–18,22,24–29 |

The discovery anchors are not proof for every general method. B1/B2 must qualify relevant primary materials where decision-sensitive source support is incomplete, e.g. boundary/equivalence classes, decision tables, metamorphic testing and flaky-test handling. No invented source IDs, unqualified upstream content or benchmark claims.

#### 14.4.3 Original decision card design

Each card uses stable QA-D identifiers and a concise question, applicability, exclusions, necessary context, alternatives and tradeoffs (including no change), counterexample, observable verification and source pointers/limitations. Index by question rather than source/tool. Load only relevant cards. No mandatory new report format or fixed number of cards. Illustrations are not executions.

- **Negative assertion:** For a rejected operation, if mutation is forbidden, assert pre/post state and absence of effect in addition to error. A generic exception from malformed setup does not prove resource authorization. Test the actual boundary with the smallest sufficient fixture; Security supplies the trust requirement. QA-S03/24.
- **Flaky browser:** Diagnose actual readiness, event order, request/state and reproducibility before extending a sleep. Prefer a bounded condition expressing observable behavior; do not change production timing solely to make a test pass. QA-S27/05.
- **Agent trace:** Match exact order only where the prerequisite or causal side-effect constraint requires it; extra authorized read may be valid, prohibited write fails even if final text matches. QA-S02/04; AIPF controls authority.
- **Test sensitivity:** Demonstrate a deliberately faulty implementation survives an inadequate assertion, then add a meaningful independent counterexample and establish the known-good implementation passes. A syntax error is not detection of the intended defect. QA-S03/25.

### 14.5. Integration and consultation

#### 14.5.1 Proposed existing registry contract

After canonical AIPF routing, the agent judges material QA intent. Eligibility across paths is not automatic activation. Use current schema version 1; no helper change expected, confirmed at B1.

| Field | Proposed value |
|---|---|
| ID / version | `aipf-qa-engineering-quality` / `0.1` |
| Applicable paths | `chapters_any: [11,12,13,14,15,16,17,18,19,20,21]` |
| Skill | `skills/qa-engineering-quality/SKILL.md` |
| Task-to-mode | `qa-plan: plan`; `qa-diagnose: diagnose`; `qa-review: review` |
| Knowledge sources | `skills/qa-engineering-quality/INDEX.md`, `knowledge/capabilities/INDEX.md` |
| Tools / retrieval | `tools: []`; omit retrieval_script |
| Authority | Advisory; AIPF, approved requirements and current authorization govern |
| Purpose | Context-grounded test design, diagnosis, regression, test effectiveness and engineering-quality critique |
| Output | Risk-selected methods and observables, causal diagnosis, source-bound findings with limitations and relevant alternatives |
| Fallback | Disclose missing guidance/tool/source/observer; use sufficient verified context or qualified alternative only where adequate; stop affected work for material decision/observation gap |

Three modes are proposed: **plan** (strategy and testability), **diagnose** (reproduction and causal repair), **review** (test quality, evidence and candidate verification). Actual verification belongs in review only when authorized. A fourth verify mode is not justified yet. Reconsult when actual decision changes, not as an automatic sequence.

#### 14.5.2 Mode inputs and outputs

| Mode | Inputs | Expected output |
|---|---|---|
| Plan | Approved behavior, constraints, risks, changed surfaces, architecture and actual feasible environment | Prioritized test levels, specific scenarios, independent expected effects, fixtures, observation/observer and limits |
| Diagnose | Exact failure, source/environment, expected invariant, prior attempts and actual logs | Falsifiable hypothesis, smallest meaningful reproduction, trace/counterevidence, probable vs confirmed cause, bounded correction and regression |
| Review | Exact candidate/source/test/fixture, requirements, raw observations and risks | Source-linked finding and impact, assertion adequacy, actual observed or missing evidence, proportionate next check and unresolved gaps |

Material facts missing remain explicit; no fabricated requirements, commands or results. Integrate outcomes into existing project/control records or T1; no new mandatory form.

#### 14.5.3 Additive interfaces and fallback

Extend `skills/specialists.json`, `skills/praxis/SKILL.md`, `PRAXIS.md`, supporting docs and focused tests. Preserve the three entries exactly. Existing `scripts/praxis_context.py` resolves an explicit task and chapter intersection, verifies framework projection, and reports availability. It neither classifies natural language nor proves reading/application of the specialist. Illustrative invocation (not a command to run now):

```sh
python scripts/praxis_context.py --task qa-plan --chapter 11
python scripts/praxis_context.py --task qa-diagnose --chapter 12 --request "Reproduce stale result"
python scripts/praxis_context.py --task qa-review --chapter 15
```

Expected existing contract: `consult` and selected mode for available applicable skill, advisory_only; request with no retrieval yields `lookup_status: not_applicable`; missing skill yields specialist_unavailable, wrong selected chapter intersection recheck_framework_path; unknown/blank input errors as currently defined. No subprocess for QA. Do not reinterpret unknown tasks as skip; nonactivation is agent judgment. No Python or helper needed for direct file reading. Missing/corrupt framework is integrity failure, not license to invent governance. Use repository discovery/explicit entry; do not claim native discovery on untested hosts.

#### 14.5.4 Execution models

Direct agent uses actual authorized operational boundary, no self-handoff. Prompt Agent derives canonical T1 with specific QA values, test cases/oracles, allowed commands/surfaces, accessible implementation inputs, evidence and stop; do not require Builder to read Praxis, AIPF, PRD, specialist or catalog. Optional access does not change authority. For the fresh independent exercise deliberately withhold governing resources and reviewer answers. Reconcile Builder report, source, reviewer execution and original/corrected evidence; preserve canonical B2 outcome and observer attribution. Distinct Builder cannot select subsequent work.

### 14.6. Verification, diagnosis and test effectiveness

#### 14.6.1 Strategy and oracles

Start from intended observable behavior and affected boundaries, not number of tests. Identify coupled consumers, contracts, state and high-impact unchanged paths. Historical churn, co-change and bug mentions can prioritize inquiry, but shallow/squashed history, generated code, renamed files and sparse critical paths distort signals. Do not assess individual quality from commit counts.

Use lowest-cost sufficient method per claim: pure logic, actual state transition, contract, local integration, rendered browser, OS/runtime or named human observer. A critical boundary may need multiple levels because each proves different facts. Specify what mocks simulate and leave unknown. Prefer existing tests/tools. For material checks identify stimulus, expected result, negative effects, oracle, observer and source/fixture identity. Include explicit false/zero/empty distinct from absent/null, edge limits, invalid types, encodings, duplicate/order cases, state preservation and unchanged behavior where relevant. Test actual effect rather than status code, DOM presence, log message or a circular assertion.

Property-based tests require independent invariant, bounded generation and seed/minimized counterexample; state models require allowed/invalid transitions, repetition and reset. Data checks cover schema, units, totals, missingness, rejection, deterministic ordering/rounding, preservation and round-trip/migration only as required. Generated data by itself is not correctness evidence. Use synthetic or approved fixtures with controlling identity, not actual secrets/customer data.

#### 14.6.2 Diagnosis and corrective regression

Retain exact baseline, command, fixture, configuration, platform/toolchain, failing output and expected invariant; reduce reproduction without removing causal condition. Form a falsifiable hypothesis and test a discriminating alternative. Separate observations from inferred causes; distinguish source, test, dependency, data, environment, timing and configuration faults. Use AIPF diagnostic breakpoint after unsuccessful same-family repairs or contradiction. Do not mutate speculatively.

Preserve original failure and diff. Demonstrate intended failure before and passing corrected behavior after where required and feasible, not unrelated import/syntax/timeout failure. If unable to reproduce, state limitation, not invented baseline. Protect unaffected invariants and run applicable standing regression. Do not weaken assertions, silently skip tests, change fixtures to exclude failures or treat retries as erasure of an observed defect.

#### 14.6.3 Differential verification (CodeVetter-derived method)

When comparison changes a decision, freeze reference and candidate plus relevant dependency/configuration, data/auth state, scenario/seed, runtime, locale/timezone/viewport, oracle and measurement method. Determine absolute acceptance on each independently. Normalize only demonstrated incidental variation; retain raw and normalized evidence, transformation reason and relevant differences. If parity cannot be established, report separate observations without comparative confidence.

| Comparative description | Interpretation |
|---|---|
| Regressed | Previously acceptable behavior is now defective |
| Improved | Material baseline defect absent under comparable conditions; absolute checks still required |
| Equivalent valid | Matched behavior meets criteria on both; preservation bounded to observations |
| Equivalent invalid | Both fail; unchanged is not a pass |
| Intended change | Approved difference meets new criteria and protected behavior |
| Incomparable/inconclusive | Insufficient parity, execution, oracle or evidence; required next observation |

These are descriptive comparison results, not AIPF execution statuses. CodeVetter's current warm browser executor is no longer bundled; use its method, not a mandatory product dependency. QA-S03 records the precise pinned evidence.

#### 14.6.4 Controlled failure, concurrency and flakiness

Use deterministic synthetic fixtures or explicit schedule/seed for timeout, out-of-order completion, delayed dependency, duplicate submit, cancellation, failure after uncertain commit, partial operation, retry and recovery. Check no extra transaction, stale overwrite, data loss or unauthorized effect; confirm correct visible error and recoverability. Include cleanup and preserved state. Do not run uncontrolled live faults or simulate success by bypassing actual boundary.

Retain first failure and every meaningful retry. Isolate time, random/order, shared state, resource contention, external dependency and weak oracle. Prefer condition-based readiness, bounded synchronization and per-test context. Repeated passing runs do not erase intermittent failures; quarantine or altered acceptance requires authorized reason and owner visibility.

#### 14.6.5 Test-suite effectiveness and maintainability

A valuable suite distinguishes invalid from valid implementations. Demonstrate a deliberately faulty synthetic implementation surviving weak checks, stronger independent counterexample failing for intended reason, and known-good passing. Target meaningful mutants, distinguishing killed, survived, equivalent, invalid/unexecutable and untested. Surviving equivalent mutation is not proof of defect; no fixed coverage/mutation-score gate. Coverage locates gaps, not correctness.

Inspect actual use, reachability, complexity, tests and error paths. SynthScan labels its risk vectors heuristic and review-minutes estimate uncalibrated. Churn or coding style is a review lead, not AI authorship, quantified reviewer time or confirmed severity. Prefer existing mechanism, clear minimal complete change or no change; preserve security/accessibility/validation/readability. Less code is not a quality guarantee.

#### 14.6.6 Findings and evidence

Material finding record: approved requirement or behavior, source/line or runtime reference, expected/observed, exact candidate/fixture, observer and evidence class, impact and scope, counterevidence, proposed next action/correction and actual disposition. Distinguish confirmed defect, unresolved lead, rejected suspicion and optional improvement as descriptive findings under existing AIPF evidence lifecycle and status vocabulary. No competing governance or labels. Report only supported observations; named observer feasibility remains separate from claimed outcome.

Untrusted code remains source-only unless effective authorized confinement established: disposable target, sanitized environment, no unauthorized network/credentials, read-only source/toolchain where appropriate, scratch-only writes, resource bounds and cleanup. Python/browser isolation alone is not OS sandbox proof. Returned logs, actual reproduction, source inference and operator attestation remain distinct. Required actual runtime/independent observation cannot be replaced by walkthrough.

### 14.7. AI, agent and instruction evaluation

This is applicable engineering knowledge for AI applications and actual Praxis representative behavioral qualification, not an autonomous evaluation platform, paid-model requirement or automatic AIPF prompt optimizer.

#### 14.7.1 Evaluation dimensions

| Dimension | Observable test | Caveat |
|---|---|---|
| Outcome and constraints | Correct required output/values, source-supported claims, final state | Fluent or similar output is not correctness |
| Activation | Material selected expertise, unrelated nonactivation and fallback | Helper tests are deterministic explicit-ID tests, not reasoning |
| Tools/parameters | Allowed action and resource, forbidden call, typed argument, actual effect | Availability is not permission |
| Causal ordering | Approval, state and required prerequisite before dependent action | Accept alternate valid sequences unless order materially constrained |
| Contract drift | Removed tool, new required field, type/meaning change vs compatible addition | Schema pass not proof of safe semantics |
| Retrieval versus answer | Source relevance, identity and support; correct answer or abstention | Correct retrieval and correct answer are separate |
| Multi-turn state | Preserve roles, intent, constraints and stop across follow-up/repair | Observable action/state, not hidden reasoning |
| Robustness | Synthetic untrusted data, unavailable tool, malformed input or partial result | No universal security/injection claim |
| Semantic quality | Independent expert or calibrated judge; completeness, clarity, usefulness | No score overrides hard required controls |

A golden trace is an example of observed behavior, not required script. Compare materially relevant invariants and permitted alternatives. Record actual tool/operation result or state sentinel for claims requiring it, not merely self-reported behavior. Use synthetic fixtures and minimized/redacted event metadata, e.g. scenario ID, action class, approved resource alias, relevant args/result and configuration. No secret-bearing transcript, hidden chain-of-thought or default telemetry collection.

#### 14.7.2 Evaluation validity and comparative method

Define hard correctness/authorization gates, cases, oracles, endpoints and hypotheses before results. Separate authored examples from held-out or independent cases; include known good, bad, ambiguous and unavailable cases. Prefer deterministic checks/domain reviewer when suitable. If model judge used, calibrate with examples, blind candidate labels and randomize order where useful; retain disagreement, abstention, invalid judgments, sample limits and shared-model biases. Do not equate ranking to correctness or ignore hard failures.

For a justified comparative claim, pin instructions/skill/model/config (host selection unknown if unavailable), fixture, evaluator, environment and relevant dependencies. Use paired tasks, fresh contexts, repeated runs when stochastic variation matters, report per-task results, uncertainty and denominators including refusal/timeout/failure. Measure total clarification/correction/verification effort, not output volume alone. Distinguish input, cached and output token costs with verified pricing/usage if claiming savings. No mandatory AIPF-only comparison or universal benchmark threshold.

#### 14.7.3 Retained instruction research

GPT Prompt Engineer (QA-S08) provides prompt generation/pairwise Elo concept; Honey and Ponytail (QA-S09/06) document author-produced paired experiments with limited task/model/host scope and cache/cost issues; Auto-evaluator (QA-S10) separates retrieval and answer evaluation. Rhesis (QA-S11) links domain-expert feedback to test cases/agent versions. Adopt original evaluation literacy; retain prompt optimization as future XR-10 separate authority. No transferred benchmark savings, automatic rewrite, model provider choice or inferred notebook compatibility. The existing [Praxis prompt quality rubric](TESTING.md#evaluation-rubric) remains authoritative where applicable.

### 14.8. Capability and source qualification

#### 14.8.1 Candidates

Discovery names are not selected/installed dependencies. Use the [shared capability index](../knowledge/capabilities/INDEX.md), compare no new tool, native/approved existing, local/self-hosted and hosted choices. Add only decision-useful records; no count gate.

| Candidate | Source IDs | Contribution | Proposed disposition / conditions |
| --- | --- | --- | --- |
| Playwright | QA-S12/27 | Browser/API interaction, isolation, traces | Candidate; exact browser/host/version/access and trace privacy. Existing optional Praxis browser test stays unchanged. |
| Hypothesis / Stryker / Pact | QA-S24–26 | Property/state, mutation and contract testing | Distinct candidates; exact language/runtime/rights/cost, actual test oracle and provider access. Native tests or hand-authored mutants may suffice. |
| EvalView / Promptfoo | QA-S02/04/28 | Agent behavior, contract diff, declarative assertions | Optional; EvalView source defaults telemetry on and installation ID; hosted/model paths and red-team/data handling need qualification. No paid/live test calls. |
| Rhesis | QA-S11 | Domain expert feedback, multi-turn case management | Optional when collaboration material; MIT core/enterprise and brand exceptions, hosted/SDK access, retention and cost. |
| Langfuse / MLflow / Opik | QA-S13–15/29 | Experiment, traces and operational monitoring | Overlapping alternatives; use existing tools first, no three integrations. QA + DevOps leads; exact deployment, licensing, data masking/retention, spend. |
| Deepchecks | QA-S16 | Data/model validation and drift | Reference/optional independent tool; AGPL and deployment obligations need review. No copying into Praxis. |
| Rainforest QA | QA-S22 | Commercial no-code test management | Alternative only; account/token, test data, run groups, plan, exit/maintenance cost. |
| CodeVetter | QA-S03 | Differential evidence and qualified task corpus | Method only initially: warm browser executor no longer bundled, repository-owned script and compatible lockfile required; platform and pnpm limits. |
| Chaos Frontend Toolkit | QA-S05 | Controlled failure ideas | Reference only; old randomized/global-patch implementation. Prefer existing deterministic test seams. |
| Codebase Recon / Ponytail / SynthScan | QA-S01/06/07 | Risk and maintainability | Original techniques only; no external skill/scanner or AI authorship claim. |
| GPT Prompt Engineer / Honey / Auto-evaluator | QA-S08–10 | Prompt variants, evaluation design, cost methodology | Reference; historical models, small/author-generated benchmark scopes, unknown Auto-evaluator license. No automatic instruction/governance rewrite. |
| Google DESIGN.md / Awesome DESIGN.md | QA-S19/20 | Design contract lint/diff and design references | XR-01/02, alpha specification, individual branding/asset rights; no required format or catalog import. |
| AgentDiff / Eleata Verify MCP | QA-S17/18 | Attribution and claim/evidence review | XR-07/08; hooks, prompt excerpts and remote refs; hosted evidence API and unverified Eleata license file. No hooks, MCP or provenance runtime. |
| AgentScope / Forgejo | QA-S21/23 | Agent architecture and forge/runner operations | XR-03/04; future authorized decisions only, no orchestration or hosting migration. |

#### 14.8.2 Point of use

Apply existing [qualification guidance](../knowledge/capabilities/QUALIFICATION.md): actual needed behavior, workload, version/host, rights, commercial status, data flow/recipients/retention/export, runtime/network/credentials, access, price units, expected/peak usage, resets/exhaustion/overages, enforceable spend cap and migration/exit cost. Self-host is not automatically free/private; disabling telemetry does not prove no outbound traffic. Unknown facts remain unknown; provide qualified alternative or material decision gap. No test calls, integrations, provisioning, account creation, install or external data transfer authorized here.

#### 14.8.3 Source and rights

The pinned [QA source register](../research/qa-engineering-quality/QA-SOURCE-REGISTER-01.md) records 29 distinct source IDs, 21 repository pins, inspected file blobs and observed docs. Root license inspection, metadata and declaration are different evidence strengths. Preserve author/project, URL, exact source/date, observed claim, rights/disposition and limits when writing original knowledge. Recheck current decision-sensitive facts. No blanket redistribution clearance, unknown license import, enterprise or brand asset reuse. Preserve [14 cross-specialist leads](../research/CROSS-SPECIALIST-RESEARCH-REGISTER.md) for concrete future decisions; no reopen or integration now. Forgejo upstream pin was not established; official documentation only.

### 14.9. Non-functional requirements

| ID | Requirement | Observable fulfillment / limits |
| --- | --- | --- |
| QA-N01 | Authority and safety | Advisory only; no independent acceptance, unauthorized tool calls, installation, real-data export, live probes, deployment or release. |
| QA-N02 | Portability and dependencies | Host/model neutral, file-based skill, no required QA executable, external browser package, API, paid model, service or skill; context-independent Builder. |
| QA-N03 | Privacy and safe evidence | Synthetic or minimal redacted inputs, no hidden reasoning or unrestricted transcripts; respect retention, authorization and isolation; no silent export. |
| QA-N04 | Proportionality and usability | Load material guidance only; use lowest-cost sufficient methods; no default exhaustive testing or benchmarks, repeated boilerplate or unnecessary specialist selection by user. |
| QA-N05 | Reproducibility and truthfulness | Exact relevant identity, environment, raw outcome, attribution and evidence purpose; distinguish source/inference/reported/observed; retain original failure. |
| QA-N06 | Maintainability | Stable IDs, navigable source-linked original guides, shared capability records, existing schema and focused tests. |
| QA-N07 | Protected baseline | Preserve framework, catalog/retrieval, existing specialist behavior, legacy outputs, Linux/native Windows standing suite and v1.2.0 tag. |
| QA-N08 | Bounded claims | No universal security/accessibility, all-host activation, AI authorship, certification, comparative superiority or numerical guarantee without actual applicable evidence. |
| QA-N09 | Source/rights integrity | Original synthesis, traceable provenance, rights/notice and current decision-sensitive facts; no unqualified redistribution; preserve research histories. |
| QA-N10 | Independence | Separate Builder, reviewer and direct observations, no simulated independent role, self-handoff or counting disposable tests as product regression. |

### 14.10. Acceptance criteria

All 18 proposed gates are required for technical qualification. Combine representative exercises only where actual evidence covers the same scope and identity; techniques within each are context-sensitive. Required actual observations cannot be replaced by hypothetical walkthroughs. Missing capability or independent observer blocks affected claim; preserve achieved evidence and assess canonical B2 outcome. No mandatory comparative AIPF-only benchmark, fixed new test count or numeric score waiver.

| ID | Criterion | Required observable evidence | Exercise families |
| --- | --- | --- | --- |
| QA-AC01 | Additive registry and helper | Mechanism tests for all three IDs/modes, applicable paths, missing/nonmatching path, unavailable skill, no lookup/subprocess, invalid/unknown/blank cases and unchanged legacy results. Preserve prior registry entries exactly. | QD07,QD12 |
| QA-AC02 | Semantic activation and fallback | Fresh actual observations for plan/diagnose/review and minor/unrelated nonactivation, missing guide and unavailable tool/host. Do not reveal expected classifications to observer beforehand. Helper output alone insufficient. | QD07 |
| QA-AC03 | Risk strategy and oracles | Actual direct planning observation: intended behavior, coupled surfaces, protected states, justified levels, exact inputs/expected and negative effects, capable observer and constraints. No invented requirement or forced tool. | QD09,QD11 |
| QA-AC04 | Boundary, state and contract | Execute synthetic relevant positive/negative and explicit zero/false/empty cases plus state transitions; actual local consumer/provider interaction, broken contract versus allowed compatible addition. Separate mock evidence. | QD02,QD03,QD04 |
| QA-AC05 | Diagnosis and differential | Retain flawed baseline, intended assertion failure, causal trace and minimal correction, corrected pass and unaffected invariant. Demonstrate equivalent invalid result and incomparable conditions are not acceptance. | QD01 |
| QA-AC06 | Test effectiveness | Material mutant survives weak suite; stronger independently authored check detects intended failure; known-good implementation passes. Separate equivalent/invalid mutant examples; no arbitrary mutation score. | QD02,QD10 |
| QA-AC07 | Failure, recovery and flake | Actual disposable deterministic delay/order/duplicate/partial failure checks; verify recovery and no unintended effects; retain schedule/seed and raw outputs. Demonstrate preservation of intermittent or failed observation, no production operation. | QD03 |
| QA-AC08 | Rendered user behavior | Actual local browser or capable assigned observer verifies interaction and keyboard/focus or responsive/error state plus observable effect. Separate mocked/API/static/rendered/accessibility scope. Unavailable observer is a required gap. | QD05 |
| QA-AC09 | Source-bound critique | Actual existing-system source review plus bounded confirmed defect, unresolved lead, rejected suspicion and optional improvement, with trace/counterevidence and real impact. Confirmed defect may be demonstrated separately on synthetic fixture; no fabricated product defect, execution or AI attribution. | QD06 |
| QA-AC10 | Data quality | Executed synthetic transformation/validation with duplicates, missing/zero/invalid rows, expected reconciliation and rejection; state preservation or round-trip when relevant; no real data export. | QD09 |
| QA-AC11 | Agent behavior and contracts | Actual bounded semantic observation: valid alternate path accepted, forbidden operation/target denied, causal prerequisite, parameter/schema drift, misleading untrusted data treated as data. Actual operation/sentinel or capable trace, not prose alone. | QD07,QD08 |
| QA-AC12 | Evaluation validity | Frozen example set, explicit gates and actual known-good/bad/ambiguous judgment or deterministic oracle, disagreement/abstention and retrieval/answer distinction; independent or separately observed checks where material. No invented metrics or paid benchmark requirement. | QD08 |
| QA-AC13 | Capability/source qualification | Actual point-of-use comparison of existing/local option and material external candidate; exact source/version/rights, platform, data/telemetry/access, cost/exhaustion and limits. Unknown remains unselected; no install or transfer. | QD06,QD11 |
| QA-AC14 | Direct and distinct Builder | Actual direct practical execution and actual fresh distinct Builder with complete authorized T1 and accessible scratch inputs only; independent reviewer inspects source identity, reproduces Builder tests and runs additional negative checks under effective safe confinement or assigned capable observer. Preserve original/corrected evidence and reconcile failures. | QD10 |
| QA-AC15 | Composition | Actual combined UI/UX, Architecture, Security and QA planning/review with coherent strategy or payload, concrete expected/negative outcomes, preserved privacy/design/contract constraints and no duplicated governance. | QD11 |
| QA-AC16 | Knowledge and provenance | Verify twelve families, question index, unique decision IDs, source/rights links, positive/negative advice, source fallback, preserved 29 source IDs and 14 XR leads, shared index and no unqualified import. | QD12 |
| QA-AC17 | Integrated regression | Exact candidate commit/tree, focused tests and full inherited 163 standing tests plus actual newly discovered cases on Linux and native Windows. Raw terminal outcome and environment; preserve framework/catalog/legacy behavior and prior tag. No silent skips or weakened assertions. | QD12 |
| QA-AC18 | Final reconciliation | Reconcile every QA-F/K/N and QA-AC against actual evidence, exceptions, observer, limits, recovery anchor and immutable candidate. Technical B4 pass only with required gates; otherwise canonical outcome. Owner acceptance and B5 separately authorized; validate consolidation/release tree and publication identity. | QD12 |

#### 14.10.1 Evidence layers and measures

- Mechanism: registry/helper, index/source/rights and deterministic focused tests.
- Semantic: actual material consultation and nonactivation/fallback, composed guidance and authorized action; static text assertions are not agent reasoning evidence.
- Target behavior: actual authorized disposable test/renderer or named capable observer; exact source/fixture, raw outputs and intended failure reason.
- Independent workflow: actual fresh Builder report/source and reviewer independently executed negative checks, original/corrected identity and reconciliation.
- Integration and release: exact tree, full standing results per platform, preserved baseline, rights and owner disposition, published tag/release identity only when observed.

Track requirements with sufficient evidence or explicit gaps, actual positive/negative and no-effect checks, fail-before/pass-after and preserved behavior, test-effectiveness counterexamples, environment/observer and unresolved source/rights. Count suites separately: disposable tests are not standing product regression. No aggregate score, test count or prose fluency substitutes for required evidence.

### 14.11. Representative qualification exercises

Discovery QD01–QD12 retained and elaborated. All are proposed, unexecuted. Original disposable synthetic fixtures or scoped source review only; actual observation required where stated. Cases may be combined when coverage is equivalent, not removed by unsupported inference.

| ID | Scenario | Stimulus and expected behavior | Evidence |
| --- | --- | --- | --- |
| QD01 | Stale asynchronous result | Original disposable search lets older request A overwrite newer B. Controlled completion order B then A; final result must be B, stale completion ignored, single-request case preserved. Alternatively equivalent material predicate defect with causal trace. | Baseline intended assertion fails, diagnosis and source identity, minimal correction, corrected pass, preserved behavior. Test equivalent bad and incomparable cases separately. |
| QD02 | Weak suite and counterexample | Original transformer treats explicit false as absent; initially weak tests miss it. Independent check distinguishes false/zero/empty from missing; protects unrelated label behavior. Include equivalent and invalid mutant classifications. | Actual weak-suite pass, material mutant failure for intended reason after strengthening, known-good pass, counterexample and oracle. No LOC/coverage target. |
| QD03 | State and failure | Disposable in-memory operation processor: duplicate event, failure after effect, cancellation or retry with explicit controlled schedule. Check no double mutation, unrelated resource unchanged, correct failure/recovery, invalid transition denied. | Raw outputs, schedule/seed, state and negative-effect assertions, first failure/retry retained. No live fault injection. |
| QD04 | Consumer/provider contract | Local consumer and provider exchange expected fields/type; break required field/type, then add allowed optional field. Test both contract and real local interaction with explicit error behavior. | Broken contract intended failure, compatible case success, actual seam and mock limitations identified. |
| QD05 | Browser/UX | Disposable local form or dashboard: keyboard/focus, delayed or failed request, duplicate submission or long text, unsaved state if required, visible result and controlled underlying effect. | Actual rendered local observer with context/viewport and bounded trace/log; static and mock evidence separate. If unavailable, pending required observation. |
| QD06 | Existing-system critique | Read-only review of Praxis or authorized source: changed/coupled paths, actual complexity or test gap, potential heuristic lead; counterevidence, rejected suspicion, unresolved runtime claim and optional improvement. Missing-history fallback. | Source identity/locations, observed facts vs inferences, real impact. Confirmed defect can come from disposable fixture; no product defect invented, no source mutation. |
| QD07 | Activation, tool boundaries | Fresh agent requests for modes, minor/unrelated and unavailable guide; controlled synthetic tool schema/operation fixture: allowed alternate sequence, forbidden target, prerequisite, malformed argument/schema drift, retrieved instruction claiming authorization. | Actual semantic decisions, operation/sentinel or trace, contract change check, no unauthorized effect. Helper tests separate. |
| QD08 | AI evaluation validity | Frozen small set: valid, invalid and ambiguous answer; right retrieval but wrong answer; allowed alternative action vs forbidden action. Calibrate evaluator, retain actual disagreement or abstention and source/model unknowns. | Actual bounded judgments/oracle outcomes, identity and limits, no fictional cost/performance or mandatory external model call. |
| QD09 | Data integrity | Synthetic CSV-like import: duplicate ID, empty/missing vs zero, malformed row, expected count/totals, rejection and preserved good rows. Round-trip or partial-write recovery where relevant. | Actual logs, expected reconciliation, rejected input and no unintended effect. Also observe risk-led plan. |
| QD10 | Fresh distinct Builder | Empty scratch workspace; complete authorized local service or data processor task, including explicit negative-effect and invalid/duplicate behavior, test/evidence/stop constraints; no external service. Prompt Agent retains independent checks separately. | Returned source/hash, raw tests/env, actual independent reviewer reproduces and adds negative checks with safe confinement, preserves original and corrected artifacts; distinct from direct execution. |
| QD11 | Composition and alternatives | Privacy-first dashboard planning/review: user interaction, data contracts and trust requirements, actual observable QA checks, compare existing/no service and suitable optional candidate under concrete constraints. | Actual composed decision/payload, coherent four-specialist contribution, no conflicting scope, qualified capability facts and limitations. |
| QD12 | Integrated candidate | Readback index, provenance, rights, deferred leads, registry and exact delta; run focused and full standing regression on Linux and native Windows; reconcile requirements, observer evidence and source identity. | Exact candidate/tree, raw results, ledger and B4 disposition; no merge/tag before separate owner acceptance and B5. |

#### 14.11.1 Independent execution and correction

Actual fresh Builder receives only canonical authorized T1 and accessible scratch implementation inputs, not reviewer answers or mandatory governing resources. Use an original bounded task; no real data, external service or production mutation. Reviewer compares source hashes, inspects boundary and oracle, reproduces submitted tests and authors independent negative checks with safe authorized execution. If effective confinement or observer unavailable, retain source evidence and mark required observation pending. Preserve original failure and corrected diff/source/raw outputs, rerun affected checks, assess B2. Same-agent direct fixture does not establish independence.

#### 14.11.2 Exact integrated regression

Run `python -m unittest discover -s tests -v` on full exact candidate Linux and native Windows, plus required separate capable observer exercises. Standing 163 tests from v1.2.0 remain intact; actual discovered new count governs. Preserve command, raw logs, checkout SHA/tree, Python/OS, skipped/failure/warning reasons; no silent skip, reduced threshold or altered legacy test expectation. B5 consolidation creates a release-bound revision; verify exact prospective merge tree and relevant regression, reconcile actual main and existing CI policy before tag. Existing Windows job intentionally skips main pushes; transfer Windows evidence only with identical controlling tree/config and documented scope. No automatic workflow change.

### 14.12. Delivery and release

Proposed work breakdown aligned to existing AIPF B1–B5, not a new governance structure or granted authority. Owner approval and separate B1–B4 authorization required. No schedule or commitment to a release date.

| Stage | Planned deliverable and exit condition |
|---|---|
| B1 — Baseline/design | Reconcile v1.2.0 source, tag, PRD/research, actual registry/helper/capabilities, requirements, observer feasibility, source/rights and guide coverage. Confirm modes and material constraints; resolve decision-sensitive source gaps before design. |
| B2 — Knowledge/capabilities | Original SKILL, index, guides, cards and source register, selected shared discovery entries and examples. Preserve deferred research and rights; no code imports/dependencies. Assess execution using canonical Block B2. |
| B3 — Integration | Additive registry/entry/docs and focused tests; preserve three entries, helper and existing behavior. Verify exact source delta. No new required runtime. |
| B4 — Qualification | Immutable candidate/tree, all 18 criteria with actual evidence, direct and independent Builder/reviewer, preserved correction history, full cross-platform regression and individual requirements ledger. Stop at technically qualified candidate if gates met, otherwise canonical PARTIAL/FAIL/BLOCKED as applicable. No merge/tag/publication. |
| B5 — Release | Separate owner acceptance and release authority; consolidate approved PRD, verify source/rights/ID parity and version docs, release-bound delta and CI/reviews, merge main only after gates, reconcile actual tree and prior tag, publish new tag/release at verified commit. No further specialist work. |

#### 14.12.1 Planned repository surfaces

| Surface | Treatment |
|---|---|
| skills/qa-engineering-quality/ | New SKILL, INDEX, SOURCES and original progressive guides |
| skills/specialists.json; skills/praxis/SKILL.md; PRAXIS.md; skills/README.md | Add material consultation and version guidance; preserve legacy IDs and behavior |
| knowledge/capabilities/ | Add useful original discovery records to existing groups/index/source register, preserve 24 existing entries |
| tests/ and scenario fixtures; docs/TESTING.md | Add focused mechanism/knowledge checks and scenario/qualification guidance; retain standing strategy and legacy assertions |
| research/ | Keep source/lead records and appropriate bounded qualification provenance; private evidence remains outside public redistribution |
| framework/, catalog/, scripts/, ui/, .github/, .agents/, licenses | Protected by default; no required behavior, runtime, CI or licensing change; material exception requires separate authorization |
| B5 docs/PRD.md and release docs | Proposed PRD v1.4 Section 14, original stable IDs and historical pin, README/changelog/release record and links; retire temporary active PRD |

#### 14.12.2 Risks and mitigations

| Risk | Mitigation |
|---|---|
| Duplicate governance | Advisory only, existing AIPF controls and T1; reject extra approval/runtime |
| False confidence | Negative effects, meaningful mutants, independent oracles, preserve failures and gaps |
| Overfit to trace or benchmark | Material constraints, valid alternate paths, held-out cases, actual oracle and hard gates |
| Tool/dependency creep | Existing/native first, source/rights and point-of-use qualification |
| Misleading heuristic or judge | Counterevidence, calibrated/independent observation, abstention, no unsupported authorship or cost |
| Synthetic evidence overclaimed | Separate actual runtime, mock, source, reported and independent evidence |
| Unsafe execution/data | Bounded authorized disposable confinement; source-only when insufficient; no unauthorized export |
| Cross-platform or observer unavailable | Named capable observation required, retain partial evidence and stop dependent qualification |
| Stale provider/license facts | Pinned provenance, recheck material facts; unresolved rights reference-only |
| Fragmented requirements | Consolidation at acceptance/release, immutable original and ID parity |
| Maintenance overhead | No fixed guide/tool/test-count target; minimal complete integration |

### 14.13. Traceability

#### 14.13.1 Existing requirement crosswalk

| Baseline obligations | QA extension |
|---|---|
| PR-01–03 entry, AIPF, project requirements | QA-F01/03/20/22, QA-N01/07; no duplicate governance |
| PR-04–06 activation and knowledge | QA-F01/19/22, QA-K01–09 |
| PR-07–09 direct/distinct, evidence | QA-F09–13/18/20, QA-N05/10, QA-AC05–07/14/17 |
| PR-10–11 extensibility/discovery | QA-F22, QA-AC01/02 |
| PR-12 and PR-14 future plugin/assurance | Deferred, no packaging or Review Parity |
| PR-13 engineering expansion | Proposed QA v0.1; preserve roadmap and future DevOps |
| KI-01–08 | QA-K01–10 and QA-F19; original progressive guides/shared capabilities and fallback |
| NFR-01–10 | QA-N01–10, all baseline attributes preserved |
| Architecture, Security and UI/UX requirements | QA-F02/06/07/08/15/18/21 and QA-AC08/15/17; verification complements protected domain constraints, no behavior/retrieval/catalog change |

#### 14.13.2 Individual requirement-to-acceptance matrix

| Requirement | Primary acceptance criteria |
| --- | --- |
| QA-F01 | QA-AC01, QA-AC02 |
| QA-F02 | QA-AC03, QA-AC09 |
| QA-F03 | QA-AC03, QA-AC04, QA-AC06 |
| QA-F04 | QA-AC03, QA-AC04, QA-AC08 |
| QA-F05 | QA-AC04, QA-AC06, QA-AC10 |
| QA-F06 | QA-AC04, QA-AC11 |
| QA-F07 | QA-AC08, QA-AC15 |
| QA-F08 | QA-AC07, QA-AC08 |
| QA-F09 | QA-AC05, QA-AC07, QA-AC09 |
| QA-F10 | QA-AC05, QA-AC06, QA-AC17 |
| QA-F11 | QA-AC05 |
| QA-F12 | QA-AC06 |
| QA-F13 | QA-AC07, QA-AC17 |
| QA-F14 | QA-AC09 |
| QA-F15 | QA-AC10, QA-AC15 |
| QA-F16 | QA-AC11, QA-AC12 |
| QA-F17 | QA-AC12 |
| QA-F18 | QA-AC05, QA-AC09, QA-AC14, QA-AC18 |
| QA-F19 | QA-AC02, QA-AC13 |
| QA-F20 | QA-AC14 |
| QA-F21 | QA-AC15 |
| QA-F22 | QA-AC01, QA-AC16, QA-AC17 |
| QA-K01 | QA-AC16 |
| QA-K02 | QA-AC16 |
| QA-K03 | QA-AC16 |
| QA-K04 | QA-AC13, QA-AC16 |
| QA-K05 | QA-AC13, QA-AC16 |
| QA-K06 | QA-AC13, QA-AC16 |
| QA-K07 | QA-AC13, QA-AC16 |
| QA-K08 | QA-AC13, QA-AC16, QA-AC17 |
| QA-K09 | QA-AC02, QA-AC06, QA-AC09, QA-AC11, QA-AC16 |
| QA-K10 | QA-AC16, QA-AC18 |
| QA-N01 | QA-AC02, QA-AC11, QA-AC14, QA-AC15, QA-AC18 |
| QA-N02 | QA-AC01, QA-AC13, QA-AC14, QA-AC17 |
| QA-N03 | QA-AC07, QA-AC10, QA-AC11, QA-AC13, QA-AC14 |
| QA-N04 | QA-AC02, QA-AC03, QA-AC12, QA-AC15 |
| QA-N05 | QA-AC05, QA-AC07, QA-AC09, QA-AC12, QA-AC14, QA-AC17 |
| QA-N06 | QA-AC01, QA-AC16, QA-AC17 |
| QA-N07 | QA-AC01, QA-AC15, QA-AC17, QA-AC18 |
| QA-N08 | QA-AC08, QA-AC09, QA-AC11, QA-AC12, QA-AC18 |
| QA-N09 | QA-AC13, QA-AC16, QA-AC18 |
| QA-N10 | QA-AC14, QA-AC17, QA-AC18 |

This is planned traceability, not completed evidence. B4 ledger expands each acceptance criterion and requirement into actual source/observer references, achieved evidence, gaps and disposition.

#### 14.13.3 Research and decision sources

| Area | Basis and scope |
|---|---|
| Integration/governance/portability | [Product PRD](PRD.md), [DEC-002](decisions/PRAXIS-DEC-002-builder-context-independence.md), [DEC-003](decisions/PRAXIS-DEC-003-quality-first-prompts.md), [DEC-004](decisions/PRAXIS-DEC-004-specialist-expansion.md), [testing](TESTING.md), [registry](../skills/specialists.json), [helper](../scripts/praxis_context.py), AIPF v8.10.1 |
| Risk and maintainability | QA-S01,06,07,09 — source and author-reported experiments, not demonstrated productivity |
| Differential/test effectiveness | QA-S03,24,25 — pinned method and official references; current CodeVetter warm executor unavailable; original fixture proposals |
| Contracts, browser, failure and design | QA-S02,05,12,20,22,26,27 — source/docs only, no actual hosted tool qualification |
| AI and evaluation validity | QA-S02,04,08–11,13–15,28 — techniques and author reports; no reproduced performance claims |
| Data/model quality | QA-S16,24,26 — rights and actual applicability must be qualified |
| Capability and cross-specialist retention | QA-S01–29 and XR-01–14, full [pinned source register](../research/qa-engineering-quality/QA-SOURCE-REGISTER-01.md), [cross-specialist register](../research/CROSS-SPECIALIST-RESEARCH-REGISTER.md) |

Discovery records control what was observed; this PRD proposes original requirements, modes, IDs and representative scenarios. Full code audit, runtime evaluation, benchmark reproduction, blanket license clearance and current service terms were not established in discovery. Further focused source review at B1/B2 only when material. Prior attachments not available can be re-provided if they change a decision; do not invent missing historical evidence.

### 14.14. Owner review and stop boundary

| Decision | Recommendation | Alternative / implication |
|---|---|---|
| Product version | Praxis v1.3.0; QA v0.1; AIPF unchanged | Defer/narrow if desired; no framework or other specialist change |
| Modes | Plan, diagnose, review, actual verify in review when authorized | Fourth verify mode only with distinct material value |
| Coverage | All 12 families, conventional software QA plus data/AI, conditional selection | Narrow only by explicit owner decision; no fixed card count |
| Integration | Existing schema/helper and file-based guidance | New runtime or platform not proposed |
| Qualification | Actual direct and distinct Builder/reviewer, defect-sensitive tests, rendered observer and full cross-platform regression | Missing required observer remains open; do not substitute hypothetical success |
| Instruction improvement | Include evaluation literacy; preserve XR-10 for separate research | No automatic optimization or mandatory benchmark |
| Other specialists | Preserve all deferred leads; revisit when concrete decision warrants | No additional specialist or Review Parity now |
| Documentation | Temporary PRD v1.0; consolidate into canonical PRD at acceptance/release | Preserve original approved revisions and all IDs |

Owner approved this specification and authorized B1–B4, then accepted the qualified immutable candidate and separately authorized B5 release and consolidation on 2026-11-26. Requirements approval itself does not authorize execution. No deployment, new service or future specialist implementation is authorized.

**Current stop:** verified published Praxis v1.3.0, subject to the release gates and publication reconciliation in the [release record](releases/1.3.0.md). Preserve v1.2.0, AIPF, prior requirements and qualification evidence, and cross-specialist research. No DevOps & Reliability development or other future work is authorized.
