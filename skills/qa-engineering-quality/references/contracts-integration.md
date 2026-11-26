# Contracts and integration

Original conditional QA guidance. Examples below are illustrative, not executed qualification. Source IDs resolve via [SOURCES](../SOURCES.md); use current official evidence for material volatile facts. AIPF and approved requirements govern.

## QA-D10 — Does a consumer test prove the provider?

**Applicability / context:** Interface boundary, service or serialization changes; no external call merely for contract inspection.

**Decision and alternatives:** Identify actual consumer assumptions and provider guarantees including required fields, type, units, status and errors. Consumer tests with stubs validate expectations; provider tests verify real implementation; local interaction verifies seam. Existing contract test or ordinary stdlib serialization may suffice; optional framework if material.

**Counterexample:** Stub always returns amount as integer while actual provider returns string; stub tests pass.

**Observable verification:** Exercise both sides with actual serialized response; broken type and missing field fail intended checks, valid response succeeds. Label stub vs actual.

**Sources and limits:** QA-S26, QA-S33. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D11 — Is a schema change compatible?

**Applicability / context:** New optional/required fields, changed type, default or semantics, versioned API/MCP.

**Decision and alternatives:** Inspect existing consumers, provider and required behavior. Test removed/renamed or changed required field/type as breaking unless supported migration; additive optional field compatible only if consumers tolerate it and semantics unchanged. Choose explicit version/migration if justified; avoid unnecessary new protocol.

**Counterexample:** A consumer rejects all unknown keys, so adding optional field breaks it despite generic compatibility advice.

**Observable verification:** Replay known consumer on baseline, breaking and proposed responses, observe actual error and preserved values; note version and scope.

**Sources and limits:** QA-S02, QA-S26. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D12 — What proves an integration or migration actually works?

**Applicability / context:** When data or protocol crosses real boundary; not every unit requires full deployment.

**Decision and alternatives:** Pin schema/config and actual dependency or safe local seam; test success, malformed/error, retry and consistency. Round-trip checks only for specified information preservation; rollback/recovery only within authority. Mock external dependency if real execution unavailable, label gap.

**Counterexample:** JSON parse passes but integer minor units are converted to a float and rounded incorrectly.

**Observable verification:** Verify expected units/types, counts and exact target effect, failed operation no partial write when required. Record actual vs mock and environment.

**Sources and limits:** QA-S26, QA-S03, QA-S33. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

