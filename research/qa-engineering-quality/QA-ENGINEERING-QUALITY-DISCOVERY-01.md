# Praxis — QA & Engineering Quality discovery checkpoint 01

Date: 2026-11-26. Status: research and proposed direction only. Owner authorized deeper research and retention of cross-specialist leads; no QA requirements approval, implementation, dependencies, live testing, integration, merge, release or AIPF modification authorized. Proposed product target v1.3.0 / specialist v0.1 remains for owner review. Baseline: released v1.2.0, commit `93da10c375b11d4f1172d9cb248b76a0fd2487d4`, tree `fdeba1d234c4825dab8b9a210910657bdcb65c20`; AIPF v8.10.1, three released specialists, 24 shared capability records, 163 standing regression tests. See [canonical PRD](../../docs/PRD.md), [test strategy](../../docs/TESTING.md), [source register](QA-SOURCE-REGISTER-01.md), [cross-specialist backlog](../CROSS-SPECIALIST-RESEARCH-REGISTER.md). This report is advisory, not a second governance or requirement home.

## 1. Decision and findings

QA contributes *how to establish and improve software quality* before, during and after implementation, while AIPF already governs authorization, evidence, acceptance, state and release. Avoid building a platform for test orchestration or a parallel evidence lifecycle. The specialist should be useful even without optional tools; it should improve actual verification decisions and portable instructions, not merely advise writing more tests.

The user list resolves into four related but distinct purposes: test application behavior; determine whether tests detect meaningful failures; evaluate AI/agent behavior; and compare/test tools or methods. A single score cannot safely substitute for these purposes. Existing Praxis regression and frozen UI retrieval experiments already establish a useful basis for scenario-driven evaluation. Prior 163/163 regression is historical baseline evidence, not evidence of the future specialist.

### Highest-impact source findings

| Source | Observed source mechanism | Proposed original Praxis technique | Boundary / counterexample |
|---|---|---|---|
| CodeVetter QA-S03 | Paired executions against immutable reference and candidate; explicit regressed/improved/equivalent/incomparable distinctions; current warm executor unavailable in product bundle | Compare the same critical behaviors with normalized, matched conditions; qualify task fixtures by demonstrating failure before and success after; retain independent oracles | Equivalent bad behavior is still bad. A changed fixture, dependency, data state or runtime may make comparisons incomparable. Do not depend on the warm bridge, macOS UI, pnpm or upstream runner. |
| EvalView QA-S02 | Diff engine compares tool order, params, output and scores; MCP schema comparison is separate; trace contract records execution context | Compare permitted actions and material outcomes against accepted behavior; distinguish contract drift from policy violation or benign path change | Tool name equality is not authorization. Alternate valid paths must pass; an exact sequence is required only if causal/order constraints matter. Default telemetry and trace contents need qualification. |
| Playwright QA-S12/27 | Official guidance uses isolated browser contexts, resilient locators, awaited behavior and traces | Verify actual user-visible state, requests, mutations, focus, accessibility and recovery at meaningful boundaries; collect diagnostic traces only as useful | Mock data success does not prove backend or actual platform; a snapshot cannot prove keyboard behavior or complete accessibility. |
| Codebase Recon QA-S01 | Git history scale calibration, churn/co-change, bug-related commits, ownership/activity | Prioritize review on changed and coupled contracts, critical flows, recurring failure locations; combine history with actual call/dependency analysis | New or shallow repo, squash history, generated files, renames, low-volume high-impact files; no personnel judgment from commit counts. |
| Chaos Frontend QA-S05 | Browser toolkit has randomized request delay, duplicate clicks, request failure, history changes, timer/localization experiments | Deterministic, bounded scenario injection with known seed or schedule, synthetic fixtures, explicit recovery assertions | No random uncontrolled production failures. A replayable injected timeout is not evidence of a real outage. Use existing test seams instead of importing old global patches. |
| Ponytail QA-S06 | Minimum complete solution; existing helper first; protect trust boundaries, callers, tests | Review unnecessary complexity and preserve behavior; small diff is a means, not a quality metric | Simpler abstraction can be warranted; never remove validation, data protections or adequate tests for fewer lines. |
| SynthScan QA-S07 | Source explicitly labels risk vectors heuristic; review-minutes estimate not calibrated | Distinguish lead from confirmed defect; inspect actual usage, requirements, counterevidence and impact | Style markers cannot identify AI authorship; repetitive defensive code may be intentional; no automatic rejection or invented cost. |
| Promptfoo QA-S04/28 | Declarative assertions and evaluations, custom graders; documented hosted paths | Explicit cases, typed deterministic checks, bounded semantic evaluation, per-criterion result and model/provider identity | Grader error is not a pass. Hosted generation, evaluation, red teaming and sharing may transmit data; no automatic red-team actions. |
| Rhesis QA-S11 | Documentation links domain-expert feedback to tests and producing version | Convert actual reviewed failures into durable acceptance scenarios; preserve disagreement and provenance | Expert feedback still requires applicable requirements; AI-generated expectations need checking. |
| GPT Prompt Engineer QA-S08 / Honey QA-S09 / Auto-evaluator QA-S10 | Alternative prompt generation, pairwise Elo, paired task comparisons and retrieval/answer separation | Only for a meaningful improvement question, compare frozen baseline and candidate using objective gates first, independent semantic review second and efficiency third | No automatic instruction optimization or rewrite of AIPF; small or biased case sets, self-judging, cache effects and outdated integrations limit claims. |

### Strong additions not in original list

- Hypothesis stateful testing (QA-S24): model operations and invariants across action sequences, e.g. create/revoke/retry/restore, instead of enumerating only happy paths. Property tests need a real oracle and reproducible counterexample; no random generation alone as correctness proof.
- Stryker (QA-S25): mutation tests deliberately introduce a defect and observe whether tests detect it. Surviving mutants expose possible gaps, but equivalent mutations and non-executable cases are distinct. Prefer small, material mutation checks over repository-wide score quotas.
- Pact (QA-S26): verify both consumer expectations and actual provider behavior; contract conformance complements integration and end-to-end coverage, not a replacement for all runtime tests.
- Additional proposed conventional topics: boundary-value/equivalence classes, decision tables, metamorphic relations, state-transition tests, error-path and race testing, flaky-test diagnosis, deterministic time/randomness, migration/reconciliation, fixture validity, environment compatibility, coverage limitations, exploratory user workflows. These are recommendations; detailed source curation is needed for decision-sensitive claims when authoring guidance.

## 2. Suggested specialist knowledge families

No fixed guide count or technology requirement. Organize around questions and observable outcomes, preserve existing PRD invariants.

| Family | Decision guidance | Candidate verification or failure example |
|---|---|---|
| Risk and impact | Determine changed surfaces and protected behavior, severity/likelihood and meaningful minimum coverage | High-impact unmodified caller is covered despite low churn |
| Test oracles and assertions | Select observable truth, positive/negative and boundary expectations, expected failure reason | Wrong return code or swallowed exception fails; meaningless assertion does not qualify |
| Unit, property and state | Select example-based, generated properties and transition sequences; isolate clock/RNG | Empty/zero/false, repetition, cancellation or reset preserves invariants |
| Contracts and integration | Provider and consumer, serialization/schema, mocks versus real fixtures, network assumptions | Removed required field breaks contract; compatible addition does not |
| Browser and UX | User journeys, keyboard/focus, viewport, semantic locators, actual render, visual diffs | Action both appears successful and performs correct state mutation |
| Failure and resilience | Deterministic failure, interruption, concurrency, retries, idempotency, rollback | Delayed old response must not overwrite latest state; duplicated event cannot double effect |
| Diagnosis and regression | Reproduce, isolate, compare baseline/known-good, classify flake vs source/fixture/env | Baseline fails for intended reason, correction fixes root cause and preserves other paths |
| Maintainability and simplicity | Identify actual complexity, unused behavior, misleading heuristics, scoped correction | Equivalent solution preserves interfaces; fewer lines cannot outweigh lost checks |
| Data quality and transformation | Schema, validity, missingness, duplicates, consistency, provenance, drift | Reconciliation detects incorrect totals or lost records; model/data drift is separate from ordinary code |
| AI and agent quality | Evaluate material semantics, tool permissions/contracts, retrieved knowledge, multi-turn state and judge limits | Allowed alternative path succeeds; forbidden action fails regardless of style or aggregate score |
| Test suite effectiveness | Mutant detection, counterexamples, coverage and test reliability, explicit gaps | Remove a critical predicate and require existing or independent tests to fail for the right reason |
| Capability selection | Existing tools/local alternatives vs hosted tools; limits, rights, privacy, cost, portability | Missing runner means unavailable evidence, not fabricated test success |

Proposed consultation modes for later design: **plan** (test strategy and acceptance implications), **diagnose** (reproduce and localize behavior), **review** (evaluate test and implementation evidence, find gaps and suggest proportionate next checks). Whether verify is a fourth mode or part of review is a B1 design choice. No task IDs or registry edits here. Consult only for material uncertainty or engineering value, not for every task mentioning testing; AIPF-required verification still applies independently.

## 3. Practical differential and defect-detection method

For an approved behavioral comparison, freeze reference, candidate, fixture, configuration, dependencies, environment, scenario and oracle. Verify relevant parity before comparing. Evaluate each side against the absolute acceptance criterion independently. Report candidate-only failure, fixed baseline failure, equivalent valid or invalid behavior, deliberate approved change, or inconclusive/incomparable. Preserve differences relevant to requirements; normalize only demonstrably incidental values (timestamps, run IDs, ephemeral ports) and document normalization. Do not mask actual user-visible changes or remove material failures from evidence. Baseline equality is not acceptance.

For a test-suite assessment, use an original deliberately flawed fixture and a known-good correction, verify the intended failure and success (not syntax/import failures), then add independently authored tests where required. Include negative assertions about no mutation/no disclosure/no extra effects. Cover at least one existing accepted invariant unrelated to the change. Run under bounded scratch-only execution with effective isolation for untrusted returned code, or source review only when isolation unavailable; use the existing AIPF/Security controls rather than new duplicate rules.

## 4. AI and instruction evaluation design

Useful for user applications containing AI and optional future Praxis improvement experiments. A golden trace is an example of observed accepted behavior, not a universal oracle. Prefer explicit structured assertions of allowed/forbidden action classes, resource constraints, expected final disposition, output completeness, decision-dependent ordering, actual outcome and evidence ownership. Record model/version or unconfirmed host selection, config, prompt/skill source, fixture and evaluator version. Do not require hidden chain-of-thought. Avoid collecting real secrets or unrestricted transcripts; synthetic fixtures, minimal redacted event metadata and explicit retention are sufficient for initial research.

If a comparison could change a specific decision: define hypotheses and hard gates before results; freeze tasks, rubric and baseline; hold out cases and retain negative controls; use fresh independent contexts and repeated runs when stochastic variance matters; blind candidate labels and randomize position for subjective grading; use objective checks or domain-expert review before relying on an LLM judge; calibrate judges with known good/bad/ambiguous examples, retain disagreement/abstention and coverage. Use task-paired summaries and uncertainty appropriate to sample size; record timed out or failed runs rather than silently excluding them. Evaluate total effort (clarification, repair, verification), not token volume alone. Do not rank failed correctness/authority gates using an average quality score. Benchmarking is justified only for a specific claim, not mandatory comparative admission.

Ponytail and Honey methodology offer useful designs (paired tasks, fresh contexts, multiple runs, costs by token class, known limitations). They are author-produced experiments with particular models, tools, task mix and restricted execution. Honey's reported handoff stratum is very small; no transfer of cost savings to Praxis or guarantee of quality. GPT Prompt Engineer's pairwise Elo can help prioritize compliant prompt variants but not establish correctness, independent review or authorization. Auto-evaluator illustrates why retrieval evidence and answer correctness need separate measurement. Current Praxis test and quality rubric remain authoritative.

## 5. Optional capability candidates

No selection, installation, hosting, account, telemetry, API calls or new dependencies approved. Compare existing unittest/browser tools and no added service first. Possible initial capability families, not fixed record count:
- Browser and API: Playwright; Rainforest as commercial no-code alternative (account, token, run groups, test data, price and maintenance qualification).
- Test-strength and contracts: Hypothesis, Stryker, Pact (ecosystem compatibility, version, rights, CI time, isolation).
- Agent evaluation: EvalView and Promptfoo; Rhesis where expert review/multi-turn testing is material.
- AI experiment/observability: Langfuse, MLflow, Opik as alternatives with substantial overlap; keep one suitable existing option where possible, no new mandatory service.
- Data/model quality: Deepchecks as reference/optional independent tool; AGPL and deployment implications require specific review.
- Heuristic review: SynthScan reference only initially; verify underlying code and actual impact, no detector claim.
- Reference only: CodeVetter methods, Chaos Frontend Toolkit, GPT Prompt Engineer, Ponytail, Honey, Auto-evaluator. Do not load third-party skills as governing instructions.

See source register for provenance and [shared qualification guidance](../../knowledge/capabilities/QUALIFICATION.md) for decision-sensitive access, terms, data, network, cost and failure behavior. No price/free-tier claim.

## 6. Candidate representative exercises for later PRD

These are proposed, unexecuted, synthetic or source-only. Combine with existing standing regression and independent Builder workflow proportionately; do not require every scenario independently if equivalent coverage is evidenced.

| ID | Purpose and observable gate |
|---|---|
| QD01 | Existing bug: reproduce a stale async response or missing ownership predicate; baseline fails expected invariant, fix passes, unrelated behavior unchanged. |
| QD02 | Assertion quality: known material mutant survives a weak suite; independent meaningful test kills it; distinguish equivalent mutant and environment failure. |
| QD03 | Resource/state transitions: duplicate request, revoke, retry and partial failure with synthetic data; verify idempotency and no unintended writes; retain seed/schedule. |
| QD04 | Consumer/provider contract: broken required field/type vs compatible additive change; test both sides and a meaningful interaction; mock-only limitation. |
| QD05 | Browser UX: keyboard focus, timeout recovery, unsaved data, long text, actual requests and state; isolated mock or actual local environment labeled. |
| QD06 | Repository impact and maintainability: read-only source review, distinguish measured facts from historical/heuristic leads, reject unrelated refactor; unavailable history fallback. |
| QD07 | Agent semantic behavior: material QA activation, unrelated/minor nonactivation, missing tool/source; valid alternative path and invalid unauthorized action; deterministic and semantic evidence separate. |
| QD08 | AI evaluation: frozen representative cases and a judge disagreement/abstention example, no fabricated performance result; compare only if decision requires it. |
| QD09 | Data integrity: duplicates, null/zero, malformed rows, transformation invariants and reconciliation, no real data export. |
| QD10 | Fresh distinct Builder receives complete authorized QA task and accessible implementation inputs only; reviewer executes independent checks when safe; preserve original/corrected identity and raw outcomes. |
| QD11 | Combined UI/UX, Architecture, Security and QA design/review: one coherent instruction or decision, actual protected invariants; do not duplicate governance. |
| QD12 | Integrated exact candidate standing regression on Linux and native Windows, focused new mechanisms, source/rights and requirement reconciliation; owner acceptance and release separate. |

## 7. Scope and unresolved decisions

- Research supports drafting the temporary QA PRD (proposed target v1.3.0), not its approval. Define SP-equivalent QA requirement/knowledge/NFR and acceptance IDs in that document, preserving prior IDs on later consolidation.
- Decide consultation modes and guide organization after requirements are explicit. No mandatory framework-only comparative study, benchmark runner, trace database, service or scanner.
- Separate cross-specialist research and AIPF/Review Parity evolution from QA v0.1. Keep future DevOps ownership of deployment and operational reliability. Security owns trust/privacy/authorization risk; QA supplies assertions and negative scenarios, not permission to probe.
- Prior QA research mentioned in DEC-004 may exist outside current repo; not all historical artifacts were accessible. Reconcile if provided and material; do not invent missing evidence. User attachments may expire.
- Full source audits and benchmark reproduction were not performed. Pinned excerpts and documented methods are observations of source, not proven runtime outcomes. No packages installed or external services invoked for tests. Source register tracks unverified rights and mutable official docs.

Discovery result: sufficient original synthesis and retained provenance for owner review of next planning step. Proposed PRD and implementation still require scoped authority. Stop at research checkpoint.
