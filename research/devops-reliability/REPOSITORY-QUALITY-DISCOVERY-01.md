# Professional README and repository quality — discovery 01

Date: 2026-11-27. Owner requested genuinely polished READMEs and well-structured GitHub repositories, with deep study of Awesome README and Best-README-Template. Proposal for future Praxis requirements; not an imposed universal template or new governance. Baseline Praxis v1.3.0 already has the approved redesigned README. Preserve its content and version; do not reopen released work. [Source register](DEVOPS-SOURCE-REGISTER-01.md), [DevOps discovery](DEVOPS-RELIABILITY-DISCOVERY-01.md).

## 1. Structural baseline: Best-README-Template (DO-S05)

Actual full README and BLANK_README include centered logo/name/short description, shields, primary docs/demo/report/feature links, collapsible contents, overview, major stack, prerequisites, install, usage, roadmap, contributing, license, contact, acknowledgments, back-to-top and reference-style link definitions. Blank file identifies placeholder substitutions. Bug template captures issue, reproduction, expected behavior, environment and context; feature template captures summary, example and motivation. Changelog records template/rights changes; root Unlicense inspected. Reuse design principles, not necessarily exact template.

Strengths: clear predictable information architecture, modular sections, scannable page, call to action, discoverable issue reporting, contribution path, explicit license and credits. Limitations: examples include global npm latest, API key in source config, dummy links, hardcoded stack badges and personal contact placeholders. None should be blindly emitted. Remove placeholders and unnecessary sections; use pinned/supported versions, safe secret references, actual supported commands, real links and authentic ownership. Decorative badges must not substitute for evidence. Do not copy upstream logo or screenshots without rights.

## 2. Presentation and adaptation: Awesome README (DO-S04)

Actual index separates project examples, architecture examples, articles, talks, tools, GIF creation and feedback. Curator highlights concise purpose, strong identity, useful badges, practical installation, screenshots/GIFs, architecture explanations, navigation and contribution. Contributions must be human-authored and focused on actual project READMEs; no upstream contribution or review performed. CC0 waiver on list does not clear individual repositories/assets.

Direct sample DO-S06 HTTPie: compact branded intro, small feature/usage section, real example syntax and a clearly identified offline mode, links to detailed docs/support. Adapt compact first success and visible output for CLI; its popularity/statistics and external URLs are not transferable evidence. DO-S07 Abblix: explicit product integration model, supported runtime/platforms, package/upgrade/docs, license and limits, distinguishes certified and noncertified security profiles. Adapt precise platform and claim scope, not its badges, legal terms or claimed conformance. Other curator examples (e.g. dbt, Terminal.Gui) remain uninspected leads; no claims of their present contents. Raw Markdown inspected, not rendered desktop/mobile screenshots. 

## 3. Proposed shared knowledge pattern

README is product landing page **and** verified onboarding, not a dump of the entire PRD. Start with audience/task, product purpose, current status and first useful action; use clear visual identity where appropriate. Documentation design belongs with UI/UX; content architecture and correct interface/setup with Architecture; security and rights with Security; actual command/render/claim verification with QA; repository lifecycle, operational instructions and delivery with DevOps. Put original documentation/repo-quality knowledge in reusable shared guidance, referenced by relevant specialist/entry as appropriate. Do not add sixth mandatory agent or parallel AIPF documentation rule home. Use AIPF Chapter 13 existing authority/semantic/source parity.

### Adapt the page by repository type

| Type | First-screen and first success | Deep links / conditional additions |
|---|---|---|
| End-user application | Product purpose, real screenshot/demo, supported install, first task | Configuration, accessibility, privacy, troubleshooting, upgrade |
| CLI/library/SDK | Exact install/runtime, small working example and expected output | API reference, compatibility, error semantics, version and migration |
| API/service | Purpose, auth boundary, minimal safe local request, expected result | Schema, examples, errors, data retention, observability, runbook |
| Infrastructure/DevOps | Purpose, architecture and target prerequisites, safe plan/dry-run, cost/authority warning | Approved apply/teardown, state/recovery, incident and security docs |
| AI/agent skill/framework | What it does/does not do, entry/activation, local example, role/authority | Provider/host limits, data/tool permissions, evaluations, versioned knowledge |
| Research/internal repo | Question, scope/status, reproduction/inputs and expected artifacts | Method, evidence limits, licenses, access and private info boundaries |

Candidate design components: restrained hero/mark, readable one-line purpose, meaningful release/build/docs/license badges tied to actual targets, concise quick navigation, useful real screenshot or short demonstration with alt text and text equivalent, diagram for meaningful architecture, copy-paste-safe setup with versions and expected result, comparison table when useful, collapsible advanced detail, consistent heading hierarchy, relative links to pinned files, responsive and dark/light legibility. Prefer locally versioned, rights-cleared assets where practical; no fabricated product screenshots, badge claims, faux certification, animated decoration or contributor statistics merely for appearance. Use actual brand and accessible colors; no mandatory logo/diagram/demo for small utilities.

## 4. Repository quality beyond README

Use proportional profile, not compulsory file count. GitHub DO-S08–11 official web discovery supports README/relative links and community health files/issue forms. Proposed levels are decision aids, not compliance score:
- Essential: meaningful README, actual project identity and scope, explicit rights/license status, appropriate ignore rules, reproducible setup or source-read instructions, relevant tests and version/status; no secret/placeholder leakage.
- Collaborative/public: CONTRIBUTING, CODE_OF_CONDUCT where appropriate, SECURITY reporting with real private path, issue templates/forms, PR template where useful, change history/releases, maintainers/support routing, actual community profile and settings verified. Do not promise response SLA without capacity.
- Deployable/service: runbook, architecture/configuration, environment variable example without secrets, deployment/rollback/recovery, backup and incident procedures, operational evidence and cost constraints; only where applicable.
- Supply-chain/CI: source and artifact identity, meaningful checks, minimal permissions, immutable action refs when supported and qualified, protected target controls, release notes/changelog parity, dependency and license provenance; no required hosted scanner or badge. Document branch protection only if observed.
- Metadata: concise repository description/topics, actual homepage if exists, social preview with original rights, consistent names and version labels. Settings changes have external effects; obtain explicit authority. Do not publish private artifacts or create social assets without request.

A project may use root or docs/ structure as supported. Prefer one authoritative source for each responsibility; do not duplicate license, PRD, architecture or test evidence into divergent copies. Existing AIPF acceptance, source/authority and release boundaries remain controlling.

## 5. Verification proposal

| Concern | Observable check |
|---|---|
| First impression | Named reader can explain purpose, audience and next action without searching |
| Onboarding | Clean applicable environment runs documented safe setup/first success, actual command/output and version/limits retained; if no runtime, disclose |
| Semantic accuracy | Each material claim, project index and badge label agrees with actual source/config/CI/release and target version; catch DO-S01 index mismatch |
| Links/anchors | Relative paths, fragments, actual external destination/title/version, assets and reference definitions; existence alone insufficient |
| Visual rendering | Actual GitHub or equivalent supported Markdown render, mobile/wide, light/dark as applicable, alt text/contrast, useful image dimensions; distinguish static from actual render |
| Security/privacy | No secrets, sensitive screenshots/logs, unsafe default admin exposure or silent destructive commands; actual authority and setup |
| Repository health | Check actual files, applicable template syntax and observed settings, required docs/owner/license/reporting links; no badges-only quality claim |
| Release freshness | Tag, changelog, PRD, docs and badge/installation parity; prior histories preserved; actual published metadata separate |

Use existing stdlib/static checks and existing browser/owner review before new tooling; markdownlint/link checker optional after source/rights/installation/CI authority. Do not automatically run setup instructions that provision, upload, install, mutate, incur cost or probe networks. Examples with expected output are not runtime proof; label simulations. Do not force a complete repository overhaul for minor edits. Gate material claims and critical onboarding; aesthetic suggestions advisory unless approved criteria require them.

## 6. Proposed PRD inclusion and qualification

Include in next temporary DevOps PRD explicitly as cross-cutting repository-quality deliverable, with stable requirement IDs, original reusable decision cards and optional adaptable starter template(s), not upstream copied files. Consult across all relevant paths, no independent specialist runtime. Candidate acceptance: a compact CLI/library README and a deployable or AI project README using distinct profiles; test valid relative links, real safe first use, source-label parity, hidden placeholder detection, secret-free examples, owner visual review with appropriate rendering, correct classification of irrelevant sections, no new dependency/mandatory tool. Include bug/feature and PR-template examples only if actual repo warrants. Distinct Builder portability and standing regression remain existing product requirements. Need owner approval of exact scope and any actual repository modifications. No implementation, no change to released Praxis README now.

## Supplementary research — repository security and automation

[Discovery 02](DEVOPS-SECURE-AUTOMATION-DISCOVERY-02.md) extends repository-quality research with DO-S19–25. Use Scorecard as an optional source of bounded repository security findings, never as a complete repository-quality or compliance score. Verify actual community docs, reporting route, CI and released content separately. Awesome Actions is discovery only; qualify candidate versions, permissions, data flows, state changes and failure behavior. Existing Praxis workflow path filters omit README/docs; assess material documentation-only validation coverage in future authorized work. No required badge, external scan, publishing or workflow changes.

## Final operational-depth research

[Discovery 03](DEVOPS-OPERATIONAL-DEPTH-DISCOVERY-03.md) adds Actionlint (DO-S32) and Lychee (DO-S33) as optional candidates. Validate workflow grammar/expressions and local links/anchors first; external link checks bounded and authorized, status/redirect/cache/credential handling explicit. Actual workflow effects, source semantic parity, onboarding and rendered presentation remain distinct observations. No mandatory linter, service or new workflow.
