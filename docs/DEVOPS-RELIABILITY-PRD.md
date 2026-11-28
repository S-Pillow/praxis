# PRAXIS / FORGEFORWARD

# DevOps & Reliability Specialist and Shared Documentation & Repository Quality

**Product Requirements Document v0.1 — WORKING DRAFT FOR OWNER REVIEW**  
**Proposed product target:** Praxis v1.4.0 · **Specialist:** DevOps & Reliability v0.1  
**Document date:** November 27, 2026 (America/Kentucky/Louisville)  
**Governing framework:** AIPF v8.10.1, unchanged  
**Decision status:** Proposed requirements only. No owner approval, implementation, installation, repository mutation, infrastructure action, merge, deployment, or B5 release is authorized by this draft.

## 0. Document control, baseline and scope of decision

| Item | Controlling identity or meaning |
|---|---|
| Existing product | Praxis v1.3.0, published November 26, 2026; tag commit `1749f9d3632efd1ab272a69e0738fdd6bd754932`; released UI/UX v0.3, Architecture v0.1, Security & Privacy v0.1, QA & Engineering Quality v0.1. |
| Current requirements | Canonical product PRD v1.4 at the published v1.3.0 tag; blob `30c9792dc55349fbc276df225dd0128919c1726c`. This temporary specialist draft does not replace or amend it. |
| Delivered regression baseline | Released QA record reports 173/173 Linux and 173/173 native Windows tests on the accepted B4 tree, plus separately attributed direct/independent/behavioral observations. These are historical results, not fresh tests of this proposal. |
| Governing AIPF | v8.10.1; canonical DOCX SHA-256 `8e66028c8ebf60ea87180be1c23933273d8a597c425d3a1595ae81d9a720b8e6`. No change or new governance authority is proposed. |
| Retained DevOps research | Git research commit `61c59f908303fb27883d3cff688c304dda620cc6`, parent `016712c9e0594beb77f977468768247ca4585798`; 55 source records, 30 pinned repositories and 133 selected file observations reported in the final register. The figures describe source research, not completed runtime qualification. |
| Document lifecycle | Temporary standalone working proposal. If approved and independently implemented/accepted, incorporate stable approved IDs and complete history into a later canonical PRD revision; preserve original revisions, decisions, source provenance, and release evidence separately. |
| Authorization boundary | This document is for product-owner review of proposed behavior. B1–B4 development, B5, external services, changes to repository controls, scans, hosted connections or deployments each require separate authority as applicable. |

**Status language.** "Delivered" refers only to verifiable Praxis v1.3.0 behavior. "Research-supported" means source/documentation analysis at identified revisions, not test execution of a third-party tool. "Requirement" means target behavior if approved. "Candidate" means a possible optional technology, not an approved dependency. "Acceptance" means a future observable gate, not a passed result.

**Proposal architecture.** There are two coordinated deliverables: (1) an advisory DevOps & Reliability Specialist and (2) shared Documentation & Repository Quality knowledge usable by DevOps, UI/UX, Architecture, Security, QA and the Praxis entry point. The shared capability is not an autonomous sixth specialist, a new rules engine or a replacement for AIPF Chapter 13.

## 1. Vision, problem and outcomes

**Product purpose.** Praxis should help an agent select, implement when separately authorized, troubleshoot and verify suitable operational systems for the actual application: from a local CLI or static site to a managed app, VM, container or distributed service. It should produce professional, maintainable repositories and trustworthy release documentation rather than adopting infrastructure or impressive-looking badges for their own sake.

**Problem.** AI-assisted projects often overselect infrastructure, confuse CI completion with working software, confuse backup with recovery, treat missing telemetry as success, trust source lists without qualifying maintenance or rights, and publish documentation that disagrees with actual implementation. The same agent may accidentally treat a hypothetical plan as permission to provision, run security scans, publish or spend money.

**Desired outcomes.** Better-fit operational choices; explicit ownership and tradeoffs; clearer failure diagnosis; actionable observability; proportionate backup/recovery and cost safeguards; reliable documentation and onboarding; source/artifact/deployment identity reconciliation; reduced preventable operational rework. The agent should advise well during build and critique actual candidate behavior before release when a capable observer and authorization are available.

**Not success metrics.** More source records, an arbitrary security score, a fixed count of guide cards, GitHub stars, fashionable technology, a greater number of CI jobs or an assertion that a workflow ran are not by themselves evidence of product value. Neither source research nor a representative exercise proves universal operational correctness, security, compliance or comparative superiority.

## 2. Users, representative jobs and responsibility boundaries

| User or mode | Job to be done | Specialist contribution |
|---|---|---|
| Product owner / operator | Choose a viable operating model and understand risk, cost, readiness and remaining decisions. | Plain-language alternatives, tradeoffs, estimated assumptions and attributable observations. |
| Direct coding agent | Make an authorized operational change in existing context without a self-handoff. | Conditional implementation guidance, safe sequencing, verification and stop criteria. |
| Prompt Agent / distinct Builder | Give an independent Builder operationally complete instructions without hidden specialist or AIPF access. | Suitable constraints, exact targets and prohibited effects, verification expectations and a portable AIPF T1 payload. |
| Maintainer / incident responder | Diagnose failures, deploy safely, recover and maintain an existing service. | Hypothesis-driven, target-scoped checks, severity/risk prioritization and evidence of restored user behavior. |
| Repository creator / contributor | Understand and present project purpose, setup, contribution and maintenance correctly. | Audience-adapted README, verified onboarding, navigability, truthful badges/release claims and proportionate community files. |

| Domain | Owns specialist knowledge | Boundary DevOps must preserve |
|---|---|---|
| AIPF | Authorization, scope, path, stop, evidence, readiness, release and status. | DevOps cannot create a competing release approval, incident permission, verification status or deployment policy. |
| Architecture | Application decomposition, technology/data/integration design. | DevOps analyzes runtime suitability and operational consequences; does not redesign architecture without separate intent. |
| Security & Privacy | Trust boundaries, data rules, threats, defensible controls. | DevOps operationalizes approved controls and assesses configuration; cannot accept security risk or initiate live probes. |
| QA & Engineering Quality | Test strategy, oracles, diagnosis, regression and AI behavior evaluation. | DevOps supplies operational systems/failure cases; QA determines adequate behavioral testing. |
| UI/UX | Brand, visual hierarchy, accessibility and rendered design. | README visuals follow approved identity; DevOps does not replace design acceptance with source linting. |
| Shared Repository Quality | Adaptive guidance used across domains. | Cross-cutting knowledge; no new registry specialist, mandatory approval committee or parallel AIPF process. |

### 2.1 In scope

Source control and repository lifecycle; CI/build systems and artifacts; delivery models and runtime selection; IaC and configuration; network/DNS/TLS diagnostics; monitoring/observability; reliability/incident/recovery; backup/data operations; operational security and supply-chain evidence; cost/billing/capacity; AI service observability when material; professional GitHub/README and operational documentation; qualified tool discovery; conditional review and critique of observed implementations.

### 2.2 Out of scope by default

No mandatory Kubernetes, containers, GitOps, cloud account, self-hosted forge, telemetry stack, external platform, paid scan, runtime daemon, hosted monitoring, vector database, orchestrator, automatic incident command, automatic infrastructure drift correction, secret collection, live fault injection, autonomous release, release approval, security certification, fixed security score, fabricated screenshot or unqualified asset import. No production data transfer, credential use, installation, privilege escalation, billing enablement, repository settings change, public publication, PR merge or deployment without action-scoped authorization. The proposed PRD itself authorizes none of these operations.

## 3. Operational decision and consultation model

**Proposed modes:** `plan` for an operational design, alternative or migration/rollout decision; `diagnose` for actual failure or degraded service; `review` for candidate operations, release evidence, repository quality and material reliability critique. Modes are advisory and may be combined only when the same authorized task genuinely needs them. "Review" is not automatic release sign-off or an independent observer claim.

**Common response contract.** Identify objective and target, current verified state, owner-approved constraints, affected users/data, governing intent, viable alternatives including no change, option recommendation and disqualifiers, planned effects and prohibited effects, operational ownership, cost and failure modes, evidence/observer feasibility and remaining decision gaps. Distinguish source claim, current source inspection, actual runtime observation, hypothesis, estimate and owner decision. Give only the task-relevant portion, not a mandatory report for every small edit.

**Decision sequence.** (1) Understand the actual system and consequence; (2) compare simplest suitable choices; (3) qualify material external facts and rights at point of use; (4) translate selected approach into bounded actions or an independent Builder payload only when authorized; (5) identify actual evidence needed for source, artifact, service, recovery and user outcome; (6) stop or disclose material unknowns without simulating a pass. Existing successful mechanisms and no new service are always candidates when suitable.

**Deployment spectrum.** Consider local/offline program → static hosting → managed application platform → VM/container → orchestration, selected on actual workload, reliability, persistence, traffic, compliance, team capability, maintenance cost and exit path. Escalation is justified by requirements, not an assumed maturity ladder.

## 4. Functional requirements — DevOps & Reliability (DO-F)

All requirements below are proposed MUST-level target behaviors when material and applicable, not a checklist for every request.

| ID | Proposed requirement and observable intent |
|---|---|
| DO-F01 | Activate only for material operational, reliability, delivery, runtime or repository lifecycle decisions after canonical AIPF routing; skip unrelated and trivial tasks. |
| DO-F02 | Ground advice in accessible approved requirements, released/working baseline, real target and operational responsibility; separate verified facts, assumptions, estimates and unknowns. |
| DO-F03 | Compare no change/existing services, local/offline, static, managed, VM/container and orchestration choices; recommend the simplest fit and explain disqualifiers and exit costs. |
| DO-F04 | Analyze source control, branch/review protections, tag/commit identity, Git worktree and repository service ownership; verify actual settings rather than inferring from files. |
| DO-F05 | Design and assess reproducible CI/build execution: dependencies, lockfiles, tested task graph, permission scope, caching, runner isolation, statuses, failures, artifact identity and retained evidence. |
| DO-F06 | Plan controlled promotion and release: accepted source, artifact/digest, exact environment, effects, verification, user-facing health, rollback/forward repair and durable reconciliation; no automatic publication. |
| DO-F07 | Qualify actual runtime/platform behavior: process lifecycle, storage, networking, limits, startup/readiness, scaling, downtime, resources and support burden. |
| DO-F08 | Explain IaC state ownership, locking, plan/apply distinction, drift, secrets, provider inputs and recovery; no unapproved apply/destroy or plan-as-permission assumption. |
| DO-F09 | Assess configuration automation and repeated execution, idempotency conditions, inventories, privilege, check/dry-run limitations and partial failures; require actual effect verification. |
| DO-F10 | Diagnose network, DNS, TLS, routing, proxy and transport issues with layer-specific hypotheses and target-scoped passive/minimally intrusive observations; no default scanning. |
| DO-F11 | Select useful metrics, logs, traces and alert rules; account for missing data, latency, sampling, queue/drop behavior, sensitive fields, storage and cost; avoid telemetry-by-default. |
| DO-F12 | Define user-impact SLIs/SLOs and alerting only when the owner/workload warrants them; distinguish short anomalies, sustained incidents and fabricated availability guarantees. |
| DO-F13 | Support incident triage, stabilization, communications, causal investigation, recovery and learning with current evidence and role/permission boundaries; no autonomous production actions. |
| DO-F14 | Evaluate backup, snapshot, retention and recovery independently; require restore/path/data-integrity/service usability evidence appropriate to owner-selected RPO/RTO. |
| DO-F15 | Identify migration, data lifecycle, persistence consistency, storage change, interrupted operation and partial-write consequences; coordinate with Architecture/Security/QA. |
| DO-F16 | Operationalize source/dependency/secret/build/artifact/infrastructure security controls conditionally; use findings rather than a single scanner score; preserve Security ownership. |
| DO-F17 | Compare estimates versus real spend, alerts versus enforced caps, typical versus peak demand, quotas, billable dimensions, teardown and ongoing maintenance; qualify current provider facts. |
| DO-F18 | Provide optional AI operations guidance: trace/model/prompt/skill/deploy correlation, costs, latency, data drift, privacy, evaluation versus telemetry and retention; avoid mandatory monitoring platforms. |
| DO-F19 | Tie material recommendations and outcomes to exact source/runtime/CI/artifact/environment identity, observer and limits; no successful status claim from a workflow name or dashboard alone. |
| DO-F20 | Explicitly classify commands, workflow automation and service actions by read/plan/write/destructive/externally published effect and required authority; preserve blast radius, stops and recovery. |
| DO-F21 | Produce accurate runbooks, setup, incident, environment, backup and release guidance through shared Repository Quality knowledge; distinguish example commands from verified results. |
| DO-F22 | Diagnose via falsifiable hypotheses and discriminating observations; reconcile stale or conflicting state, do not shotgun changes and verify recovered user behavior. |
| DO-F23 | Qualify optional Actions, scanners, monitoring, hosting and IaC candidates for version, maintenance, license, permissions, data flow, cost, operational complexity and failure behavior. |
| DO-F24 | Support direct agents without self-handoff and distinct Builders through complete AIPF T1 operational payloads, accessible implementation inputs and clearly attributed returns. |
| DO-F25 | Compose with Architecture, Security, QA, UI/UX and shared repository-quality guidance as needed; avoid duplicate authority, competing recommendations and repeated reviews. |
| DO-F26 | Extend the existing specialist registry, entry guidance, local file-based knowledge and affected tests additively; preserve framework bytes, four entries, catalogs, compatibility and recovery. |

## 5. Knowledge architecture and research curation (DO-K)

### 5.1 Knowledge requirements

| ID | Proposed requirement |
|---|---|
| DO-K01 | Original progressively loaded guides and question-led offline index cover all twelve knowledge families; no arbitrary guide/card count or new runtime. |
| DO-K02 | Conditional decision records identify context, applicability/exclusions, alternatives including no change, tradeoffs, failure/cost/privacy impacts, observables and source limits. |
| DO-K03 | Keep stable operational methods separate from volatile provider plans, regions, limits, versions, terms, prices, permissions and implementation details; reverify material facts at use. |
| DO-K04 | Preserve author, source URL, exact pin or dated edition, inspected file/section, supported claim, license, attribution, caveat and reuse/redistribution decision. |
| DO-K05 | Original synthesis only. Do not wholesale vendor third-party skills, workflows, README templates, code, images, licenses, policies or diagrams; unresolved rights mean reference-only. |
| DO-K06 | Include both positive and negative examples, false confidence cases, unavailable tool/observer and reasoning about unsuitable options. Illustrations are clearly unexecuted. |
| DO-K07 | Include source-linked patterns for safety-sensitive operational transitions: target, plan, consequence, observed state, rollback/forward repair and permission boundary. |
| DO-K08 | Reuse shared capability index and existing OpenTelemetry/EvalView or similar records rather than duplicate; discoveries are not installed or authorized integrations. |
| DO-K09 | If exact material current facts, implementation evidence, API access or required observer is unavailable, explicitly identify the gap and either choose sufficient bounded alternative or stop affected work. |
| DO-K10 | Retain research source IDs and prior deferred leads with historical scope; future technology review is triggered by actual requirements, not a perpetual repository survey. |

### 5.2 Twelve decision families

| Family / suggested guide | Decision questions and critical negative case |
|---|---|
| 01 · Git and repository lifecycle (`source-repository.md`) | What is authoritative source and release identity? Are protections/permissions actually configured? A GitHub badge, license file or branch name does not establish enforcement. |
| 02 · Builds and CI (`build-ci.md`) | What task actually ran with which dependencies/runner and what artifact was produced? A test report stage is not proof tests executed. |
| 03 · Delivery and releases (`delivery-release.md`) | Where is the exact target, durable deployment, health and accepted artifact? Successful sync/build is not evidence of user success or permission to publish. |
| 04 · Infrastructure as code/config (`infrastructure-config.md`) | Who owns plan/state/locks, credentials and restore? A dry run may be incomplete; saved plans and stdout can expose secrets. |
| 05 · Runtime/platform selection (`runtime-platform.md`) | What is the simplest model that meets workload, data, reliability and operations? Do not impose Kubernetes for a small static or local application. |
| 06 · Networking/DNS/TLS (`networking-dns-tls.md`) | Is failure resolution, connect, TLS, routing or application? Avoid unauthorized probing or changing zones before discriminating observation. |
| 07 · Observability (`observability.md`) | Which meaningful signal is collected, where does it travel, how can it be lost, and can it be queried? Collector retries do not guarantee delivery. |
| 08 · Reliability/incidents (`reliability-incidents.md`) | Which user outcome and service level matter, what constitutes incident and recovery, who can act? Do not promise SLA from monitoring configuration. |
| 09 · Data/backup/disaster recovery (`data-recovery.md`) | What data is recoverable, how recent, and was restore observed in a safe target? Backup process success does not prove recoverability. |
| 10 · DevSecOps/operational trust (`devsecops.md`) | What threat/control is relevant, how is evidence scoped, are credentials/runner/artifact protected? Scanner score cannot approve release. |
| 11 · Cost and resources (`cost-resource.md`) | What is estimated vs billed, alerts vs hard caps, cleanup cost, AI usage and exit burden? A free tier does not mean enforceable zero spend. |
| 12 · Operational docs/repository quality (`operational-documentation.md`) | Can a real user follow accurate instructions, understand status and reproduce stated behavior? Links and badges can be valid yet misleading. |

## 6. Shared Documentation & Repository Quality — scope and requirements

**Intended product.** An original adaptive knowledge layer which helps generate, improve and verify a repository’s presentation, onboarding, documentation information architecture, maintainability signals and release truth. It is jointly applicable across specialists, not a mandatory documentation redesign or a new approval process. Existing AIPF Chapter 13 continues to govern documentation changes, including semantic qualifiers and source-label/target parity.

### 6.1 Repository profiles

| Profile | First-screen priority | Add only if applicable |
|---|---|---|
| End-user desktop/mobile/web product | Plain purpose, current support, real visual, first use or install. | Privacy, accessibility, troubleshooting, update/recovery instructions. |
| CLI, library or SDK | Exact supported installation, short runnable example, expected result. | API contracts, compatibility matrix, migration and examples. |
| API or hosted service | Purpose, trust/auth boundary, safe local request and output. | Schema, data lifecycle, operations, integration, monitoring. |
| IaC/DevOps project | Target/preconditions, safe plan path, authority and possible cost. | Approved apply/teardown, state, rollback, recovery and secrets practices. |
| AI agent, skill or framework | What it does/does not do, activation, roles, provider/host limits. | Tool permissions, evidence limits, evaluations, data practices. |
| Research/internal project | Question, status, reproduction and limitations. | Inputs/data provenance, results, attribution and confidential handling. |

### 6.2 Functional requirements (RQ-F)

| ID | Proposed requirement |
|---|---|
| RQ-F01 | Select an audience/project profile based on actual repository purpose, current status and constraints; avoid universal README templates or mandatory sections. |
| RQ-F02 | Provide a concise, distinctive first-screen statement of purpose, audience, supported state and first useful action; real branding, no generic filler. |
| RQ-F03 | Offer modular original README section patterns for overview, installation, usage, demos, architecture, support, contribution, security, license and releases only when relevant. |
| RQ-F04 | Keep documented commands, versions, environment variables, prerequisites, expected outcomes and compatibility tied to real sources; do not silently assume installation/production authority. |
| RQ-F05 | Provide professional, accessible presentation: hierarchy, navigation, authentic visual examples/diagrams, alt text, mobile/dark-light readability and proportionate badges. |
| RQ-F06 | Require actual source or permitted runtime support for material marketing, capability, support, security and performance claims; decorative badges are not certifications. |
| RQ-F07 | Validate relative links, anchor fragments, reference definitions, destination identity and meaning; external checkers are optional and failure/reporting semantics must be qualified. |
| RQ-F08 | Inspect actual rendered Markdown in applicable viewing environments when visual acceptance is material; static source review cannot establish rendered appearance. |
| RQ-F09 | Adapt contribution, code of conduct, support, issue/PR forms, change history, vulnerability reporting, licensing and repository metadata to actual team/community needs. |
| RQ-F10 | Address CI, dependencies, releases, branch/settings and supply-chain quality by qualified findings; do not invent settings or equate aggregate scores with compliance. |
| RQ-F11 | Provide consistent version/status/installation/release/documentation identity; preserve historical release records and distinguish published tag from test/source artifact. |
| RQ-F12 | Preserve asset-level rights, attribution, trademarks and user permissions for copied images, videos, logos, icons and screenshots; example/reference catalog licenses do not automatically clear embedded assets. |
| RQ-F13 | Support safe, proportionate review and correction without broad makeover of stable repositories; document actual exclusions, unknowns and needed owner visual review. |
| RQ-F14 | Remain shared guidance, accessible from the relevant existing specialist/entry via file links or index, not a sixth registered service or mandatory runtime dependency. |

### 6.3 Knowledge requirements (RQ-K)

| ID | Proposed requirement |
|---|---|
| RQ-K01 | Original concise question-led documentation/repository index with reusable profiles and decision cards; preserve AIPF Chapter 13 primacy. |
| RQ-K02 | Profile-specific examples of strong and faulty READMEs, expected first-success workflow and suitability of sections; no fixed boilerplate requirement. |
| RQ-K03 | Source and asset register distinguishes metadata, permitted code/template adaptation, reference-only examples, media rights and required notices. |
| RQ-K04 | Verification guidance separates deterministic local validation, optional external checks, actual clean-install, rendered observation and owner judgment. |
| RQ-K05 | Any starter snippet, issue/PR template or README skeleton is original, placeholder-free when shipped and tested against an appropriate profile, not copied wholesale. |
| RQ-K06 | Material owner feedback and approved style/brand rules are scoped to the relevant product/repository; do not globalize house-style bans. |

## 7. Nonfunctional requirements (DO-N)

| ID | Required quality and restraint |
|---|---|
| DO-N01 | Provider, model, repository host and operating-platform neutral; no required Vercel, GitHub, AWS, Docker, Kubernetes, SaaS or local service. |
| DO-N02 | Preserve exact released framework and four specialist contracts, knowledge/catalog behavior and accepted integration compatibility. |
| DO-N03 | Task-relevant progressive guidance with minimal avoidable reading, tool calls, approvals and model/provider cost. |
| DO-N04 | Evidence and identity truthfulness: version, target, source, configuration, observer, result and limitation are not interchangeable. |
| DO-N05 | Security and privacy by default: secrets, operational traces, source code, customer data and debug exporters do not leave trust boundaries without permission. |
| DO-N06 | Tool rights and redistribution: original synthesis, source-specific license/NOTICE, no unqualified third-party asset reuse. |
| DO-N07 | Safe dependency and integration posture: no new mandatory executable, daemon, network service, deployment or paid account unless independently justified/approved. |
| DO-N08 | Portability: distinct Builder works with supplied accessible inputs and T1 without hidden governing sources; direct model needs no artificial handoff. |
| DO-N09 | Operational usefulness: recommendations consider operator capacity, recovery burden, maintainability, cost and existing service capabilities. |
| DO-N10 | Proportional evidence: appropriate real environment, rendered, runtime, independent or human observation where required; never one universal scanner score. |
| DO-N11 | Failure safety: controlled scope, target identification, idempotency, partial failure, inability to observe, rollback/forward repair and cleanup are explicit as material. |
| DO-N12 | Clear, accessible documentation and truthful status across README, code, CI, release, tags and support instructions. |

## 8. Proposed registry, integration and knowledge delivery

**Existing schema.** Use `skills/specialists.json` schema_version 1 unless B1 proves a compatible change is required. Proposed `id`: `aipf-devops-reliability`, version `0.1`, path `skills/devops-reliability/SKILL.md`; proposed tasks: `devops-plan → plan`, `devops-diagnose → diagnose`, `devops-review → review`. `chapters_any` may use `[11,12,13,14,15,16,17,18,19,20,21]`; chapter eligibility alone does not activate it. B1 must check real helper parser and avoid unconditional Chapter 14/13 overactivation.

**Knowledge sources:** `skills/devops-reliability/INDEX.md`, progressive guides/cards, and the existing `knowledge/capabilities/INDEX.md`. Shared Repository Quality could live under `knowledge/repository-quality/` and be referenced by DevOps and other relevant entries without altering their activation semantics. Exact paths are candidate design choices, not approved repo structure. Initial `tools: []`; no required retrieval script, MCP, API, vector store, shell or network calls.

**Fallback.** Missing guide, monitoring data, cloud API, GitHub setting, license record, qualified tool or observer must be disclosed. Continue with suitable verified local/approved evidence where sufficient, otherwise surface the precise material decision or observation gap. Tool discovery is not installation and available credentials are not authorization.

**Compatibility.** The current four registry entries, helper error/skip/consult behavior, source catalogs, version labels, PRD source history, existing optional browser tools, CI and regression should be preserved. Any later change to helper dispatch must receive targeted and full standing verification. No independent router or mandatory multi-agent architecture.

**Documentation capability consumption.** Consult shared guidance when generating or correcting README, operating guides, release notes and repository metadata, independent of whether the DevOps specialist is activated. UI/UX covers appearance, QA covers actual testing, Security covers safety and data rights, Architecture covers technical accuracy, and DevOps covers operation/delivery consequences. One coherent result and one AIPF authority boundary remain.

## 9. Candidate technologies and source interpretation

The following are research leads with specific transferable lessons. None is an approved Praxis dependency or a commitment to deploy a stack. Exact pins, license/NOTICE and data terms remain in the retained source register and must be reconciled before reuse. Do not copy README/media/example assets from third-party projects without file-level clearance.

| Candidate(s) | Transferable contribution | Qualification or misuse warning |
|---|---|---|
| OpenSSF Scorecard, OSPS Baseline | Per-finding repo/supply-chain security assessment and structured evidence. | Heuristics may be inapplicable/false; experimental conformance and public API/MCP are not unreleased-candidate scans or certification. |
| Awesome Actions | Discover GitHub automation categories and existing implementations. | List entries may be archived/old; independently inspect maintenance, action inputs, permission scope and exact revision. |
| Scorecard Action, GH Release, Upload Artifact | Optional recurring checks, controlled releases and evidence retention. | Mutable pins, overwrite defaults, unmatched assets, immutability/digest semantics and retention need explicit configuration and verification. |
| Actionlint, Lychee | Static workflow grammar/expressions and documentation link verification. | Neither proves runtime semantics, real setup, visual quality or target/source claim parity; network checks and runner version qualified. |
| OpenTofu, Ansible | Infrastructure state/plan/lock and idempotent configuration strategies. | State plans and diff outputs can contain secrets; check mode incomplete; no automatic apply or permission from plan. |
| Argo CD, Forgejo | Declarative sync, runner isolation, self-hosted Git and recovery considerations. | Hooks repeat; prune risky; runner host access; full forge backup consistency. Avoid unnecessary adoption. |
| Restic | Backup integrity, snapshots, retention and controlled restore. | Recoverability requires actual restore; retention/prune and password loss can impair recovery. |
| Prometheus, OpenTelemetry Collector | SLO alert states, metrics and pipeline/drop/queue/redaction boundaries. | Missing samples, retention headroom and failed export; no default external telemetry or claim of guaranteed delivery. |
| Langfuse, MLflow, Opik | AI/ML traces, model/prompt versions, experiments and evaluations. | Overlapping alternatives; multi-service ops, enabled telemetry, broad dev listeners, credentials, retention, data egress/cost. |
| Deepchecks, EvalView, Chaos Frontend Toolkit | Data drift literacy, agent trace contracts and controlled failure ideas. | Drift not quality failure; prior runtime not qualified; use deterministic safe fixtures not global production patches. |
| Infracost / Infracost CLI | Infrastructure estimate and billable parameter modeling. | Estimated != incurred, budget alert != hard cap; local CLI parameters vs Plan JSON API upload are different data flows. |
| Awesome README, Best-README-Template, selected examples | README information architecture, first use, visuals, contribution paths. | Curated list/Unlicense does not transfer image/brand rights; avoid placeholder commands, hard-coded badges and generic copying. |
| Official GitHub docs, Google SRE, OpenTelemetry guidance | Community/files/README and reliability/telemetry engineering practices. | Current platform settings and provider facts are verified when decisions depend on them; docs alone do not prove configured behavior. |

## 10. Acceptance criteria — DevOps (DO-AC)

Each criterion requires a named observer and actual executed or inspected evidence when implementation is authorized. A successful representative exercise proves only the observed case. No fixed count of tests, source entries or score threshold substitutes for these outcomes.

| ID | Future observable acceptance |
|---|---|
| DO-AC01 | Material operational task consults DevOps; minor unrelated task does not; routing/helper behaviors remain compatible. |
| DO-AC02 | A local/static/small managed scenario selects a justifiably minimal option, rejects unsupported complexity and records actual assumptions/costs. |
| DO-AC03 | CI exercise distinguishes workflow/report presence from a test actually executed; identifies permissions, inputs and artifact identity. |
| DO-AC04 | Release scenario binds accepted commit and artifact to environment and user outcome, stops unauthorized publication, distinguishes successful build from live service. |
| DO-AC05 | IaC dry-run/plan scenario protects state/secrets, recognizes stale/partial plans and does not equate plan with apply authority. |
| DO-AC06 | Configuration automation and repeated-run scenario handles incomplete check mode, idempotency conditions and partial failure. |
| DO-AC07 | Network/DNS/TLS diagnosis isolates plausible layer using authorized observations, avoids invasive actions and preserves competing hypotheses. |
| DO-AC08 | Observability scenario handles true zero versus absent data, metric cardinality/PII, queue loss, firing/pending alerts and access boundaries. |
| DO-AC09 | Incident scenario identifies observed user impact, safe stabilization, responsibility, recovery observer and unresolved risk; no invented availability/SLA. |
| DO-AC10 | Backup/recovery scenario demonstrates why successful backup/check is insufficient and specifies safe isolated restoration with actual file/app checks. |
| DO-AC11 | DevSecOps scenario uses itemized, context-sensitive findings; does not promote aggregate Scorecard or scan success into release approval. |
| DO-AC12 | Cost scenario distinguishes free allowance, total/peak units, forecast/actual, alerts/hard caps, deletion and data transmission. |
| DO-AC13 | AI operations scenario correlates version/trace/evaluation with correct data boundaries and chooses no new integration where sufficient. |
| DO-AC14 | Failure diagnosis exercise uses a falsifiable observation and verifies user-relevant effect after correction without speculative infrastructure mutation. |
| DO-AC15 | Optional source/tool record captures pin, supported claim, data/permission/cost, maintenance/rights and unresolved limitations; no unqualified import. |
| DO-AC16 | Direct and distinct Builder scenarios preserve approved intent, full executable instructions, AIPF authority and stop without hidden specialist access. |
| DO-AC17 | Multi-specialist plan preserves separate security, QA, architecture, UI and operational responsibilities without duplicate governance. |
| DO-AC18 | Full affected and standing cross-platform regression, fallback, version/registry, source rights, framework integrity and recovery gates pass for exact candidate; independent observation when material, owner B4 decision and separate B5 authorization. |

## 11. Acceptance criteria — Repository Quality (RQ-AC)

| ID | Future observable acceptance |
|---|---|
| RQ-AC01 | Two substantially different repository profiles (e.g. CLI/library and deployable/AI project) receive appropriately different READMEs; no forced sections or empty placeholders. |
| RQ-AC02 | A fresh reader can identify purpose, scope/status and first useful action from the rendered entry page; brand and content are relevant, not decorative. |
| RQ-AC03 | Safe documented first-use commands reproduce the stated outcome in a suitable clean environment where feasible; otherwise clear non-execution disclosure. |
| RQ-AC04 | Source labels, badge targets, version claims, release history, internal relative paths, fragments and external destination identity are reconciled; no false-claim propagation. |
| RQ-AC05 | A capable reviewer inspects actual Markdown rendering and applicable viewport/theme/accessibility issues; no claim of rendered acceptance from source alone. |
| RQ-AC06 | Repository/community/security files and settings are evaluated against real project profile; absent enforcement is not invented and sensitive/private reporting routes are accurate. |
| RQ-AC07 | Sample illustrations, icons/screenshots, README patterns and snippets respect file-level rights and attribution; unknown rights stay reference-only. |
| RQ-AC08 | Shared guidance is accessible to relevant specialties without a new registered agent, mandatory tool or regression of existing behavior. |
| RQ-AC09 | Documentation-only CI trigger/verification issue is recognized where material and assessed for a future authorized correction, not silently changed during planning. |
| RQ-AC10 | Small docs edit is handled proportionately; protected meaning, original history and existing design are preserved rather than replaced by an unsolicited makeover. |

## 12. Representative qualification exercises and evidence design

| Scenario | Concrete challenge and minimum evidence |
|---|---|
| DQ01 · Local tool | Select local or no-host approach for small offline utility; state reasons not to provision cloud. |
| DQ02 · Managed web app | Compare static vs managed process with real state, background work, low/high traffic, region and cost constraints. |
| DQ03 · CI false green | A job claims testing but command skips tests; identify gap from actual workflow and raw output. |
| DQ04 · Release identity | Tested SHA, tag, published release and documentation-only delta differ; reconcile without rewriting historical evidence. |
| DQ05 · Plan state leak | Sensitive value in saved IaC plan and interrupted lock; stop unsafe artifact sharing/force-unlock. |
| DQ06 · Repeated automation | Dry-run omits arbitrary command, restart fails after configuration change; report actual partial outcome. |
| DQ07 · DNS/TLS incident | Distinguish authoritative DNS error, resolver cache, network reachability, TLS handshake and application timeout without unauthorized scan. |
| DQ08 · Telemetry loss | Collector queue saturation and missing samples with otherwise healthy metric; do not report zero failures. |
| DQ09 · Alert routing | Short spike vs sustained user error; separate pending/firing/notification path. |
| DQ10 · Disaster recovery | Backup exists and checksum passes but needed database/config data absent; isolated restore and user test expose failure. |
| DQ11 · Security score | Scorecard shows good aggregate but relevant permission/release provenance gap remains; itemized assessment. |
| DQ12 · AI operations | Choose among existing logs, OTel, Langfuse/MLflow/Opik; data masking, retention and true cost qualified; no three-tool default. |
| DQ13 · Cost | Estimate vs actual, hard budget limit, peak usage, side effects after teardown, privacy differences between APIs. |
| DQ14 · Independent Builder | Fresh Builder with only approved payload performs bounded synthetic change; separate reviewer challenges failure/unauthorized action and records exact evidence. |
| RQ01 · CLI README | Concise real installation and first success, verified links, no generic hero template. |
| RQ02 · Deployed/AI README | Correct architecture/authority/provider limits, relevant visual and privacy/operation docs. |
| RQ03 · Claim parity | Material project index, README, badge and release metadata disagree; verify right source, not just that URL resolves. |
| RQ04 · Render and accessibility | Actual rendered view in representative wide/narrow, light/dark when material, alt text and navigation. |
| RQ05 · License and community | Source list has CC0 but linked asset is separately licensed; do not import; include appropriate governance/contact docs. |
| RQ06 · Proportional docs correction | One safe typo and one material operational instruction; different evidence and approval needs. |

**Evidence layers.** Source inspection establishes what a file or documented implementation says. A static/tool check establishes its own bounded result. Actual runtime/CI/artifact/restore observations establish only the tested target and configuration. Independent human/agent review establishes only the judgment and evidence accessed by that observer. Owner acceptance and release authorization remain separate. Record source revision, environment, fixture, observer, command/raw status, exact observed effect and known blind spots. No new mandatory evaluation platform, comparative superiority test or artificial cardinality gate.

**Negative controls.** Deliberately include at least one known-bad candidate whose success report is misleading (e.g., green job without test, incomplete restore, invalid link target, telemetry dropped) and at least one suitable valid alternate design. Ensure the oracle detects intended defect, not a harness syntax or import failure; preserve any original failure and corrected evidence. Simulations must be labeled unexecuted unless actually run.

## 13. Requirement-to-acceptance traceability

| Requirement family | Acceptance anchors | Notes |
|---|---|---|
| DO-F01–03, DO-K01–03, DO-N03/09 | DO-AC01–02, DQ01–02 | Materiality, alternatives and minimal operational model. |
| DO-F04–06, DO-F19–20 | DO-AC03–04, DO-AC18, DQ03–04 | Source/release/artifact integrity and permission. |
| DO-F07–10 | DO-AC02, DO-AC05–07, DQ02, DQ05–07 | Environment, configuration and networking. |
| DO-F11–15 | DO-AC08–10, DQ08–10 | Telemetry, incidents, data and restore. |
| DO-F16–18, DO-F23 | DO-AC11–13/15, DQ11–13 | Security, operational costs, AI and optional tools. |
| DO-F21–22, DO-K06–09 | DO-AC14–15, DQ07–10, RQ-AC03/10 | Useful runbooks, diagnosis, source evidence and fallback. |
| DO-F24–26, DO-N01–02/07–11 | DO-AC16–18, DQ14 | Portable roles, composition and compatibility. |
| DO-K04–05/10, DO-N04–06 | DO-AC15/18, RQ-AC07 | Rights, research identity and bounded claims. |
| RQ-F01–05, RQ-K01–02/05–06 | RQ-AC01–03/05/10, RQ01–02/04/06 | Profile-first quality and rendered presentation. |
| RQ-F06–08/11 | RQ-AC03–05/09, RQ03–04 | Verified links, semantics, onboarding and release parity. |
| RQ-F09–10/12–14, RQ-K03–04 | RQ-AC06–10, RQ05–06 | Repository health, licensing, proportionate shared guidance. |
| DO-N05/12 | DO-AC08/18, RQ-AC02/05/07 | Privacy, clear content and accessibility. |

## 14. Delivery plan, risks and owner decisions

### 14.1 Proposed B1–B5 delivery gates (not authorized by this PRD)

| Stage | Proposed work and observable exit |
|---|---|
| B1 · Baseline and approval | Product owner reviews scope, IDs, conflict resolutions, source/rights and acceptance; confirm exact v1.3.0 recovery anchor, canonical PRD v1.4, registry/helper/schema, evidence feasibility, paths and authority for development. Reconcile research commit and available rights. No implementation before authorization. |
| B2 · Original knowledge | Create twelve-family progressive guides, conditional cards and separate shared repository-quality guidance/profiles. Source and license sampling, positive/negative examples, offline navigation, no wholesale copy. No fixed count required. |
| B3 · Additive integration | Register one advisory specialist; update entry, shared knowledge links and docs, preserve all four existing entries/tools/AIPF bytes; focused activation, fallback, docs semantics and link tests. No new execution runtime. |
| B4 · Qualification | Apply representative direct, distinct Builder, negative-control and cross-specialist exercises, source-rights and clean-environment/renders, affected tests and full Linux + native Windows standing regression, independent challenge where required; exact report/evidence, owner acceptance decision. |
| B5 · Delivery and release | Only after separate owner authority: reconcile approved requirements into canonical PRD, prepare limited release docs and source/version identity, validate exact merge/main, tag and published release, preserve recovery and risk ledger; no automatic infrastructure provisioning. |

### 14.2 Principal risks and mitigations

| Risk | Proposed treatment |
|---|---|
| DevOps becomes another governing framework | Domain intelligence only; preserve AIPF authority, existing status vocabulary, acceptance and release gates. |
| Stack bloat and cloud overengineering | Compare existing/no new option first; require actual workload/recovery and operating-cost rationale. |
| Tool catalog mistaken for qualification | Source pins/claims and runtime results separate; repeat verification on decision-sensitive versions, data flows and permissions. |
| False green CI, scanning or recovery claims | Item-level oracles, actual target/artifact/restore and user outcome, counterexamples and attributable observations. |
| Telemetry/privacy/cost creep | Minimal signals, pre-export redaction, bounded retention, explicit cost and target permission, fallback to existing tools. |
| Unsafe CI/workflow automation | Explicit allowed triggers, write permissions, secrets, release overwrite semantics and destructive side effects. |
| Unqualified images/third-party content | Original documentation examples, file-level rights and attribution; unresolved media reference-only. |
| README perfectionism harms maintenance | Audience-first, smallest meaningful correction, preserve accurate content and stable presentation. |
| Repository baseline drift during development | Recheck source tree, tag, registry, CI and canonical PRD before mutation and before release, delta-only evidence transfer. |

### 14.3 Owner decisions requested by this proposal

1. Approve or revise the two-deliverable scope and stable ID families (DO-F/K/N/AC, RQ-F/K/AC) as a temporary specialist PRD.
2. Approve whether DevOps consultation modes are `plan`, `diagnose`, `review` and whether shared Repository Quality should be a referenced knowledge location rather than a registered specialist.
3. Confirm no new mandatory runtime, cloud, paid service or third-party direct asset bundling for v0.1, and that changes to live repository policies/workflows remain separately authorized.
4. Set the B1–B4 development authority, permitted repository targets/branches, qualification observers and any approval boundaries in a separate action-scoped instruction if the PRD is accepted. B5 remains separate.

**Proposal stop boundary.** This working draft concludes at owner review. No repository files were modified, no scans/tools installed, no external services connected, no infrastructure operated, no CI rerun and no Praxis release proposed as already delivered. Actual implementation results, acceptance, canonical PRD consolidation and publication belong to subsequent, separately authorized work.

## 15. Sources, provenance and verification limits

**Verified project sources (read-only on November 27, 2026):**

- Praxis v1.3.0 published release: https://github.com/S-Pillow/praxis/releases/tag/v1.3.0
- Immutable release tag: https://github.com/S-Pillow/praxis/tree/1749f9d3632efd1ab272a69e0738fdd6bd754932
- Canonical product PRD v1.4 at release: https://github.com/S-Pillow/praxis/blob/v1.3.0/docs/PRD.md
- Released QA qualification record: https://github.com/S-Pillow/praxis/blob/v1.3.0/docs/releases/1.3.0.md
- Existing specialist registry: https://github.com/S-Pillow/praxis/blob/v1.3.0/skills/specialists.json
- Final DevOps research commit: https://github.com/S-Pillow/praxis/commit/61c59f908303fb27883d3cff688c304dda620cc6
- DevOps operational depth: https://github.com/S-Pillow/praxis/blob/61c59f908303fb27883d3cff688c304dda620cc6/research/devops-reliability/DEVOPS-OPERATIONAL-DEPTH-DISCOVERY-03.md
- Repository quality discovery: https://github.com/S-Pillow/praxis/blob/61c59f908303fb27883d3cff688c304dda620cc6/research/devops-reliability/REPOSITORY-QUALITY-DISCOVERY-01.md
- DevOps primary discovery: https://github.com/S-Pillow/praxis/blob/61c59f908303fb27883d3cff688c304dda620cc6/research/devops-reliability/DEVOPS-RELIABILITY-DISCOVERY-01.md
- DevOps source register (pinned metadata/rights): https://github.com/S-Pillow/praxis/blob/61c59f908303fb27883d3cff688c304dda620cc6/research/devops-reliability/DEVOPS-SOURCE-REGISTER-01.md

**Supporting supplied references:** the pasted prior conversation containing the final extensive research summary; the supplied QA & Engineering Quality PRD v1.0 APPROVED and earlier Praxis PRD v1.2; and AIPF v8.10.1 packaged canonical guidance. Superseded PRDs are historical baselines, not current product status.

**Limits.** The external-repository behavior described here is inherited from identified pinned-source research. This draft did not independently execute OpenTofu, Argo CD, Ansible, Restic, Prometheus, OpenTelemetry Collector, Scorecard or other candidates, and did not confirm live hosted price/plan/license changes. Source findings are not native runtime qualification, production safety, guaranteed coverage or legal clearance of every asset. Exact decisions requiring volatile facts must recheck official current sources and authorized environments. The only newly confirmed live project facts are the publicly published Praxis release/tag, repository files, existing registry and retained research commit read above.
