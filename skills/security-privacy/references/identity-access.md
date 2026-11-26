# Identity and access

Advisory decisions; examples use dummy inputs and require actual authorization and safe observation. No blanket requirements.

## SD05

**Decision:** Identity need and trust source

**Context / use when:** Local single-user, team sharing or remote access.

**Alternatives and tradeoffs:** No account if OS/local trust suffices; reuse approved identity provider where shared identities needed; self-host only with lifecycle capacity.

**Constraints / unsuitable conditions:** Establish who must be distinguished and trusted identity source. Authentication is not ownership. No bespoke credentials simply to avoid a service.

**Verification / revisit:** Local case: no unnecessary identity network call/profile. Shared case: identity derived from trusted validation, never user-controlled field. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V6/V8; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD06

**Decision:** Authentication and credential lifecycle

**Context / use when:** Interactive login, recovery or service identity actually required.

**Alternatives and tradeoffs:** Keep suitable existing provider/framework; choose stronger factors or step-up for consequence, not universal thresholds.

**Constraints / unsuitable conditions:** Use vetted password verification when needed; protect enrollment, recovery, factor changes, throttling, enumeration-sensitive responses and backup codes. No real credentials.

**Verification / revisit:** Dummy valid/invalid login, recovery rejection, revoked access and bounded throttling cases; verify logs/errors contain no credential. Actual provider behavior requires observation. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V6; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD07

**Decision:** Session and token lifecycle

**Context / use when:** Browser, API or machine credential persists across calls.

**Alternatives and tradeoffs:** Compare existing framework sessions and validated signed tokens for revocation, availability and state cost; avoid sessions if unnecessary.

**Constraints / unsuitable conditions:** Define issuer, audience, scope, validation, expiry, renewal, revocation, storage and transport. Specify effective timing of membership/account change; never trust client parsing as authorization.

**Verification / revisit:** Valid access and relevant expired, invalid, wrong-audience/revoked rejection. Verify logout and membership change against policy using dummy credentials. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V7/V9/V10; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD08

**Decision:** Resource and tenant authorization

**Context / use when:** Shared objects, admin functions, tenant or field constraints.

**Alternatives and tradeoffs:** Reuse actual server-side guard if it covers all paths; ownership checks or central policy according to complexity. UI hiding is usability only.

**Constraints / unsuitable conditions:** Bind trusted principal to action, resource, tenant and fields at actual boundary; deny ambiguous permissions. Explicitly preserve public resources. Cover list/detail/write/export.

**Verification / revisit:** Dummy owner succeeds, other/unknown/revoked actor fails without contents or write; check mixed-resource requests and permitted public cases. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V8 (8.1.1, 8.1.2); original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.
