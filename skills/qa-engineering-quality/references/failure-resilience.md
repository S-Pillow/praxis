# Failure and resilience

Original conditional QA guidance. Examples below are illustrative, not executed qualification. Source IDs resolve via [SOURCES](../SOURCES.md); use current official evidence for material volatile facts. AIPF and approved requirements govern.

## QA-D16 — How do I inject failures without uncontrolled chaos?

**Applicability / context:** Authorized disposable fixture or test seam; never production fault injection from QA consultation.

**Decision and alternatives:** Select concrete failure modes from risk: delayed or failed response, duplicate submit, interrupted navigation, partial update, cancellation. Use explicit seed/schedule and bounded time, not uncontrolled random global patches. Existing mocks/local seam first; actual integration if required and authorized.

**Counterexample:** Random failures reproduce inconsistently and can affect unrelated systems; generic catch hides partial write.

**Observable verification:** Force exact order/failure point; assert visible failure, no unintended mutation, cleanup and recovery. Retain raw schedule/output and limits.

**Sources and limits:** QA-S05, QA-S03. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D17 — What if a retry follows an uncertain commit?

**Applicability / context:** Operation may succeed before response fails; duplicate requests or cancellation.

**Decision and alternatives:** Identify intended idempotency and transaction boundaries. Test same operation identity, conflicting payload, retry after success/failure and unrelated entity. Choose no automatic retry if effects uncertain; use approved deduplication or recovery contract. Do not invent exactly-once guarantee.

**Counterexample:** Retry on timeout charges or inserts twice; UI sees one success but records doubled.

**Observable verification:** Observe first effect and thrown response, retry and count/identity, conflicting key denial without state change; verify preserved other records.

**Sources and limits:** QA-S24, QA-S03. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D18 — How do I diagnose stale results and flakiness?

**Applicability / context:** Asynchronous completion or intermittently failing verification.

**Decision and alternatives:** Construct explicit A then B requests, finish B then A; check latest intent wins. Isolate event readiness, state, timers, order and dependencies; retain first failed run, repeat only to distinguish causes. Choose controlled scheduler or fake time when it preserves boundary; no silent retry/quarantine.

**Counterexample:** A longer sleep makes 9/10 tests pass but old results still overwrite the new query.

**Observable verification:** Verify both completion orders and normal one-request path, expected no stale state; report fail/retry separately and actual evidence coverage.

**Sources and limits:** QA-S05, QA-S32, QA-S27. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

