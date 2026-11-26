# Diagnostic signals and operations evidence

**No new service / existing / local first:** Use existing application logs and local tracing first. Choose signals from actual incident/release questions; no collection or export solely because available.

The following are independently authored discovery candidates. Verify decisive facts at use; none grants installation, access, data transfer, billing or release permission.

## CAP-V01
**Name:** OpenTelemetry
- **Tags:** local, self-hosted, instrumentation
- **Candidate use:** Vendor-neutral instrumentation reference where project needs telemetry.
- **Constraints to check:** Language/runtime version, sampling, exporter, redaction, environment/release correlation, local/remote storage and maintenance.
- **Official documentation pointer(s):** https://opentelemetry.io/docs/what-is-opentelemetry/
- **Pricing / terms / licensing pointer(s):** https://opentelemetry.io/docs/
- **Observation / verification state:** P2 reference; no upstream code bundled; no exporter/provider selected, cost of chosen backend separate.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

## CAP-V02
**Name:** Sentry
- **Tags:** hosted, errors
- **Candidate use:** Optional error and performance investigation candidate.
- **Constraints to check:** Events/volume billing, PII, sampling, retention, environment identity, access and data residency.
- **Official documentation pointer(s):** https://docs.sentry.io/
- **Pricing / terms / licensing pointer(s):** https://sentry.io/pricing/
- **Observation / verification state:** P2 candidate and pricing pointer; plan/actual capability unqualified.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

## CAP-V03
**Name:** Interfere
- **Tags:** hosted, investigation, MCP
- **Candidate use:** Optional candidate for production error investigation and release correlation; not an integration.
- **Constraints to check:** Read-only vs write endpoint, workspace access, traces/logs/sessions, privacy and retention, pricing unknown, actual access/coverage. No session replay by default.
- **Official documentation pointer(s):** https://interfere.com/docs ; https://interfere.com/docs/integrations/mcp
- **Pricing / terms / licensing pointer(s):** https://interfere.com/docs
- **Observation / verification state:** P2 provider-stated separate read-only/read-write endpoints; pricing unqualified, no live access/telemetry export. No verified operational capability.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

