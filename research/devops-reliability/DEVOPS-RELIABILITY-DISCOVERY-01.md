# DevOps & Reliability — discovery 01

Date: 2026-11-27. Baseline: released Praxis v1.3.0, commit `1749f9d3632efd1ab272a69e0738fdd6bd754932`, tree `f180c8fe93222b07674fc8a05158c2cd40cf84a4`, canonical PRD v1.4 blob `30c9792dc55349fbc276df225dd0128919c1726c`, AIPF v8.10.1 unchanged. Owner requested deep research on five supplied repositories and inclusion of professional README/GitHub quality in future development. Research only; no implementation, release, provisioning or new PRD approval. Decision-changing purpose: define the scope and useful sources for the fifth specialist and prevent documentation quality being limited to one discipline. See [source register](DEVOPS-SOURCE-REGISTER-01.md), [repository-quality proposal](REPOSITORY-QUALITY-DISCOVERY-01.md), [existing cross-specialist leads](../CROSS-SPECIALIST-RESEARCH-REGISTER.md).

## 1. Evidence synthesis

### DO-S01 — practical projects, not a production baseline

Inventory: 41 numbered directories, 1,955 blobs. Root README calls out AWS/Azure/GCP, Terraform, Jenkins, containers, CI, GitOps, cost, backup, migration, observability. Actual sampled titles differ materially: 24 is .NET DevSecOps not standalone monitoring; 26 GitLab/Terraform not cost optimization; 27 EKS/Argo CD not disaster recovery; 28 AI chatbot EKS not generic multienvironment; 32 Java server delivery not blue-green; 33 three-tier Kubernetes pipeline not migration; 34 local multitiers not compliance; 36 React/Flask/Postgres EKS not generic GitOps; 40 MERN DevSecOps/GitOps not cloud migration. This makes semantic source-to-index reconciliation a real repository-quality case, not a hypothetical lesson.

Project 01 infrastructure guide: modular boundaries, public/private subnet separation, load balancer, autoscaling, private RDS, outputs and plan/apply. Transfer decision method: identify state ownership, target/account, network and data boundaries, plan-review and exact authorized apply. Avoid copying topology for small projects. Project 06 Jenkinsfile: explicit quality gate and artifact metadata, but build command skips Maven tests and later report goal alone does not establish actual test execution. Inspect task graph, inputs, exit codes and artifact identity; do not infer gate from stage names. Project 07 lab 6 explicitly reports InSpec Azure trouble and temporary local workaround; lab 7 outlines availability/log/metric observation. Preserve limitations, check current compatibility, distinguish local test from CI. Project 26 pipeline uses auto-approve apply/destroy: unsafe as default autonomous workflow; destructive scope and effects require explicit authorization. Project 27 GitOps, Project 36 migration job and private database, Project 41 source-to-deploy workflow and scans offer concrete cases. Project 33 names non-free resources and cleanup. Public endpoints/credential examples, remote installation and unreviewed apply are context-dependent, not production-safe defaults. No imported code or images; restrictive rights statement controls reference-only treatment.

### DO-S02 — foundational taxonomy and troubleshooting

Inventory 632 blobs including vendor node_modules. Directory structure covers CI/CD, Git, cloud, container orchestration, infrastructure, OS/network, databases, servers, streaming, observability and package management. Selected Kubernetes concepts distinguish desired state/control loops and stateful workloads; Helm explains upgrade/revision semantics; Prometheus explains metrics/scraping/alerts; network notes contain DNS, routes and socket tools plus active scanning. Transfer: symptom -> layer -> authorized observation -> hypothesis -> correction -> observed recovery. Do not run generic network scans, secret-reading or shell examples without actual authorization. Two selected concept/performance files consist of headings only; markdownlint workflow lacks an event trigger, points at absent root CHANGELOG and uses older action references. Coverage varies; topic links are leads, not verified knowledge. MIT root text inspected; linked content rights independent.

### DO-S03 — lifecycle security map

Manifesto treats security as functional, collaborative, automated when appropriate and self-documented. Catalog sections span pre-commit/threat modeling, secrets, OSS/dependency, supply chain, SAST/DAST/IAST, continuous delivery, containers/Kubernetes/cloud, policy-as-code, chaos, IaC, network and AI. Use categories to choose controls and distinguish scope/ownership. Examples below are unqualified directory leads, not approved integrations.

| Decision | Candidate families | Boundaries |
|---|---|---|
| Secret detection and handling | Gitleaks; Vault or existing provider secret store | Detection is not rotation; avoid logging discovered secrets; no secret retrieval during discovery |
| Dependencies and inventory | Dependabot/Renovate, Syft/cdxgen | Inventory vs vulnerability result vs update; actual license, database freshness, access and transitive graph |
| Build provenance | in-toto/SLSA, Cosign, native attestations | Signature/attestation proves only specified identity/claims; not correctness; validate subject and trust |
| Source/application security | Semgrep, ZAP, existing native checks | SAST/DAST distinct; rules rights, false positives/negatives, test authorization and targets; no live probes |
| Images and infrastructure | Trivy/Grype, Checkov | Scan actual immutable artifact or plan, severity/exceptions, exit behavior and database age |
| Policy and runtime | OPA/Kyverno, Falco | Enforcement vs audit vs detection, admission scope, false denial and operational effects |
| Chaos and cloud | existing local fault seam or provider-native tools | Controlled isolation, blast radius, reversible recovery and actual authority; no production chaos |

Security specialist owns trust, threat and control requirements; QA owns test methods/negative oracles; DevOps owns delivery wiring, runtime configuration, operation and recovery. Architecture owns structural/technology tradeoffs. Avoid duplicate capabilities or approval engines. DO-S12/13 official GitHub search observations corroborate full-SHA workflow pinning and artifact provenance subject binding; exact current platform availability/permissions and terms still require point-of-use verification.

## 2. Proposed knowledge coverage (not approved requirements)

| Family | Material decision and evidence |
|---|---|
| Source control and repository lifecycle | Branch/rules/tag/release identity, reviewed change, fork permissions, repo quality, semantic documentation parity; actual provider controls |
| Build and CI | Reproducible inputs, lockfiles/toolchain, cache identity, runner isolation, least-privilege permissions, tests vs reports, exact artifacts, skipped/failed jobs |
| Delivery and release | Environment promotion, immutable artifact/digest, staging vs live, rolling/canary/blue-green only when justified, health and user journey, rollback/forward recovery |
| Infrastructure and configuration | Desired state, plan/apply, drift, remote state locking/secret exposure, config/version and least-complex implementation; no unapproved mutation |
| Runtime/platform selection | VM/PaaS/serverless/container/orchestrator tradeoffs, lifecycle, workload fit, ops and exit costs; no default Kubernetes/cloud |
| Networking and DNS/TLS | Resolution vs transport vs TLS vs routing vs app, proxy/ingress, timeouts, certificate renewal, target-scoped diagnostics |
| Observability | User-impact metrics, logs/traces and correlation, cardinality, sampling, redaction, retention, alert routing and data/spend budgets |
| Reliability engineering | SLIs/SLOs, error budgets, burn alerts, capacity and dependency failures, degraded behavior, incident roles and postmortems; no invented SLA |
| Data operations and recovery | Backup scope, retention, restore drills, RPO/RTO based on owner needs, migration compatibility and rollback/forward recovery |
| Secure delivery and operational trust | Secret/identity scope, dependency/IaC/image checks, artifact provenance, policy and runtime controls, bounded exceptions and recovery |
| Cost and sustainable operations | Existing/no new service, total and peak usage, quota exhaustion, enforceable cap, cost after teardown, operational toil and migration |
| Operational documentation and repo quality | Verified runbooks, exact commands/targets, safe examples, onboarding, professional presentation and truthful release evidence; use cross-cutting guidance |

Supplementary web discovery DO-S14–16 (Google SRE) addresses the reliability gap in the educational walkthroughs: service objectives based on actual user outcomes, error budgets, actionable alerts, incident handling and learning. DO-S17–18 (OpenTelemetry) supports signal selection, not mandatory instrumentation or collector; avoid high-cardinality user identifiers/raw paths and secret-bearing logs. More precise primary-source qualification needed for actual selected technologies, Terraform state and locks, backup/restore, deployment strategies, cloud quotas and current provider facts. Do not infer advanced reliability from tutorial branding.

## 3. Proposed integration shape

Continue existing registry and progressive question-led skill design. Candidate modes **plan**, **operate/diagnose**, **review** (names not finalized; choose whether diagnosis needs a distinct task ID based on real intent). Include material operational decisions across AIPF paths, not automatic activation for every repo. Direct agent may inspect and act only within scope. Prompt Agent distills applicable operational constraints, commands, targets, negative effects, recovery and observer into canonical T1; separate Builder does not need governance sources. Use shared capability index, original cards, source register; no extra platform, scanner, CI engine, telemetry pipeline or fixed stack. Preserve AIPF governance, prior four specialists, catalog, legacy tests and releases. Actual implementation and mode names await PRD approval.

## 4. Representative qualification proposals (unexecuted)

| ID | Scenario | Evidence intended |
|---|---|---|
| DV-Q01 | Pipeline fixture reports tests without actual execution, and skipped gate | Detect missing observable, corrected local pipeline/fixture fails known defect and passes known good; preserve first failure |
| DV-Q02 | Two local artifacts or revisions and a stale tag/receipt | Exact candidate/subject identity, deny stale promotion, verify recovery anchor |
| DV-Q03 | Disposable deployment simulator with failed readiness and rollback | Actual synthetic state transitions, no unauthorized promotion, restored known-good user behavior; no real cloud |
| DV-Q04 | Declarative plan with drift/destructive change | Identify target, state, allowed delta, reject unapproved apply; safe synthetic plan/reconciliation |
| DV-Q05 | DNS/transport/TLS/app failure diagnostic fixture | Layer-specific evidence; discriminate hypotheses, no live probing |
| DV-Q06 | Synthetic metrics and alerts | User outcome SLI, bounded SLO example, error budget calculation, bad alert counterexample, no external telemetry |
| DV-Q07 | Backup/restore and migration in disposable data | Actual restore integrity, counts/checksum and compatibility; distinguish backup existence from recoverability |
| DV-Q08 | Secure pipeline fixture with untrusted input and forbidden mutation | Actual deny/no effect, scoped credentials, immutable artifact, scan status vs attestation claim |
| DV-Q09 | Cost/exhaustion and hosted/local selection | Verified source assumptions, units/limits, unknown facts, no paid call; stop if budget/authority absent |
| DV-Q10 | Fresh Builder and independent reviewer on bounded operational task | Portable payload, raw tests, source/observer identity, independent negative checks |
| DV-Q11 | Repository-quality exercise across multiple project types | Actual rendered and semantic README review, verified setup/output, source links, no overclaim and appropriate nonactivation |
| DV-Q12 | Integrated regression and multi-specialist composition | Preserve existing 173 standing tests and exact framework, actual additional cases, all five roles coherent, owner acceptance/release separate |

Exercises are discovery proposals, not tests run or imposed counts. Combine equivalent evidence where appropriate. Require real observations for claims; no simulated independent actor, no mandatory hosted environment, external cost or live production operation.

## 5. Retained cross-specialist research

Keep existing XR-01–14 register unchanged. Revisit prior XR-04 (Forgejo), XR-05 (Langfuse/MLflow/Opik), XR-06 (Deepchecks), XR-12 (controlled failure) for actual DevOps decisions with exact current facts. Proposed additional leads, stable DR IDs for this research unit (not new CAP records):
- DR-01: documentation/repo experience, all specialists, DO-S04/05/06/07/08–11; see separate proposal.
- DR-02: Security + DevOps + QA, DO-S03/12/13; supply-chain controls and meaningful verification.
- DR-03: Architecture + DevOps, DO-S01/02; platform/infra/operability tradeoffs and lifecycle.
- DR-04: QA + DevOps, DO-S01/02/14–18; actual readiness, synthetic recovery, SLO evaluation.
- DR-05: UI/UX + documentation, DO-S04/05/06/07; visual hierarchy and actual task demonstrations with asset rights.
- DR-06: deferred Review Parity, DO-S03/13; source/subject identity and stale evidence, not a new governance runtime.

Next decision: approve a detailed temporary DevOps & Reliability PRD, with repository-quality coverage explicitly cross-cutting and proportionate. Proposed target Praxis v1.4.0 / DevOps v0.1, subject to owner review. Do not change standalone AIPF or start implementation now.

## Supplementary research — Scorecard and Awesome Actions

See [discovery 02](DEVOPS-SECURE-AUTOMATION-DISCOVERY-02.md) and extended [source register](DEVOPS-SOURCE-REGISTER-01.md#supplement-02--scorecard-and-github-actions), DO-S19–25. Refine secure delivery, repository lifecycle, CI, release/artifact and QA/DevOps coverage: individual posture findings with unknowns, action qualification, archived action avoidance, artifact retention and verified publication. Extend DR-01/02/06 and add DR-07/08 as described there. No new requirements, dependency or score threshold authorized.
