## **T1 - Orchestrated Authorization Unit and Builder Payload**

### **Full Packet - managed change**

Prompt-Agent Derivation Record - RETAIN PROMPT-AGENT-SIDE: framework version - ; route/application baseline - ; activated chapters - ; current Control Record revision - ; capability-profile ID when Platform Capability controls are active - ; Section 9 treatment plus urgent-corrective overlay when active - ; preflight type/result READY / READY WITH CONDITIONS - ; derivation proof/current-state check - .

Builder Payload - TRANSPORT TO BUILDER: authorization-unit ID - ; objective - ; exact operational context and accessible inputs OR accessible stable Builder-baseline identity plus required delta - ; authorized actions: actor/action/target/state-preconditions - ; targets - ; constraints, allowed surfaces, and forbidden work - ; work_allowance (optional; omitted = none) - ; planned procedural transitions/conditional gates - ; workstream dependency/independence map and continuation authorization when applicable - ; expected automatic mutations/evaluations/external consequences and closure signals when material - ; relevant risks/scoped locked rules/governing intent - ; acceptance criteria - ; deterministic verification, evidence purpose, observer, feasibility/fallback - ; durability requirement - ; runtime/quota/artifact checks - ; exact stop conditions and stop scope - ; handoff requirements - . Include batch item IDs and their item-level fields only for an explicitly pre-authorized batch.

### **Compact Packet - compact known-pattern unit**

Prompt-Agent Derivation Record - RETAIN PROMPT-AGENT-SIDE: framework version - ; route/application baseline - ; activated chapters - ; current Control Record revision - ; capability-profile ID when Platform Capability controls are active - ; treatment compact; urgent-corrective overlay when active - ; Compact Preflight READY - ; derivation proof/current-state check - .

Builder Payload - TRANSPORT TO BUILDER: authorization-unit ID - ; one bounded meaningful objective OR batch item list - ; exact operational context/accepted baseline/authoritative state OR accessible stable Builder-baseline identity plus required delta - ; authorized actor/action/target - ; targets - ; shared allowed/forbidden boundary and constraints - ; material governing intent/protected invariants and relevant scoped rules/risks - ; work_allowance (optional; omitted = none) - ; planned transitions/conditional gates - ; workstream dependency/independence map and continuation authorization when applicable - ; expected automatic mutations/evaluations/external consequences/closure signals when material - ; deterministic acceptance/verification with evidence purpose, named observer, and feasibility/fallback - ; durability closure - ; binding stop and stop scope - ; compact handoff requirements - . For a batch, each item adds only item_id / exact_delta / allowed_surface / acceptance / evidence_observer / reversal_or_undo.

Use rule: When a distinct Builder exists, T1 is one orchestrated authorization unit with two partitions and only the Builder Payload is transported. A T1 with a missing, stale, conflicting, or non-passed Prompt-Agent Derivation Record is invalid and MUST NOT be sent. Prompt-Agent metadata stays internal unless an operational value materially affects execution. Do not duplicate shared fields per batch item or split one coherent objective merely because it contains multiple components, files, implementation tasks, derivations, verification steps, or procedural transitions. A current correction/continuation may carry only the delta plus an accessible immutable Builder-baseline reference when Chapter 21 No Phantom Context permits it. Omit mechanism fields that confirmed project-state controls establish as N/A only when omission is operationally unambiguous. Expand to the Full Packet when any Section 9 compact condition fails, item-level evidence cannot be separated, or a later step cannot be safely pre-authorized inside the current envelope. When no distinct Builder exists, do not manufacture the two partitions: record the same objective, authority, targets, constraints, acceptance, evidence, durability, and stop fields as the direct execution boundary, then reconcile result and applicable durability/closure state before new work.

## **T2 - Risk and Decision Register**

Finding - ; severity (Section 4.1 Phase -2A) - ; disposition (Section 4.1 Phase -2A) - ; affected component - ; why it matters - ; consequence - ; recommended resolution - ; decision question when applicable - ; build/authorization impact - ; owner - ; revisit trigger when deferred - .

## T3 - Project-State and Release Plan

Project root - ; authoritative editable/version state - ; state revision/version/guard - ; repository/remote/synchronization when applicable - ; stable branch/version when applicable - ; clean/expected state - ; expected/forbidden files - ; secret/log/runtime/build checks - ; tests/build/lint - ; planned durability/version closure - ; integration/synchronization plan - ; deploy/release plan - ; restart/reload/cache - ; backup when required - ; rollback/recovery action - ; rollback readiness required/achieved (Block B4), or n-a when inapplicable - ; least-sufficient mechanism confirmed: yes/no/reason - ; verification surface - ; cleanup decision - . Complete only fields material to the current change; full T3 is required only when the activated path/treatment needs it.

## **T4 - Field Purpose and Record Lifecycle**

Field/record - ; purpose scope: object-inherited / field-specific - ; required - ; collected/validated/stored/returned/displayed/editable - ; workflow/search/report/reference use - ; sensitivity/retention when material - ; resolution - ; approval/status - ; lifecycle actions and classifications (Section 2 Created records need an explicit lifecycle policy) - ; state protection - ; history/audit only when required - ; related-record impact - .

## **T5 - Runtime Data and Generated Artifact Inventory**

Runtime store/surface/path/output/artifact - ; purpose - ; format - ; owner/permissions - ; sensitive item-level data - ; retention - ; missing/corrupt-state behavior - ; backup/rollback - ; versioning policy; source-control inclusion/exclusion when applicable - ; cleanup - ; test-isolation mechanism/scope - .

## **T6 - Test Baseline and Raw Command Evidence**

Phase/authorization unit - ; governing test command/set - ; baseline GREEN / REGISTERED FAILING - ; registered failures with owner/disposition - ; registered verification limitation (claim/test, signature, environment, owner/disposition, accepted alternative evidence, invalidation triggers) when applicable - ; environment - ; affected surface - ; relevance decision/evidence - ; evidence purpose (Section 7 Evidence purpose and sufficiency) - ; claim under test - ; evidence source/provenance and exact evaluated identity (Block B3) - ; verification method - ; verification result - ; verification independence when Section 7 requires it - ; raw status/exit code and capture - ; log/output - ; failed assertions - ; comparison to baseline - ; evidence attribution and material assertion basis (Block B1) - ; acceptance interpretation - ; further evidence can change next action: yes/no - .

## **T7 - File and Data Exchange Contract**

Complete only applicable import/upload and export/report subsections. This contract governs application/product file/data exchange for users or systems. Development/executor artifact transfers and downloads use Chapter 19 rather than T7 solely for transport. When a transferred artifact also exercises an application/product exchange feature, apply T7 to that feature's contract and Chapter 19 to the execution transfer, without duplicating requirements. Update packages, installers, executable replacement, plugins, models, and rule packs delivered to update the application use Chapter 17.

Import/upload: formats/size - ; required/optional fields - ; aliases/case - ; blank/extra/missing/duplicate/merged/malformed behavior - ; date/number/locale/encoding - ; preview/confirmation - ; partial/rejected rows - ; runtime/storage/quota/external-call effects - ; errors/recovery - ; sample artifact - ; acceptance - .

Export/report: purpose - ; format/filename - ; exact fields/order - ; source data - ; timestamp/locale - ; missing/corrupt behavior - ; sensitive exclusions - ; access model - ; runtime/quota effects - ; sample artifact - ; acceptance - .

## **T8 - Decision Request**

Question - ; why no authorized default exists - ; governing intent/protected invariant at issue when applicable - ; options/consequences - ; recommendation/reasoning - ; affected work blocked - ; stop scope: local / workstream / hard - ; decision owner - ; affected authorization unit/route/evidence - ; exact fields or criteria changed by answer - ; requested response format - ; no further affected execution authorization until resolved - .

