# Praxis — QA & Engineering Quality Specialist

**Product Requirements Document v1.0 — Proposed for owner approval**

26 November 2026 · Proposed Praxis v1.3.0 · QA specialist v0.1 · AIPF v8.10.1 unchanged.

## 0. Document control and governing baseline

| Item | Identity / status |
|---|---|
| Product baseline | Praxis v1.2.0, released commit `93da10c375b11d4f1172d9cb248b76a0fd2487d4`, tree `fdeba1d234c4825dab8b9a210657bdcb65c20` |
| Requirements authority | [Canonical product PRD v1.3](PRD.md), blob `4509b8e4c3d9dbe16f7386f8be682727fd63c85a`; all existing PR/AR/KI/NFR/SP/SK/SN requirements retained |
| AIPF | v8.10.1. Canonical DOCX SHA-256 `8e66028c8ebf60ea87180be1c23933273d8a597c425d3a1595ae81d9a720b8e6`; full Markdown projection SHA-256 `b11dfa2c12deb4d5b90833af4f10a02b5daf5e26d143469560b896fe9c85e0fd`; neither is manifest-file digest |
| Released modules | UI/UX v0.3, Architecture v0.1, Security & Privacy v0.1; 24 shared capability records; 163 standing regression tests on Linux and native Windows for the v1.2.0 qualified release tree. [Release evidence](releases/1.2.0.md) |
| Discovery | `b0f9fd6d3b19fb1e9a363c1a2320a0662710db48`; [Discovery report](../research/qa-engineering-quality/QA-ENGINEERING-QUALITY-DISCOVERY-01.md), [source register](../research/qa-engineering-quality/QA-SOURCE-REGISTER-01.md), [cross-specialist research register](../research/CROSS-SPECIALIST-RESEARCH-REGISTER.md) |
| Owner decision | Proposed requirements for review; not approved implementation or release authority. AIPF governs all execution. |
| Lifecycle | Temporary specialist PRD; upon acceptance and separately authorized release, consolidate into canonical PRD (proposed revision v1.4, Section 14), preserving approved IDs, wording, original history, provenance and evidence. Retire separate active PRD only after reconciliation. |

QA-F, QA-K, QA-N and QA-AC identifiers extend the existing product requirements without renumbering them. QD01–QD12 are representative exercise families retained from discovery, not product test counts. All prospective requirements, modes and exercises are proposals; no completed QA implementation or test outcome is implied.

**Navigation:** [Vision](#1-vision-and-problem) · [Scope](#2-users-and-scope) · [Requirements](#3-functional-requirements) · [Knowledge](#4-knowledge-architecture) · [Integration](#5-integration-and-consultation) · [Methods](#6-verification-diagnosis-and-test-effectiveness) · [AI evaluation](#7-ai-agent-and-instruction-evaluation) · [Capabilities](#8-capability-and-source-qualification) · [Quality attributes](#9-non-functional-requirements) · [Acceptance](#10-acceptance-criteria) · [Exercises](#11-representative-qualification-exercises) · [Delivery](#12-delivery-and-release) · [Traceability](#13-traceability) · [Owner decisions](#14-owner-review-and-stop-boundary).

## 1. Vision and problem

Praxis brings material engineering intelligence into decisions, operational prompts and direct implementation. QA & Engineering Quality supplies expertise in determining whether software actually behaves correctly, how to detect meaningful failures, how to diagnose their causes, and how to prove a correction preserves approved behavior. It should contribute before, during and after implementation, not become a mandatory final sign-off department or autonomous test platform. AIPF already governs scope, authority, evidence, acceptance and release.

### 1.1 Problem statements

- Green tests can be irrelevant, circular, mock-only or insensitive to the defect. The v1.2.0 independent Builder's original 15 tests passed, yet its reviewer identified four findings; corrected v2 passed independent checks. That bounded historical result illustrates test blind spots, not a claim about general defect rates or the future QA specialist.
- Material regressions occur in unchanged callers, coupled contracts, state, migrations, failure paths, asynchronous ordering and platform differences.
- AI-generated code may look correct but silently discard zero/false/empty, violate trust boundaries, add needless dependencies, use misleading assertions or report evidence never obtained.
- A screenshot, HTTP success status, coverage percentage or test count can create false confidence if actual effect, recovery and independent oracles remain unobserved.
- Agents can solve a problem through different valid paths. Exact trace equality is not correctness; unauthorized effects are unacceptable even if the response looks correct.
- Distributed execution requires explicit source/fixture/environment/observer identity, separate reports and observed results, and preservation of failures and corrections.

### 1.2 Outcomes and success

The specialist must help translate requirements and risk into observable tests; select the right verification layer and feasible observer; reproduce and diagnose failures with falsifiable hypotheses; assess test effectiveness; verify corrections and preserve existing behavior; supply applicable AI and data evaluation expertise; and synthesize material guidance into one direct action or portable Builder Payload.

Success means sufficient technical evidence for representative use and the integrated regression, not a target number of cards/tests/tools, code reduction, universal host support, certification, accuracy/coverage SLA, or comparative superiority over AIPF alone. Additional comparisons require a decision or claim that depends on them.

## 2. Users and scope

| Actor | Job to be done | QA contribution |
|---|---|---|
| Product owner | Understand what works, what remains unverified and which decision is needed | Concrete observed outcomes, impact and limitations in usable language; no specialist IDs required |
| Prompt Agent | Turn requirements into precise, executable verification | Risk-selected tests, acceptance oracles, negative effects, environment, authority and stop in T1 |
| Direct executing agent | Design/perform authorized tests or repair | Suitable methods, bounded diagnosis and actual verification, without self-handoff |
| Distinct Builder | Execute complete authorized work without governing context | Portable instructions and accessible inputs, raw test evidence and stop |
| Independent reviewer | Detect blind spots and verify correction | Source identity, independently authored checks, counterevidence, original/corrected history |
| Maintainer | Keep meaningful regression and avoid overengineering | Causal findings, focused corrections, reliable tests and proportionate coverage |

### 2.1 In scope

Risk and impact, test design and oracles, unit/property/state, contracts/integration, browser and UX verification, controlled failure and concurrency, reproduction/regression, flakiness, test strength, maintainability, data quality and AI/agent evaluation. Deliver original progressive knowledge, a question-led index, source/rights records, selected shared capability records, compatible additive integration, focused tests, representative direct and independent exercises and full cross-platform standing regression.

### 2.2 Out of scope

No second governance, status vocabulary, evidence lifecycle or acceptance authority; no autonomous test daemon, orchestrator, crawler, scanner, trace database, telemetry platform, benchmark service or automatic instruction optimization. No mandatory Playwright/EvalView/Promptfoo/etc., dependency installs, paid calls, accounts, production fault injection, live security probing, customer-data export or infrastructure provisioning. No AIPF change, DevOps or Review Parity implementation, replacement of released retrieval/catalog behavior, broad refactor, certification or automatic AI authorship claims. No new hosting, packaging or release through this planning document.

### 2.3 Domain boundaries

| Domain | QA contribution | Protected boundary |
|---|---|---|
| UI/UX | Observable user flows, render/interaction, accessibility and adverse states | UI/UX defines design/usability intent; QA cannot redesign to make tests pass |
| Architecture | Structural contract, consistency, integration/test seams and change impact | Architecture owns design/technology tradeoffs; no speculative refactor for tests |
| Security & Privacy | Negative auth, no disclosure/mutation, safe inputs and data lifecycle verification | Security supplies trust/control requirements; QA grants no live probing or risk acceptance |
| Future DevOps | Application recovery and CI evidence | Infrastructure, live operations and delivery expertise remain separate |
| Review Parity (deferred) | Source-bound claim/evidence sufficiency | No independent approval/signature/provenance runtime |
| AIPF | Engineering techniques and concrete observables | Canonical governance, routing, readiness, evidence, status, correction, acceptance and release remain authoritative |

Compose relevant expertise into one coherent decision or instruction. Do not duplicate reports or create separate approvals merely because domains overlap.

## 3. Functional requirements

All 22 are proposed Must requirements, applied conditionally to material work and approved constraints, not a checklist for every task.

| ID | Requirement | Observable fulfillment / limits |
| --- | --- | --- |
| QA-F01 | Material activation | Consult QA after canonical AIPF path selection for material verification, diagnosis or engineering-quality decisions. Select plan/diagnose/review; skip minor or unrelated work without concrete benefit. No mandatory extra consultation for routine AIPF verification. |
| QA-F02 | Risk and impact strategy | Identify intended behaviors, changed and coupled surfaces, high-impact invariants, failure modes, actual environment and feasible observations. Prioritize decision-changing tests over blanket coverage; history is a lead, not proof. |
| QA-F03 | Requirements-to-oracle mapping | Translate approved requirements into explicit preconditions, stimuli, expected results, negative effects and observable checks. Resolve material ambiguity through AIPF; distinguish requirement, assumption, suggestion and unknown. |
| QA-F04 | Test level and isolation | Select smallest sufficient unit, component, property, contract, integration, system or exploratory method. Distinguish mock, synthetic fixture, actual provider and observed runtime; retain meaningful integration coverage. No test pyramid quota. |
| QA-F05 | Boundary, property and state testing | Use relevant equivalence classes, limits, missing/null/zero/false/empty, invariants, invalid states and action sequences. Use reproducible generated counterexamples; protect unrelated behavior. |
| QA-F06 | Contracts and integration | Verify consumer/provider expectations, schema/serialization, error semantics, compatible versus breaking changes, dependency assumptions and actual interaction when required. Mock success is not provider proof. |
| QA-F07 | User-facing quality | Derive observable user outcomes, actual mutations, keyboard/focus and accessible semantics, loading/error/empty and responsive/long-text behavior as material. Distinguish computed contrast, static checks and observed rendering. |
| QA-F08 | Controlled failure and concurrency | Design bounded deterministic delay, timeout, duplicate, stale/out-of-order response, cancellation and partial failure scenarios. Verify recovery, idempotency and no extra writes or silent loss. No live chaos testing without separate authority. |
| QA-F09 | Diagnosis and reproduction | Capture exact failing stimulus, source, environment, expected/observed, causal hypothesis and next discriminating observation. Distinguish code/test/data/timing/dependency/configuration/infrastructure faults; honor AIPF diagnostic breakpoint. |
| QA-F10 | Correction and regression | Preserve original failure identity and reason; demonstrate material fail-before/pass-after where required/feasible; verify affected and unrelated invariants. Changed oracle, silent skip or unrelated environment repair is not a demonstrated fix. |
| QA-F11 | Differential verification | Pin baseline and candidate plus parity inputs when comparison changes a decision; judge absolute acceptance independently; classify improved, regressed, equivalent valid/invalid, approved intentional change or incomparable. Unchanged failure is not a pass. |
| QA-F12 | Test effectiveness | Assess assertion sensitivity, oracle independence, defect detection and coverage gaps; target meaningful mutant/counterexample. Distinguish killed, surviving, equivalent, invalid and untested mutations; no arbitrary score target. |
| QA-F13 | Flakiness and reliability | Separate deterministic failure, nondeterministic behavior and environment noise; control clock, random seed, state, order and readiness when suitable; retain intermittent failures and retries. No silent quarantine, retries or weakened checks to get green. |
| QA-F14 | Maintainability and critique | Identify actual duplication, unused logic, excessive complexity, suspicious imports, misleading tests and unnecessary abstractions. Inspect real use and counterevidence; prefer smallest complete correction, existing mechanisms or no change. No AI authorship judgment or LOC quota. |
| QA-F15 | Data and transformation quality | Verify relevant schema, types, units, missing/zero, duplicate/order, totals, reconciliation, rejection, round-trip/migration and partial writes. Distinguish data/model quality and drift; use authorized synthetic data. |
| QA-F16 | AI and agent evaluation | Assess outcome, constraints, tool permissions/target/arguments, causal prerequisites, contract drift, retrieval versus answer correctness and multi-turn behavior. Accept valid alternate paths; unauthorized action fails regardless of final text. |
| QA-F17 | Evaluation validity | Freeze material cases and gates; use reliable oracle or calibrated domain/model judge, disagreement/abstention, independent/held-out cases and repetition where warranted. Control model/config/task parity, report failures/denominators/uncertainty. No automatic prompt optimization or required comparative benchmark without a specific claim. |
| QA-F18 | Findings and evidence | Trace material finding to requirement, exact source or runtime, observation, impact and counterevidence. Distinguish confirmed defect, unresolved observation, rejected suspicion and optional improvement; propose proportionate next check/correction under existing AIPF evidence and status controls. |
| QA-F19 | Capability qualification and fallback | Compare no new tool, existing, local/self-hosted and hosted alternatives; qualify actual version/platform, rights, access, data, costs/limits and failure behavior. Missing guide/runner/observer remains explicit; do not fabricate or downgrade required evidence. |
| QA-F20 | Direct and distinct workflows | Direct agent uses current operational boundary without self-handoff. Prompt Agent distills material verification into canonical T1 payload with accessible inputs, no required governing-resource access for Builder; preserve evidence ownership and stop boundary. |
| QA-F21 | Multi-specialist composition | Synthesize material QA, Architecture, UI/UX and Security expertise once. Preserve requirements and trust/design boundaries; resolve material conflicts through AIPF, no duplicate governance or approvals. |
| QA-F22 | Compatible integration | Extend entry, registry, optional helper and shared knowledge index additively. Preserve three existing entries, versions/modes/results, framework bytes, catalog/retrieval, standing suite and recovery anchor. No new routing engine or required executable. |

### 3.1 Activation examples

| Actual request | Expected material consultation |
|---|---|
| Plan local CSV reconciliation with invalid and duplicate rows | Plan: data oracles, rejection, counts, protected output |
| Intermittent stale autocomplete after rapid input | Diagnose: causal order, deterministic reproduction, minimal correction |
| Candidate tests green but ownership or other negative effect untested | Review: assertion strength, counterexample and source-bound evidence |
| AI app with several legitimate tool paths | Plan/review: material constraints, actual action/target and causal gates |
| Substantial privacy-first dashboard redesign | Plan/review with UI/UX, Architecture, Security where material |
| Typo-only docs change or unrelated routine backend edit | Normally none; AIPF verification still applies |
| Missing required browser or reviewer | Disclose pending observation and request authorized feasible alternative, not qualification |

## 4. Knowledge architecture

### 4.1 Knowledge requirements

| ID | Requirement | Observable fulfillment / limits |
| --- | --- | --- |
| QA-K01 | Navigable original knowledge | Question-led offline index, stable decision IDs, progressive loading and working guide links. |
| QA-K02 | Conditional decisions | Each decision card gives actual question, applicability/exclusions, context, alternatives including no change, tradeoffs, counterexample, observables and source pointers. |
| QA-K03 | Coverage | All twelve decision families in Section 4.2 are covered with positive and negative guidance. Guide/card count is design discretion. |
| QA-K04 | Provenance | Author/project, URL, revision/edition or date, file/section, supported claim, rights and limits. Pin repository sources where possible. |
| QA-K05 | Primary sources | Verify decision-sensitive facts against authoritative source/docs; inspect implementation when necessary. Separate observed source from author benchmarks and runtime evidence. |
| QA-K06 | Volatile versus stable | Separate stable methods from versions, supported hosts, plans, prices, terms, features, retention and quotas; recheck at point of use. |
| QA-K07 | Rights and originality | Original synthesis; no wholesale imported third-party skills, prompts, code, fixtures, data or assets. Preserve notices and verify rights before reuse; unknown rights reference-only. |
| QA-K08 | Shared capabilities | Add only useful, qualified discovery records to existing independent capability index; preserve 24 existing entries and avoid duplicates or new tool directory/runtime. |
| QA-K09 | Examples and limitations | Show meaningful correct and faulty cases, false confidence, unavailable resources, counterevidence and interpretation limits. Label illustrations unexecuted. |
| QA-K10 | Deferred research continuity | Preserve 29 source IDs and 14 XR leads in pinned research; add later dispositions only under separate authorized decision. No backlog-to-requirement conversion. |

### 4.2 Decision families

All 12 families must be navigable; proposed filenames can be grouped or revised during design, without a fixed file/card count.

| Family | Candidate guide | Questions for decision cards | Discovery anchors |
| --- | --- | --- | --- |
| Risk and impact | risk-impact.md | Which changed and coupled contracts matter? What high-risk unchanged caller is affected? How use churn/co-change and handle shallow history? What can safely be omitted? | QA-S01,03,07 |
| Test design and oracles | test-design.md | Independent expected result, equivalence/boundary classes, decision tables, metamorphic relations, negative effects, intended failure reason and fixture validity. | QA-S03,24–26 |
| Unit, property and state | unit-property-state.md | Example versus generated invariant, explicit zero/false/empty, state transitions and sequences, deterministic clock/seed and counterexample minimization. | QA-S24,03 |
| Contracts and integration | contracts-integration.md | Consumer/provider, actual vs stub, serialization, schema evolution, dependency substitution, round-trip/migration and error semantics. | QA-S26,02,03 |
| Browser and UX | browser-ux.md | User journeys, semantic locators, readiness, keyboard/focus, actual rendering, accessibility, screenshots/DOM/network/state and responsive stress. | QA-S12,27,05,20,22 |
| Failure and resilience | failure-resilience.md | Timeout, partial completion, stale responses, duplicate events, cancellation, retry/idempotency, deterministic injection and cleanup. | QA-S05,03,24 |
| Diagnosis and regression | diagnosis-regression.md | Reproduction, causal hypothesis, minimal correction, fail-before/pass-after, differential parity, intermittent failure and stale evidence. | QA-S03,01,27 |
| Maintainability | maintainability.md | Actual duplication, complexity, unused paths, false-positive leads, smallest complete change, useful test seams and protected constraints. | QA-S06,07,09 |
| Data quality | data-quality.md | Schema/types/units, missingness, duplicates, totals/reconciliation, migration, model/data drift, privacy-preserving fixtures. | QA-S16,24,26 |
| AI and agent quality | ai-agent-quality.md | Outcome/authority gates, parameters, causal order, alternate valid paths, MCP drift, retrieval/answer, multi-turn state and evaluator validity. | QA-S02,04,08–11,13–15,28 |
| Test-suite effectiveness | test-effectiveness.md | Detect meaningful defect, independently authored oracle, weak and known-good suite, mutation classifications, flake, coverage limitations. | QA-S03,25,06 |
| Capability selection | capability-selection.md | No new tool/existing/local/hosted alternatives, version/platform/rights, actual costs/data access, failure and fallback. | QA-S02,04,12–18,22,24–29 |

The discovery anchors are not proof for every general method. B1/B2 must qualify relevant primary materials where decision-sensitive source support is incomplete, e.g. boundary/equivalence classes, decision tables, metamorphic testing and flaky-test handling. No invented source IDs, unqualified upstream content or benchmark claims.

### 4.3 Original decision card design

Each card uses stable QA-D identifiers and a concise question, applicability, exclusions, necessary context, alternatives and tradeoffs (including no change), counterexample, observable verification and source pointers/limitations. Index by question rather than source/tool. Load only relevant cards. No mandatory new report format or fixed number of cards. Illustrations are not executions.

- **Negative assertion:** For a rejected operation, if mutation is forbidden, assert pre/post state and absence of effect in addition to error. A generic exception from malformed setup does not prove resource authorization. Test the actual boundary with the smallest sufficient fixture; Security supplies the trust requirement. QA-S03/24.
- **Flaky browser:** Diagnose actual readiness, event order, request/state and reproducibility before extending a sleep. Prefer a bounded condition expressing observable behavior; do not change production timing solely to make a test pass. QA-S27/05.
- **Agent trace:** Match exact order only where the prerequisite or causal side-effect constraint requires it; extra authorized read may be valid, prohibited write fails even if final text matches. QA-S02/04; AIPF controls authority.
- **Test sensitivity:** Demonstrate a deliberately faulty implementation survives an inadequate assertion, then add a meaningful independent counterexample and establish the known-good implementation passes. A syntax error is not detection of the intended defect. QA-S03/25.

## 5. Integration and consultation

### 5.1 Proposed existing registry contract

After canonical AIPF routing, the agent judges material QA intent. Eligibility across paths is not automatic activation. Use current schema version 1; no helper change expected, confirmed at B1.

| Field | Proposed value |
|---|---|
| ID / version | `aipf-qa-engineering-quality` / `0.1` |
| Applicable paths | `chapters_any: [11,12,13,14,15,16,17,18,19,20,21]` |
| Skill | `skills/qa-engineering-quality/SKILL.md` |
| Task-to-mode | `qa-plan: plan`; `qa-diagnose: diagnose`; `qa-review: review` |
| Knowledge sources | `skills/qa-engineering-quality/INDEX.md`, `knowledge/capabilities/INDEX.md` |
| Tools / retrieval | `tools: []`; omit retrieval_script |
| Authority | Advisory; AIPF, approved requirements and current authorization govern |
| Purpose | Context-grounded test design, diagnosis, regression, test effectiveness and engineering-quality critique |
| Output | Risk-selected methods and observables, causal diagnosis, source-bound findings with limitations and relevant alternatives |
| Fallback | Disclose missing guidance/tool/source/observer; use sufficient verified context or qualified alternative only where adequate; stop affected work for material decision/observation gap |

Three modes are proposed: **plan** (strategy and testability), **diagnose** (reproduction and causal repair), **review** (test quality, evidence and candidate verification). Actual verification belongs in review only when authorized. A fourth verify mode is not justified yet. Reconsult when actual decision changes, not as an automatic sequence.

### 5.2 Mode inputs and outputs

| Mode | Inputs | Expected output |
|---|---|---|
| Plan | Approved behavior, constraints, risks, changed surfaces, architecture and actual feasible environment | Prioritized test levels, specific scenarios, independent expected effects, fixtures, observation/observer and limits |
| Diagnose | Exact failure, source/environment, expected invariant, prior attempts and actual logs | Falsifiable hypothesis, smallest meaningful reproduction, trace/counterevidence, probable vs confirmed cause, bounded correction and regression |
| Review | Exact candidate/source/test/fixture, requirements, raw observations and risks | Source-linked finding and impact, assertion adequacy, actual observed or missing evidence, proportionate next check and unresolved gaps |

Material facts missing remain explicit; no fabricated requirements, commands or results. Integrate outcomes into existing project/control records or T1; no new mandatory form.

### 5.3 Additive interfaces and fallback

Extend `skills/specialists.json`, `skills/praxis/SKILL.md`, `PRAXIS.md`, supporting docs and focused tests. Preserve the three entries exactly. Existing `scripts/praxis_context.py` resolves an explicit task and chapter intersection, verifies framework projection, and reports availability. It neither classifies natural language nor proves reading/application of the specialist. Illustrative invocation (not a command to run now):

```sh
python scripts/praxis_context.py --task qa-plan --chapter 11
python scripts/praxis_context.py --task qa-diagnose --chapter 12 --request "Reproduce stale result"
python scripts/praxis_context.py --task qa-review --chapter 15
```

Expected existing contract: `consult` and selected mode for available applicable skill, advisory_only; request with no retrieval yields `lookup_status: not_applicable`; missing skill yields specialist_unavailable, wrong selected chapter intersection recheck_framework_path; unknown/blank input errors as currently defined. No subprocess for QA. Do not reinterpret unknown tasks as skip; nonactivation is agent judgment. No Python or helper needed for direct file reading. Missing/corrupt framework is integrity failure, not license to invent governance. Use repository discovery/explicit entry; do not claim native discovery on untested hosts.

### 5.4 Execution models

Direct agent uses actual authorized operational boundary, no self-handoff. Prompt Agent derives canonical T1 with specific QA values, test cases/oracles, allowed commands/surfaces, accessible implementation inputs, evidence and stop; do not require Builder to read Praxis, AIPF, PRD, specialist or catalog. Optional access does not change authority. For the fresh independent exercise deliberately withhold governing resources and reviewer answers. Reconcile Builder report, source, reviewer execution and original/corrected evidence; preserve canonical B2 outcome and observer attribution. Distinct Builder cannot select subsequent work.

## 6. Verification, diagnosis and test effectiveness

### 6.1 Strategy and oracles

Start from intended observable behavior and affected boundaries, not number of tests. Identify coupled consumers, contracts, state and high-impact unchanged paths. Historical churn, co-change and bug mentions can prioritize inquiry, but shallow/squashed history, generated code, renamed files and sparse critical paths distort signals. Do not assess individual quality from commit counts.

Use lowest-cost sufficient method per claim: pure logic, actual state transition, contract, local integration, rendered browser, OS/runtime or named human observer. A critical boundary may need multiple levels because each proves different facts. Specify what mocks simulate and leave unknown. Prefer existing tests/tools. For material checks identify stimulus, expected result, negative effects, oracle, observer and source/fixture identity. Include explicit false/zero/empty distinct from absent/null, edge limits, invalid types, encodings, duplicate/order cases, state preservation and unchanged behavior where relevant. Test actual effect rather than status code, DOM presence, log message or a circular assertion.

Property-based tests require independent invariant, bounded generation and seed/minimized counterexample; state models require allowed/invalid transitions, repetition and reset. Data checks cover schema, units, totals, missingness, rejection, deterministic ordering/rounding, preservation and round-trip/migration only as required. Generated data by itself is not correctness evidence. Use synthetic or approved fixtures with controlling identity, not actual secrets/customer data.

### 6.2 Diagnosis and corrective regression

Retain exact baseline, command, fixture, configuration, platform/toolchain, failing output and expected invariant; reduce reproduction without removing causal condition. Form a falsifiable hypothesis and test a discriminating alternative. Separate observations from inferred causes; distinguish source, test, dependency, data, environment, timing and configuration faults. Use AIPF diagnostic breakpoint after unsuccessful same-family repairs or contradiction. Do not mutate speculatively.

Preserve original failure and diff. Demonstrate intended failure before and passing corrected behavior after where required and feasible, not unrelated import/syntax/timeout failure. If unable to reproduce, state limitation, not invented baseline. Protect unaffected invariants and run applicable standing regression. Do not weaken assertions, silently skip tests, change fixtures to exclude failures or treat retries as erasure of an observed defect.

### 6.3 Differential verification (CodeVetter-derived method)

When comparison changes a decision, freeze reference and candidate plus relevant dependency/configuration, data/auth state, scenario/seed, runtime, locale/timezone/viewport, oracle and measurement method. Determine absolute acceptance on each independently. Normalize only demonstrated incidental variation; retain raw and normalized evidence, transformation reason and relevant differences. If parity cannot be established, report separate observations without comparative confidence.

| Comparative description | Interpretation |
|---|---|
| Regressed | Previously acceptable behavior is now defective |
| Improved | Material baseline defect absent under comparable conditions; absolute checks still required |
| Equivalent valid | Matched behavior meets criteria on both; preservation bounded to observations |
| Equivalent invalid | Both fail; unchanged is not a pass |
| Intended change | Approved difference meets new criteria and protected behavior |
| Incomparable/inconclusive | Insufficient parity, execution, oracle or evidence; required next observation |

These are descriptive comparison results, not AIPF execution statuses. CodeVetter's current warm browser executor is no longer bundled; use its method, not a mandatory product dependency. QA-S03 records the precise pinned evidence.

### 6.4 Controlled failure, concurrency and flakiness

Use deterministic synthetic fixtures or explicit schedule/seed for timeout, out-of-order completion, delayed dependency, duplicate submit, cancellation, failure after uncertain commit, partial operation, retry and recovery. Check no extra transaction, stale overwrite, data loss or unauthorized effect; confirm correct visible error and recoverability. Include cleanup and preserved state. Do not run uncontrolled live faults or simulate success by bypassing actual boundary.

Retain first failure and every meaningful retry. Isolate time, random/order, shared state, resource contention, external dependency and weak oracle. Prefer condition-based readiness, bounded synchronization and per-test context. Repeated passing runs do not erase intermittent failures; quarantine or altered acceptance requires authorized reason and owner visibility.

### 6.5 Test-suite effectiveness and maintainability

A valuable suite distinguishes invalid from valid implementations. Demonstrate a deliberately faulty synthetic implementation surviving weak checks, stronger independent counterexample failing for intended reason, and known-good passing. Target meaningful mutants, distinguishing killed, survived, equivalent, invalid/unexecutable and untested. Surviving equivalent mutation is not proof of defect; no fixed coverage/mutation-score gate. Coverage locates gaps, not correctness.

Inspect actual use, reachability, complexity, tests and error paths. SynthScan labels its risk vectors heuristic and review-minutes estimate uncalibrated. Churn or coding style is a review lead, not AI authorship, quantified reviewer time or confirmed severity. Prefer existing mechanism, clear minimal complete change or no change; preserve security/accessibility/validation/readability. Less code is not a quality guarantee.

### 6.6 Findings and evidence

Material finding record: approved requirement or behavior, source/line or runtime reference, expected/observed, exact candidate/fixture, observer and evidence class, impact and scope, counterevidence, proposed next action/correction and actual disposition. Distinguish confirmed defect, unresolved lead, rejected suspicion and optional improvement as descriptive findings under existing AIPF evidence lifecycle and status vocabulary. No competing governance or labels. Report only supported observations; named observer feasibility remains separate from claimed outcome.

Untrusted code remains source-only unless effective authorized confinement established: disposable target, sanitized environment, no unauthorized network/credentials, read-only source/toolchain where appropriate, scratch-only writes, resource bounds and cleanup. Python/browser isolation alone is not OS sandbox proof. Returned logs, actual reproduction, source inference and operator attestation remain distinct. Required actual runtime/independent observation cannot be replaced by walkthrough.

## 7. AI, agent and instruction evaluation

This is applicable engineering knowledge for AI applications and actual Praxis representative behavioral qualification, not an autonomous evaluation platform, paid-model requirement or automatic AIPF prompt optimizer.

### 7.1 Evaluation dimensions

| Dimension | Observable test | Caveat |
|---|---|---|
| Outcome and constraints | Correct required output/values, source-supported claims, final state | Fluent or similar output is not correctness |
| Activation | Material selected expertise, unrelated nonactivation and fallback | Helper tests are deterministic explicit-ID tests, not reasoning |
| Tools/parameters | Allowed action and resource, forbidden call, typed argument, actual effect | Availability is not permission |
| Causal ordering | Approval, state and required prerequisite before dependent action | Accept alternate valid sequences unless order materially constrained |
| Contract drift | Removed tool, new required field, type/meaning change vs compatible addition | Schema pass not proof of safe semantics |
| Retrieval versus answer | Source relevance, identity and support; correct answer or abstention | Correct retrieval and correct answer are separate |
| Multi-turn state | Preserve roles, intent, constraints and stop across follow-up/repair | Observable action/state, not hidden reasoning |
| Robustness | Synthetic untrusted data, unavailable tool, malformed input or partial result | No universal security/injection claim |
| Semantic quality | Independent expert or calibrated judge; completeness, clarity, usefulness | No score overrides hard required controls |

A golden trace is an example of observed behavior, not required script. Compare materially relevant invariants and permitted alternatives. Record actual tool/operation result or state sentinel for claims requiring it, not merely self-reported behavior. Use synthetic fixtures and minimized/redacted event metadata, e.g. scenario ID, action class, approved resource alias, relevant args/result and configuration. No secret-bearing transcript, hidden chain-of-thought or default telemetry collection.

### 7.2 Evaluation validity and comparative method

Define hard correctness/authorization gates, cases, oracles, endpoints and hypotheses before results. Separate authored examples from held-out or independent cases; include known good, bad, ambiguous and unavailable cases. Prefer deterministic checks/domain reviewer when suitable. If model judge used, calibrate with examples, blind candidate labels and randomize order where useful; retain disagreement, abstention, invalid judgments, sample limits and shared-model biases. Do not equate ranking to correctness or ignore hard failures.

For a justified comparative claim, pin instructions/skill/model/config (host selection unknown if unavailable), fixture, evaluator, environment and relevant dependencies. Use paired tasks, fresh contexts, repeated runs when stochastic variation matters, report per-task results, uncertainty and denominators including refusal/timeout/failure. Measure total clarification/correction/verification effort, not output volume alone. Distinguish input, cached and output token costs with verified pricing/usage if claiming savings. No mandatory AIPF-only comparison or universal benchmark threshold.

### 7.3 Retained instruction research

GPT Prompt Engineer (QA-S08) provides prompt generation/pairwise Elo concept; Honey and Ponytail (QA-S09/06) document author-produced paired experiments with limited task/model/host scope and cache/cost issues; Auto-evaluator (QA-S10) separates retrieval and answer evaluation. Rhesis (QA-S11) links domain-expert feedback to test cases/agent versions. Adopt original evaluation literacy; retain prompt optimization as future XR-10 separate authority. No transferred benchmark savings, automatic rewrite, model provider choice or inferred notebook compatibility. The existing [Praxis prompt quality rubric](TESTING.md#evaluation-rubric) remains authoritative where applicable.

## 8. Capability and source qualification

### 8.1 Candidates

Discovery names are not selected/installed dependencies. Use the [shared capability index](../knowledge/capabilities/INDEX.md), compare no new tool, native/approved existing, local/self-hosted and hosted choices. Add only decision-useful records; no count gate.

| Candidate | Source IDs | Contribution | Proposed disposition / conditions |
| --- | --- | --- | --- |
| Playwright | QA-S12/27 | Browser/API interaction, isolation, traces | Candidate; exact browser/host/version/access and trace privacy. Existing optional Praxis browser test stays unchanged. |
| Hypothesis / Stryker / Pact | QA-S24–26 | Property/state, mutation and contract testing | Distinct candidates; exact language/runtime/rights/cost, actual test oracle and provider access. Native tests or hand-authored mutants may suffice. |
| EvalView / Promptfoo | QA-S02/04/28 | Agent behavior, contract diff, declarative assertions | Optional; EvalView source defaults telemetry on and installation ID; hosted/model paths and red-team/data handling need qualification. No paid/live test calls. |
| Rhesis | QA-S11 | Domain expert feedback, multi-turn case management | Optional when collaboration material; MIT core/enterprise and brand exceptions, hosted/SDK access, retention and cost. |
| Langfuse / MLflow / Opik | QA-S13–15/29 | Experiment, traces and operational monitoring | Overlapping alternatives; use existing tools first, no three integrations. QA + DevOps leads; exact deployment, licensing, data masking/retention, spend. |
| Deepchecks | QA-S16 | Data/model validation and drift | Reference/optional independent tool; AGPL and deployment obligations need review. No copying into Praxis. |
| Rainforest QA | QA-S22 | Commercial no-code test management | Alternative only; account/token, test data, run groups, plan, exit/maintenance cost. |
| CodeVetter | QA-S03 | Differential evidence and qualified task corpus | Method only initially: warm browser executor no longer bundled, repository-owned script and compatible lockfile required; platform and pnpm limits. |
| Chaos Frontend Toolkit | QA-S05 | Controlled failure ideas | Reference only; old randomized/global-patch implementation. Prefer existing deterministic test seams. |
| Codebase Recon / Ponytail / SynthScan | QA-S01/06/07 | Risk and maintainability | Original techniques only; no external skill/scanner or AI authorship claim. |
| GPT Prompt Engineer / Honey / Auto-evaluator | QA-S08–10 | Prompt variants, evaluation design, cost methodology | Reference; historical models, small/author-generated benchmark scopes, unknown Auto-evaluator license. No automatic instruction/governance rewrite. |
| Google DESIGN.md / Awesome DESIGN.md | QA-S19/20 | Design contract lint/diff and design references | XR-01/02, alpha specification, individual branding/asset rights; no required format or catalog import. |
| AgentDiff / Eleata Verify MCP | QA-S17/18 | Attribution and claim/evidence review | XR-07/08; hooks, prompt excerpts and remote refs; hosted evidence API and unverified Eleata license file. No hooks, MCP or provenance runtime. |
| AgentScope / Forgejo | QA-S21/23 | Agent architecture and forge/runner operations | XR-03/04; future authorized decisions only, no orchestration or hosting migration. |

### 8.2 Point of use

Apply existing [qualification guidance](../knowledge/capabilities/QUALIFICATION.md): actual needed behavior, workload, version/host, rights, commercial status, data flow/recipients/retention/export, runtime/network/credentials, access, price units, expected/peak usage, resets/exhaustion/overages, enforceable spend cap and migration/exit cost. Self-host is not automatically free/private; disabling telemetry does not prove no outbound traffic. Unknown facts remain unknown; provide qualified alternative or material decision gap. No test calls, integrations, provisioning, account creation, install or external data transfer authorized here.

### 8.3 Source and rights

The pinned [QA source register](../research/qa-engineering-quality/QA-SOURCE-REGISTER-01.md) records 29 distinct source IDs, 21 repository pins, inspected file blobs and observed docs. Root license inspection, metadata and declaration are different evidence strengths. Preserve author/project, URL, exact source/date, observed claim, rights/disposition and limits when writing original knowledge. Recheck current decision-sensitive facts. No blanket redistribution clearance, unknown license import, enterprise or brand asset reuse. Preserve [14 cross-specialist leads](../research/CROSS-SPECIALIST-RESEARCH-REGISTER.md) for concrete future decisions; no reopen or integration now. Forgejo upstream pin was not established; official documentation only.

## 9. Non-functional requirements

| ID | Requirement | Observable fulfillment / limits |
| --- | --- | --- |
| QA-N01 | Authority and safety | Advisory only; no independent acceptance, unauthorized tool calls, installation, real-data export, live probes, deployment or release. |
| QA-N02 | Portability and dependencies | Host/model neutral, file-based skill, no required QA executable, external browser package, API, paid model, service or skill; context-independent Builder. |
| QA-N03 | Privacy and safe evidence | Synthetic or minimal redacted inputs, no hidden reasoning or unrestricted transcripts; respect retention, authorization and isolation; no silent export. |
| QA-N04 | Proportionality and usability | Load material guidance only; use lowest-cost sufficient methods; no default exhaustive testing or benchmarks, repeated boilerplate or unnecessary specialist selection by user. |
| QA-N05 | Reproducibility and truthfulness | Exact relevant identity, environment, raw outcome, attribution and evidence purpose; distinguish source/inference/reported/observed; retain original failure. |
| QA-N06 | Maintainability | Stable IDs, navigable source-linked original guides, shared capability records, existing schema and focused tests. |
| QA-N07 | Protected baseline | Preserve framework, catalog/retrieval, existing specialist behavior, legacy outputs, Linux/native Windows standing suite and v1.2.0 tag. |
| QA-N08 | Bounded claims | No universal security/accessibility, all-host activation, AI authorship, certification, comparative superiority or numerical guarantee without actual applicable evidence. |
| QA-N09 | Source/rights integrity | Original synthesis, traceable provenance, rights/notice and current decision-sensitive facts; no unqualified redistribution; preserve research histories. |
| QA-N10 | Independence | Separate Builder, reviewer and direct observations, no simulated independent role, self-handoff or counting disposable tests as product regression. |

## 10. Acceptance criteria

All 18 proposed gates are required for technical qualification. Combine representative exercises only where actual evidence covers the same scope and identity; techniques within each are context-sensitive. Required actual observations cannot be replaced by hypothetical walkthroughs. Missing capability or independent observer blocks affected claim; preserve achieved evidence and assess canonical B2 outcome. No mandatory comparative AIPF-only benchmark, fixed new test count or numeric score waiver.

| ID | Criterion | Required observable evidence | Exercise families |
| --- | --- | --- | --- |
| QA-AC01 | Additive registry and helper | Mechanism tests for all three IDs/modes, applicable paths, missing/nonmatching path, unavailable skill, no lookup/subprocess, invalid/unknown/blank cases and unchanged legacy results. Preserve prior registry entries exactly. | QD07,QD12 |
| QA-AC02 | Semantic activation and fallback | Fresh actual observations for plan/diagnose/review and minor/unrelated nonactivation, missing guide and unavailable tool/host. Do not reveal expected classifications to observer beforehand. Helper output alone insufficient. | QD07 |
| QA-AC03 | Risk strategy and oracles | Actual direct planning observation: intended behavior, coupled surfaces, protected states, justified levels, exact inputs/expected and negative effects, capable observer and constraints. No invented requirement or forced tool. | QD09,QD11 |
| QA-AC04 | Boundary, state and contract | Execute synthetic relevant positive/negative and explicit zero/false/empty cases plus state transitions; actual local consumer/provider interaction, broken contract versus allowed compatible addition. Separate mock evidence. | QD02,QD03,QD04 |
| QA-AC05 | Diagnosis and differential | Retain flawed baseline, intended assertion failure, causal trace and minimal correction, corrected pass and unaffected invariant. Demonstrate equivalent invalid result and incomparable conditions are not acceptance. | QD01 |
| QA-AC06 | Test effectiveness | Material mutant survives weak suite; stronger independently authored check detects intended failure; known-good implementation passes. Separate equivalent/invalid mutant examples; no arbitrary mutation score. | QD02,QD10 |
| QA-AC07 | Failure, recovery and flake | Actual disposable deterministic delay/order/duplicate/partial failure checks; verify recovery and no unintended effects; retain schedule/seed and raw outputs. Demonstrate preservation of intermittent or failed observation, no production operation. | QD03 |
| QA-AC08 | Rendered user behavior | Actual local browser or capable assigned observer verifies interaction and keyboard/focus or responsive/error state plus observable effect. Separate mocked/API/static/rendered/accessibility scope. Unavailable observer is a required gap. | QD05 |
| QA-AC09 | Source-bound critique | Actual existing-system source review plus bounded confirmed defect, unresolved lead, rejected suspicion and optional improvement, with trace/counterevidence and real impact. Confirmed defect may be demonstrated separately on synthetic fixture; no fabricated product defect, execution or AI attribution. | QD06 |
| QA-AC10 | Data quality | Executed synthetic transformation/validation with duplicates, missing/zero/invalid rows, expected reconciliation and rejection; state preservation or round-trip when relevant; no real data export. | QD09 |
| QA-AC11 | Agent behavior and contracts | Actual bounded semantic observation: valid alternate path accepted, forbidden operation/target denied, causal prerequisite, parameter/schema drift, misleading untrusted data treated as data. Actual operation/sentinel or capable trace, not prose alone. | QD07,QD08 |
| QA-AC12 | Evaluation validity | Frozen example set, explicit gates and actual known-good/bad/ambiguous judgment or deterministic oracle, disagreement/abstention and retrieval/answer distinction; independent or separately observed checks where material. No invented metrics or paid benchmark requirement. | QD08 |
| QA-AC13 | Capability/source qualification | Actual point-of-use comparison of existing/local option and material external candidate; exact source/version/rights, platform, data/telemetry/access, cost/exhaustion and limits. Unknown remains unselected; no install or transfer. | QD06,QD11 |
| QA-AC14 | Direct and distinct Builder | Actual direct practical execution and actual fresh distinct Builder with complete authorized T1 and accessible scratch inputs only; independent reviewer inspects source identity, reproduces Builder tests and runs additional negative checks under effective safe confinement or assigned capable observer. Preserve original/corrected evidence and reconcile failures. | QD10 |
| QA-AC15 | Composition | Actual combined UI/UX, Architecture, Security and QA planning/review with coherent strategy or payload, concrete expected/negative outcomes, preserved privacy/design/contract constraints and no duplicated governance. | QD11 |
| QA-AC16 | Knowledge and provenance | Verify twelve families, question index, unique decision IDs, source/rights links, positive/negative advice, source fallback, preserved 29 source IDs and 14 XR leads, shared index and no unqualified import. | QD12 |
| QA-AC17 | Integrated regression | Exact candidate commit/tree, focused tests and full inherited 163 standing tests plus actual newly discovered cases on Linux and native Windows. Raw terminal outcome and environment; preserve framework/catalog/legacy behavior and prior tag. No silent skips or weakened assertions. | QD12 |
| QA-AC18 | Final reconciliation | Reconcile every QA-F/K/N and QA-AC against actual evidence, exceptions, observer, limits, recovery anchor and immutable candidate. Technical B4 pass only with required gates; otherwise canonical outcome. Owner acceptance and B5 separately authorized; validate consolidation/release tree and publication identity. | QD12 |

### 10.1 Evidence layers and measures

- Mechanism: registry/helper, index/source/rights and deterministic focused tests.
- Semantic: actual material consultation and nonactivation/fallback, composed guidance and authorized action; static text assertions are not agent reasoning evidence.
- Target behavior: actual authorized disposable test/renderer or named capable observer; exact source/fixture, raw outputs and intended failure reason.
- Independent workflow: actual fresh Builder report/source and reviewer independently executed negative checks, original/corrected identity and reconciliation.
- Integration and release: exact tree, full standing results per platform, preserved baseline, rights and owner disposition, published tag/release identity only when observed.

Track requirements with sufficient evidence or explicit gaps, actual positive/negative and no-effect checks, fail-before/pass-after and preserved behavior, test-effectiveness counterexamples, environment/observer and unresolved source/rights. Count suites separately: disposable tests are not standing product regression. No aggregate score, test count or prose fluency substitutes for required evidence.

## 11. Representative qualification exercises

Discovery QD01–QD12 retained and elaborated. All are proposed, unexecuted. Original disposable synthetic fixtures or scoped source review only; actual observation required where stated. Cases may be combined when coverage is equivalent, not removed by unsupported inference.

| ID | Scenario | Stimulus and expected behavior | Evidence |
| --- | --- | --- | --- |
| QD01 | Stale asynchronous result | Original disposable search lets older request A overwrite newer B. Controlled completion order B then A; final result must be B, stale completion ignored, single-request case preserved. Alternatively equivalent material predicate defect with causal trace. | Baseline intended assertion fails, diagnosis and source identity, minimal correction, corrected pass, preserved behavior. Test equivalent bad and incomparable cases separately. |
| QD02 | Weak suite and counterexample | Original transformer treats explicit false as absent; initially weak tests miss it. Independent check distinguishes false/zero/empty from missing; protects unrelated label behavior. Include equivalent and invalid mutant classifications. | Actual weak-suite pass, material mutant failure for intended reason after strengthening, known-good pass, counterexample and oracle. No LOC/coverage target. |
| QD03 | State and failure | Disposable in-memory operation processor: duplicate event, failure after effect, cancellation or retry with explicit controlled schedule. Check no double mutation, unrelated resource unchanged, correct failure/recovery, invalid transition denied. | Raw outputs, schedule/seed, state and negative-effect assertions, first failure/retry retained. No live fault injection. |
| QD04 | Consumer/provider contract | Local consumer and provider exchange expected fields/type; break required field/type, then add allowed optional field. Test both contract and real local interaction with explicit error behavior. | Broken contract intended failure, compatible case success, actual seam and mock limitations identified. |
| QD05 | Browser/UX | Disposable local form or dashboard: keyboard/focus, delayed or failed request, duplicate submission or long text, unsaved state if required, visible result and controlled underlying effect. | Actual rendered local observer with context/viewport and bounded trace/log; static and mock evidence separate. If unavailable, pending required observation. |
| QD06 | Existing-system critique | Read-only review of Praxis or authorized source: changed/coupled paths, actual complexity or test gap, potential heuristic lead; counterevidence, rejected suspicion, unresolved runtime claim and optional improvement. Missing-history fallback. | Source identity/locations, observed facts vs inferences, real impact. Confirmed defect can come from disposable fixture; no product defect invented, no source mutation. |
| QD07 | Activation, tool boundaries | Fresh agent requests for modes, minor/unrelated and unavailable guide; controlled synthetic tool schema/operation fixture: allowed alternate sequence, forbidden target, prerequisite, malformed argument/schema drift, retrieved instruction claiming authorization. | Actual semantic decisions, operation/sentinel or trace, contract change check, no unauthorized effect. Helper tests separate. |
| QD08 | AI evaluation validity | Frozen small set: valid, invalid and ambiguous answer; right retrieval but wrong answer; allowed alternative action vs forbidden action. Calibrate evaluator, retain actual disagreement or abstention and source/model unknowns. | Actual bounded judgments/oracle outcomes, identity and limits, no fictional cost/performance or mandatory external model call. |
| QD09 | Data integrity | Synthetic CSV-like import: duplicate ID, empty/missing vs zero, malformed row, expected count/totals, rejection and preserved good rows. Round-trip or partial-write recovery where relevant. | Actual logs, expected reconciliation, rejected input and no unintended effect. Also observe risk-led plan. |
| QD10 | Fresh distinct Builder | Empty scratch workspace; complete authorized local service or data processor task, including explicit negative-effect and invalid/duplicate behavior, test/evidence/stop constraints; no external service. Prompt Agent retains independent checks separately. | Returned source/hash, raw tests/env, actual independent reviewer reproduces and adds negative checks with safe confinement, preserves original and corrected artifacts; distinct from direct execution. |
| QD11 | Composition and alternatives | Privacy-first dashboard planning/review: user interaction, data contracts and trust requirements, actual observable QA checks, compare existing/no service and suitable optional candidate under concrete constraints. | Actual composed decision/payload, coherent four-specialist contribution, no conflicting scope, qualified capability facts and limitations. |
| QD12 | Integrated candidate | Readback index, provenance, rights, deferred leads, registry and exact delta; run focused and full standing regression on Linux and native Windows; reconcile requirements, observer evidence and source identity. | Exact candidate/tree, raw results, ledger and B4 disposition; no merge/tag before separate owner acceptance and B5. |

### 11.1 Independent execution and correction

Actual fresh Builder receives only canonical authorized T1 and accessible scratch implementation inputs, not reviewer answers or mandatory governing resources. Use an original bounded task; no real data, external service or production mutation. Reviewer compares source hashes, inspects boundary and oracle, reproduces submitted tests and authors independent negative checks with safe authorized execution. If effective confinement or observer unavailable, retain source evidence and mark required observation pending. Preserve original failure and corrected diff/source/raw outputs, rerun affected checks, assess B2. Same-agent direct fixture does not establish independence.

### 11.2 Exact integrated regression

Run `python -m unittest discover -s tests -v` on full exact candidate Linux and native Windows, plus required separate capable observer exercises. Standing 163 tests from v1.2.0 remain intact; actual discovered new count governs. Preserve command, raw logs, checkout SHA/tree, Python/OS, skipped/failure/warning reasons; no silent skip, reduced threshold or altered legacy test expectation. B5 consolidation creates a release-bound revision; verify exact prospective merge tree and relevant regression, reconcile actual main and existing CI policy before tag. Existing Windows job intentionally skips main pushes; transfer Windows evidence only with identical controlling tree/config and documented scope. No automatic workflow change.

## 12. Delivery and release

Proposed work breakdown aligned to existing AIPF B1–B5, not a new governance structure or granted authority. Owner approval and separate B1–B4 authorization required. No schedule or commitment to a release date.

| Stage | Planned deliverable and exit condition |
|---|---|
| B1 — Baseline/design | Reconcile v1.2.0 source, tag, PRD/research, actual registry/helper/capabilities, requirements, observer feasibility, source/rights and guide coverage. Confirm modes and material constraints; resolve decision-sensitive source gaps before design. |
| B2 — Knowledge/capabilities | Original SKILL, index, guides, cards and source register, selected shared discovery entries and examples. Preserve deferred research and rights; no code imports/dependencies. Assess execution using canonical Block B2. |
| B3 — Integration | Additive registry/entry/docs and focused tests; preserve three entries, helper and existing behavior. Verify exact source delta. No new required runtime. |
| B4 — Qualification | Immutable candidate/tree, all 18 criteria with actual evidence, direct and independent Builder/reviewer, preserved correction history, full cross-platform regression and individual requirements ledger. Stop at technically qualified candidate if gates met, otherwise canonical PARTIAL/FAIL/BLOCKED as applicable. No merge/tag/publication. |
| B5 — Release | Separate owner acceptance and release authority; consolidate approved PRD, verify source/rights/ID parity and version docs, release-bound delta and CI/reviews, merge main only after gates, reconcile actual tree and prior tag, publish new tag/release at verified commit. No further specialist work. |

### 12.1 Planned repository surfaces

| Surface | Treatment |
|---|---|
| skills/qa-engineering-quality/ | New SKILL, INDEX, SOURCES and original progressive guides |
| skills/specialists.json; skills/praxis/SKILL.md; PRAXIS.md; skills/README.md | Add material consultation and version guidance; preserve legacy IDs and behavior |
| knowledge/capabilities/ | Add useful original discovery records to existing groups/index/source register, preserve 24 existing entries |
| tests/ and scenario fixtures; docs/TESTING.md | Add focused mechanism/knowledge checks and scenario/qualification guidance; retain standing strategy and legacy assertions |
| research/ | Keep source/lead records and appropriate bounded qualification provenance; private evidence remains outside public redistribution |
| framework/, catalog/, scripts/, ui/, .github/, .agents/, licenses | Protected by default; no required behavior, runtime, CI or licensing change; material exception requires separate authorization |
| B5 docs/PRD.md and release docs | Proposed PRD v1.4 Section 14, original stable IDs and historical pin, README/changelog/release record and links; retire temporary active PRD |

### 12.2 Risks and mitigations

| Risk | Mitigation |
|---|---|
| Duplicate governance | Advisory only, existing AIPF controls and T1; reject extra approval/runtime |
| False confidence | Negative effects, meaningful mutants, independent oracles, preserve failures and gaps |
| Overfit to trace or benchmark | Material constraints, valid alternate paths, held-out cases, actual oracle and hard gates |
| Tool/dependency creep | Existing/native first, source/rights and point-of-use qualification |
| Misleading heuristic or judge | Counterevidence, calibrated/independent observation, abstention, no unsupported authorship or cost |
| Synthetic evidence overclaimed | Separate actual runtime, mock, source, reported and independent evidence |
| Unsafe execution/data | Bounded authorized disposable confinement; source-only when insufficient; no unauthorized export |
| Cross-platform or observer unavailable | Named capable observation required, retain partial evidence and stop dependent qualification |
| Stale provider/license facts | Pinned provenance, recheck material facts; unresolved rights reference-only |
| Fragmented requirements | Consolidation at acceptance/release, immutable original and ID parity |
| Maintenance overhead | No fixed guide/tool/test-count target; minimal complete integration |

## 13. Traceability

### 13.1 Existing requirement crosswalk

| Baseline obligations | QA extension |
|---|---|
| PR-01–03 entry, AIPF, project requirements | QA-F01/03/20/22, QA-N01/07; no duplicate governance |
| PR-04–06 activation and knowledge | QA-F01/19/22, QA-K01–09 |
| PR-07–09 direct/distinct, evidence | QA-F09–13/18/20, QA-N05/10, QA-AC05–07/14/17 |
| PR-10–11 extensibility/discovery | QA-F22, QA-AC01/02 |
| PR-12 and PR-14 future plugin/assurance | Deferred, no packaging or Review Parity |
| PR-13 engineering expansion | Proposed QA v0.1; preserve roadmap and future DevOps |
| KI-01–08 | QA-K01–10 and QA-F19; original progressive guides/shared capabilities and fallback |
| NFR-01–10 | QA-N01–10, all baseline attributes preserved |
| Architecture, Security and UI/UX requirements | QA-F02/06/07/08/15/18/21 and QA-AC08/15/17; verification complements protected domain constraints, no behavior/retrieval/catalog change |

### 13.2 Individual requirement-to-acceptance matrix

| Requirement | Primary acceptance criteria |
| --- | --- |
| QA-F01 | QA-AC01, QA-AC02 |
| QA-F02 | QA-AC03, QA-AC09 |
| QA-F03 | QA-AC03, QA-AC04, QA-AC06 |
| QA-F04 | QA-AC03, QA-AC04, QA-AC08 |
| QA-F05 | QA-AC04, QA-AC06, QA-AC10 |
| QA-F06 | QA-AC04, QA-AC11 |
| QA-F07 | QA-AC08, QA-AC15 |
| QA-F08 | QA-AC07, QA-AC08 |
| QA-F09 | QA-AC05, QA-AC07, QA-AC09 |
| QA-F10 | QA-AC05, QA-AC06, QA-AC17 |
| QA-F11 | QA-AC05 |
| QA-F12 | QA-AC06 |
| QA-F13 | QA-AC07, QA-AC17 |
| QA-F14 | QA-AC09 |
| QA-F15 | QA-AC10, QA-AC15 |
| QA-F16 | QA-AC11, QA-AC12 |
| QA-F17 | QA-AC12 |
| QA-F18 | QA-AC05, QA-AC09, QA-AC14, QA-AC18 |
| QA-F19 | QA-AC02, QA-AC13 |
| QA-F20 | QA-AC14 |
| QA-F21 | QA-AC15 |
| QA-F22 | QA-AC01, QA-AC16, QA-AC17 |
| QA-K01 | QA-AC16 |
| QA-K02 | QA-AC16 |
| QA-K03 | QA-AC16 |
| QA-K04 | QA-AC13, QA-AC16 |
| QA-K05 | QA-AC13, QA-AC16 |
| QA-K06 | QA-AC13, QA-AC16 |
| QA-K07 | QA-AC13, QA-AC16 |
| QA-K08 | QA-AC13, QA-AC16, QA-AC17 |
| QA-K09 | QA-AC02, QA-AC06, QA-AC09, QA-AC11, QA-AC16 |
| QA-K10 | QA-AC16, QA-AC18 |
| QA-N01 | QA-AC02, QA-AC11, QA-AC14, QA-AC15, QA-AC18 |
| QA-N02 | QA-AC01, QA-AC13, QA-AC14, QA-AC17 |
| QA-N03 | QA-AC07, QA-AC10, QA-AC11, QA-AC13, QA-AC14 |
| QA-N04 | QA-AC02, QA-AC03, QA-AC12, QA-AC15 |
| QA-N05 | QA-AC05, QA-AC07, QA-AC09, QA-AC12, QA-AC14, QA-AC17 |
| QA-N06 | QA-AC01, QA-AC16, QA-AC17 |
| QA-N07 | QA-AC01, QA-AC15, QA-AC17, QA-AC18 |
| QA-N08 | QA-AC08, QA-AC09, QA-AC11, QA-AC12, QA-AC18 |
| QA-N09 | QA-AC13, QA-AC16, QA-AC18 |
| QA-N10 | QA-AC14, QA-AC17, QA-AC18 |

This is planned traceability, not completed evidence. B4 ledger expands each acceptance criterion and requirement into actual source/observer references, achieved evidence, gaps and disposition.

### 13.3 Research and decision sources

| Area | Basis and scope |
|---|---|
| Integration/governance/portability | [Product PRD](PRD.md), [DEC-002](decisions/PRAXIS-DEC-002-builder-context-independence.md), [DEC-003](decisions/PRAXIS-DEC-003-quality-first-prompts.md), [DEC-004](decisions/PRAXIS-DEC-004-specialist-expansion.md), [testing](TESTING.md), [registry](../skills/specialists.json), [helper](../scripts/praxis_context.py), AIPF v8.10.1 |
| Risk and maintainability | QA-S01,06,07,09 — source and author-reported experiments, not demonstrated productivity |
| Differential/test effectiveness | QA-S03,24,25 — pinned method and official references; current CodeVetter warm executor unavailable; original fixture proposals |
| Contracts, browser, failure and design | QA-S02,05,12,20,22,26,27 — source/docs only, no actual hosted tool qualification |
| AI and evaluation validity | QA-S02,04,08–11,13–15,28 — techniques and author reports; no reproduced performance claims |
| Data/model quality | QA-S16,24,26 — rights and actual applicability must be qualified |
| Capability and cross-specialist retention | QA-S01–29 and XR-01–14, full [pinned source register](../research/qa-engineering-quality/QA-SOURCE-REGISTER-01.md), [cross-specialist register](../research/CROSS-SPECIALIST-RESEARCH-REGISTER.md) |

Discovery records control what was observed; this PRD proposes original requirements, modes, IDs and representative scenarios. Full code audit, runtime evaluation, benchmark reproduction, blanket license clearance and current service terms were not established in discovery. Further focused source review at B1/B2 only when material. Prior attachments not available can be re-provided if they change a decision; do not invent missing historical evidence.

## 14. Owner review and stop boundary

| Decision | Recommendation | Alternative / implication |
|---|---|---|
| Product version | Praxis v1.3.0; QA v0.1; AIPF unchanged | Defer/narrow if desired; no framework or other specialist change |
| Modes | Plan, diagnose, review, actual verify in review when authorized | Fourth verify mode only with distinct material value |
| Coverage | All 12 families, conventional software QA plus data/AI, conditional selection | Narrow only by explicit owner decision; no fixed card count |
| Integration | Existing schema/helper and file-based guidance | New runtime or platform not proposed |
| Qualification | Actual direct and distinct Builder/reviewer, defect-sensitive tests, rendered observer and full cross-platform regression | Missing required observer remains open; do not substitute hypothetical success |
| Instruction improvement | Include evaluation literacy; preserve XR-10 for separate research | No automatic optimization or mandatory benchmark |
| Other specialists | Preserve all deferred leads; revisit when concrete decision warrants | No additional specialist or Review Parity now |
| Documentation | Temporary PRD v1.0; consolidate into canonical PRD at acceptance/release | Preserve original approved revisions and all IDs |

Owner may approve, revise, narrow or defer this proposal. Requirements approval does not by itself authorize B1–B4. Recommended next authorization: develop and qualify QA & Engineering Quality v0.1 under AIPF v8.10.1, target Praxis v1.3.0, stop at technically qualified immutable candidate and reconciled raw evidence; no merge/tag/publication, deployment, new service or future specialist implementation. B5 requires owner acceptance and separate release authorization.

**Current stop:** detailed proposed QA PRD for owner review. No QA skill, registry entry, dependency, test execution, integration or release is authorized or implemented by this planning artifact. Preserve v1.2.0, AIPF and cross-specialist research.
