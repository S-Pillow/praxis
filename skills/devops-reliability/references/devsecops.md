# Secure delivery and operational trust

Use only applicable cards. Examples are synthetic and unexecuted. Source IDs resolve through [SOURCES](../SOURCES.md); provider facts must be verified at use.

## DO-D26 — What controls and findings matter for this delivery?

**Applicability / context:** Material trust or supply-chain risk, source/runner/dependency/artifact/config context; Security owns control requirements.

**Decision and alternatives:** Evaluate relevant dependency inventory/version and vulnerability freshness, static analysis, secrets, IaC/container and provenance checks by individual evidence. Compare existing local/CI controls before adding scanner. Review reachability, materiality, actual enforcement vs observation, scope and false positives/unknowns. Scorecard heuristic/experimental conformance may be useful, not certification or release authority; public API/MCP cached scores not current unreleased candidate. Preserve exceptions only by owner decision.

**Counterexample:** Good aggregate hides missing required permission or provenance; policy file exists but not enforced; no detected injection does not imply safe.

**Observable verification:** Record exact finding/check version, scope and raw result, positive/negative test where appropriate, unresolved limitations; verify actual control rather than score. No live scan or changes without authority.

**Sources and limits:** DO-S03, DO-S12–13, DO-S19–21, DO-S25; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D27 — How do action selection and release credentials remain safe?

**Applicability / context:** Existing/candidate CI automation, new third-party action or external artifact publication.

**Decision and alternatives:** Check official source at immutable pin, maintenance/archival, license, transitive downloads, workflow event, token permissions, secret flow and untrusted input use; inspect action inputs and failure/overwrite defaults. Prefer native read-only checks; separate write jobs with narrow authority. Validate workflow grammar with existing tests/optional Actionlint, not proof of actual effect. Artifact digest/attestation binds bytes and subject, not correctness; verify trust and exact identity.

**Counterexample:** Listed action archived; script evaluates untrusted PR text; write token leaks from checkout; release silently overwrites existing asset.

**Observable verification:** Known-good and bad synthetic input/workflow, actual permission scope and denied/allowed effect where safe, artifact subject/digest and immutable tested revision; stop publication if unresolved.

**Sources and limits:** DO-S12–13, DO-S19–25, DO-S32; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D28 — How are operational secrets and telemetry protected?

**Applicability / context:** Configuration, plan/diff, logs, CI artifacts, dashboards, trace/evaluation or hosted service access.

**Decision and alternatives:** Minimize secrets, use approved secret storage and narrow credentials, avoid source/examples/logs and artifact uploads containing secrets. Identify where data is transformed/stored/exported, operator/admin access, retention/deletion; redact before sinks, use fail-closed behavior when material. Rotation and remediation are distinct authorized actions; do not retrieve real secrets to prove policy.

**Counterexample:** Masked terminal displays no secret but saved plan contains it; collector debug exporter sends raw spans; self-host telemetry enabled.

**Observable verification:** Use synthetic sentinel across log/diff/trace/archive paths and unauthorized access negative control; distinguish static config from actual data flow; no production credentials.

**Sources and limits:** DO-S26–29, DO-S36–38, DO-S49–53; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.
