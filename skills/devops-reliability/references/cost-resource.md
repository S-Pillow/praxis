# Cost and sustainable resource management

Use only applicable cards. Examples are synthetic and unexecuted. Source IDs resolve through [SOURCES](../SOURCES.md); provider facts must be verified at use.

## DO-D29 — Is the proposed system economically feasible?

**Applicability / context:** Hosted/external service, infrastructure, CI or AI model decision; owner budget and workload known.

**Decision and alternatives:** Compare no new service, existing, local/self-hosted and hosted. Model normal and peak requests/compute/runtime/storage/egress, build minutes, logs/traces, backup, AI tokens/evaluation, licensing and people/time. Use verified current unit prices and terms, region/account scope and commercial eligibility; distinguish estimate, actual bill and uncertainty. Alerts notify, hard caps stop where enforceable; zero-spend binding requirement needs actual ceiling or stop before incur. Include retained resources after teardown and migration/exit.

**Counterexample:** Free requests do not cover CPU or egress; budget alert arrives after overage; orphaned storage continues billing.

**Observable verification:** Verify exact tariff/quota/limit and billing dimensions against official current evidence; compare estimates to actual authorized usage/bill; demonstrate no spend beyond permitted cap or disclose unestablished. No invented price.

**Sources and limits:** DO-S01, DO-S34–35, DO-S54–55; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D30 — What data does cost estimation transmit?

**Applicability / context:** IaC cost prediction, provider plan/API or local estimation.

**Decision and alternatives:** Choose local/manual estimate if adequate. Infracost's documented local CLI pricing-parameter transmission differs from separate Plan JSON API upload; evaluate actual chosen version/data path, credentials, sensitive attributes, billing and permissions. Protect plan/state and use minimized synthetic inputs if testing. Do not send plan merely to get estimate.

**Counterexample:** Local-looking tool uploads sensitive plan; estimate assumes resources never scale or omits egress. Cost number is not actual spend.

**Observable verification:** Inspect allowed data flow, model normal/peak and missing billing categories, validate output assumptions; no upload or installation without authorization.

**Sources and limits:** DO-S26, DO-S34–35, DO-S54–55; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D31 — How should ongoing toil and quota exhaustion be handled?

**Applicability / context:** System expected to run regularly, spend/maintenance/monitoring limits or retry loops.

**Decision and alternatives:** Track meaningful resource use, owners, limits, bounded retries and cleanup/retention obligations. Define graceful degraded behavior if quota/disk/time exhausted, protect state and operator notice. Scale/simplify based on observation. Teardown means approved resource cleanup plus independent billing/account check, not blanket destructive delete.

**Counterexample:** Deleting compute leaves snapshots/IPs/log storage, or a failed job retries until spend cap. More replicas increase cost without addressing database bottleneck.

**Observable verification:** Measure actual resource state/usage and bounds, controlled limit test and cleanup readback. Avoid guarantees without verified cap.

**Sources and limits:** DO-S01, DO-S28–29, DO-S34–35; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.
