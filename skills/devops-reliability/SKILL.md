---
name: aipf-devops-reliability
description: Context-grounded operational design, diagnosis and review for material delivery, infrastructure, reliability, runtime, repository lifecycle and cost decisions after AIPF routing.
---

> **Praxis resource root:** in a repository checkout or installed Claude plugin, use the directory two levels above this skill’s directory (containing `framework/`, `skills/` and `catalog/`). In another host, use the verified source root supplied by its distribution adapter. Resolve Praxis paths there, not against the target project; run helpers from that root only when accessible and authorized.

# DevOps & Reliability v0.1

Advisory expertise under AIPF v8.10.1; use when a material operational decision can change the work, not merely because a chapter or DevOps tool is present. Do not consult for trivial/unrelated edits or routine AIPF checks with no benefit. Shared [Documentation & Repository Quality](../../knowledge/repository-quality/INDEX.md) may apply independently.

## Decide whether to consult

Ask which operational decision could change and what would happen if the current assumption were wrong. A harmless spelling correction does not warrant consultation. Correcting a typo in a restore path or deployment flag can change the target and recovery behavior: inspect the exact command and approved target before deciding whether to change it. Use the smallest relevant guidance; no new classification engine or automatic permission follows.

## Select the applicable mode

- **plan:** actual target, workload, approved intent, constraints and owner; compare no change/existing/local/static/managed/VM/container/orchestration, justify simplest fit, operational responsibility, cost/privacy, effects and evidence.
- **diagnose:** exact symptom and source/config/environment, expected/observed, competing hypotheses, smallest discriminating permitted observation, bounded correction and recovery at original user path. Reconcile partial/uncertain effects; suspend speculative repeated repairs under AIPF.
- **review:** exact candidate, tested source/artifact/target, material controls and itemized findings, evidence and limitations; propose proportionate correction/next observation. Not automatic release sign-off or independent reviewer.

Consult [question-led index](INDEX.md), only relevant cards, [source record](SOURCES.md) and existing [shared capability index](../../knowledge/capabilities/INDEX.md) where a technology decision warrants. No mandatory lookup, installation, telemetry, cloud or runtime. A helper consult result does not prove application. Verify decision-sensitive provider claims at use. If knowledge, source, actual target/access, signal or observer unavailable, disclose; use bounded verified alternative only where sufficient or stop affected decision.

## Apply in context

Identify allowed target and exact read / plan / write / destructive / external publication effects, expected automatic effects, prohibited effects, permission and recovery boundaries. Available access is not authority. Never silently run provider calls, scans, installs, apply/destroy, force-unlock, upload data, modify repository controls, change quotas or publish. Preserve actual approved architectural/data/security intent. Distinguish source and provider claims, actual observations, hypotheses, estimates and decisions. Report real zero vs absent data, actual tested artifact vs claimed result, estimated vs actual cost, alerts vs enforceable caps, backups vs observed restoration. No single score proves safety; no fabricated SLA, source, run, rendering or independent review.

Compose Architecture (design/contracts), Security (trust and data rules), QA (oracles/negative effects), UI/UX (brand/usability/render), DevOps (operational fit/delivery/recovery) and shared repository quality once as relevant. Use the conflict-resolution guidance in the [Praxis entry](../praxis/SKILL.md). Eliminate options that violate approved constraints; compare viable alternatives and raise unresolved material decisions through AIPF. No competing process, status, approval or risk acceptance. Direct agent applies current operational boundary without self-handoff; Prompt Agent synthesizes canonical T1 with accessible implementation inputs, concrete operational requirements, targets, constraints, commands, permission, test/oracle, evidence and stop. Distinct Builder needs no Praxis, AIPF, PRD or specialist access and returns actual scoped evidence; no subsequent action authority. Do not make an unavailable required observer appear available.
