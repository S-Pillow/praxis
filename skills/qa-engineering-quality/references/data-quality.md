# Data quality

Original conditional QA guidance. Examples below are illustrative, not executed qualification. Source IDs resolve via [SOURCES](../SOURCES.md); use current official evidence for material volatile facts. AIPF and approved requirements govern.

## QA-D25 — How do I verify an import or transform?

**Applicability / context:** Data schema/units, duplicate identities, missingness, totals or output integrity; use synthetic data.

**Decision and alternatives:** Derive accepted schema/types/units and reject policy from approved requirements; decide atomic vs partial acceptance explicitly. Check independent expected counts, exact totals, rejected rows and preserved state. Include absent/empty/zero/false, malformed and duplicates. No new persistence or data retention assumption.

**Counterexample:** A truthiness check silently drops zero, and duplicate IDs inflate totals.

**Observable verification:** Use original fixture with valid zero, duplicate and malformed rows; assert accepted IDs, rejection reasons, total/count and unchanged input/other state. Reconcile using independent calculation.

**Sources and limits:** QA-S24, QA-S30, QA-S33. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D26 — What should a migration or round trip preserve?

**Applicability / context:** Serialization/export/import or schema evolution affects data; no unauthorized production migration.

**Decision and alternatives:** Pin before/after contract, required identity, units, ordering, null semantics, allowed normalization and explicit loss. Test old/new fixtures, partial failure and recovery using disposable data. Reuse supported format where sufficient; avoid new datastore.

**Counterexample:** Export/import preserves count but loses leading-zero identifiers or rounds currency.

**Observable verification:** Assert per-record identity and required fields, totals, rejected cases and approved transformations; label recovery/rollback only if actually observed.

**Sources and limits:** QA-S26, QA-S03. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D27 — When is data drift or model quality relevant?

**Applicability / context:** AI/ML or data-driven application with intended distribution/decision behavior; not ordinary defect automatically.

**Decision and alternatives:** Separate data schema/quality, distribution change and predictive/task performance. Compare validated reference dataset and comparable sampling, label coverage and unknowns. Existing deterministic checks first; specialized tools only after rights/data/cost qualification. No collection beyond authority.

**Counterexample:** Different season shifts input distribution without model failure; stable aggregate hides subgroup change.

**Observable verification:** Check required data rules and task-specific outcome with denominator/representative cases; do not claim drift or quality from one sample.

**Sources and limits:** QA-S16, QA-S14, QA-S15. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

