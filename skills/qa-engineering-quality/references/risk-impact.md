# Risk and impact

Original conditional QA guidance. Examples below are illustrative, not executed qualification. Source IDs resolve via [SOURCES](../SOURCES.md); use current official evidence for material volatile facts. AIPF and approved requirements govern.

## QA-D01 — Which behaviors need verification after a change?

**Applicability / context:** Plan/review material change to data, shared helper or user flow; trivial text-only edits need no extra strategy.

**Decision and alternatives:** Start from approved observable effects and preserved contracts. Map changed entry points to callers, shared state, error and recovery paths. Select high consequence even if unchanged source; retain accepted regression for affected paths. Choose targeted local checks versus broader integration when coupling is uncertain; no change if existing evidence covers exact state.

**Counterexample:** A low-churn currency formatter used by every invoice is more material than many generated-file edits.

**Observable verification:** Verify an unchanged caller with zero, normal and invalid input, and its actual effect. Trace one failure across caller/provider. Record uncovered surfaces and observer feasibility.

**Sources and limits:** QA-S01, QA-S03, QA-S30. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D02 — Can history help prioritize investigation?

**Applicability / context:** Read-only history available, repeated defects or uncertain coupling; do not use commit statistics to rate people.

**Decision and alternatives:** Review representative commit/rename history and co-change, compare actual current imports/callers and bug context. If shallow/squashed/generated history, limit claims and use source or runtime instead. No need to reconstruct history when source gives sufficient answer.

**Counterexample:** Two files co-change because a formatter runs globally, not because behavior is coupled.

**Observable verification:** Check actual data/control dependence and contrary examples; identify history span or absence. Treat churn as lead, not defect.

**Sources and limits:** QA-S01, QA-S07. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D03 — How much verification is sufficient?

**Applicability / context:** Choose among available unit, integration, rendered and human evidence for material risks.

**Decision and alternatives:** Assign each invariant an observable, feasible observer, expected effect and negative effect. Prefer smallest test that actually sees relevant boundary; combine levels for auth/data and UI effects. A current exact prior result can be reused when unaffected. Extra testing only if decision changes.

**Counterexample:** A mocked success confirms consumer UI logic but cannot prove the actual provider or database write.

**Observable verification:** Check distinct claims with suitable test seams and note unobserved host/runtime. Do not replace required evidence with a cheaper proxy.

**Sources and limits:** QA-S03, QA-S26, QA-S27. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

