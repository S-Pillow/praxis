# Secrets, cryptography and communication

Advisory decisions; examples use dummy inputs and require actual authorization and safe observation. No blanket requirements.

## SD13

**Decision:** Secrets storage and access

**Context / use when:** Credential, signing key, token, configuration or model context.

**Alternatives and tradeoffs:** No secret if no protected integration; reuse approved secret facility or short-lived identity. Avoid copying values.

**Constraints / unsuitable conditions:** Classify credentials vs public identifiers. Keep references separate, restrict role/process/environment access, avoid argument/log exposure, redact evidence. Scanner hit is a lead; no rotation authority implied.

**Verification / revisit:** Dummy marker tests check source, logs, exceptions and outputs. No real values or public findings; unknown paths remain unverified. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V13/V14/V16; PS-03; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD14

**Decision:** Key rotation, revocation and recovery

**Context / use when:** Long-lived key, compromise, membership changes.

**Alternatives and tradeoffs:** Retain sufficient lifecycle; consider scoped short-lived credentials or rotation with continuity tradeoffs. No automatic credential action.

**Constraints / unsuitable conditions:** Name key owner, purpose, scope, expiration, storage, revocation and recovery; overlap only where allowed. Do not restore compromised access.

**Verification / revisit:** Synthetic old credential denied at intended time, new credential succeeds, dependents recover. Provider/operator-only evidence pending where unavailable. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V6/V7/V11; PS-06; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD15

**Decision:** Vetted cryptography and transport

**Context / use when:** Confidentiality, integrity, authentication or password handling.

**Alternatives and tradeoffs:** Use approved library/protocol and qualified key facility; no custom crypto or encryption for threats it cannot address.

**Constraints / unsuitable conditions:** Distinguish password verification, encryption, authenticated integrity and transport. Verify applicable parameters from authoritative docs for exact version. Specify key ownership and peer validation.

**Verification / revisit:** Synthetic correct operation and relevant altered-data, wrong-key or invalid-peer failure. Algorithm choice alone not proof; avoid arbitrary numeric mandates. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V11/V12; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD16

**Decision:** Sensitive storage and backup

**Context / use when:** Sensitive data is intentionally persisted.

**Alternatives and tradeoffs:** No persistence if not required; existing OS/storage access control where sufficient. Encryption at rest does not stop misuse by authorized application.

**Constraints / unsuitable conditions:** Map primary/temp/backup copies, keys, restore authority and retention. Choose protection according to actual threat; recovery must not silently restore revoked access or expired data.

**Verification / revisit:** Dummy access and restore checks, revoked access, retention and key-unavailable failure. Source config does not establish live backup/encryption behavior. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V11/V14; PS-04; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.
