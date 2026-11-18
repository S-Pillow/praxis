# License / provenance review register

**Not legal advice.** Repository-level licenses are preliminary evidence, not blanket clearance for all third-party assets in a repository. For actual redistribution, capture source revision, exact file/blob, author, license/NOTICE, any embedded third-party dependency, attribution and modification record.

| Source | Repository license observed | Additional considerations | Current action |
|---|---|---|---|
| [Hallmark](https://github.com/Nutlope/hallmark) | MIT | README claims openly licensed/credited photos; each photo and theme preview needs original credit/license verification. Fonts may have separate licenses. | metadata/reference only; photo bundling blocked |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT | Font and Phosphor catalogs carry license/provenance snapshots; individual font binaries, icons, import URLs and included font assets need matching notices. | pairing/palette/style metadata; do not bundle font binaries |
| [Open Design Agent Kit](https://github.com/feimacode/open-design-agent-kit) | MIT repo; README identifies vendored open-design Apache-2.0 content | Preserve exact upstream Apache 2.0 notices/provenance and check brand-derived visual assets individually. | token references and metadata; no wholesale vendoring |
| [Impeccable](https://github.com/pbakaus/impeccable) | Apache-2.0 | Contains NOTICE.md third-party provenance; screenshots and case-study images separately need license checks. | techniques as references only |
| [MengTo Skills](https://github.com/MengTo/Skills) | MIT repo | Demos include images, textured grounds, external JS, SVG illustrations, and reference assets; per-file provenance needed. | illustration style metadata, no asset bundle |

## Item-level gate

No `redistribution_status=approved_for_bundle` until:
1. direct file path + immutable revision pinned;
2. license holder and exact license established (including embedded resources);
3. notices, attribution, share-alike/copyright or trademark limitations checked;
4. font/icon/photo dependencies inspected and embedding/commercial terms understood;
5. derivative/modification details recorded;
6. approved by the repository owner if risk/rights unclear.

Upstream source links and metadata references may be listed while rights review remains pending; do not assume this grants permission to rehost original preview screenshots or branded assets.
