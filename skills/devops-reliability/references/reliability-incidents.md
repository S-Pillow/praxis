# Reliability and incident management

Use only applicable cards. Examples are synthetic and unexecuted. Source IDs resolve through [SOURCES](../SOURCES.md); provider facts must be verified at use.

## DO-D21 — What user outcome deserves an SLI/SLO?

**Applicability / context:** Reliability decision warranted by real user or business impact; identify measurement window, allowed failure and owner tradeoff.

**Decision and alternatives:** Use user-facing availability/correctness/latency denominator rather than raw infrastructure uptime; choose only justified target and error budget with owner. Distinguish pending/firing/notification and sustained burn from transient spikes. No samples is unknown, not success; route alerts to responsible maintainers with actionable instructions. No SLO or SLA invented for small local work.

**Counterexample:** CPU spike pages operator while users fine; metric missing hides failures; pending alert not delivered.

**Observable verification:** Use bounded synthetic good/bad/missing data and short/sustained events; verify evaluation interval, notification path and user outcome. Track actual denominator and coverage.

**Sources and limits:** DO-S14–16, DO-S28; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D22 — How to diagnose and stabilize an incident?

**Applicability / context:** Observed degradation or failure; exact user symptom, scope, timing, release/config/traffic changes and responsibilities.

**Decision and alternatives:** Preserve symptom and evidence; classify observed impact vs hypotheses. First minimize further harm using already authorized reversible actions, coordinate communication and escalation. Compare candidate causes by a discriminating observation (dependency errors, latency path, changed configuration); don't shotgun changes. Reconcile uncertain writes and partial effects; if repeated repairs fail, stop mutation under AIPF diagnostic breakpoint. Recovery includes original user path and protected state, not only a service restart. Record cause uncertainty, follow-up and learning without blame.

**Counterexample:** Restart appears healthy but queued requests duplicate writes or original timeout persists; log timestamp alone is not cause.

**Observable verification:** Capture initial failure, relevant versions and environment, one hypothesis test, authorized bounded correction and user recovery/negative side effects. Preserve counterevidence and remaining unknowns.

**Sources and limits:** DO-S02, DO-S14–18, DO-S29, DO-S40; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D23 — When should capacity or resilience be expanded?

**Applicability / context:** Observed saturation, expected workload or availability requirement; identify dependency limits, recovery and maintenance capacity.

**Decision and alternatives:** Use workload-based estimate and actual profiling; bounded timeouts, retry budgets/backoff/jitter, concurrency and backpressure coordinated with Architecture and QA. Evaluate simpler caching/load shedding/scale-up before additional services. Define graceful degradation and incident thresholds; avoid live chaos experiments without distinct authority. A synthetic fault fixture tests controlled effects only.

**Counterexample:** Retries amplify an overloaded dependency and overload queue; dashboard restored but delayed work never completed.

**Observable verification:** Test delay, timeouts, duplicate request, queue limit and recovery in isolated fixture; observe latency, failure rate and actual no-extra-write outcomes. No generalized production availability claim.

**Sources and limits:** DO-S14–18, DO-S28–29, DO-S40; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.
