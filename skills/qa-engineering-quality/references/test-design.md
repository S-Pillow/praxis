# Test design and oracles

Original conditional QA guidance. Examples below are illustrative, not executed qualification. Source IDs resolve via [SOURCES](../SOURCES.md); use current official evidence for material volatile facts. AIPF and approved requirements govern.

## QA-D04 — What is a meaningful expected result?

**Applicability / context:** When translating requirement to tests; no invented defaults for ambiguous acceptance.

**Decision and alternatives:** Define input/precondition, expected exact value or predicate, negative effect and oracle independent of implementation. Compare explicit expected data, known reference or actual state; avoid calling same function to compute expected. Select no additional oracle if already sufficient. Ask owner about material ambiguity.

**Counterexample:** A 200 response and success toast can coexist with zero committed rows.

**Observable verification:** Assert result and stored state, count and unaffected record. Rejected operation must preserve state; verify intended error not generic exception.

**Sources and limits:** QA-S03, QA-S33. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D05 — Which inputs and rule combinations matter?

**Applicability / context:** Boundary/equivalence, decision-table cases for constraints and branching; do not create exhaustive combinations when equivalent.

**Decision and alternatives:** Partition valid and invalid behavior, test actual boundary and closest meaningful values on either side; for combinations with different effects derive feasible rule rows. Include null, absent, empty, false and zero when distinct. Select representative pairwise/targeted combinations if risk permits, explicit full critical conditions where necessary.

**Counterexample:** An allowed size 1–80 accepts 0 or 81 due to off-by-one; checking length 40 alone misses it. False and absent may require different behavior.

**Observable verification:** Use subtests with named values and exact expected results; record valid/invalid rule and state/no-effect; do not claim all combinations.

**Sources and limits:** QA-S30, QA-S33. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D06 — When can a relation replace an exact expected output?

**Applicability / context:** Hard-to-enumerate result with independently justified relation; not substitute for known business oracle.

**Decision and alternatives:** Choose a meaningful relation over input transforms: order-insensitive totals unchanged by permutation, adding a known valid item changes total by its amount, normalization idempotent when specified. Confirm relation is required, not assumed. Pair with direct examples and negative cases. No relation when transformation changes intended semantics.

**Counterexample:** Sorting a list twice can still consistently drop items; idempotence alone misses loss.

**Observable verification:** Check multiset preservation as well as order, original and follow-up cases, exact baseline known cases and counterexample. Retain input/transform/outputs.

**Sources and limits:** QA-S31, QA-S24. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

