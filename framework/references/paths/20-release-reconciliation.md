# **Chapter 20 - Release Evidence and Ground-State Reconciliation Path**

When to use: Section 8 Release and reconciliation state activates this chapter: release, formal acceptance, external delivery, a demo used as acceptance/release evidence, or mixed-source evidence; a board, report, artifact stamp, release note, or claim may be stale; an operator-only gate remains; or explicit ground-state reconciliation is required. Routine implementation, informal sprint/demo feedback, and ordinary handoff do not activate the full chapter solely because they contain a completion claim. They still use Blocks B1-B3 and the verification fields in T1/T6 as applicable.

Companion chapters: composes with every releasing work path in Chapters 11-18.

## **20.1 Observability Matrix and Canonical Evidence Ledger**

When this chapter activates, define each material gate with: observable by (agent / tool / operator / platform UI / external service / mixed), tool or surface, required evidence, fallback when unavailable, and missing-evidence disposition. Assign evidence collection only to a named actor or tool with the required access and observation capability. Use the assigned actor's access in the applicable preflight and retain the observer's identity in the evidence ledger. If the assigned actor cannot observe the required evidence, use an authorized capable observer/tool or record the unmet prerequisite under Block B2. Apply the Section 5 Decision-changing work test and Section 7 Evidence purpose and sufficiency before adding a new gate or recheck.

The canonical evidence ledger records per material gate: claim or gate, status, Block B1 attribution, evidence source/provenance, verification method, verification result, acceptance interpretation, owner, Block B3 identity, retained location, and recheck trigger. For carried evidence, also record verified surface, controlling dependencies, environment or artifact identity, invalidation conditions, recheck method, and transferability. When the Section 7 verification-independence rule applies, record the independent observer/surface or the explicit reason self-observed evidence is sufficient.

Artifact proportionality. A compact known-pattern change records only the affected evidence row or rows in the Project Control Record or handoff. A full observability matrix is required when multiple observers, mixed evidence, release acceptance, stale claims, or operator-only gates make ownership or closure non-obvious. Do not create empty ledger rows for unaffected gates.

Verified surface means the smallest user-, operator-, integration-, artifact-, or system-observable behavior the evidence supports, including material environment and dependency assumptions; it is not automatically the file implementing that behavior. Invalidate evidence only when the current authorization unit changes that behavior, a controlling dependency/configuration, the containing artifact, an environment assumption, or the factual claim supported.

Review-cycle proportionality. One broad review of a stable state is normally sufficient for the surface it covers. After a correction, re-review only the changed or invalidated acceptance/evidence surface unless the correction can invalidate broader review evidence or a new decision-relevant uncertainty appears. Prior material findings must be closed or dispositioned, but cosmetic, stylistic, speculative, or non-acceptance-affecting observations do not automatically reopen a closed broad review gate. Apply Section 5 Decision-changing work and Section 7 Evidence purpose and sufficiency before repeating a review.

## **20.2 Human Attestation Protocol**

For a human-only gate, a short response block suffices: checklist identifier, result (PASS / FAIL / PASS WITH NOTES), exceptions, environment only when material, and evidence retained. "Passed \[checklist ID\] with no exceptions" closes an explicit checklist. Missing browser, device, timestamp, or screenshot detail is a documentation gap, not an automatic blocker, unless it materially affects risk, reproducibility, accessibility, or the acceptance claim. Attested evidence stays attested.

## **20.3 Ground-State Reconciliation Procedure**

1 Identify the claim that may be stale: board status, control sheet, release note, acceptance report, artifact version, summary, docs, or completion claim.

2 Re-check project/source ground state: intended root, authoritative editable/version state, revision/version/state_guard, branch/synchronization/integration state when applicable, expected/forbidden files, and generated artifacts.

3 Re-check runtime or artifact ground state: deployed artifact, package, installer, report output, version stamp, generated files, target environment, and operator workflow.

4 Classify drift: aligned / stale claim / stale artifact / stale docs / wrong provenance / incomplete verification / partial fix / operator-validation gap.

5 Correct the stale source of truth and add/update regression evidence when warranted. Block only the affected release, claim, or dependent workstream while drift can affect release or operator trust; unrelated independent work may continue when Section 5 Scoped stopping proves no shared-state, evidence, authority, or release dependency.

6 Apply Section 5.2 Risk/impact-triggered reconciliation when selecting the next reconciliation trigger. Record its decision-relevant drift risk or consequence; omit an unjustified recurring check.

### **Release Closure Playbook**

1\. List material release gates and their observers; build or update the observability matrix and ledger at the scale the release needs.

2\. Give human-only checks one compact checklist ID and accept concise attestation under 20.2.

3\. Confirm source/version, artifact, and deployment identity (Block B3), required durability/closure facts and evidence state (Block B2), and required rollback readiness (Block B4).

4\. Require explicit authorization before AI or automation executes release. When merge automatically deploys, the merge approval must state that deployment consequence.

5\. When Chapter 13 source-backed factual-content controls apply, load Section 13.3 and resolve its source-registration and verification-stamp requirements before closing.

6\. Reconcile documentation required by the Phase -1 documentation-scope declaration with source, released/packaged state, verification evidence, operator acceptance, and handoff. If deferred, record reason, owner, risk, and follow-up.

7\. Close only unresolved or impact-triggered ledger rows. Run 20.3 when any claim may have drifted.

