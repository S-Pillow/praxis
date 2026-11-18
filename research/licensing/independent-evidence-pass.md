# Independent asset-rights evidence pass — 2026-11-18

**Scope:** evidence inspection after full-catalog structural validation. This ledger is **not** a mass clearance to redistribute copyrighted media. A repo-level open-source license does not automatically authorize copies of every embedded photo, trademark, preview, font or example.

## Verified independent source evidence (limited, item-level)

| Asset or family | Upstream catalog record | Independent source checked | Finding | Redistribution |
|---|---|---|---|---|
| Hallmark photo: `Gyedong-gil street with climbing plants at golden hour in Seoul South Korea.jpg` | `skills/hallmark/scripts/photos.json` (first item) | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Gyedong-gil_street_with_climbing_plants_at_golden_hour_in_Seoul_South_Korea.jpg) accessed 2026-11-18 | Commons names Basile Morin and CC BY-SA 4.0; matches Hallmark manifest. Attribution and share-alike conditions matter; exact local transformed preview matching remains unchecked. | **Blocked** until intended use, derivative treatment, and credit record are resolved |
| UI UX Pro Max pairing font **DM Sans** | `data/google-font-licenses.json` / `typography.csv` | [Google Fonts DM Sans OFL text](https://github.com/google/fonts/blob/main/ofl/dmsans/OFL.txt) checked in upstream Google Fonts repository | SIL OFL 1.1 license file is present. Exact binary, redistribution/derivative obligations still require checking. | Metadata only; binary blocked |
| UI UX Pro Max pairing font **Space Grotesk** | same | [Google Fonts Space Grotesk OFL text](https://github.com/google/fonts/blob/main/ofl/spacegrotesk/OFL.txt) | SIL OFL 1.1 license file is present. | Metadata only; binary blocked |
| UI UX Pro Max icon source **Phosphor core/react** | upstream icon manifest points to `@phosphor-icons/core`, `@phosphor-icons/react` | [Core LICENSE](https://github.com/phosphor-icons/core/blob/main/LICENSE) and [React LICENSE](https://github.com/phosphor-icons/react/blob/main/LICENSE) | MIT license files present in independent upstream repositories. Exact package tag and included asset checks remain open. | Metadata only; no bundled icon source |

## Stronger upstream provenance, but NOT independent asset license verification

- **Hallmark:** `skills/hallmark/scripts/photos.json` provides 755 Commons file pages, license labels, author, and asset URLs; only one Commons page independently checked above. No blanket verification of all 755, no local file-to-original/derivative mapping proven. Local photo copies, theme screenshot JPG/WEBP still blocked.
- **UI UX Pro Max:** 1,934 Google Fonts license claims use pinned `google/fonts` metadata revision `038b637da7b3fd956a4ed93ffc607c3d5e4ce172`, with eight exclusions. Metadata entries retained individually. Exact font license texts verified only for DM Sans and Space Grotesk; some entries report `UFL` or `APACHE2`, so do not assume all are SIL OFL. Bundled local `.ttf` files have per-folder OFL notices for many fonts and `ui-styling/LICENSE.txt` (Apache-2.0); individual binary checks remain open.
- **Open Design Agent Kit:** `packages/content/local/design-system-sources.json` explicitly records source-selection decisions and differences between `DESIGN.md` and tokens (e.g. placeholder vs rendered values). `packages/core/src/vendored/SOURCE.md` records Apache-2.0 upstream adaptation. `packages/content/assets/open-design/notices/` contains third-party MIT notices for some skills. These are genuine provenance indicators, **not** proof that branded tokens, logos, external imagery or all bundled example assets may be redistributed freely.
- **MengTo Skills:** many `agent-skills/web-design/*/demo/source.json` files record original Neuform URL, source/bundled SHA-256, and linked external Supabase image URLs and CDN runtime JS. Hashes help trace copies but do not confer reproduction rights. Treat such demos as **reference only**. Illustration `style.json` describes original stylecards, without independent author/title verification for each SVG.
- **Impeccable:** `NOTICE.md` credits third-party platform design skills (MIT). No independently corroborated per-screenshot/case-study image license found in inspected materials.

## Release rules

- `catalog_id` + pinned source commit + source path + reported license != asset rights clearance.
- `redistribution_status=metadata_only`, `reference_only` or `blocked_pending_review` means never bundle media/binaries by inference.
- Exact binary/source file, attribution, license/NOTICE, modifications/derivatives, reserved font names, trademark, and distribution target must be checked for any proposed packaged asset.
- If no source-level rights evidence can be established, preserve a **source pointer** and design knowledge, but do not import or publish that asset.

**Research outcome:** independent verification exists for a *small set* of source assets above. It does not justify broad clearance. Proceed with metadata enrichment and specialist implementation planning while keeping unresolved assets blocked.
