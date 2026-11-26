# Interfaces and integrations

Original conditional decision guidance; apply only within approved project intent. Source keys link to [source register](../SOURCES.md). No claim of current provider facts or project-specific acceptance.

## A16
**Decision:** Synchronous or asynchronous boundary?
- **Use when:** Integration has variable latency, workload spikes or independent producer/consumer timing.
- **Disqualifiers / stop:** No asynchronous queue if user needs immediate outcome and no meaningful independent work; no unbounded synchronous wait.
- **Alternatives and consequences:** Sync calls are easy to understand but couple availability; local worker/durable job may decouple latency; broker only if necessary delivery/scaling requirements justify it.
- **Implementation implications:** Specify timeout, completion state, correlation, cancellation, ownership and response/error contract. For async, define pending/failed/complete and recovery; preserve consumer compatibility.
- **Verification / revisit:** Observe slow/failing downstream, duplicate delivery and user-facing pending/error behavior; prove bounded work.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A17
**Decision:** Can an uncertain operation be retried?
- **Use when:** Network failure or timeout can occur after side effect commits but before reply.
- **Disqualifiers / stop:** Never blindly retry a non-idempotent operation, especially payment, creation, notification or destructive action. Do not claim failure proves no side effect.
- **Alternatives and consequences:** Use stable operation key and atomic deduplication where contract allows; query status or reconcile unknown completion; manual handling when no safe recovery. A broker alone does not solve duplicates.
- **Implementation implications:** Define key scope, same-key/different-payload rejection, transaction boundary, retry budget, timeout and status lookup. Preserve legacy API semantics or get decision.
- **Verification / revisit:** Inject failure after commit before response; retry same key and verify exactly one business effect, reject conflicting payload, check bounded retry and reconciliation.
- **Provenance:** P1,P2,K3 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A18
**Decision:** How should API/event schemas evolve?
- **Use when:** Consumers can upgrade independently or serialized data persists.
- **Disqualifiers / stop:** Do not silently reinterpret existing fields or assume all consumers ignore unknown fields.
- **Alternatives and consequences:** Prefer compatible additive changes; use explicit versioning or adapter for breaking meaning; avoid universal contract changes when local adaptation sufficient.
- **Implementation implications:** Name supported versions, required/optional fields, defaults, invalid/unknown handling, error semantics, deprecation and migration path.
- **Verification / revisit:** Run old and new consumers against representative messages; verify malformed/unknown version and error behavior.
- **Provenance:** P1,P2,K3 (original synthesis; no upstream content copied). **Maintenance:** version-sensitive.

