# Privacy and lifecycle

Advisory decisions; examples use dummy inputs and require actual authorization and safe observation. No blanket requirements.

## SD17

**Decision:** Purpose, minimization and collection

**Context / use when:** New field, analytics, export or data processing.

**Alternatives and tradeoffs:** No collection first; local aggregate/ephemeral alternative; identifiable records only when necessary and approved.

**Constraints / unsuitable conditions:** Map purpose, necessary fields, affected people, recipients and lifecycle; separate notice/choice from actual processing. Flag unresolved legal/contract issues; no compliance inference.

**Verification / revisit:** Synthetic allowlist verifies fields; disabled optional collection creates no corresponding record/transfer in observed scope. Unobserved recipients remain unknown. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-04; PS-01 V14; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD18

**Decision:** Identifiers, analytics and replay

**Context / use when:** Usage measurement, tracking or session replay.

**Alternatives and tradeoffs:** No tracking or aggregate-only counts first; qualify self-hosted/hosted alternatives only when warranted.

**Constraints / unsuitable conditions:** Examine identifiers, session linkage, event/query fields, replay, masking, recipients, access and retention. Cookieless or pseudonymous is not necessarily anonymous. Do not enable replay by default.

**Verification / revisit:** Inspect dummy events, requests and stored fields; verify prohibited IDs and sensitive text absent in tested paths. Schema/marketing is not runtime proof. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-04; SR-04; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD19

**Decision:** Retention, deletion, export and derived data

**Context / use when:** A lifecycle change or new store/cache/log/backup.

**Alternatives and tradeoffs:** Preserve verified policy; avoid indefinite retention; define scoped expiry/deletion or approved exceptions. Legal conflict requires qualified decision.

**Constraints / unsuitable conditions:** Map primary, derived, cache, export, backup and processor copies; specify who may delete/export, scope/timing, exceptions and restore behavior. Do not promise unobserved erasure.

**Verification / revisit:** Dummy eligible deletion/export, denied cross-user request, expected derived/cache state and restore. Report backup/processor gaps precisely. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-04; PS-01 V14; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD20

**Decision:** Local processing and external disclosure

**Context / use when:** Transformation, clipboard, generated public pages or external AI/API.

**Alternatives and tradeoffs:** Existing library or local utility first; cloud or extensions only if data boundary and benefit justify.

**Constraints / unsuitable conditions:** Trace clipboard, logs, temp files, plugins, network and generated artifacts. Separate intended public fields from private source; crawler directives not access control.

**Verification / revisit:** Dummy values verify outputs and writes, capable observer verifies network where required. Verify generated public fields; do not assert no traffic without evidence. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-04; SR-03; SR-08; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.
