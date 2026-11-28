# Delivery and release management

Use only applicable cards. Examples are synthetic and unexecuted. Source IDs resolve through [SOURCES](../SOURCES.md); provider facts must be verified at use.

## DO-D07 — Which delivery strategy meets the real need?

**Applicability / context:** Deployable target, user-impact and data compatibility known; not every local/static release needs staged cloud delivery.

**Decision and alternatives:** Prefer existing simple process/atomic static replacement if adequate. Consider rolling for replicated compatible instances, canary for measurable risk with bounded traffic, blue-green for quick switch where parallel capacity/state permits. Include startup/readiness, version skew, migrations, traffic routing, downtime, resource cost, failure/abort and rollback vs forward repair. Identify owner-approved target and effects before execution.

**Counterexample:** Two identical environments share incompatible database migration; swapping traffic back does not undo schema changes.

**Observable verification:** Check immutable artifact digest, target config and state, readiness plus representative user outcome; observe old/new coexistence and safe recovery where required.

**Sources and limits:** DO-S01, DO-S02, DO-S14–16, DO-S31; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D08 — When is sync or release actually complete?

**Applicability / context:** Declarative controller, manual deployment, release workflow or external publication.

**Decision and alternatives:** Distinguish desired source, evaluated plan, actual applied resource, health, actual user success and published metadata. Verify accepted source and artifact before authorized promotion; reconcile after. In GitOps, inspect auto-sync/self-heal/prune/allow-empty options separately; protect resource ownership, namespace and destructive prune. Hooks may repeat; design migration and credential ordering to be safe. On uncertain commit, inspect target state before retry.

**Counterexample:** A sync succeeds while a dependency or user transaction fails; a release action silently overwrites an asset or ignores a missing glob.

**Observable verification:** Observe actual deployment/release identity and digest, exact user effect and failure, no unauthorized PR/tag/asset changes; confirm recovery. Recheck exact action semantics rather than assume current defaults.

**Sources and limits:** DO-S21–23, DO-S31; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D09 — How do migrations and recovery constrain promotion?

**Applicability / context:** Data/schema/config changes, partial rollouts, interrupted publish or dependent services.

**Decision and alternatives:** Prefer compatible expand/contract or bounded maintenance when justified by approved workload; coordinate Architecture, Security, QA. Pin migration input/target, inspect before applying, preserve recovery and data invariants. Choose reversible source rollback only if data/side effects compatible, otherwise planned forward correction/restore. Record trigger, abort threshold and responsible actor; no automatic retry of uncertain non-idempotent effects.

**Counterexample:** Old application cannot read new persisted state; previous artifact exists but recovery is not actionable.

**Observable verification:** Use synthetic compatible/incompatible versions, interrupted or repeated migration, actual pre/post state and user read/write; verify rollback or forward path at appropriate readiness level.

**Sources and limits:** DO-S01, DO-S30–31, DO-S37–38; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.
