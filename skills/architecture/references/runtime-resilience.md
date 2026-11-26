# Runtime and resilience

Original conditional decision guidance; apply only within approved project intent. Source keys link to [source register](../SOURCES.md). No claim of current provider facts or project-specific acceptance.

## A19
**Decision:** How do we bound work and cancellation?
- **Use when:** Long-running I/O, background tasks, user cancellation or resource exhaustion are plausible.
- **Disqualifiers / stop:** Avoid fire-and-forget or unbounded concurrency; cancellation is not proof remote side effects stopped.
- **Alternatives and consequences:** Use simple synchronous bounded operation if adequate; worker pool/queue with admission controls when load warrants; avoid introducing scheduler service needlessly.
- **Implementation implications:** Define deadline, queue bound, concurrency, owner, cancellation propagation, shutdown cleanup and effect reconciliation. Distinguish queued/running/cancelled/unknown.
- **Verification / revisit:** Test slow/hung task, saturated queue and cancellation; observe process/resource cleanup and no unapproved follow-on actions.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A20
**Decision:** How should partial failures and retries behave?
- **Use when:** Dependencies can be temporarily unavailable or return partial/invalid data.
- **Disqualifiers / stop:** Do not retry deterministic validation failures or indefinitely; do not convert unknown response to success.
- **Alternatives and consequences:** Fail fast, degrade explicitly or use bounded retry with backoff/jitter when safe. Isolate failure at responsibility boundary rather than multiplying infrastructure.
- **Implementation implications:** Classify failure, deadlines, retry eligibility and idempotency; set observable terminal state and recover/reconcile uncertain results. Keep error messages actionable.
- **Verification / revisit:** Inject timeout, malformed response and exhausted budget; assert no prohibited downstream action and accurate result state.
- **Provenance:** P1,P2,K3 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A21
**Decision:** What level of recovery is required?
- **Use when:** A stateful or operationally important service risks interruption, corruption or loss.
- **Disqualifiers / stop:** Do not promise recovery from a backup that was never tested or define recovery policy from arbitrary availability targets.
- **Alternatives and consequences:** For disposable work restart may suffice; durable state can require checkpoint/restore; high-consequence system may need redundancy only if recovery objectives justify it.
- **Implementation implications:** Define approved recovery objectives, protected data, ownership, restoration path and external effects; separate availability from durability.
- **Verification / revisit:** Test the representative interrupted path and restore on isolated data; report actual recovery observations and gaps.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

