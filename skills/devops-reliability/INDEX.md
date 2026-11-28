# DevOps & Reliability — question-led index

Start with the actual operational question; use only relevant cards. These are original advisory decisions, not a new process or authority. See [skill](SKILL.md), [sources](SOURCES.md), [shared repository quality](../../knowledge/repository-quality/INDEX.md), [shared capabilities](../../knowledge/capabilities/INDEX.md). All examples are illustrative, not executed.

## Git and repository lifecycle
- [DO-D01 — Which source, branch and release are authoritative?](references/source-repository.md#do-d01--which-source-branch-and-release-are-authoritative)
- [DO-D02 — What repository controls and review permissions matter?](references/source-repository.md#do-d02--what-repository-controls-and-review-permissions-matter)
- [DO-D03 — Hosted or self-hosted forge and runners?](references/source-repository.md#do-d03--hosted-or-self-hosted-forge-and-runners)

## Build automation and CI
- [DO-D04 — Did the intended tests actually run?](references/build-ci.md#do-d04--did-the-intended-tests-actually-run)
- [DO-D05 — How to isolate and reproduce a build?](references/build-ci.md#do-d05--how-to-isolate-and-reproduce-a-build)
- [DO-D06 — Which build evidence and artifacts should survive?](references/build-ci.md#do-d06--which-build-evidence-and-artifacts-should-survive)

## Delivery and release management
- [DO-D07 — Which delivery strategy meets the real need?](references/delivery-release.md#do-d07--which-delivery-strategy-meets-the-real-need)
- [DO-D08 — When is sync or release actually complete?](references/delivery-release.md#do-d08--when-is-sync-or-release-actually-complete)
- [DO-D09 — How do migrations and recovery constrain promotion?](references/delivery-release.md#do-d09--how-do-migrations-and-recovery-constrain-promotion)

## Infrastructure as code and configuration
- [DO-D10 — How should plan, state and apply be separated?](references/infrastructure-config.md#do-d10--how-should-plan-state-and-apply-be-separated)
- [DO-D11 — Can configuration automation be repeated safely?](references/infrastructure-config.md#do-d11--can-configuration-automation-be-repeated-safely)
- [DO-D12 — What changes should remain manual or provider-native?](references/infrastructure-config.md#do-d12--what-changes-should-remain-manual-or-provider-native)

## Runtime and platform selection
- [DO-D13 — What is the simplest viable operating model?](references/runtime-platform.md#do-d13--what-is-the-simplest-viable-operating-model)
- [DO-D14 — How does workload and state affect operation?](references/runtime-platform.md#do-d14--how-does-workload-and-state-affect-operation)
- [DO-D15 — How should operational ownership and exit be compared?](references/runtime-platform.md#do-d15--how-should-operational-ownership-and-exit-be-compared)

## Networking, DNS and TLS
- [DO-D16 — At which layer does a network symptom arise?](references/networking-dns-tls.md#do-d16--at-which-layer-does-a-network-symptom-arise)
- [DO-D17 — What should DNS/TLS and routing changes protect?](references/networking-dns-tls.md#do-d17--what-should-dnstls-and-routing-changes-protect)

## Observability and monitoring
- [DO-D18 — Which signals answer the operational question?](references/observability.md#do-d18--which-signals-answer-the-operational-question)
- [DO-D19 — Can telemetry be lost or overrun?](references/observability.md#do-d19--can-telemetry-be-lost-or-overrun)
- [DO-D20 — How should AI operational traces and data drift be interpreted?](references/observability.md#do-d20--how-should-ai-operational-traces-and-data-drift-be-interpreted)

## Reliability and incident management
- [DO-D21 — What user outcome deserves an SLI/SLO?](references/reliability-incidents.md#do-d21--what-user-outcome-deserves-an-slislo)
- [DO-D22 — How to diagnose and stabilize an incident?](references/reliability-incidents.md#do-d22--how-to-diagnose-and-stabilize-an-incident)
- [DO-D23 — When should capacity or resilience be expanded?](references/reliability-incidents.md#do-d23--when-should-capacity-or-resilience-be-expanded)

## Data operations and disaster recovery
- [DO-D24 — Which state needs backup, and can it be restored?](references/data-recovery.md#do-d24--which-state-needs-backup-and-can-it-be-restored)
- [DO-D25 — What retention, cleanup and migration effects are permitted?](references/data-recovery.md#do-d25--what-retention-cleanup-and-migration-effects-are-permitted)

## Secure delivery and operational trust
- [DO-D26 — What controls and findings matter for this delivery?](references/devsecops.md#do-d26--what-controls-and-findings-matter-for-this-delivery)
- [DO-D27 — How do action selection and release credentials remain safe?](references/devsecops.md#do-d27--how-do-action-selection-and-release-credentials-remain-safe)
- [DO-D28 — How are operational secrets and telemetry protected?](references/devsecops.md#do-d28--how-are-operational-secrets-and-telemetry-protected)

## Cost and sustainable resource management
- [DO-D29 — Is the proposed system economically feasible?](references/cost-resource.md#do-d29--is-the-proposed-system-economically-feasible)
- [DO-D30 — What data does cost estimation transmit?](references/cost-resource.md#do-d30--what-data-does-cost-estimation-transmit)
- [DO-D31 — How should ongoing toil and quota exhaustion be handled?](references/cost-resource.md#do-d31--how-should-ongoing-toil-and-quota-exhaustion-be-handled)

## Operational documentation and repository quality
- [DO-D32 — What runbook or README information actually helps?](references/operational-documentation.md#do-d32--what-runbook-or-readme-information-actually-helps)
- [DO-D33 — How should documentation and release parity be checked?](references/operational-documentation.md#do-d33--how-should-documentation-and-release-parity-be-checked)
