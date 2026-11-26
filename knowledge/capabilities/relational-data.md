# Structured data and persistence

**No new service / existing / local first:** No persistence if not authorized; in-memory for ephemeral state; existing database before a new one; embedded or self-managed stores where suitable.

The following are independently authored discovery candidates. Verify decisive facts at use; none grants installation, access, data transfer, billing or release permission.

## CAP-D01
**Name:** SQLite
- **Tags:** local, embedded, SQL
- **Candidate use:** Authorized local durable data with modest writer contention.
- **Constraints to check:** Concurrent writes, DB file ownership and path, filesystem locking, backup/restore, exact version, lifecycle.
- **Official documentation pointer(s):** https://www.sqlite.org/whentouse.html
- **Pricing / terms / licensing pointer(s):** https://www.sqlite.org/copyright.html
- **Observation / verification state:** P2 primary appropriate-use pointer; local software and licensing facts to qualify by exact version; not zero total operating cost.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

## CAP-D02
**Name:** PostgreSQL
- **Tags:** existing, local, self-hosted, SQL
- **Candidate use:** Shared relational data with transactional constraints; existing approved instance first.
- **Constraints to check:** Operations, authentication, concurrency, backups, maintenance, version, license and hosting costs.
- **Official documentation pointer(s):** https://www.postgresql.org/docs/
- **Pricing / terms / licensing pointer(s):** https://www.postgresql.org/about/licence/
- **Observation / verification state:** P2 documentation pointer; license pointer not newly inspected; no redistribution of upstream material.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

## CAP-D03
**Name:** Neon
- **Tags:** hosted, PostgreSQL
- **Candidate use:** Managed relational candidate when external hosting is permitted.
- **Constraints to check:** Plan/account compute, storage, idle/startup, connections, backups, region, terms, export and spend control.
- **Official documentation pointer(s):** https://neon.com/docs
- **Pricing / terms / licensing pointer(s):** https://neon.com/pricing
- **Observation / verification state:** P2 dated pricing observed 2026-11-25; no quota carried as current.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

## CAP-D04
**Name:** Supabase
- **Tags:** hosted, PostgreSQL, backend
- **Candidate use:** Relational backend when platform responsibilities fit; avoid adopting unrelated bundled features.
- **Constraints to check:** Projects, storage/compute, pausing, connection pool, backup, auth/tenant model, region, egress, commercial terms.
- **Official documentation pointer(s):** https://supabase.com/docs
- **Pricing / terms / licensing pointer(s):** https://supabase.com/pricing
- **Observation / verification state:** P2 dated pricing observed 2026-11-25; no quota or idle guarantee carried as current.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

## CAP-D05
**Name:** Cloudflare D1
- **Tags:** hosted, relational
- **Candidate use:** Managed data near compatible application runtime.
- **Constraints to check:** Transactions/concurrency semantics, query features, read/write metering, storage, export, region, overage and terms.
- **Official documentation pointer(s):** https://developers.cloudflare.com/d1/
- **Pricing / terms / licensing pointer(s):** https://developers.cloudflare.com/d1/platform/pricing/
- **Observation / verification state:** 2026-11-25 official documentation/pricing search identified pointer; no limits or operational claims qualified.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

