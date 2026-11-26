# Diagnosis and regression

Original conditional QA guidance. Examples below are illustrative, not executed qualification. Source IDs resolve via [SOURCES](../SOURCES.md); use current official evidence for material volatile facts. AIPF and approved requirements govern.

## QA-D19 — How do I find the actual cause?

**Applicability / context:** Observed failure with uncertain code, test, data, environment or dependency cause.

**Decision and alternatives:** Freeze exact source/config/fixture, reproduce failing assertion and reduce stimulus without losing cause. Form competing falsifiable explanations and choose one discriminating observation (trace, controlled input, known-good environment). Honor diagnostic breakpoint under AIPF, no speculative multi-fix. If reproduction unavailable, report unknown.

**Counterexample:** Changing app code when fixture uses stale schema makes tests pass for wrong reason.

**Observable verification:** Record failing output and actual cause evidence, compare one changed variable; distinguish hypothesis from confirmed cause. Verify minimal correction and unaffected behavior.

**Sources and limits:** QA-S03, QA-S32. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D20 — When is candidate comparison meaningful?

**Applicability / context:** A regression or improvement claim changes a decision; no obligatory paired experiment for every test.

**Decision and alternatives:** Pin baseline and candidate plus relevant dependencies/config, scenario/seed, data, runtime, oracle and environment. Test absolute criterion independently. Normalize only incidental IDs/time if irrelevant and retain raw values. Classify regression, improvement, equivalent valid/invalid, approved intended difference or incomparable; no baseline equality waiver.

**Counterexample:** Both implementations drop explicit zero, so identical output is equivalent invalid.

**Observable verification:** Show original intended failure and corrected pass, protected behavior, parity or why not comparable. Different fixture/versions may invalidate relative claim; no claim beyond observed tests.

**Sources and limits:** QA-S03, QA-S09. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D21 — What evidence establishes a correction?

**Applicability / context:** Material defect and accepted expected behavior; target-controlled execution separately authorized.

**Decision and alternatives:** Retain original source/fixture/raw failure, specific cause and smallest complete correction. Use same meaningful oracle, rerun relevant negative and positive plus preserved path, then required full suite. No weakened test, changed expectation or hidden skipped case. Reuse unaffected prior evidence only with identity/scope justification.

**Counterexample:** Baseline test fails from import error; later fix installs dependency, not behavior.

**Observable verification:** Ensure baseline fails for intended reason, correction passes same assertion and unaffected invariant. If not feasible, report exact gap; preserve original report and corrected identity.

**Sources and limits:** QA-S03, QA-S25, QA-S33. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

