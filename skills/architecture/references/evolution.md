# Existing system evolution

Original conditional decision guidance; apply only within approved project intent. Source keys link to [source register](../SOURCES.md). No claim of current provider facts or project-specific acceptance.

## A25
**Decision:** Preserve, extend, refactor or replace?
- **Use when:** Existing system change has approved behavior and architecture constraints.
- **Disqualifiers / stop:** Do not reinterpret a bug fix as permission for redesign; preserve protected intent even if implementation can improve.
- **Alternatives and consequences:** Keep existing behavior/design if sufficient; narrow extension if new capability fits; refactor only with clear benefit and protected interfaces; replace if constraints cannot be met and approved.
- **Implementation implications:** Inspect actual source, current state and consumers; classify exact affected surfaces and invariants; choose reversible steps and scope.
- **Verification / revisit:** Baseline representative working behavior, verify new delta and relevant regressions; report unobserved runtime rather than infer.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A26
**Decision:** How can a change be migrated reversibly?
- **Use when:** Large or risky change spans consumer, storage or deployment boundaries.
- **Disqualifiers / stop:** Do not assume rollback is safe after irreversible data mutation; do not run live migration from advice.
- **Alternatives and consequences:** Use compatible additive change, adapter or feature boundary where useful; staged migration may reduce blast radius; direct replacement only when safe and authorized.
- **Implementation implications:** Map dependencies and transition ordering, state compatibility, recovery and cleanup authorization; define stop/rollback or forward-fix criteria.
- **Verification / revisit:** Exercise old/new version combinations, interrupted transition and recovery in disposable environment; verify no unauthorized live effects.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A27
**Decision:** Is architecture debt material?
- **Use when:** A concrete change or defect exposes coupling, duplicated invariants or fragile dependencies.
- **Disqualifiers / stop:** No blanket cleanup; style preference or missing named pattern is not debt evidence.
- **Alternatives and consequences:** Leave stable code when costs of change exceed benefit; targeted refactor when repeated failures, complexity or change friction are evidenced; redesign only by decision.
- **Implementation implications:** Link observed files/behavior to consequence and proposed minimal correction; separate candidate findings from confirmed failures.
- **Verification / revisit:** Demonstrate the failure structure or constraint impact; verify protected behavior and intended improvement, not number of refactored files.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

