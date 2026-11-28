# Build automation and CI

Use only applicable cards. Examples are synthetic and unexecuted. Source IDs resolve through [SOURCES](../SOURCES.md); provider facts must be verified at use.

## DO-D04 — Did the intended tests actually run?

**Applicability / context:** A green job, report, cache or quality gate is being used to decide candidate correctness. Identify event, commit, runner and build graph.

**Decision and alternatives:** Trace real commands, flags, dependency locks, conditional skips, exit propagation and produced artifacts; distinguish compiled output, test execution, report generation and aggregate job result. Use existing minimal test mechanism first. A failing assertion must prevent false success when relevant; don't hide failure with continue-on-error or retries. Assess path filters, matrix omissions and manual dispatch.

**Counterexample:** A build skips tests but later emits an old report; job success says nothing about new behavior. A docs-only trigger omission may matter for tests of README/version parity.

**Observable verification:** Observe raw execution/count/failure reason, exact checkout and environment; use known-bad input that fails for intended reason, known-good control. Report skipped/unavailable separately.

**Sources and limits:** DO-S01 (Jenkinsfile), DO-S02, DO-S12–13, DO-S32; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D05 — How to isolate and reproduce a build?

**Applicability / context:** Build consumes dependencies, artifacts, caches or credentials; especially external contributions or matrix jobs.

**Decision and alternatives:** Pin supported toolchain and dependency graph, choose reviewed immutable action references where available, protect lockfiles and verify action inputs/version/maintenance. Cache by relevant dependency, OS and config identity; treat cache as performance, not trust. Separate untrusted PR validation from privileged release; scope token/job permissions and checkout credential persistence. Prefer native tests over new service. Never execute arbitrary upstream workflows merely because reviewed.

**Counterexample:** Cache hit using incompatible compiled output; a mutable tag can refer to different code; a signed artifact can still be wrong.

**Observable verification:** Record exact inputs, actual runner OS/toolchain, digest, exit status, rerun only affected failure after classification. Test cold/warm differences and denied credential use in safe target.

**Sources and limits:** DO-S03, DO-S12–13, DO-S19–25, DO-S32; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D06 — Which build evidence and artifacts should survive?

**Applicability / context:** Need handoff, audit, test logs or release identity; identify sensitivity, retention needs and consumer.

**Decision and alternatives:** Use existing local or CI artifact mechanism when sufficient. Preserve raw logs and candidate digest/ID; minimize and redact sensitive data before storing. Distinguish unique immutable artifact identity from mutable name and replacement; set expiration consistent with acceptance and recovery; record deletion/overwrite effects. Never upload hidden credential/config files implicitly.

**Counterexample:** An upload name reused with overwrite removes old identity; artifact SHA is integrity for bytes, not evidence of test validity.

**Observable verification:** Check exact archive contents, digest, artifact ID, expiry and retrieval; missing artifact remains unobserved. Verify failed/stalled jobs do not publish accepted artifacts.

**Sources and limits:** DO-S13, DO-S22–23, DO-S29; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.
