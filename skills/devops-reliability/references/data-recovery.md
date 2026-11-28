# Data operations and disaster recovery

Use only applicable cards. Examples are synthetic and unexecuted. Source IDs resolve through [SOURCES](../SOURCES.md); provider facts must be verified at use.

## DO-D24 — Which state needs backup, and can it be restored?

**Applicability / context:** Approved persistence with recovery needs; identify data/config/secrets/metadata relationships and restore targets. Choose RPO/RTO with owner, not arbitrary durations.

**Decision and alternatives:** Prefer native/approved mechanisms if adequate. Map consistent state snapshot, retention, access/encryption keys, independent copies as appropriate, backup timing, expected data-loss window and restore time. Distinguish existence, integrity check, correct snapshot selection, file filters and actual application recoverability. Restore in isolated target, validate data invariants and user functionality. Verify restore access without exposing secrets.

**Counterexample:** Backup command and integrity check pass but database/config or keys absent; copying repository files omits service metadata; no recovery when password lost.

**Observable verification:** Restore specified snapshot to disposable path; verify required paths, content/metadata, database consistency and app read/write; record duration and actual restore point vs required RTO/RPO. Never overwrite live data implicitly.

**Sources and limits:** DO-S30, DO-S42–43; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D25 — What retention, cleanup and migration effects are permitted?

**Applicability / context:** Backup retention/pruning, storage migration, recovery/forward repair, uncertain interrupted actions.

**Decision and alternatives:** Separate ordinary backup from destructive forget/prune and approved deletion rules. Understand snapshot references, locking, concurrent backup and unreferenced storage, cost and recovery before cleanup. Verify exact target and preserve last known acceptable recovery, key access and data lifecycle. Migrate with data compatibility, transactional/partial failure semantics and reconciliation of uncertain operations. Prefer safe repeat/attach to already running operation rather than duplicate destructive restore.

**Counterexample:** Prune locks backup repo during incident; job restarts and starts second restore; deletion policy removes only apparent copy while backups retain data.

**Observable verification:** Use isolated restore and controlled interrupt/resume, count expected records/files, verify no loss/duplicate effects; inspect actual retention target before/after. Record key and operator-access feasibility without logging secret.

**Sources and limits:** DO-S30–31, DO-S38; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.
