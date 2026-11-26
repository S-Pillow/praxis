# Performance and capacity

Original conditional decision guidance; apply only within approved project intent. Source keys link to [source register](../SOURCES.md). No claim of current provider facts or project-specific acceptance.

## A22
**Decision:** What should be measured before optimizing?
- **Use when:** Latency, throughput or resource problem has a concrete workload/target.
- **Disqualifiers / stop:** Do not infer a bottleneck from code length or benchmark a toy workload as production proof.
- **Alternatives and consequences:** Keep simple design until representative profile shows bottleneck; optimize algorithm/query/batch first; scale infrastructure only for demonstrated capacity need.
- **Implementation implications:** State workload size/distribution, peak concurrency, target, environment and measurement method; profile relevant path and avoid uncontrolled production load.
- **Verification / revisit:** Compare reproducible baseline and candidate under same input; test tail/failure cases if material, disclose environment limits.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A23
**Decision:** Should we add an index or cache?
- **Use when:** Repeated expensive queries or reads are evidenced and consistency expectations are known.
- **Disqualifiers / stop:** Reject cache if correctness depends on immediate authoritative state and invalidation cannot be guaranteed; indexes add write/storage cost.
- **Alternatives and consequences:** Improve query/data model or index first; in-process cache for local repeated reads; shared cache only when cross-process state actually required.
- **Implementation implications:** Choose keys/TTL/invalidation, stale behavior, size/eviction and sensitive data rules. Index representative predicates and sort; do not duplicate authoritative records.
- **Verification / revisit:** Measure representative query and write costs; exercise invalidation, eviction, restart and stale/missing cache behavior.
- **Provenance:** P1,P2,K2 (original synthesis; no upstream content copied). **Maintenance:** version-sensitive.

## A24
**Decision:** When is scaling or splitting justified?
- **Use when:** Measured capacity or isolation limit conflicts with approved demand, growth or availability.
- **Disqualifiers / stop:** Do not use hypothetical millions of users to overbuild modest workloads.
- **Alternatives and consequences:** Tune bounded concurrency, indexes or batching; vertical scale may be simpler; horizontal split when measured constraints require it with explicit consistency and coordination tradeoffs.
- **Implementation implications:** Define scaling trigger and capacity assumptions, state ownership, backpressure, workload partitioning and operational costs.
- **Verification / revisit:** Reproduce workload at meaningful bounds, observe bottleneck and saturation behavior; avoid invented service-level guarantees.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

