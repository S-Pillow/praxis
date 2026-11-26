# Deployment and abuse resistance

Advisory decisions; examples use dummy inputs and require actual authorization and safe observation. No blanket requirements.

## SD29

**Decision:** Secure runtime and configuration

**Context / use when:** Deployment, role, exposure or environment changes.

**Alternatives and tradeoffs:** Retain safe defaults, disable unnecessary privileges/ingress, use existing approved infrastructure where sufficient.

**Constraints / unsuitable conditions:** Identify environment-specific roles, ingress/egress, debug/errors and fail-safe settings. Advice never authorizes infra mutation.

**Verification / revisit:** Synthetic config accepts allowed and rejects unsafe/missing values; actual deployed controls separately observed. Source config not live proof. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V13; PS-06; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD30

**Decision:** Resource and abuse limits

**Context / use when:** Untrusted work, parser, API, queue or cost quota.

**Alternatives and tradeoffs:** Existing controls; bounded in-process work before shared infrastructure. Base limits on workload/risk, not universal numbers.

**Constraints / unsuitable conditions:** Specify payload/concurrency/queue/time/retry/cost boundaries and graceful rejection/recovery. Rate limit not proof of hard spend cap. No live load tests.

**Verification / revisit:** Bounded synthetic accepted/rejected work and recovery with no partial writes or unbounded growth; provider limits require qualified evidence. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V2/V4; PS-06; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD31

**Decision:** Security events and operational signals

**Context / use when:** Control failure or material investigation.

**Alternatives and tradeoffs:** Existing local signals first; no new telemetry or replay by default.

**Constraints / unsuitable conditions:** Choose actionable event, approved fields, access, redaction, retention, correlation and response owner. Do not log credentials/full payloads or unnecessary identifiers.

**Verification / revisit:** Dummy events contain necessary signal but no prohibited fields; logging failure does not bypass access control. Runtime/provider retention separate. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-01 V16; PS-04; PS-06; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD32

**Decision:** Change and recovery readiness

**Context / use when:** Config drift, rollback, revocation or restore.

**Alternatives and tradeoffs:** Reuse verified recovery; bounded runbook for material controls only. No restore of compromised access.

**Constraints / unsuitable conditions:** Identify known-good config, recovery owner/authority, data and rollback effects; revalidate current access/retention. Coordinate architecture/operations without new DevOps scope.

**Verification / revisit:** Disposable restore/config exercise where allowed; recovered behavior preserves current invariants. Record untested production recovery. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-03; PS-06; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.
