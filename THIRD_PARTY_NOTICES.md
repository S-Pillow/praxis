# Third-party materials and provenance

Original Praxis source, documentation and the incorporated AIPF framework are licensed under [Apache-2.0](LICENSE). This grant applies to material the project is entitled to license, not to third-party material. See [NOTICE](NOTICE).

Praxis catalogs information from other projects. Records include source-derived descriptions, labels, values, tokens, restrictions and reference URLs. The normalization and enrichment work does not relicense those extracts. The original licenses, copyright notices and applicable attribution requirements continue to apply. License texts retained below are copies of the identified upstream files; the root license is the standard Apache-2.0 text, not a replacement for an upstream license.

| Source | Upstream terms and preserved notices | Scope |
| --- | --- | --- |
| [Hallmark](https://github.com/Nutlope/hallmark/blob/04977e15f3dfd6ee4b74c887dac3eb52665d6c92/LICENSE) | [MIT](licenses/hallmark-MIT.txt), Copyright 2026 Hallmark contributors | Theme metadata and adapted token extraction; photo pointers and credits; separate asset rights |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/f2cc36555984fbfb08f1dca037da2467578f33d2/LICENSE) | [MIT](licenses/ui-ux-pro-max-MIT.txt), Copyright 2024 Next Level Builder | CSV and metadata extraction, including font-family and icon metadata; separate upstream rights |
| [Open Design Agent Kit](https://github.com/feimacode/open-design-agent-kit/blob/1b3832c3452720f028a96b1bdab805ecc1aa3213/LICENSE) | [MIT](licenses/open-design-agent-kit-MIT.txt), Copyright 2026 Iven Xu; [awesome-ios-design-md MIT](licenses/awesome-ios-design-md-MIT.txt); [ux-ui-agent-skills MIT](licenses/ux-ui-agent-skills-MIT.txt) | Indexed and extracted descriptions, design-system tokens and metadata; vendored and brand-derived material requires source-specific review |
| [Open Design](https://github.com/nexu-io/open-design/blob/89e64d813bb1c7a11519b3f668f011f7017637d7/LICENSE) | [Exact observed upstream license](licenses/open-design-upstream-LICENSE.txt), Copyright 2026 Open Design contributors | Provenance via Agent Kit's dated content manifest; its observed license changes standard Apache-2.0 wording. Do not assume identical terms or blanket coverage of catalog extracts. |
| [Impeccable](https://github.com/pbakaus/impeccable/blob/d41d9860b0094dcb68030657da63461212835aaa/LICENSE) | [Exact observed upstream license](licenses/impeccable-upstream-LICENSE.txt), Copyright 2025 Paul Bakaus; [upstream NOTICE](licenses/impeccable-NOTICE.md) | Reference metadata and extracted guidance; underlying MIT platform guidance attributed to ehmo ([license observed on default branch](licenses/platform-design-skills-MIT.txt), not a pinned source proof). |
| [MengTo Skills](https://github.com/MengTo/Skills/blob/3cc93458c4949c39a04e938ea7892a1d6d3d40bf/LICENSE) | [MIT](licenses/mengto-skills-MIT.txt), Copyright 2026 Meng To | Extracted stylecard descriptions and design guidance; demo and SVG asset rights separate |
| [Phosphor Icons](https://github.com/phosphor-icons/react/blob/v2.1.10/LICENSE) | [React v2.1.10 MIT](licenses/phosphor-react-MIT.txt), Copyright 2020 Phosphor Icons | Names, categories and metadata; core v2.1.1 license reference not independently resolved at that exact version |
| [Google Fonts](https://github.com/google/fonts/tree/038b637da7b3fd956a4ed93ffc607c3d5e4ce172) | Individual family terms, including OFL, Apache and UFL labels | Family metadata, not permission to bundle font files |

### Open Design design-system extracts

The 198 design-system records in `catalog/entries/open-design-design-systems.json` are normalized extracts, not unchanged copies of upstream token files. The immediate source is Agent Kit at `1b3832c3452720f028a96b1bdab805ecc1aa3213`; the upstream content manifest dated 2026-10-22 identifies `open-design-v0.24.1` as Open Design commit `89e64d813bb1c7a11519b3f668f011f7017637d7`. The exact license at that commit matches the retained `open-design-upstream-LICENSE.txt`. Agent Kit also contains locally adapted design systems, including material attributed to awesome-ios-design-md under MIT and independently re-authored concepts attributed to Bergside/typeui.sh. [Bergside MIT notice](licenses/bergside-awesome-design-skills-MIT.txt) is retained as a precaution. Original notices are retained; no endorsement, brand fidelity rights or permission to reproduce third-party artwork, logos or font binaries is implied. See [provenance resolution and remaining scope](research/licensing/open-design-provenance-resolution.md).

The source register, pinned source paths and historical research record provenance and the limits of the earlier review. Catalog records with `metadata_only` or `reference_only` status are not asset redistribution approvals. The project does not bundle third-party font binaries, photos or screenshot files in this candidate. The Hallmark Studio token record includes a small SVG data URI for a grain effect; that source-derived token remains subject to upstream terms. Source links, names and trademark references do not imply endorsement.

- [Source license register](research/licensing/source-license-register.md)
- [Independent licensing evidence](research/licensing/independent-evidence-pass.md)
- [Pinned upstream sources](catalog/provenance/pinned-upstream-sources.md)
- [Source field map](catalog/mappings/source-field-map.md)
- [Framework identity](framework/README.md)

This notice preserves observed attributions and describes boundaries. It is not a completed item-level legal clearance or permission to change repository visibility. Inspect actual copied material, applicable licenses and source-specific notices before further redistribution. If rights are uncertain, retain source pointers rather than unapproved media or expressive extracts.

## DevOps and repository-quality reference material

The v1.4.0 additions are original advisory synthesis and synthetic illustrative examples. The [DevOps source register](research/devops-reliability/DEVOPS-SOURCE-REGISTER-01.md), [DevOps sources](skills/devops-reliability/SOURCES.md) and [repository-quality sources](knowledge/repository-quality/SOURCES.md) preserve 55 source IDs and reference-only dispositions. No external tool code, README, screenshots, workflows or media were imported. Root license metadata does not clear independently licensed components or assets; qualify exact rights and operational terms before any later reuse. The shared discovery records are not selected dependencies.
