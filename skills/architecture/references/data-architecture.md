# Data architecture

Original conditional decision guidance; apply only within approved project intent. Source keys link to [source register](../SOURCES.md). No claim of current provider facts or project-specific acceptance.

## A13
**Decision:** Do we need to persist this data?
- **Use when:** A feature requests history, durable state, audit, recovery or cross-session behavior.
- **Disqualifiers / stop:** Existing prohibition on saved results or data retention is controlling until owner explicitly changes it; never persist by convenience.
- **Alternatives and consequences:** Ephemeral state supports no-history behavior; local files or database support durable data when authorized; remote/shared store adds trust and operations.
- **Implementation implications:** Define data purpose, lifecycle, ownership, sensitivity, recovery and permitted actions before selecting store. Separate configuration from runtime results.
- **Verification / revisit:** Verify restart behavior, expected retention/deletion and no unauthorized writes; when no persistence required, assert writes do not occur.
- **Provenance:** P1,P2,K1 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A14
**Decision:** Embedded SQL, server SQL, document/KV or object storage?
- **Use when:** Authorized persistence needs queries, transactions, concurrent access, or media storage.
- **Disqualifiers / stop:** Do not assume one database fits all; remote sharing and writer concurrency can rule out embedded design; unstructured bytes may not need relational modeling.
- **Alternatives and consequences:** Embedded SQLite can fit local/modest workloads; server SQL fits shared multi-client transactional work with operational burden; document/KV for access patterns not relational constraints; object/files for blobs. Keep existing when fit.
- **Implementation implications:** Choose from data ownership, query shape, invariants, concurrency, durability, backup/export and deployment. Define unique keys, transaction boundary and indexes from real queries.
- **Verification / revisit:** Use representative concurrent writes or failure cases; verify duplicate handling, transaction rollback, export/restore and query performance where relevant.
- **Provenance:** P1,P2,K1,K2 (original synthesis; no upstream content copied). **Maintenance:** version-sensitive.

## A15
**Decision:** How do we change a schema safely?
- **Use when:** A change affects stored data or downstream consumers.
- **Disqualifiers / stop:** Do not migrate or alter retention without authorization; backups alone do not prove recoverability; incompatible consumers may block a change.
- **Alternatives and consequences:** No change or additive migration where feasible; staged expand/migrate/contract for live consumers; replace only with explicit plan and evidence.
- **Implementation implications:** Identify old/new schemas, migration preconditions, idempotence, validation, data integrity, backup/restore and rollback or forward recovery. Preserve reader/writer compatibility during transition.
- **Verification / revisit:** Run disposable copy/fixtures including malformed/duplicate data; compare invariant counts/values, interrupted migration, version compatibility and actual restore if required.
- **Provenance:** P1,P2,K2 (original synthesis; no upstream content copied). **Maintenance:** stable.

