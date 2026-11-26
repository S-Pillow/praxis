# Threat modeling and trust boundaries

Advisory decisions; examples use dummy inputs and require actual authorization and safe observation. No blanket requirements.

## SD01

**Decision:** Assets, actors and flows

**Context / use when:** Material new or changed resource, actor, service or flow.

**Alternatives and tradeoffs:** Retain a verified unchanged model; otherwise trace actual entry, processing, storage, recipients and trust transitions. A small table may suffice; add a diagram only when useful.

**Constraints / unsuitable conditions:** Identify actor/resource/action, ownership, privileged effects and trust boundaries; label assumptions. Do not invent actors or collect secrets.

**Verification / revisit:** For a dummy report trace actual input, output and error locations. For sharing trace owner/non-owner server paths; enumerate uninspected background paths. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-02; PS-01 V15; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD02

**Decision:** Threat and privacy risk lens

**Context / use when:** Material risk or privacy processing needs a decision.

**Alternatives and tradeoffs:** Use targeted misuse cases for small changes, STRIDE for system threats, LINDDUN for privacy harm where helpful. Avoid mandatory modeling ceremony.

**Constraints / unsuitable conditions:** Describe actor, action, asset and plausible harm; distinguish harm to people from system compromise. Tie each relevant concern to a control and uncertainty.

**Verification / revisit:** Test a denied read or unwanted correlation with synthetic records and ordinary authorized success. A hypothetical abuse case is not a confirmed flaw. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-02; PS-04; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD03

**Decision:** Existing controls and residual risk

**Context / use when:** A suspected weakness or proposed additional layer.

**Alternatives and tradeoffs:** Retain sufficient existing controls; strengthen weak boundary or add independent protection when consequence justifies cost. More layers can increase failures.

**Constraints / unsuitable conditions:** Trace guard, configuration, alternate paths and assumptions; separate owner risk decisions and hardening from defects. Do not weaken controls for convenience.

**Verification / revisit:** Observe allowed/denied cases at actual guard; identify exact missing facts if alternate path uninspected. Do not assume one guard covers all. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V8/V15; SR-06; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD04

**Decision:** Security requirements and trust contract

**Context / use when:** A risk needs actionable implementation constraints.

**Alternatives and tradeoffs:** Preserve existing explicit invariants when sufficient; otherwise specify bounded controls, not blanket compliance or security levels.

**Constraints / unsuitable conditions:** Specify actor, resource, action, allow/deny predicate, side-effect and disclosure limits, errors and evidence. Preserve reasonable implementation discretion.

**Verification / revisit:** Authorized dummy read returns only permitted fields; denied read leaks no contents and causes no write. UI visibility is not enforcement. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V8; PS-02; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.
