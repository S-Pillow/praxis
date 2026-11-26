# Praxis — Security & Privacy Specialist

Product Requirements Document | v1.0 | 25 November 2026

**Status:** Proposed for product-owner review. Planning and documentation authorized; implementation, integration, testing against live systems and release are not authorized. Proposed component version: 0.1; proposed next product release: v1.2.0, subject to later owner approval. Governing framework: AIPF v8.10.1.

**Baseline:** Praxis v1.1.0, commit `37b98b9a21f14c609e4ed656cc47bb08d7133819`, tree `b634d72d89aa07e2411061e9a5d9493d81048b92`. This specialist-specific PRD supplements the product PRD v1.2 (`docs/PRD.md`) and its accepted architecture requirements; it does not replace historical acceptance records. Source register in section 10 derives from Research Checkpoint 01, dated 2026-11-25.

## 1. Product vision and outcomes

Praxis should give a Prompt Agent or direct executing agent practical security and privacy expertise at the point of decision, not only after code has been written. The specialist should help build the simplest sufficient controls for the actual assets, actors, data flows and risks, improve existing systems without avoidable behavioral changes, and distinguish source-backed findings from suspected weaknesses and optional hardening. AIPF remains the sole governing authority for execution, authorization, evidence, acceptance and release.

The product problem is not a shortage of security lists or scanning tools. It is the difficulty of selecting appropriate controls, recognizing material trust boundaries, translating security decisions into implementation requirements, and verifying what a control actually prevents. Privacy needs equivalent attention: avoiding unnecessary collection, limiting exposure, honoring retention and deletion, and evaluating third-party processing. A clean scan, a privacy-oriented brand or a checklist alone does not establish security or legal compliance.

| Outcome | Observable success |
| --- | --- |
| Prevent avoidable design flaws | Identify assets, principals, boundaries, abuse cases and context-appropriate controls before implementation; specify negative tests. |
| Reduce disclosure | Prefer no new collection or external transfer where sufficient; explicitly address logs, identifiers, exports, backups and agent context. |
| Make review actionable | Tie each material finding to evidence, expected behavior, impact, uncertainty and the smallest suitable remediation. |
| Preserve extensibility | Compose with Architecture and UI/UX without new governing rules, mandatory delegation or runtime services. |
| Improve portability | An independent Builder can implement a complete authorized payload without access to Praxis, the source catalog or the PRD. |

### Users and representative jobs

- Product owners and technical leads: decide what protection is justified, assess residual risks and approve material tradeoffs.
- Prompt Agents and direct developers: choose controls, reason about data and trust boundaries, produce concrete implementation and verification instructions.
- Builders and reviewers: implement authorized controls, test negative cases, assess evidence, correct specific defects and disclose unresolved gaps.
- Operators: understand configuration, data flows, access, recovery and tool risks without having to become security specialists.

Success does not mean more controls, more scanners, more findings or more process. The first release must not claim penetration-testing coverage, universal protection, compliance certification, detection rates or comparative superiority.

## 2. Scope and operating modes

The initial component covers material security and privacy decisions in new and existing software. It supports local utilities, web applications, APIs, agents and service integrations; additional platforms are covered only to the extent that the relevant evidence and domain knowledge are available.

| Mode / proposed task ID | Expected behavior |
| --- | --- |
| Design / `security-design` | Establish threat and privacy context, select suitable controls and alternatives, define requirements and observable verification. |
| Harden / `security-harden` | Diagnose a material weakness or changed boundary, preserve approved behavior, select a bounded mitigation and regression tests. No silent fixes. |
| Review / `security-review` | Perform proportionate source-based assessment, distinguish observed evidence from unresolved leads and hardening, specify safe verification and recommendations. |

Activation requires a material security/privacy question or boundary change after canonical AIPF routing. Examples: new identity/session flow, resource authorization, untrusted file or URL handling, sensitive storage, telemetry/export, credential lifecycle, dependency selection, agent permissions or a requested security critique. Routine cosmetic edits, ordinary formatting and unrelated minor fixes do not activate it solely because a chapter applies. Existing specialist consultation remains available; one agent synthesizes recommendations rather than creating competing approvals.

A full audit, live probing, target-controlled execution, dependency installation, persistent audit outputs, credential use, access changes or external data transfer requires separately established authority and capability under AIPF. A request for guidance is not an audit authorization. Security work must remain defensive and scoped to authorized targets; use synthetic inputs and dummy identities for exercises. If execution safety cannot be enforced, do not execute and identify the precise evidence gap.

### Explicit exclusions for the first release

- No embedded scanner, exploit catalog, autonomous pentest harness, mandatory multi-agent system, hosted audit service, secrets manager, telemetry, network crawler or new database.
- No automatic installation, account creation, external scanning, upload, remediation, production policy change or release action.
- No duplicated AIPF governance, Review Parity runtime or future QA/DevOps specialist implementation.
- No bulk source import, blanket license clearance, legal advice, compliance certification or mandatory framework-specific control on every project.

## 3. Functional requirements

All SP requirements are proposed Must requirements for the first qualified candidate unless an explicit scope decision changes them. Acceptance IDs are in section 8. The specialist supplies advice and concrete requirements; only the active project authorization permits action.

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

## 4. Knowledge architecture and curation

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

### Knowledge and source requirements

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

### Suggested decision record contract

Stable ID; domain; trigger and decision question; project context assumptions; alternatives and rationale; applicable/non-applicable conditions; implementation constraints; security/privacy tradeoff; negative/positive checks; unresolved facts and revisit trigger; primary reference(s), date/version and rights disposition. A card is advisory knowledge, not a finding, execution instruction or authorization. Knowledge examples must use dummy data.

## 5. Findings and verification integrity

A security review must distinguish evidence from a hypothesis. A source location or scanner warning does not by itself demonstrate an exploitable boundary failure. Identify the affected principal, protected resource, expected control, relevant source/configuration, counterevidence and observed result. Do not imply a stronger impact than evidence supports.

| Disposition | Required interpretation |
| --- | --- |
| Confirmed | Concrete boundary/control failure established by source and/or sufficient bounded observation; material claims independently verified when required by AIPF. Record exact verified surface and impact. |
| Needs validation | Plausible source-backed concern with an exact missing fact, environment, permission or observation. No definitive severity or success claim when evidence is insufficient. |
| Rejected | Evidence refutes the candidate or establishes an effective controlling mitigation. Preserve concise reason when material. |
| Hardening / design recommendation | Optional defense-in-depth or architectural improvement; do not report as a confirmed vulnerability solely because another layer could be added. |

These are security-domain interpretations of evidence, not a replacement for AIPF outcome or acceptance vocabularies. Use severity/likelihood and impact only at the strength supported by the available facts; identify methodology/version and assumptions. Report coverage as assessed surfaces and exclusions, not a percentage unless the denominator is defined and evidenced. Avoid equating no findings with a secure system.

### Evidence contract and safe observation

For material findings, retain an ID/fingerprint, source revision, target/configuration, trace and relevant lines, expected control, evidence attribution, counterevidence, disposition, bounded impact, recommended correction, regression check, unresolved fact and recheck trigger. Redact sensitive values and avoid putting private findings in public issues or PRs. Revalidate affected evidence after source/configuration changes. Prior evidence transfers only for unchanged controlling conditions.

A scoped review is source-read-only by default. Actual execution of untrusted target code requires an authorized isolated environment with no external network, sanitized environment, read-only source/toolchain, scratch-only writes and bounded resources. Use dummy accounts and data, never live targets or real secrets; record inability to observe if required controls are missing. No automatic finding publication, broad scans or retention of sensitive artifacts. Independent verification is real, named and observable, not simulated by relabeling the same agent.

## 6. Shared capability intelligence

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

## 7. Integration and nonfunctional requirements

### Logical design

Use the existing Praxis entry, registry and helper; AIPF chooses the applicable path first, the agent identifies material security/privacy intent, and optional specialist consultation returns advice. The agent reconciles domain contributions into one authorized execution decision or payload. Architecture owns structure and tradeoffs; Security owns risk, controls and privacy; UI/UX owns interaction/accessibility, including comprehensible privacy choices; QA owns broader behavioral verification; DevOps owns broader operational delivery; Review Parity remains deferred. Domain boundaries are advisory, not exclusive; cross-domain issues should be synthesized, not duplicated.

Proposed paths: `skills/security-privacy/SKILL.md`, `INDEX.md`, `SOURCES.md`, nine progressive guides, additive `knowledge/capabilities/` entries, `skills/specialists.json` registration, narrowly affected entry/helper/tests/docs. Exact path naming and applicability representation are B1 design decisions. Security can be relevant across more than Chapters 11/12; do not restrict it solely to one application type or introduce a new AIPF chapter. Determine the smallest compatible representation after inspecting the existing registry/helper and canonical routing; no unconditional activation by chapter alone. Existing UI singular `chapter` and architecture `chapters_any`, optional lookup semantics and serialized legacy outputs must remain compatible.

| ID | Quality constraint |
| --- | --- |
| SN-01 | Preserve AIPF authority, existing product/version boundaries and explicit scope. Neither source material nor scanner finding grants action authority. |
| SN-02 | No new mandatory runtime, external dependency, storage, telemetry, paid quota or provider integration. Prefer bounded, progressive loading and existing helper mechanisms. |
| SN-03 | Privacy by default: minimize collection/retention, no real secrets in output/fixtures, no silent network or target execution; sanitized evidence and scope-safe storage. |
| SN-04 | Portability: direct mode and independent Builder payload; no hidden governing context, unavailable capabilities or mandatory separate agent. |
| SN-05 | Reproducibility: pinned source and exact test identity, cross-platform UTF-8/path handling, deterministic local fixtures, raw statuses and truthful limitations. |
| SN-06 | Maintainability: unique IDs, links, source rights, small original knowledge, clear separation of stable vs volatile information; do not duplicate AIPF or prior specialist content. |
| SN-07 | Security/availability claims proportionate to evidence; no guarantees, certification, universal detection or benchmark superiority without separately authorized evidence. |

## 8. Acceptance and qualification

The following criteria are proposed release-candidate gates, not completed evidence. The candidate must satisfy each applicable criterion, with exact source identity, actual results, evidence ownership, limitations and recovery anchors. A blocked required observation is not a pass. Any owner acceptance and publication decision remains separate.

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

### Representative exercise set

Combine scenarios where sensible, without substituting one kind of evidence for another. A realistic small API with dummy users and resources can cover tenant isolation, input validation, negative tests and portable Builder handoff. A local-only utility can test no unnecessary network or persistence, secret-safe logs and fallback. A privacy-oriented dashboard can exercise retention, telemetry minimization and combined UI/Architecture/Security consultation. A controlled source-only review of an existing app can assess trust boundaries and findings without contacting deployed services. A deliberately untrusted agent-input fixture can test permissions and non-disclosure. A scanner result can be represented by a synthetic fixture; real scanning is not mandatory and requires separately authorized capability. Include failure/correction and reopening where material.

Evidence types: deterministic tests for mechanisms, observed semantic decisions for advisory quality, source references for claims, actual independent handoff for portability, and hosted CI on exact release-bound source for cross-platform regression. Record commands, raw exit/status, environment, commit/tree, observer and limitations. Do not count disposable exercise tests as product regression tests. No mandatory comparative benchmark or new audit infrastructure.

## 9. Delivery, milestones and risk

The following B1–B5 sequence is a proposed delivery plan aligned to the prior Architecture build; it is not additional AIPF governance and does not grant execution authority.

| Stage | Scope / exit |
| --- | --- |
| B1 – Baseline and design | Reconcile owner-approved PRD, exact released source, implementation surfaces, activation strategy, source/rights gaps and acceptance matrix. Exit: bounded authorized build and exact protected invariants. |
| B2 – Knowledge and capabilities | Curate original guides/cards and selective shared records; verify sources/rights, decision coverage and link integrity. Exit: source-linked knowledge, honest limits and no mandatory tools. |
| B3 – Integration | Add compatible registry/entry/help changes, relevant tests, direct and portable output behavior; preserve existing specialists and AIPF. Exit: deterministic focused integration passes. |
| B4 – Candidate qualification | Run full regression, meaningful practical and independent Builder exercises, reconcile every requirement and limitation; preserve exact candidate and evidence. Stop at qualified candidate. |
| B5 – Delivery and release | Separate owner authorization: pre-release documentation, protected PR, native Linux/Windows CI, source reconciliation, owner acceptance, merge and publication only when explicitly authorized. |

### Principal risks and mitigation

| Risk | Mitigation / revisit trigger |
| --- | --- |
| Over-activation or second governance model | Task materiality, canonical AIPF routing, negative routing tests; review any new authority language. |
| False confidence or false positives | Evidence classifications, existing-control analysis, safe negative tests, bounded claims; recheck on source/config changes. |
| Sensitive data exposure | No real credentials or private findings in public artifacts; explicit data flow and offline alternatives; recheck when tools/telemetry change. |
| Untrusted code or prompt execution | Read-only discovery, authorized sandbox checks, no hidden privileges or mandatory tools; block execution when isolation absent. |
| Stale guidance or mixed rights | Pinned sources, file-level rights, current primary references for material facts; recheck editions/terms at point of use. |
| Scope creep and review duplication | Original selective records, shared index, no Review Parity or other specialist implementation; defer nonessential tools. |

### Decisions for owner review

- Approve or adjust the proposed first-release scope, three operating modes and nine knowledge domains. Proposed release labels (specialist 0.1 / Praxis v1.2.0) are not commitments.
- Confirm acceptable reference-only reuse, source-backed original synthesis and optional tool records; resolve any desired source imports individually.
- Authorize B1–B4 separately after PRD review; B5 preparation and merge/publication remain separately controlled. No implied changes to live apps, provider settings or licenses.

## 10. Source register and traceability

The seven GitHub repository root licenses were inspected at pinned revisions during Research Checkpoint 01 (2026-11-25). Selected documentation, tree listings and limited source samples were read. This is not a comprehensive code audit, tool execution, performance validation or redistribution clearance. The PRD is original synthesis; it does not incorporate source code or copied third-party guides. Exact license blob IDs and selected source observations are recorded below; individual third-party content and recipe rights remain separate.

### Research sources (SR)

**SR-01 — [H4cker](https://github.com/The-Art-of-Hacking/h4cker/tree/72e3da0fa1411ef754a5d61b59cb0f58bf64f5f4).** MIT; LICENSE `e87b7062645d6f36a5f71a908b039b4c5533bfb9`. README, 720-file tree, application-security, AI-security and ethics/privacy/governance landing pages. Discovery only; verify original references individually. Exclude irrelevant training/exploit artifacts.

**SR-02 — [Safe Anything](https://github.com/erkamyaman/safe-anything/tree/09a7269eac49000f6cee64af2f94d2ce05da64be).** MIT; LICENSE `c98b47c040b56fcb3bd9a460aae26fa4fee684e8`. README; docs/privacy.md; docs/STATUS.md; docs/adr/0001-patterns-first.md. Candidate optional scanner. Upstream test claims, not locally reproduced. No data-flow guarantee; offline mode omits OSV dependency checks. Default advisory query sends package names, ecosystems and versions according to docs.

**SR-03 — [DevToys](https://github.com/DevToys-app/DevToys/tree/2dbbc8aa594978d11165a0e8112243c96a277dbc).** MIT; LICENSE.md `a9a469ec012931f7ff027cdfa52c3de917af33df`. README, PRIVACY-POLICY.md (dated 2021), EXTENSIONS-TERM-AND-CONDITIONS.md. Local processing reference; extension trust, clipboard and log boundaries warrant separate assessment. Policy claims not verified at runtime.

**SR-04 — [Umami](https://github.com/umami-software/umami/tree/dbb8d606fbd4e99220fb83bcb4abad3e0f97f42a).** MIT; LICENSE `eff41369347b0c5e88a96bd00c9266343b758e7a`. README, 2,163-file tree, selected prisma/schema.prisma fields (blob `ba94dbceaab7617b8554450a119f3716703a1dff`), collection pixel route (blob `d7fc2416709a903ea5d0dfedabc688539a06f3b2`). Session IDs, event data, distinct IDs and replay configuration make this a useful privacy-design case, not an assertion of anonymization or a product vulnerability. [Replay docs](https://docs.umami.is/docs/replays) describe masking.

**SR-05 — [OpenRewrite](https://github.com/openrewrite/rewrite/tree/4d2110dbbf7098a3185b6eb0e94c7f5f55a20d35).** Apache-2.0 root; LICENSE `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`. README and root tree; [official licensing](https://docs.openrewrite.org/licensing/openrewrite-licensing). Individual modules/recipes have differing terms. Optional targeted remediation, not autonomous bulk source mutation.

**SR-06 — [Cloudflare Security Audit Skill](https://github.com/cloudflare/security-audit-skill/tree/c1c8a8c1471069fb0e188eeaff69b8e8db6564a8).** MIT; LICENSE `6dbc9ecb3a5b9080e95b962869e8c7ab16cfdc20`. README, 22-file tree, selected SKILL.md, VALIDATION-AND-REPORTING.md and report-schema.json. Source-first review, coverage tracking, candidate refutation, outcome distinctions, real independence, sandbox boundary. Do not adopt six-phase workflow as parallel governance or claim fresh verifier without capability. No audit run.

**SR-07 — [Agent Skills](https://github.com/addyosmani/agent-skills/tree/e997ac5b9a74eab332d5e9793bb38a38c8cfdd74).** MIT; LICENSE `d67778ada6b9cda6227e9130da182c13e73c8b2e`. README, 280-file tree, selected security-and-hardening/SKILL.md, references/security-checklist.md and evals/cases/security-and-hardening.json. Secure-design guidance and positive/negative activation tests; no imported authority model or rigid universal thresholds.

**SR-08 — [aeo.js](https://aeojs.org/getting-started/introduction/).** Unverified. Introduction and [configuration](https://aeojs.org/reference/configuration/). Generated full text, raw Markdown, index and robots configuration. Review actual generated disclosure, distinguish crawler guidance from access control. Cross-specialist discovery; do not import code yet.

### Primary standards and reference candidates (PS)

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

## 11. Final planning boundary

This PRD is a proposed requirements baseline for owner review, not an implemented specialist or release promise. Security & Privacy is the next planning priority after the released Architecture & Engineering Design specialist. Preserve Praxis v1.1.0, AIPF v8.10.1, existing UI/UX and Architecture behaviors, catalog/rights, source history and prior acceptance evidence. No implementation, audit against real targets, merge of product changes or publication follows from this document. After approval, the next separate authorization is B1–B4 development stopping at a qualified candidate.
