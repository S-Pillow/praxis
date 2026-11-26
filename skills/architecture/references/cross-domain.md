# Cross-domain design

Original conditional decision guidance; apply only within approved project intent. Source keys link to [source register](../SOURCES.md). No claim of current provider facts or project-specific acceptance.

## A28
**Decision:** Where is the trust/data boundary?
- **Use when:** An interface accepts user/external input, holds credentials, or exposes sensitive data.
- **Disqualifiers / stop:** Never infer permission from access or move secrets to an untrusted client; no external transfer from advisory guidance.
- **Alternatives and consequences:** Keep data local/minimized when possible; server-mediated access for trusted operations; use existing identity boundaries before new infrastructure.
- **Implementation implications:** Identify principals, data classes, permitted flows, least privilege, validation, redaction, retention and failure behavior; seek qualified security/privacy input when depth needed.
- **Verification / revisit:** Test unauthorized/malformed inputs and no forbidden read/write/transfer with isolated fixtures. Do not claim security conformance from source alone.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A29
**Decision:** How should system and interface states agree?
- **Use when:** Data-driven UI, asynchronous work or error-prone backend affects operator behavior.
- **Disqualifiers / stop:** Do not treat pending, skipped, unknown or stale as completed; do not redesign UI or change product intent from architecture advice.
- **Alternatives and consequences:** Use explicit status semantics and existing accessible UI patterns; involve UI/UX if material; direct action may suffice without background job.
- **Implementation implications:** Define source-of-truth status and error/empty/loading/retry/cancel states, accessibility and consumer contracts; keep backend and interface semantics coherent.
- **Verification / revisit:** Test representative transitions and error states; real rendered/interaction observation by capable observer where needed, not source-only assurance.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A30
**Decision:** What observability and release evidence do we need?
- **Use when:** A material runtime risk or diagnosis needs attributable behavior and source identity.
- **Disqualifiers / stop:** No telemetry export, session replay, credentials, automatic approval or provider enablement by default; provider hypothesis is not proof.
- **Alternatives and consequences:** Existing logs/tests may suffice; vendor-neutral instrumentation if justified; managed investigation/review tools only as qualified optional candidates.
- **Implementation implications:** Define signal, environment/release correlation, sampling, redaction, retention, access and known gaps. Preserve claim/source/observation/freshness so future audit can use evidence without protocol adoption.
- **Verification / revisit:** Observe controlled failures, correlate actual state, verify sensitive exclusions and gaps; separate tool/source observation from inference.
- **Provenance:** P1,P2,E1,E2,E4 (original synthesis; no upstream content copied). **Maintenance:** version-sensitive.

