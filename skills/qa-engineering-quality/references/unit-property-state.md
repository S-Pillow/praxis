# Unit, property and state

Original conditional QA guidance. Examples below are illustrative, not executed qualification. Source IDs resolve via [SOURCES](../SOURCES.md); use current official evidence for material volatile facts. AIPF and approved requirements govern.

## QA-D07 — When should I use examples or generated properties?

**Applicability / context:** Logic with many inputs, invariants or boundary combinations; avoid property framework if simple explicit tests suffice.

**Decision and alternatives:** Start with known examples and invalid cases. Add bounded generation for stable independent property; control seed and shrink counterexample while preserving cause. Reuse project-native tool or standard library first; qualify optional generator for target version/rights.

**Counterexample:** All generated amounts within one range never exercise missing or negative amounts; a tautological total assertion is meaningless.

**Observable verification:** Run examples plus selected generated cases with explicit expected invariants, include counterexample and replay value; report sampled scope only.

**Sources and limits:** QA-S24, QA-S30. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D08 — What state transitions need coverage?

**Applicability / context:** Resource lifecycle, retries, cancellation, reorder, reset or permission change.

**Decision and alternatives:** Map states and allowed actions, invalid edges and effects, model critical sequences and invariants. Test state after each transition rather than terminal status alone. Prefer deterministic sequence for known fault; generated sequence if broad state interaction material.

**Counterexample:** Revoke then update returns denial but note text changes; a final failure status hides the write.

**Observable verification:** Check initial/allowed/invalid/repeated transitions, negative mutation, independent resource and reset; preserve sequence or seed.

**Sources and limits:** QA-S24, QA-S30, QA-S03. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D09 — How do I control time, randomness and shared state?

**Applicability / context:** Tests depend on time/order/global state or platform; avoid mocking actual boundary whose behavior is claim.

**Decision and alternatives:** Inject narrow clock/randomness seams or deterministic completion order when already supported; create fresh test fixtures and clean up. Compare actual integration with controlled test. No global runtime patch unless isolated/authorized; don't change product semantics for tests.

**Counterexample:** Mocking all network and time removes the race being investigated.

**Observable verification:** Run known order A/B and B/A with expected effect; check cleanup, no extra effects; record seed/schedule and mock limits.

**Sources and limits:** QA-S24, QA-S27, QA-S32. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

