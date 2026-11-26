# Maintainability

Original conditional QA guidance. Examples below are illustrative, not executed qualification. Source IDs resolve via [SOURCES](../SOURCES.md); use current official evidence for material volatile facts. AIPF and approved requirements govern.

## QA-D22 — Is apparent duplication an actual quality problem?

**Applicability / context:** Source review, complexity or repeated code; no broad rewrite from heuristic signal.

**Decision and alternatives:** Trace callers, invariants and reasons for divergence; compare existing helper, local clearer code, no change or abstraction only where common contract and maintenance benefit established. Preserve security/accessibility/error handling. No LOC quota.

**Counterexample:** Two superficially similar validators differ in resource authority; merging them could weaken trust boundary.

**Observable verification:** Show actual duplication/maintenance impact and affected paths, negative cases and expected behavior; reject suspicion if contexts differ.

**Sources and limits:** QA-S06, QA-S07. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D23 — How should heuristic findings be treated?

**Applicability / context:** Churn, static flags, suspicious imports or AI-like style from reviewed source.

**Decision and alternatives:** Use signal to select an inspection. Check reachable usage, build/config, source history and counterexample; classify confirmed defect, unresolved observation, rejected suspicion or optional improvement. No author attribution, automatic severity or uncalibrated effort estimate.

**Counterexample:** An apparently unused import has registration side effects, or generated code duplicates intentional data.

**Observable verification:** Trace actual call/use and source identity; confirm behavior only with appropriate evidence, retain rejected lead and limitations.

**Sources and limits:** QA-S01, QA-S07. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D24 — Does simpler implementation mean better quality?

**Applicability / context:** Candidate has unnecessary layers or test-specific complexity; avoid cosmetic churn.

**Decision and alternatives:** Compare simplest complete approach and existing mechanisms to actual requirements. Keep useful seams, clear responsibilities and meaningful checks. Refactor only where concrete benefit and authority; no change when current design sufficient. Prefer fewer dependencies over clever but fragile substitutions.

**Counterexample:** Removing checks to reduce line count loses malformed-input handling; a small diff can preserve a bad abstraction.

**Observable verification:** Test real public contract and adverse states, independently inspect readability and boundary preservation; no claim of measured productivity from upstream benchmarks.

**Sources and limits:** QA-S06, QA-S09, QA-S03. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

