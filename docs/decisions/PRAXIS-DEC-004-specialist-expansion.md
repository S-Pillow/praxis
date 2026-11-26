# PRAXIS-DEC-004 — Specialist expansion and engineering intelligence

Status: Owner-approved roadmap direction, 2026-11-25. Applies to Praxis only. Supersedes the earlier QA-first expansion preference; preserves the initial release baseline, historical research and prior decisions. Implementation and release authorization are separate.

## Context

The early specialist research emphasized skills for an AI performing implementation and quality checks. Praxis v1.0.0 now supports both direct execution and separate Prompt Agent/Builder execution. [DEC-002](PRAXIS-DEC-002-builder-context-independence.md) establishes Builder context independence, and [DEC-003](PRAXIS-DEC-003-quality-first-prompts.md) establishes quality-first operational synthesis.

The priority question is therefore which expertise materially improves decisions and instructions before implementation, while still helping with diagnosis, critique and verification. AIPF already governs how development, verification and acceptance are conducted; more procedural instructions are not a substitute for domain expertise.

## Decision

Software Architecture & Engineering Design is the next planned specialist. Decisions about system boundaries, data, technology, integrations and tradeoffs shape implementation and downstream quality. An architecture specialist should help select the simplest appropriate design for a project's actual constraints, not prescribe complexity or a preferred stack.

The indicative subsequent sequence is Security & Privacy, QA & Engineering Quality, then DevOps & Reliability. Security expertise informs design and trust boundaries early; QA supplies specialist testing and diagnosis techniques rather than duplicating AIPF governance; DevOps supplies operational and infrastructure expertise when relevant. This is a reasoned prioritization, not evidence of comparative superiority or a commitment to dates. UI/UX remains the only available specialist.

Review Parity remains a separate experimental initiative and a possible source of cross-cutting engineering assurance mechanisms. Its future role is distinct from domain expertise and governing authority. Read-only evidence auditing is a candidate starting point, not an approved implementation plan. No production readiness or efficacy claim is made.

## Consequences

- Keep AIPF authoritative and preserve the existing role and authorization boundaries.
- Consult specialists for material benefit; synthesize their useful outputs into decisions and portable instructions rather than requiring the Builder to install them.
- Prefer proven, source-linked techniques and context-specific tradeoffs; choose catalogs, tools and dependencies only where useful.
- Qualify new capabilities through proportionate mechanism tests and meaningful project use. Comparative superiority over AIPF alone is not a blanket prerequisite; claims must match evidence.
- Preserve earlier QA research and Review Parity experimental evidence without treating unfinished comparative research as either a success or failure of the proposed Praxis integration.

The [PRD roadmap](../PRD.md#6-specialist-expansion-roadmap) is the current product planning reference. No change to standalone AIPF, v1.0.0 release contents, runtime registration or existing acceptance requirements is implied.

## Research and planning consolidation — 2026-11-25

The completed discovery and build-plan research led to an original progressive guide/decision-card design and a shared external capability index. Free-for-Dev is discovery-only; material provider facts are verified at point of recommendation. Interfere and Claude Ship remain optional candidate references, not integrations. See [Historical PRD v1.2](https://github.com/S-Pillow/praxis/blob/c6393f6174e8d83e6760cf64bfbe889710d8919d/docs/PRD.md) and [build plan](../ARCHITECTURE-SPECIALIST-BUILD-PLAN.md). This final planning copy does not claim implementation approval, completed tests or publication of v1.1.0.
