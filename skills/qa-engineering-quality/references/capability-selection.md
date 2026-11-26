# Capability selection

Original conditional QA guidance. Examples below are illustrative, not executed qualification. Source IDs resolve via [SOURCES](../SOURCES.md); use current official evidence for material volatile facts. AIPF and approved requirements govern.

## QA-D35 — Do we actually need another test tool?

**Applicability / context:** Material test capability gap or external service proposal; existing tool usually sufficient.

**Decision and alternatives:** Identify required observation, existing framework and manual/local alternatives, actual version/platform, runtime/access and ownership. Compare no new dependency, existing, local and hosted. Qualify rights, data paths, telemetry, plan/spend/exhaustion and operational failure before selecting. No install or connection from advice.

**Counterexample:** Hosted evaluator would export sensitive prompts while local deterministic assertions meet gate.

**Observable verification:** Document source-linked decisive facts and unknowns, select compatible existing alternative or identify decision gap. No guaranteed free operation.

**Sources and limits:** QA-S12, QA-S27, QA-S28, QA-S29, QA-S33. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D36 — When is a browser, generator or mutation framework warranted?

**Applicability / context:** Test seam/coverage need exceeds native tools; not every project needs a framework.

**Decision and alternatives:** Browser automation for actual interactions, property/state generator for complex domains, mutation tool for material assertion gaps, contract tool for cross-boundary expectations. Use existing local/manual, explicit sequence or hand mutant first. Qualify exact version, license, platform, availability, execution effects and CI time; no mandatory selection.

**Counterexample:** Using remote browser to check pure arithmetic adds exposure/cost without evidence gain.

**Observable verification:** Compare feasible existing direct observations and alternative limitations; if no suitable renderer, assign required observer rather than claim screenshot or source proof.

**Sources and limits:** QA-S12, QA-S24, QA-S25, QA-S26, QA-S27. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D37 — How do I qualify AI evaluation or observability tools?

**Applicability / context:** Material AI test or operational trace question; no trace collection as default.

**Decision and alternatives:** Compare existing structured test events versus EvalView/Promptfoo or overlapping Langfuse/MLflow/Opik/Rhesis. Determine exact tool version, allowed providers/inputs, data/telemetry/retention, rights, account and usage/spend/exhaustion. EvalView pinned configuration defaults telemetry on; CodeVetter warm browser executor unavailable at its pin. Unknown outbound/access/cost means unselected. Do not infer offline from telemetry toggle.

**Counterexample:** A trace tool stores prompt excerpts remotely or a model judge makes paid calls despite local CLI.

**Observable verification:** Use original deterministic checks or qualified local alternative; record source claim, actual/unknown behavior, no new accounts, network or installation. Keep DevOps and Review Parity leads deferred.

**Sources and limits:** QA-S02, QA-S03, QA-S04, QA-S11, QA-S13, QA-S14, QA-S15, QA-S28, QA-S29. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

