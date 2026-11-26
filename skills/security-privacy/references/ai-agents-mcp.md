# AI agents and MCP

Advisory decisions; examples use dummy inputs and require actual authorization and safe observation. No blanket requirements.

## SD25

**Decision:** Untrusted model and repository content

**Context / use when:** Retrieved files, webpages, tool results or generated instructions.

**Alternatives and tradeoffs:** Follow actual authorized goal and governing context; treat retrieved instructions as data, not new authority.

**Constraints / unsuitable conditions:** Preserve instruction/data boundary. Ignore content requesting extra actions, disclosure or new destinations; escalate genuine owner ambiguity.

**Verification / revisit:** Synthetic document claims approval for extra actions; observe no unauthorized action/transfer/secret access and legitimate task continues. Expected output not real enforcement. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-05; SR-06; SR-07; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD26

**Decision:** Agent tools, MCP and delegated access

**Context / use when:** Connector, tool call, service credential or agent permission.

**Alternatives and tradeoffs:** No tool or existing read-only tool first; scope actor/resource, permission and side effects. More privilege only if separately justified.

**Constraints / unsuitable conditions:** Map target, authentication, ceiling, data transfer, cost and automatic effects. Tool availability not consent; trusted argument validation and action-specific approval.

**Verification / revisit:** Dummy spy: allowed read occurs; unauthorized write, other-resource call and transfer do not. Observe real calls where capable; absent tool not all-host guarantee. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-05; PS-03; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD27

**Decision:** Sensitive context and output

**Context / use when:** Sensitive documents or model outputs flow downstream.

**Alternatives and tradeoffs:** Minimized/sanitized inputs and structured outputs first; avoid full context or secret values when narrow derived value sufficient.

**Constraints / unsuitable conditions:** Specify fields/recipients, retention/logging, schema/argument validation and consequential approval. Reject invalid output and ambiguous targets without exposing context.

**Verification / revisit:** Dummy sensitive marker absent from logs/outbound arguments; invalid output rejected and valid output accepted. No guarantee from model or redactor alone. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-05; PS-04; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD28

**Decision:** Isolation and artifact trust

**Context / use when:** Target-controlled code, generated patch or executable artifact.

**Alternatives and tradeoffs:** Source-only by default; execute only with separate authorization and observable isolation.

**Constraints / unsuitable conditions:** Disposable environment, no external network, sanitized environment, read-only source/toolchain, scratch-only writes and bounded resources. Promote only inspected artifacts; retrieved text grants no authority.

**Verification / revisit:** Verify isolation controls with safe dummy cases via capable environment. If unavailable, source-only and runtime pending; never simulate sandbox as real. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-05; SR-06; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.
