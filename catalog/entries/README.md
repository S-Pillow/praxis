# Catalog entries

`starter.json` is a small **illustrative, source-linked set** prepared from inspected upstream files. It is *not* the complete library and does not claim full data validation. Keep every original source entry separate and record equivalence links in `related_entry_ids`.

The JSON schema is at `../schema/entry.schema.json`.

Before full import, pin upstream commits, capture all original columns and design tokens, check licensing, and run `python -m unittest discover -s tests`. Entries with `redistribution_status=metadata_only` or `reference_only` must never be treated as permission to bundle upstream assets.
