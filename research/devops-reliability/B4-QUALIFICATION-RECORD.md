# B4 qualification record — DevOps & Reliability v0.1 / Praxis v1.4.0 candidate

**Disposition:** implemented; deterministic regression GREEN; B4 not accepted or fully qualified. Independent DQ14 execution, fresh-reader/independent review, remaining scenario evidence and owner acceptance are open. Do not merge, tag, publish or consolidate the canonical PRD under this authorization.

## Identity and evidence

- Owner approved temporary PRD v0.1 and B1–B4 development. Exact approved source: [PRD](../../docs/DEVOPS-RELIABILITY-PRD.md), Git blob a19359548ec2f7d586763e414e758f483ee86c0c; SHA-256 c1a19ca79c56d742c417c7f0b9909275dae0cd813dca7eec910b2159dc0f0f50.
- Released recovery anchor: v1.3.0 and main 1749f9d3632efd1ab272a69e0738fdd6bd754932; released tree f180c8fe93222b07674fc8a05158c2cd40cf84a4. Both refs re-observed unchanged after testing.
- Research 61c59f908303fb27883d3cff688c304dda620cc6 retained. B1 60c8ce499746e4ec4abfcfceb226a41a186a901b; B2 f70dca01f871fd4b61c98cee387dd8190b41265e; B3 b869125d90c36696a694d6470c10b214f3ec3ea7. Draft PR [#19](https://github.com/S-Pillow/praxis/pull/19).
- First tested candidate 016d62662860a75c48a579596568522d406e630c; [CI run 46094786507](https://github.com/S-Pillow/praxis/actions/runs/46094786507): 188 tests, Linux 17.517s, Windows 22.992s, both OK. This is historical evidence, not the corrected candidate.
- Corrected implementation 68e3d34b1db742fc4a54d8c10a9f5c98f2e91a29, tree ad475e7a686b3fad09ba7f2cd9524ce19e7c65e8. [CI run 46094928636](https://github.com/S-Pillow/praxis/actions/runs/46094928636): actual checkout in both jobs was PR test merge 27e08a5cea36b24cf82760a5e51212f94765fa8e, whose parents and identical tree were independently inspected through GitHub API. Linux job [140823997722](https://github.com/S-Pillow/praxis/actions/runs/46094928636/job/140823997722), raw unittest 191 tests in 16.405s, OK; Windows [140823997498](https://github.com/S-Pillow/praxis/actions/runs/46094928636/job/140823997498), 191 tests in 29.299s, OK. Both terminal success. Observer: GitHub-hosted runners, raw log and API inspection by implementing Prompt Agent. Existing checkout/setup-python Node 20 deprecation warnings remain; not a newly introduced failure.
- Exact prior four registry entries tested; framework bytes, catalog, helper, existing workflows and canonical PRD/released README preserved. No new runtime dependencies; 9 new discovery-only CAP-R01–09 entries, 39 total. Twelve family guides/33 decision records and 9 shared repository decision records. Counts describe inventory only, not quality scores.
- Local direct execution: six initial example/negative-control tests passed in 4.163s under Python 3.13.5 on a transferred subset whose Git blobs matched original source. Full local checkout unavailable (GitHub DNS); actual full regression obtained on authorized CI instead. No local full-checkout claim.
- Actual same-context rendering of both original and corrected examples: MarkdownIt CommonMark, Chromium 144.0.7559.96, local stylesheet, blocked external network, 1120x800 and 375x812, light/dark. Source blobs for corrected CLI 81adf8298961c1a3a65e7e2bb2e158a911f445a2 and service 8db3e677395f74b6814e0a71755446994ef5f5dc match remote. Initial long service code preceded first useful command and duplicate H1. Corrected headings and command placement; all 8 corrected observations show viewport-width body, command first screen (CLI y394 wide/y526 narrow; service y443/y682), code-only overflow where needed. Images not applicable to text-only examples. Three additional deterministic tests check heading/command ordering, wrong service route and semantic link parity. Screenshots, observed geometry and local logs retained in downloadable evidence bundle in development conversation. This is equivalent-renderer evidence, not GitHub-native or independent visual acceptance.
- Source licenses and limits retained in research and SOURCES; original advisory synthesis, no third-party asset imports, no operational tool installation or live third-party execution. No assertion of current provider price, service SLA, actual branch protection or arbitrary license clearance.

## Acceptance reconciliation

Legend: O = observed bounded runtime/source/test evidence; S = source inspection and same-context decision exercise, not independent or operational runtime proof; P = additional required observation open. Multiple codes can apply. This ledger does not promote S or O to independent acceptance. Observer for S: implementing Prompt Agent. CI for O as identified above. External actors not yet assigned.

| Criterion | Evidence / disposition |
|---|---|
| DO-AC01 | O registry helper modes, missing skill and unknown-task behavior; S material operational request versus typo-only task. P independent semantic activation. |
| DO-AC02 | S DQ01 offline utility with one local user/no remote access: local CLI, no provisioning; DQ02 synthetic stateful background job with remote users: static alone insufficient, compare existing managed service to VM and local; actual traffic/region/limit/price not supplied, no cost guarantee or specific provider recommendation. |
| DO-AC03 | O DQ03 two successful commands but only one ran an oracle; CI checkout, logs, permissions and workflow file inspected. No build artifact inferred from test job. S design for lockfile/runtime/runner scope; P broader operational observer where material. |
| DO-AC04 | O DQ04 main/tag/test merge/tree identities reconciled, no publication. S approved artifact/digest, staging target and user-level verification needed before release; no live deployment. |
| DO-AC05 | S DQ05 synthetic plan with sensitive output and uncertain lock holder: keep plan private, confirm backend/holder and recover via owner-approved path; no force unlock/apply. No actual IaC run. |
| DO-AC06 | S DQ06 incomplete check mode, config write then restart failure: partial effect, do not report idempotence; inspect actual config/service, compare rerun and rollback only if authorized. No live automation run. |
| DO-AC07 | S DQ07 synthetic correct authoritative record, stale resolver or failed TLS: compare allowed resolver answer, connection, hostname/cert and app response, distinguish cache from origin. No external probing. |
| DO-AC08 | O DQ08 missing-vs-zero counterexample; S queue overflow can mean missing samples, remove PII/high-cardinality labels, compare sent/received/drop counters; DQ09 distinguish alert pending/firing from delivery. No telemetry platform run. |
| DO-AC09 | S sustained synthetic user error: bound incident impact using actual request outcome, stabilize within authority, retain logs and assign recovery observer; no SLA inference or production mutation. |
| DO-AC10 | O DQ10 archive integrity/checksum valid while required config absent; isolated synthetic restore and required-file oracle detect defect; S actual DB consistency, app usability, RPO/RTO remain dependent on real target. |
| DO-AC11 | S DQ11 strong aggregate with missing release provenance or excess permission: investigate individual control with exact identity; no automatic approval or Scorecard runtime claim. |
| DO-AC12 | S DQ13 synthetic 1,000 requests normally, 10,000 peak; compare billable units, retention/egress and teardown, alert not hard cap, estimate not actual; no vendor prices invented. |
| DO-AC13 | S DQ12 choose existing logs for adequate trace correlation before new integrations; track model/prompt/deploy versions, redact data, separate quality eval from telemetry, verify retention and billable usage. No provider connected. |
| DO-AC14 | O actual initial example first-action/hierarchy flaw, bounded correction and observed rendered improvement; unknown service route and CLI missing-file negative tests. S causal network/infra reasoning is hypothetical. |
| DO-AC15 | O retained source register and exact discovery-index extension tests; S point-of-use maintenance/license/permissions/data flow/cost must be qualified; no runtime endorsement. |
| DO-AC16 | O direct execution and registry/entry role constraints; P fresh distinct Builder + separate reviewer DQ14. Prepared input packet only; no claim executed or issued to an available actor. |
| DO-AC17 | S synthetic hosted stateful service: architecture selects storage/runtime contract, Security specifies trust/secret boundaries, QA supplies user/recovery oracle, UI handles outage semantics, DevOps controls promotion/recovery; shared docs describe truth, AIPF remains sole authority. P independent composition observation. |
| DO-AC18 | O both full standing+affected CI jobs 191/191, source identities, registry/fallback, protected framework, recovery anchor; P independent DQ14 and fresh review, owner B4 decision. B5 not authorized. |
| RQ-AC01 | O two distinct original executable examples, CLI vs loopback service; S content/profile suitability review. No real deployed service implied. |
| RQ-AC02 | O first action visible in corrected renders; P fresh-reader comprehension, independent visual judgment. |
| RQ-AC03 | O CLI actual first success and missing file; service actual loopback success and unknown-route 404; both clean CI runner tests. No package install claim or hosted deployment. |
| RQ-AC04 | O relative links/anchors and wrong-but-resolving destination negative control; exact release/tag/source identities; S full material claim/badge parity must apply to B5 release docs then. |
| RQ-AC05 | O actual local rendered views 8 corrected combinations; same-context inspection, no GitHub-native/accessibility certification; P independent reviewer where material. |
| RQ-AC06 | S repository health/community/security guidance and actual accessible source files; actual server-side settings/enforcement not assumed. P independent profile review. |
| RQ-AC07 | O original text/examples and reference-only sources retained; no imported media/brand assets; source-level license restrictions remain. |
| RQ-AC08 | O shared guidance link/entry access, registry preservation, no sixth specialist/new runtime. |
| RQ-AC09 | O existing CI path-filter limitation recognized in research, unchanged; future correction separate authorization. |
| RQ-AC10 | O scoped README-example correction retained history and original command behavior, no broad makeover; S hypothetical typo-only change needs narrower proof than operational change. |

## Requirements coverage ledger

All 68 stable IDs retain approved meaning. The following source/acceptance crosswalk records implementation coverage and open evidence, not a blanket claim that each MUST is qualified. DO-D ranges refer to progressive family records, RQ-D to shared records. Individual criterion status above controls interpretation.

| IDs | Implemented knowledge and acceptance references |
|---|---|
| DO-F01–03 | skill/entry, DO-D13–15, DO-AC01–02 |
| DO-F04–06 | DO-D01–09, DO-AC03–04/18 |
| DO-F07–10 | DO-D10–17, DO-AC02/05–07 |
| DO-F11–13 | DO-D18–23, DO-AC08–09 |
| DO-F14–15 | DO-D24–25, DO-AC10 |
| DO-F16–18 | DO-D26–31 and AI operations card, DO-AC11–13 |
| DO-F19–20 | skill, operational transition cards, DO-AC03–04/15/18 |
| DO-F21–23 | DO-D32–33, diagnosis and optional capability guidance, DO-AC07/14–15, RQ-AC03/10 |
| DO-F24–26 | skill/entry, registry, DO-AC16–18; distinct Builder open |
| DO-K01–03 | INDEX, all guides, conditional context/current-fact separation, DO-AC01–02/15 |
| DO-K04–05 | SOURCES, research register, reference-only rights, DO-AC15/18 |
| DO-K06–07 | positive/negative decision cards and controlled transition guidance, DO-AC03–10/14 |
| DO-K08–10 | existing shared capabilities + CAP-R01–09, fallback and retained research, DO-AC15/18 |
| DO-N01–03 | advisory file-based neutral scope, protected framework/registry, selective consultation, DO-AC01–02/18 |
| DO-N04–07 | identity, privacy and rights constraints; no new runtime, DO-AC04/08/15/18, RQ-AC07 |
| DO-N08–09 | direct/portable role and practical alternatives, DO-AC02/16; independent portability open |
| DO-N10–12 | evidence and failure boundary, accessible docs, DO-AC08–10/14/18, RQ-AC02/05/10 |
| RQ-F01–05 | profiles, examples, RQ-D01–03 and verification, RQ-AC01–03/05 |
| RQ-F06–08 | verification, RQ-D04–06, RQ-AC03–05 |
| RQ-F09–11 | repository-health, RQ-D07–09, RQ-AC04/06/09 |
| RQ-F12–14 | asset rights, proportionality, shared access, RQ-AC07–10 |
| RQ-K01–02 | shared INDEX/cards and examples, RQ-AC01–03/08 |
| RQ-K03–04 | SOURCES and verification, RQ-AC03–07 |
| RQ-K05–06 | original examples and scoped profile/brand guidance, RQ-AC01–03/05/10 |

## Remaining work and stop

Do not call this accepted B4. DQ14 requires a fresh Builder with only portable authorized inputs and an independent reviewer, including meaningful negative and scope checks. No such independently assignable actor is available in this session. A prepared packet is retained separately; preflight and actual actor/root must be confirmed before issue. A fresh reader/reviewer should inspect corrected examples and actual evidence, challenge semantic activation and composed guidance, and distinguish scenarios from runtime. Direct source/fixture evidence does not substitute. Record actual returned artifacts, commands/status, observers and unresolved findings; corrections stay within authorized B1–B4. Then reconcile all criteria and request owner B4 acceptance. No permission to treat owner acceptance as B5 authorization.

This record is evidence-only and is not a product/runtime/acceptance claim for a different tree. If appended to the candidate, inspect the exact delta and any resulting CI before relying on transferable evidence. Historical CI remains tied to the tested tree.
