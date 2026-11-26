# QA & Engineering Quality — question-led decision index

Select only material questions after canonical AIPF routing. Cards are original advisory guidance, not a required checklist or execution authorization. [Skill](SKILL.md) · [Source register](SOURCES.md) · [Shared capabilities](../../knowledge/capabilities/INDEX.md).

## Risk and impact

- [QA-D01 — Which behaviors need verification after a change?](references/risk-impact.md#qa-d01--which-behaviors-need-verification-after-a-change)
- [QA-D02 — Can history help prioritize investigation?](references/risk-impact.md#qa-d02--can-history-help-prioritize-investigation)
- [QA-D03 — How much verification is sufficient?](references/risk-impact.md#qa-d03--how-much-verification-is-sufficient)

## Test design and oracles

- [QA-D04 — What is a meaningful expected result?](references/test-design.md#qa-d04--what-is-a-meaningful-expected-result)
- [QA-D05 — Which inputs and rule combinations matter?](references/test-design.md#qa-d05--which-inputs-and-rule-combinations-matter)
- [QA-D06 — When can a relation replace an exact expected output?](references/test-design.md#qa-d06--when-can-a-relation-replace-an-exact-expected-output)

## Unit, property and state

- [QA-D07 — When should I use examples or generated properties?](references/unit-property-state.md#qa-d07--when-should-i-use-examples-or-generated-properties)
- [QA-D08 — What state transitions need coverage?](references/unit-property-state.md#qa-d08--what-state-transitions-need-coverage)
- [QA-D09 — How do I control time, randomness and shared state?](references/unit-property-state.md#qa-d09--how-do-i-control-time-randomness-and-shared-state)

## Contracts and integration

- [QA-D10 — Does a consumer test prove the provider?](references/contracts-integration.md#qa-d10--does-a-consumer-test-prove-the-provider)
- [QA-D11 — Is a schema change compatible?](references/contracts-integration.md#qa-d11--is-a-schema-change-compatible)
- [QA-D12 — What proves an integration or migration actually works?](references/contracts-integration.md#qa-d12--what-proves-an-integration-or-migration-actually-works)

## Browser and UX

- [QA-D13 — What should a rendered UI test observe?](references/browser-ux.md#qa-d13--what-should-a-rendered-ui-test-observe)
- [QA-D14 — How can browser tests survive legitimate UI changes?](references/browser-ux.md#qa-d14--how-can-browser-tests-survive-legitimate-ui-changes)
- [QA-D15 — What do screenshots and traces prove?](references/browser-ux.md#qa-d15--what-do-screenshots-and-traces-prove)

## Failure and resilience

- [QA-D16 — How do I inject failures without uncontrolled chaos?](references/failure-resilience.md#qa-d16--how-do-i-inject-failures-without-uncontrolled-chaos)
- [QA-D17 — What if a retry follows an uncertain commit?](references/failure-resilience.md#qa-d17--what-if-a-retry-follows-an-uncertain-commit)
- [QA-D18 — How do I diagnose stale results and flakiness?](references/failure-resilience.md#qa-d18--how-do-i-diagnose-stale-results-and-flakiness)

## Diagnosis and regression

- [QA-D19 — How do I find the actual cause?](references/diagnosis-regression.md#qa-d19--how-do-i-find-the-actual-cause)
- [QA-D20 — When is candidate comparison meaningful?](references/diagnosis-regression.md#qa-d20--when-is-candidate-comparison-meaningful)
- [QA-D21 — What evidence establishes a correction?](references/diagnosis-regression.md#qa-d21--what-evidence-establishes-a-correction)

## Maintainability

- [QA-D22 — Is apparent duplication an actual quality problem?](references/maintainability.md#qa-d22--is-apparent-duplication-an-actual-quality-problem)
- [QA-D23 — How should heuristic findings be treated?](references/maintainability.md#qa-d23--how-should-heuristic-findings-be-treated)
- [QA-D24 — Does simpler implementation mean better quality?](references/maintainability.md#qa-d24--does-simpler-implementation-mean-better-quality)

## Data quality

- [QA-D25 — How do I verify an import or transform?](references/data-quality.md#qa-d25--how-do-i-verify-an-import-or-transform)
- [QA-D26 — What should a migration or round trip preserve?](references/data-quality.md#qa-d26--what-should-a-migration-or-round-trip-preserve)
- [QA-D27 — When is data drift or model quality relevant?](references/data-quality.md#qa-d27--when-is-data-drift-or-model-quality-relevant)

## AI and agent quality

- [QA-D28 — Which agent actions are actually constrained?](references/ai-agent-quality.md#qa-d28--which-agent-actions-are-actually-constrained)
- [QA-D29 — How should retrieval and answer quality be separated?](references/ai-agent-quality.md#qa-d29--how-should-retrieval-and-answer-quality-be-separated)
- [QA-D30 — When is comparative evaluation justified?](references/ai-agent-quality.md#qa-d30--when-is-comparative-evaluation-justified)
- [QA-D31 — How do I test multi-turn and untrusted inputs?](references/ai-agent-quality.md#qa-d31--how-do-i-test-multi-turn-and-untrusted-inputs)

## Test-suite effectiveness

- [QA-D32 — Can the suite detect the defect we care about?](references/test-effectiveness.md#qa-d32--can-the-suite-detect-the-defect-we-care-about)
- [QA-D33 — What do mutant results mean?](references/test-effectiveness.md#qa-d33--what-do-mutant-results-mean)
- [QA-D34 — Can coverage or reruns establish confidence?](references/test-effectiveness.md#qa-d34--can-coverage-or-reruns-establish-confidence)

## Capability selection

- [QA-D35 — Do we actually need another test tool?](references/capability-selection.md#qa-d35--do-we-actually-need-another-test-tool)
- [QA-D36 — When is a browser, generator or mutation framework warranted?](references/capability-selection.md#qa-d36--when-is-a-browser-generator-or-mutation-framework-warranted)
- [QA-D37 — How do I qualify AI evaluation or observability tools?](references/capability-selection.md#qa-d37--how-do-i-qualify-ai-evaluation-or-observability-tools)

