# Observability and monitoring

Use only applicable cards. Examples are synthetic and unexecuted. Source IDs resolve through [SOURCES](../SOURCES.md); provider facts must be verified at use.

## DO-D18 — Which signals answer the operational question?

**Applicability / context:** User-impact, incident, release or capacity question; available logs/metrics/traces and permitted data.

**Decision and alternatives:** Prefer existing structured logs and a small set of meaningful signals. Define units, denominators, time windows and correlation (source/release/request or pseudonymous ID). Select metrics for trends, traces for paths, logs for detail; no raw sensitive fields, unbounded user-ID labels or full prompt capture by default. Sampling, redaction, retention and budgets depend on risk and volume. Distinguish a real zero count from absent samples and unhealthy scrape.

**Counterexample:** Dashboard shows zero errors because no telemetry arrived; high-cardinality path/identifier labels exhaust storage and expose sensitive data.

**Observable verification:** Inject synthetic known success/error/absent samples; verify emitted, received and queryable values, units/denominator, redaction before export and behavior when collection fails.

**Sources and limits:** DO-S14–18, DO-S28–29, DO-S49–50; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D19 — Can telemetry be lost or overrun?

**Applicability / context:** Receiver→processor→exporter→storage pipeline or retrying sender; quantify peak rate and acceptable loss/delay.

**Decision and alternatives:** Use simplest adequate pipeline; no processors assumed by default. Choose memory limits early, filtering/redaction before storage/export, batching and bounded queue/retry appropriate to rate; size disk and memory headroom. Distinguish accepted by producer, enqueued, exported, persisted and queryable. Queue overflow can reject before retry; persistent queues fail on storage exhaustion. Prefer bounded loss/backpressure over uncontrolled retry storm; define signal for dropped/late data and data retention/access.

**Counterexample:** Queue full leads to discarded spans while exporter retry looks healthy; retention size is not an absolute disk ceiling.

**Observable verification:** Controlled fixture with queue saturation, missing backend, expired retries and recovery; inspect queue/drop counters, actual backend query, protected fields and resource ceilings. Do not transfer production payloads.

**Sources and limits:** DO-S28–29, DO-S49–50; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D20 — How should AI operational traces and data drift be interpreted?

**Applicability / context:** AI/ML application with actual need for model/prompt/skill, evaluation and deployment correlation.

**Decision and alternatives:** Start with existing minimized metadata: request/run correlation, model/config/prompt/skill version, latency, token usage, actual outcome and evaluator identity; distinguish telemetry, QA evaluation and billing. Compare existing instrumentation, OpenTelemetry, Langfuse, MLflow, Opik only where useful; no three-platform default. Self-hosting may still send telemetry, debug exporters or nested sensitive fields; confirm redaction failure behavior, storage/access/retention/deletion, backup and current edition. Treat distribution drift as diagnostic, compare representative reference/current windows and user/model quality; no automatic retrain or prompt rewrite.

**Counterexample:** A new model trace looks fast but data masking silently fails; feature distribution changes seasonally without quality degradation. Trace similarity is not correctness.

**Observable verification:** Synthetic nested sensitive fields and exporter failure, exact version correlation, trace vs result/cost comparison, known drift and stable controls; observe actual configured data flow or disclose not observed. QA evaluates behavior; no hidden reasoning capture.

**Sources and limits:** DO-S36–41, DO-S51–53, QA-S02/13–16; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.
