# Source field map — initial observed fields

**Status:** field-level mapping starter; no full-catalog extraction yet. Multiple upstream entries with similar meaning must retain separate source records.

| Source | Actual upstream source | Source fields | Unified destination | Notes |
|---|---|---|---|---|
| Hallmark | `skills/hallmark/references/themes/index.json` | `themes[].slug` | `catalog_id` suffix / `source_path_or_key` | Keep original slug |
| Hallmark | same | `name`, `material`, `keywords` | `original_name`, `description`, `keywords` | Material is design-direction prose |
| Hallmark | same | `picture`, `file` | `preview_reference`, `source_path_or_key` | Links not redistribution permission |
| Hallmark | `site/themes/{slug}/tokens.css` | `--color-*`, `--font-*`, spacing/motion vars | `design_tokens` | Separate CSS source, preserve exact values on verified extraction |
| UI UX Pro Max | `.claude/skills/ui-ux-pro-max/data/styles.csv` | `Style ID`, `Style Category`, `Type`, `Keywords` | `catalog_id`, `original_name`, `entry_type`, `keywords` | Status active/supplemental/deprecated requires dedicated field in future revision |
| UI UX Pro Max | same | `Design System Variables`, `Framework Compatibility`, `Accessibility`, `Do Not Use For` | `design_tokens`, `compatibility_restrictions`, `review_notes` | Do not treat heuristic as universal rule |
| UI UX Pro Max | `data/colors.csv` | `Product Type`, `Primary`, `On Primary`, `Accent`, `Background`, `Foreground`, etc. | `original_name`, `design_tokens` | Preserve all semantic color role pairs in full import |
| UI UX Pro Max | `data/typography.csv` | `Font Pairing Name`, `Heading Font`, `Body Font`, `Best For`, `Google Fonts URL` | `original_name`, `design_tokens`, `compatibility_restrictions` | Font binaries not included |
| Open Design Agent Kit | `claude-design-systems/{name}/project/tokens.json` | `name`, `meta`, `color.tokens`, `type.families`, `spacing.tokens` | `original_name`, provenance, `design_tokens` | Preserve upstream `meta.upstream`; account for Apache 2 vendor content |
| Impeccable | `.agents/skills/impeccable/reference/critique.md`, `audit.md` | Named procedures and quality dimensions | `design_knowledge` entries | Knowledge reference, **not** invented palette/theme |
| MengTo | `agent-skills/illustration/{skill}/style.json` | `name`, `blurb`, `mechanism`, `palette[]`, `rules[]`, `cards[]` | `original_name`, `description`, `design_tokens`, `review_notes`, `preview_reference` | Cards/examples require file-level asset review |

The initial source inventory is intentionally illustrative; the full upstream datasets, their source commit SHAs, asset manifests and license lineage remain to be imported/verified.
