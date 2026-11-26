# Module and interface design

Original conditional decision guidance; apply only within approved project intent. Source keys link to [source register](../SOURCES.md). No claim of current provider facts or project-specific acceptance.

## A07
**Decision:** Where should responsibility and dependency boundaries sit?
- **Use when:** Business rules, presentation and I/O are entangled or independently changeable.
- **Disqualifiers / stop:** Avoid adding layers that only forward calls or break accepted package boundaries without benefit.
- **Alternatives and consequences:** Group behavior around cohesive responsibility; direct use of simple library may be sufficient; ports/adapters help when I/O variation or test isolation matters, at abstraction cost.
- **Implementation implications:** Place stable policy inward; adapt storage/network at boundary; avoid circular dependency and duplicate validation rules. Expose small meaningful interfaces, not internals.
- **Verification / revisit:** Check import/dependency graph where relevant; exercise policy without external dependencies and integration via real adapter.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A08
**Decision:** When is an abstraction worth introducing?
- **Use when:** Several callers share a stable concept, a volatile implementation must be isolated, or actual tests need an interface.
- **Disqualifiers / stop:** Do not abstract speculative future variants or hide distinct semantics behind a misleading common interface.
- **Alternatives and consequences:** Keep direct call if it is clear; extract cohesive module when reuse/independent change is real; add an interface only if its contract is stable and meaningful.
- **Implementation implications:** Define inputs, outputs, error and ownership semantics; do not expose redundant setters or duplicate state. Preserve relevant compatibility.
- **Verification / revisit:** Exercise each promised contract and verify implementation can change without consumer edits; check no forwarding-only complexity added.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A09
**Decision:** How do we evolve a public interface?
- **Use when:** Existing API, CLI, module or serialized contract has consumers.
- **Disqualifiers / stop:** Do not silently change field meanings, status values, default behavior or consumer errors.
- **Alternatives and consequences:** Add optional compatible fields/modes where possible; version breaking changes only if necessary; retain adapters/deprecation path when consumers need it.
- **Implementation implications:** Inventory consumers, examples, frozen output and fixtures. Document default/absent/invalid inputs and compatibility. Do not version merely because internals changed.
- **Verification / revisit:** Compare old fixtures/output and positive/negative contract cases; verify unknown inputs fail as specified and old clients continue.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

