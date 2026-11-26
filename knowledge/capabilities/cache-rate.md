# Caching and admission control

**No new service / existing / local first:** Do not add shared state by default; use bounded in-process cache/rate controls for single process or existing shared store if necessary. Establish staleness and failure policy.

The following are independently authored discovery candidates. Verify decisive facts at use; none grants installation, access, data transfer, billing or release permission.

## CAP-C01
**Name:** Redis
- **Tags:** existing, self-hosted, cache
- **Candidate use:** Shared cache/counters when shared semantics justified.
- **Constraints to check:** Version-specific license, persistence, atomicity, eviction, network cost, data protection and recovery.
- **Official documentation pointer(s):** https://redis.io/docs/latest/
- **Pricing / terms / licensing pointer(s):** https://redis.io/legal/licenses/
- **Observation / verification state:** 2026-11-25 official docs/licensing search identified references; exact version/rights not qualified.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

## CAP-C02
**Name:** Upstash Redis
- **Tags:** hosted, cache
- **Candidate use:** Managed shared cache or counters when network and plan fit.
- **Constraints to check:** Command and bandwidth billing, latency, atomic semantics, memory, exhaustion, availability, terms.
- **Official documentation pointer(s):** https://upstash.com/docs/redis/overall/getstarted
- **Pricing / terms / licensing pointer(s):** https://upstash.com/pricing/redis
- **Observation / verification state:** P2 dated pricing observation 2026-11-25; no quota asserted.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

