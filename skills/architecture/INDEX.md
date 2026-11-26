# Architecture decision index

Use question/alias to load only the relevant guide. IDs are stable within v0.1; no ranking or mandatory sequence. For material provider selection also consult the independent [capability index](../../knowledge/capabilities/INDEX.md). Each card is advisory original synthesis; sources and maintenance classes are explained in [SOURCES.md](SOURCES.md).

## [Drivers and constraints](references/drivers-constraints.md)
Aliases: requirements, quality attributes, workload, constraints, ADR, assumptions.

- [A01 — Which requirements actually change architecture?](references/drivers-constraints.md#a01)
- [A02 — How much uncertainty warrants a spike?](references/drivers-constraints.md#a02)
- [A03 — When should a decision be recorded or revisited?](references/drivers-constraints.md#a03)

## [System shape](references/system-shape.md)
Aliases: local app, monolith, modular monolith, client/server, microservices, event-driven.

- [A04 — Does this need a server at all?](references/system-shape.md#a04)
- [A05 — One deployable, modular monolith or separate services?](references/system-shape.md#a05)
- [A06 — Does event-driven processing improve the workflow?](references/system-shape.md#a06)

## [Module and interface design](references/modules-interfaces.md)
Aliases: cohesion, coupling, dependency direction, abstraction, ports, adapters, public contract.

- [A07 — Where should responsibility and dependency boundaries sit?](references/modules-interfaces.md#a07)
- [A08 — When is an abstraction worth introducing?](references/modules-interfaces.md#a08)
- [A09 — How do we evolve a public interface?](references/modules-interfaces.md#a09)

## [Technology and cost](references/technology-cost.md)
Aliases: stack, runtime, build reuse buy, maintenance, dependencies, lifecycle, licensing, TCO.

- [A10 — Should we retain the existing stack?](references/technology-cost.md#a10)
- [A11 — Build, reuse, buy or do without?](references/technology-cost.md#a11)
- [A12 — How does a fixed budget affect the design?](references/technology-cost.md#a12)

## [Data architecture](references/data-architecture.md)
Aliases: persistence, SQLite, PostgreSQL, key value, object, transactions, migration, backup.

- [A13 — Do we need to persist this data?](references/data-architecture.md#a13)
- [A14 — Embedded SQL, server SQL, document/KV or object storage?](references/data-architecture.md#a14)
- [A15 — How do we change a schema safely?](references/data-architecture.md#a15)

## [Interfaces and integrations](references/integration.md)
Aliases: HTTP, API, schema, sync async, versioning, retries, idempotency, uncertain completion.

- [A16 — Synchronous or asynchronous boundary?](references/integration.md#a16)
- [A17 — Can an uncertain operation be retried?](references/integration.md#a17)
- [A18 — How should API/event schemas evolve?](references/integration.md#a18)

## [Runtime and resilience](references/runtime-resilience.md)
Aliases: timeouts, retry, cancellation, process ownership, backpressure, failure isolation, recovery.

- [A19 — How do we bound work and cancellation?](references/runtime-resilience.md#a19)
- [A20 — How should partial failures and retries behave?](references/runtime-resilience.md#a20)
- [A21 — What level of recovery is required?](references/runtime-resilience.md#a21)

## [Performance and capacity](references/performance.md)
Aliases: workload estimation, indexes, profiling, cache, invalidation, scaling.

- [A22 — What should be measured before optimizing?](references/performance.md#a22)
- [A23 — Should we add an index or cache?](references/performance.md#a23)
- [A24 — When is scaling or splitting justified?](references/performance.md#a24)

## [Existing system evolution](references/evolution.md)
Aliases: preserve, extend, refactor, replace, consumers, debt, migrations, compatibility.

- [A25 — Preserve, extend, refactor or replace?](references/evolution.md#a25)
- [A26 — How can a change be migrated reversibly?](references/evolution.md#a26)
- [A27 — Is architecture debt material?](references/evolution.md#a27)

## [Cross-domain design](references/cross-domain.md)
Aliases: trust boundaries, privacy, UI states, observability, testing, deployment identity.

- [A28 — Where is the trust/data boundary?](references/cross-domain.md#a28)
- [A29 — How should system and interface states agree?](references/cross-domain.md#a29)
- [A30 — What observability and release evidence do we need?](references/cross-domain.md#a30)

## [External capability selection](references/external-capabilities.md)
Aliases: provider, free tier, hosted, existing, local, terms, quotas, interoperability.

- [A31 — Do we need an external service?](references/external-capabilities.md#a31)
- [A32 — How can we qualify free/low-cost operation?](references/external-capabilities.md#a32)
- [A33 — When is an external engineering tool useful?](references/external-capabilities.md#a33)

