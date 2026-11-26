# System shape

Original conditional decision guidance; apply only within approved project intent. Source keys link to [source register](../SOURCES.md). No claim of current provider facts or project-specific acceptance.

## A04
**Decision:** Does this need a server at all?
- **Use when:** Single operator, offline operation, modest local workload, or no multi-user shared state.
- **Disqualifiers / stop:** Disqualify local-only when approved requirements demand remote concurrency, centralized control, cross-device shared state or server-side secrets.
- **Alternatives and consequences:** Local process or static client reduces network and deployment cost; client/server supports shared state and controlled secrets but introduces uptime and trust boundaries. Keep the existing deployment when suitable.
- **Implementation implications:** Separate presentation from I/O and domain logic where useful; decide persistence independently; constrain file access, cancellation and secret placement.
- **Verification / revisit:** Run with network unavailable; verify expected local workload, failure recovery and absence of unauthorized persistence/network.
- **Provenance:** P1,P2,K1 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A05
**Decision:** One deployable, modular monolith or separate services?
- **Use when:** Boundaries and deployment independence are under discussion.
- **Disqualifiers / stop:** No service split solely for fashion, theoretical scale or organizational symmetry. Shared transactions and small team can disfavor distributed deployment.
- **Alternatives and consequences:** Single deployable minimizes ops; modules establish ownership without network failures; services may suit independently changing/scaling workloads or isolation needs but add contracts, latency and operational coordination.
- **Implementation implications:** Identify actual responsibility/data ownership and dependency direction. Keep in-process contracts until measured drivers justify remote boundary; plan versioning, failure isolation and operations if split.
- **Verification / revisit:** Verify dependency boundaries, transaction semantics and representative workload; if distributed, test partial failure and consumer compatibility.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A06
**Decision:** Does event-driven processing improve the workflow?
- **Use when:** Independent consumers, latency-tolerant work, buffering or asynchronous integration are actual requirements.
- **Disqualifiers / stop:** Avoid events for simple synchronous request/response or when immediate atomic cross-domain consistency is essential.
- **Alternatives and consequences:** Direct calls or a local durable work table may suffice; event delivery decouples time but introduces ordering, duplicate, replay and visibility complexity.
- **Implementation implications:** Define event identity, schema, ownership, delivery expectations, cancellation, correlation and reconciliation. Treat a broker as candidate, not default.
- **Verification / revisit:** Test duplicate/reordered/missing events, interruption and backpressure; verify user-visible completion semantics.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

