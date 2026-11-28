# Infrastructure as code and configuration

Use only applicable cards. Examples are synthetic and unexecuted. Source IDs resolve through [SOURCES](../SOURCES.md); provider facts must be verified at use.

## DO-D10 — How should plan, state and apply be separated?

**Applicability / context:** Existing/proposed managed infrastructure; confirm owner, environment/account/workspace, backend, provider version and target ownership.

**Decision and alternatives:** Prefer no new infrastructure or existing qualified provider controls. If IaC is useful, version definitions, protect provider lockfile and state; inspect desired/observed changes including deletion/replacement and out-of-band drift. State locking coordinates participating clients, not all writers. Treat saved plans/state as sensitive even if CLI masks values; protect encryption keys and backup. Revalidate plan identity/freshness and authority before apply. Do not force-unlock until lock owner, actual operation and risk reconciled.

**Counterexample:** A plan succeeded but contains secrets and a stale resource diff; force-unlock interrupts another active operation. No approval is implied by plan generation.

**Observable verification:** Inspect plan redacted with target and state lineage; negative case stale plan/no write, actual resource/state effect only if authorized. Confirm protected artifact/log exclusions, recovery and changed-resource scope.

**Sources and limits:** DO-S01, DO-S26, DO-S45–47; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D11 — Can configuration automation be repeated safely?

**Applicability / context:** Provisioning or changes across hosts, configuration drift, partial service restart.

**Decision and alternatives:** Select existing config mechanism or idempotent modules rather than arbitrary command where fit. Bound exact inventory, credentials, privilege, variables and ordering; check/diff may not model unsupported tasks or conditionals and can expose secrets. For commands establish safe preconditions or creates/removes conditions and actual repeat behavior. Observe per-host changed state and readiness. Stop partial rollout, reconcile actual state before retry.

**Counterexample:** Dry-run omits arbitrary command; file write succeeds but restart fails. Recap is green on some hosts, service remains degraded.

**Observable verification:** Use isolated representative config and two runs; verify convergence (no unintended second effect), failed restart and preserved prior state/recovery, service behavior not recap.

**Sources and limits:** DO-S27, DO-S48; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D12 — What changes should remain manual or provider-native?

**Applicability / context:** Low frequency change, uncertain provider support, limited team capacity.

**Decision and alternatives:** Compare documented manual, provider-native and code-managed paths. Adopt IaC only when reproducibility and lifecycle value outweigh state/credential/tool burden. Never introduce automation just to satisfy a governance label; when drift is detected, first determine authoritative intent and scope before correcting. Separate destroy, replacement and import from ordinary edits.

**Counterexample:** Reconciling an out-of-band emergency change by auto-applying obsolete desired state breaks an approved incident mitigation.

**Observable verification:** Observe known-good state, intended delta and changed resources; demonstrate actual revert/recovery capability and owner decision for destructive effects.

**Sources and limits:** DO-S02, DO-S26–27, DO-S31; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.
