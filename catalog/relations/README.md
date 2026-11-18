# Cross-source overlap reconciliation

This is a **non-destructive relationship register**. Source entries are never discarded or rewritten simply because a name is similar.

- `name_overlap_candidate`: normalized names match; **not** proof of visual or technical equivalence.
- Review must inspect source descriptions and actual design tokens; only then may entries be marked `related`, `variant_of` or `semantic_equivalent`.
- An equivalent relationship **never** automatically authorizes removal of an original entry.
- Relations currently cover the first comparable source-level style/theme/design-system and illustration family sets, not entire product-guidance/knowledge catalogs.
- False positives are plausible: “Flat” illustration vs “Flat” UI design system are different asset classes.

The adjacent JSON file stores candidate relations while retaining both independent source catalog IDs.
