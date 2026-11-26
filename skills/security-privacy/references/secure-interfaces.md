# Secure interfaces and data handling

Advisory decisions; examples use dummy inputs and require actual authorization and safe observation. No blanket requirements.

## SD09

**Decision:** Input and output contracts

**Context / use when:** External request, file, model output or database boundary.

**Alternatives and tradeoffs:** Retain verified schema and safe framework APIs; use parameterized operations and context-specific rendering instead of handcrafted filters.

**Constraints / unsuitable conditions:** Validate type, length, range and business semantics before side effects. Treat input as data. Bound errors and preserve valid Unicode/formats.

**Verification / revisit:** Test valid and malformed fields, boundary sizes and harmless punctuation; assert no partial state effects or unintended interpretation. One field test does not cover all paths. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V1/V2/V4; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD10

**Decision:** Files, paths and uploads

**Context / use when:** User file, archive, path or generated artifact.

**Alternatives and tradeoffs:** Keep user-selected local paths/approved roots; avoid uploads and persistence if unnecessary. Use platform-safe APIs and parsers.

**Constraints / unsuitable conditions:** Resolve authorized root and account for links, canonicalization and concurrent replacement; enforce ownership, size/count/format limits, cleanup and collision policy; never execute input.

**Verification / revisit:** Disposable valid, disallowed path, oversize, malformed and interrupted cases; original input preserved and rejected work leaves no forbidden output. Unobservable filesystem controls remain unknown. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V5; SR-07; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD11

**Decision:** URLs, outbound requests and callbacks

**Context / use when:** URL fetch, redirect, webhook or agent network call.

**Alternatives and tradeoffs:** No network when local processing suffices; approved endpoints/connector before unrestricted URLs.

**Constraints / unsuitable conditions:** Specify destination scheme/service identity, redirects, connection-time policy, timeout and response bounds. Authenticate callbacks and define replay behavior. String prefix is not trust.

**Verification / revisit:** Synthetic adapter tests allowed/denied destination and redirect with no external call, duplicate callback and bounded failure. Real network enforcement requires capable observation. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V4/V12; SR-07; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD12

**Decision:** Protocol, client and integration boundaries

**Context / use when:** Browser credentials, webhooks, serialization, shared caches.

**Alternatives and tradeoffs:** Keep verified framework defaults and add only relevant protocol controls.

**Constraints / unsuitable conditions:** Distinguish cross-origin response access from authorization; protect ambient-credential state changes as appropriate. Validate message identity/schema, avoid unsafe deserialization and scope cache keys to data boundary.

**Verification / revisit:** Dummy allowed/denied requests, duplicate messages, malformed fields and cache isolation; CORS or hidden UI alone does not establish authorization. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V3/V4/V8/V15; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.
