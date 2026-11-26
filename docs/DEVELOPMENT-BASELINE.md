# Praxis — Development Baseline

Version: 0.1 | Product planning approved: 2026-11-24

**Historical planning checkpoint.** For the later QUALITY-01 / VALIDATION-05 acceptance and v1.0.0 preparation, see [historical v1.0.0 release evidence](releases/1.0.0.md). The original roadmap and earlier state below are retained as historical evidence. For current expansion priorities, see [PRD section 6](PRD.md#6-specialist-expansion-roadmap) and [DEC-004](decisions/PRAXIS-DEC-004-specialist-expansion.md); the historical phase statuses below are not current release gates.

## 1. Approved baseline

The product owner selected Praxis and approved the preceding product definition with “Approved.” This record, the [PRD](PRD.md) and [architecture](ARCHITECTURE.md) transcribe that decision into repository-ready documentation. The selection does not establish trademark availability, authorize a release, or establish implementation acceptance.

## 2. Existing assets

| Asset | Disposition |
|---|---|
| AIPF v8.10.1 | Incorporate; preserve purpose and source identity |
| UI/UX specialist v0.3 | Retain |
| 5,500-record design catalog | Retain |
| Recommendation engine | Retain |
| Manual catalog search | Retain |
| Existing regression tests | Retain |
| Specialist discovery adapters | Adapt |
| Core integration candidate | Review and adapt |
| Research and evaluation history | Preserve |
| URL Activity Scanner pilot evidence | Preserve |

Recorded source identities from prior project work (verify current repository before implementation):

- Canonical AIPF DOCX SHA-256: `8e66028c8ebf60ea87180be1c23933273d8a597c425d3a1595ae81d9a720b8e6`.
- Released specialist v0.3 main commit: `3e18d3dead376976ea3f18560eeaedd2cc2f43cd` in `S-Pillow/aipf-specialist-suite`.
- Earlier local integration candidate was developed against v0.2 archive commit `481bb188453b14108890ef0b803249759c5363f4`, not verified against v0.3. Treat its patch and test results as candidate evidence, not proof of current integration compatibility.

## 3. Roadmap

| Phase | Status | Deliverable |
|---|---|---|
| 0 — Existing foundation | Completed | Framework, UI/UX specialist, catalog, retrieval, practical pilot |
| 1 — Product definition | Owner approved | Product identity, PRD, architecture, integration contract |
| 2 — Core integration | Locally integrated; CORRECTION-01 verified on Linux/Windows | Reconcile candidate, establish product naming, complete repository integration |
| 3 — Independent validation | Partial evidence; outstanding portable Builder and visual/boundary verification | Cursor real-world testing, including actual activation and agent behavior |
| 4 — Initial Praxis release | Pending | Documentation, repository release, usage instructions and owner acceptance |
| 5 — Expansion | Future | Additional specialists, broader agent compatibility, eventual plugin distribution |

## 4. Responsibilities

| Participant | Responsibility |
|---|---|
| Product owner | Direction, decisions, final acceptance |
| ChatGPT | Architecture, planning, implementation, repository management, integration testing |
| Cursor | Independent execution testing and real-world validation |

Cursor is not a mandatory development intermediary.

## 5. Current implementation boundary

The initial PRAXIS-CORE-01 plan is historical; the integrated v0.3 candidate and CORRECTION-01 portability verification have superseded it. PRAXIS-BOUNDARY-01 implements DEC-002 and DEC-003 locally. Preserve the prior candidate and accepted evidence; verify only impacted behavior before independent portable-payload validation. Do not claim live activation or product acceptance from static tests. See the approved decisions and testing strategy below.

No further retrieval optimization, new specialist development, standalone AIPF modification or infrastructure work is included. Repository renaming should preserve history; actual remote mutation and release require appropriate authorization. Product name availability remains unverified.

## 6. Current state

Product definition: approved. CORE-01 incorporated the verified v0.3 baseline. CORRECTION-01 passed 118/118 on Linux and Windows (Windows assigned-observer report). Repository-based activation and context-sensitive retrieval were reported in VALIDATION-01; that unit remains FAIL/reconciliation owing to the external-asset boundary issue and incomplete evidence. VALIDATION-02 accepted with notes. BOUNDARY-01 incorporates the owner clarification of context independence and quality-first payload synthesis; independent verification remains pending for changed instructions. Repository rename, shared synchronization and Praxis release: not performed.

## 7. Standing regression strategy (owner approved 2026-11-24)

[PRAXIS-DEC-001](decisions/PRAXIS-DEC-001-scenario-regression.md) establishes permanent scenario-based regression alongside unit and integration tests. See [testing strategy](TESTING.md) for the retained corpus, evidence levels and impact-triggered extension. This does not modify standalone AIPF or establish release acceptance. The decision record preserves its original historical evidence limitations; the later full report was received and hash verified during CORRECTION-01.

## 8. Subsequent approved decisions

- [DEC-002 — Builder Context Independence](decisions/PRAXIS-DEC-002-builder-context-independence.md): optional Builder access is not a workflow prerequisite or authority; supersedes the earlier exclusive-access interpretation.
- [DEC-003 — Quality-first prompt synthesis](decisions/PRAXIS-DEC-003-quality-first-prompts.md): minimize unnecessary tokens only after preserving product quality and operational meaning. See the [testing strategy](TESTING.md) for regression evaluation.

- [DEC-004 — Specialist expansion](decisions/PRAXIS-DEC-004-specialist-expansion.md): subsequent roadmap decision (2026-11-25). Architecture & Engineering Design is the next planned specialist; QA research remains valuable. Review Parity is a potential cross-cutting assurance capability, not a released feature.

Historical release gates at this planning checkpoint: independent portable Builder execution, final source-bound rendered evidence and external-asset boundary verification, impact-triggered regression and owner release authorization. No new runtime infrastructure or specialist work was authorized at this checkpoint. See the published [v1.0.0 release record](releases/1.0.0.md) for subsequent disposition.

For the current consolidated requirements, see [PRD v1.3](PRD.md) and [architecture specialist build plan](ARCHITECTURE-SPECIALIST-BUILD-PLAN.md). Historical phase status and release evidence are unchanged. The architecture specialist is qualified for v1.1.0; see [release qualification](releases/1.1.0.md).
