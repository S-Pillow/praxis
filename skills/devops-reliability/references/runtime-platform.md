# Runtime and platform selection

Use only applicable cards. Examples are synthetic and unexecuted. Source IDs resolve through [SOURCES](../SOURCES.md); provider facts must be verified at use.

## DO-D13 — What is the simplest viable operating model?

**Applicability / context:** New or changed application; establish local vs shared users, persistent state, execution duration/background work, concurrency, uptime, latency, data/region and budget.

**Decision and alternatives:** Offline/local for a single-user tool without remote needs; static hosting for immutable client assets without server-only secret/data processing; managed app when API/process/state constraints fit; VM/container when custom runtime/OS, long jobs or network control justify maintenance; orchestration only for genuine multi-service scheduling, isolation, scale and team capacity. Retain existing if adequate. Separate app/data from deployment choice. Reject serverless for unsupported duration/state assumptions, static host for server secrets.

**Counterexample:** A small CLI gains a public database and cluster for no user need; a static site attempts to store API secrets in client code.

**Observable verification:** Trace first useful action, exact runtime/limits and dependencies, deployment/recovery/cost responsibility; verify volatile provider facts via shared qualification rather than guess.

**Sources and limits:** DO-S01–02, DO-S14–18, DO-S31, DO-S34–35; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D14 — How does workload and state affect operation?

**Applicability / context:** Service lifecycle, scaling, start/stop, memory/disk/network or worker scheduling; determine expected and peak loads.

**Decision and alternatives:** Map startup/readiness/liveness, bounded queue/work, cancellation and shutdown, ephemeral vs durable storage, concurrent writers, process ownership and restarts. Prefer existing runtime controls and meaningful resource measures. Containers are packaging/isolation context, not automatic durability or sandbox. Define degraded behavior on limit/exhaustion and dependencies; scale based on observed bottleneck, not technology popularity.

**Counterexample:** A health probe returns 200 while a worker cannot access persistent data; a restart silently loses queued jobs.

**Observable verification:** Test actual startup, bounded load, limit and restart with authorized fixture, verify state, user outcomes and cleanup. No universal throughput claims.

**Sources and limits:** DO-S01–02, DO-S28–29, DO-S31; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D15 — How should operational ownership and exit be compared?

**Applicability / context:** Hosted vs local/self-managed platform decision; identify account/tenant and maintainers.

**Decision and alternatives:** Compare security patches, TLS renewal, backups, alerts, incident response, access/support, lock-in/export, dependency changes and actual cost. Consider data export and migration before selecting proprietary service. Recheck current plan, region, commercial rights, quota and hard caps if material; avoid treating a provider claim as observed runtime.

**Counterexample:** A free plan pauses an idle service or cannot export needed data; self-hosted platform needs unavailable maintenance.

**Observable verification:** Verify exact plan constraints and authorized representative runtime, recovery/export and spend boundary; unknown facts remain unknown.

**Sources and limits:** DO-S14–18, DO-S34–35, DO-S42–44; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.
