# Browser and UX

Original conditional QA guidance. Examples below are illustrative, not executed qualification. Source IDs resolve via [SOURCES](../SOURCES.md); use current official evidence for material volatile facts. AIPF and approved requirements govern.

## QA-D13 — What should a rendered UI test observe?

**Applicability / context:** Material user journey or UI behavior; UI/UX supplies approved design, Security supplies trust rules.

**Decision and alternatives:** Choose a critical journey, stable role/name selectors where appropriate, keyboard navigation/focus, loading/error/empty and actual business effect. Compare static source or computed tokens only for those claims; real rendering and interaction require capable browser/observer. Reuse existing browser or manual verification; no redesign to satisfy test.

**Counterexample:** A success banner appears without saving the record, or mouse click works while keyboard focus cannot reach control.

**Observable verification:** Use actual input/key/click, wait for observable readiness, assert visible status and controlled underlying state/request. Capture viewport and evidence scope, not universal accessibility.

**Sources and limits:** QA-S12, QA-S27. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D14 — How can browser tests survive legitimate UI changes?

**Applicability / context:** Locators/waiting brittle, changing user experience while preserving behavior.

**Decision and alternatives:** Prefer user-visible roles/labels or stable explicit contracts, condition-based waits with bounded timeouts, isolated contexts and deterministic data. Visual snapshot useful when design identity is material; avoid pixel-perfect for nonvisual changes. Do not use fixed sleeps to hide failure.

**Counterexample:** Selector based on nth child breaks when a harmless wrapper is added; page can be ready before sleep or not ready after.

**Observable verification:** Run meaningful interaction and expected effect at required viewport, negative/error case and actual focus. Separate static, mocked response and actual local backend evidence.

**Sources and limits:** QA-S27, QA-S32. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D15 — What do screenshots and traces prove?

**Applicability / context:** Failure reproduction or visual/accessibility review; minimize sensitive content.

**Decision and alternatives:** Select screenshot for rendered state, trace/DOM for sequence and actual request/response, accessibility inspection and human task where relevant. Pin runtime and viewport, redact data, capture only authorized content. Existing local browser trace or manual note may suffice; no hosted export by default.

**Counterexample:** A single screenshot hides a transient duplicate request; a computed contrast ratio does not prove focus order.

**Observable verification:** Pair screen with observed action/state, inspect required negative behavior and actual render. Record trace retention and limitations; never call a browser context an OS sandbox.

**Sources and limits:** QA-S27, QA-S20, QA-S22. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

