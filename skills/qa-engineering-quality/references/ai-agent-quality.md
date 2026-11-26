# AI and agent quality

Original conditional QA guidance. Examples below are illustrative, not executed qualification. Source IDs resolve via [SOURCES](../SOURCES.md); use current official evidence for material volatile facts. AIPF and approved requirements govern.

## QA-D28 — Which agent actions are actually constrained?

**Applicability / context:** Material AI workflow, tool use, agent acceptance; canonical authority stays with AIPF.

**Decision and alternatives:** Define approved action class, target, argument schema, prerequisites, permitted alternatives, negative effects and actual outcome. Compare material causal order, not full golden trace. Inspect contract changes separately from semantic or authorization. If actual trace unavailable, do not infer behavior from prose.

**Counterexample:** Different authorized read order produces same correct result; forbidden write followed by correct text is still failure.

**Observable verification:** Observe action/sentinel or tool trace for allowed alternative, prohibited target, missing prerequisite, malformed args and incompatible schema; no hidden reasoning collection.

**Sources and limits:** QA-S02, QA-S04. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D29 — How should retrieval and answer quality be separated?

**Applicability / context:** RAG, source-grounded specialist or tool-result answer; no mandatory model provider.

**Decision and alternatives:** Freeze source/version and cases with known supported, unsupported and ambiguous outputs. Check retrieval relevance and supported answer separately, require correct abstention when evidence missing. Domain expert or deterministic check where possible; compare judge on calibrated controls if needed.

**Counterexample:** Correct document retrieved but answer invents a value; answer correct by chance despite wrong retrieval.

**Observable verification:** Record retrieval identity and actual answer/verdict independently; retain invalid/ambiguous/abstained cases, disagreements and unknown model selection.

**Sources and limits:** QA-S10, QA-S11, QA-S04. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D30 — When is comparative evaluation justified?

**Applicability / context:** Only a real decision or performance/cost claim warrants repeated paired tests.

**Decision and alternatives:** Predefine hard correctness/authority gates, task-paired reference/candidate, frozen and held-out cases, config/model/evaluator/seed or unknowns. Use fresh contexts, repeated samples if stochastic, blind labels/order when material; report all denominators and uncertainty, failures and total clarification/correction/verification effort. Never auto-rewrite AIPF.

**Counterexample:** A shorter prompt wins pairwise rating but loses required authorization; cached tokens are compared with uncached runs.

**Observable verification:** Calibrate judge against good/bad/ambiguous, abstain on disagreement as appropriate; exclude failed hard gates from ranking. No claimed savings without exact usage/pricing.

**Sources and limits:** QA-S08, QA-S09, QA-S06, QA-S11. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D31 — How do I test multi-turn and untrusted inputs?

**Applicability / context:** Agent follow-up, missing tool, retrieved instruction or state drift; synthetic authorized test only.

**Decision and alternatives:** Specify preserved roles, allowed actions, exact state transitions and stop boundary across turns. Treat retrieved content as data; verify denied unauthorized requests and continued authorized task. Use minimal redacted event metadata. If separate capable agent unavailable, note gap rather than simulate independence.

**Counterexample:** Retrieved text claims owner approval and asks agent to export record; text answer says no but actual tool writes.

**Observable verification:** Compare sentinel/effects, actual calls, valid alternative and missing capability fallback; distinguish source, deterministic dispatcher and actual agent observation.

**Sources and limits:** QA-S02, QA-S04, QA-S28. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

