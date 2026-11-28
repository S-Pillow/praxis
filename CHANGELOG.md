# Changelog

## v1.4.0 — DevOps & Reliability and Repository Quality (source candidate)

- DevOps v0.1: plan, diagnose and review; 12 guide families, 33 original decision cards; nine additional discovery records (39 total). Shared repository quality adds nine cards and two illustrative README profiles, not a sixth registered specialist.
- Owner accepted corrected B4 `44749d2` PASS WITH NOTES: 192/192 on Linux and native Windows, separate Linux reproduction, corrected synthetic fixture and mutation checks, native GitHub rendering and bounded advisory observations. Same-model/scenario-overlap and settings-observation limits retained.
- Consolidate 68 approved requirements and 28 acceptance criteria into [PRD v1.5](docs/PRD.md#15-devops--reliability-and-shared-documentation--repository-quality), preserve 55 source records and existing specialist/framework behavior; align repository documentation and release identity. [Preparation and qualification](docs/releases/1.4.0.md). Publication is separately authorized and verified; source changelog is not proof of publication.

## v1.3.0 — QA & Engineering Quality

- QA v0.1: plan, diagnose and review; 12 guide families, 37 original decision cards, six discovery-only records (30 total).
- Additive test, diagnosis, test-effectiveness, failure/recovery, data and AI/agent evaluation guidance; no mandatory runtime, scanner or service.
- Corrected B4 candidate `b36e6f5`: 173/173 on Linux and native Windows; distinct Builder 19/19 reported and reproduced, nine independent reviewer tests, bounded behavioral observation and 42 requirements/18 acceptance criteria reconciled. Owner accepted and authorized B5.
- Consolidate QA requirements into [PRD v1.4](docs/PRD.md), preserving stable identifiers, original history, 33 QA source identifiers and 14 deferred cross-specialist leads. [Release qualification and limitations](docs/releases/1.3.0.md).

## v1.2.0 — Security & Privacy

- Security & Privacy v0.1: material design, harden and review; nine progressive guides, 36 original decision cards.
- Four discovery-only capability records; 24 shared records total. No mandatory scanner, runtime, integration or separate governance.
- B4 accepted implementation `c6393f6`: 163/163 standing tests on Linux and native Windows. Independent Builder v2 22/22 reproduced and 14/14 reviewer checks after four v1 findings. Owner accepted and authorized B5.
- Consolidate product and specialist requirements into [PRD v1.3](docs/PRD.md), preserving IDs, historical revisions and future QA/DevOps boundaries. See [qualification and release record](docs/releases/1.2.0.md) for exact identities and limits.

## v1.1.0 — Architecture & Engineering Design

- Architecture v0.1: design, evolve and critique; progressive local decision guides.
- Shared, independent capability discovery and point-of-use qualification guidance.
- Additive any-path registry and optional lookup; existing UI contract retained.
- B5 qualification: 155/155 standing tests passed on hosted Linux and native Windows on the accepted implementation tree; independent disposable Builder exercise passed after correction (25 separate tests). Owner accepted the candidate and authorized integration and publication. See [release qualification and limitations](docs/releases/1.1.0.md) for source identities and publication reconciliation.

## v1.0.0 — Praxis

Initial integrated Praxis product release, based on the accepted QUALITY-01 implementation. The product version is independent of AIPF v8.10.1 and the retained UI/UX v0.3 component identity.

- Unified entry, incorporated canonical framework, context-aware specialist registry and support for direct and distinct-agent execution.
- Portable Builder Payload guidance, quality-first synthesis and permanent scenario regressions.
- Cross-platform portability corrections, evidence attribution and independent workflow validation.
- Accepted QUALITY-01 baseline: 134 regression tests passed on Linux and Windows; VALIDATION-05 operator acceptance with notes. Native Codex discovery is unverified; R4 PR and main CI passed 136/136; final verified tip regression **137/137**.
- Repository renamed to `S-Pillow/praxis`; Apache-2.0 for original Praxis and AIPF materials; residual third-party redistribution risk accepted with notices and asset restrictions intact.
- Public-release safeguards: manual read-only enrichment verification, no bot commits to main, explicit source attribution and upstream content-manifest provenance.
- Final release correction: enforce canonical LF checkout bytes for framework references and frozen retrieval evidence, with a Git CRLF checkout regression. No framework version or catalog content changes.
- Published 2026-11-25: public repository, protected `main`, tag `v1.0.0`. Verified implementation commit `4009f436ad3cff02a34749988e6e4da25000e248`.

### QUALITY-01 corrections

- Correct specialist discovery YAML and CI path coverage, Catalog Explorer keyboard/search/mobile behavior, Saved search matching, commerce/color aliases and focused accessibility correction wording.
- Strengthen specialist retrieval budget, exact design-token contrast checks and framework identity labels. Prior v0.3 evidence remains historical; no release claimed.

## v0.3 — UI/UX Specialist

Retrieval-quality release of the agent shortlist (`scripts/recommend_design.py`). The specialist procedure, governance boundaries, catalog (5,500 records) and manual search ranking are unchanged. AIPF v8.10.1 remains authoritative.

### Retrieval improvements

- **Restrictions are not evidence.** "Avoid: …" and "Avoid for: …" text is returned unchanged but never scored. A stated desktop-first or mobile-first priority excludes records that advocate the opposite priority, independent of `--platform`.
- **Explicit constraints.** Prohibited items ("do not use dark mode or glassmorphism") are removed from the query and exclude matching identity records. A limit on exclusive reliance ("without relying on colour alone") is not a prohibition.
- **Preservation versus redesign.** "Keep the current theme", "without changing its established appearance" or "do not alter the look and feel" protects the existing identity, and the shortlist then holds usability guidelines (`selection_scope: preserve_identity`).
  - A prohibition implies preservation only when it names a bare identity part ("no new colours or fonts"). A qualified prohibition ("avoid saturated accent colors") constrains a new design.
  - A preservation instruction no longer cancels a prohibition in the same sentence.
  - Preserve and request cues apply to their own part of a sentence ("keep the palette and choose a new font pairing").
  - Explicit redesign requests stay available.
- **Critique.** A theme or style reference is offered only for visual-direction critiques, and it must share at least two query terms. Usability and operational critiques return guidelines.
- **Lexical noise.** Grammatical words, the platform word "web", "help" and "support" outside interface contexts, and words that occur only inside hyphenated compounds no longer drive matches. The British "colour" matches "color".
- **Eligibility and abstention.**
  - Native platform labels count as mobile.
  - Framework guidance requires the framework to be named.
  - Clearly non-visual work returns no references (`non_visual_task`).
  - A blank request or missing catalog is an error, not an empty result.
- **Output.** Arguments, defaults (limit 3), the 1–5 limit and all v0.2 keys are unchanged. Additions: `task_signals`, and new `selection_scope` values.

### Evidence

All evidence is in `research/evaluations/`. The figures below are development and regression evidence. Only the fresh evaluation was withheld during development.

- **Pilot (UIUX-01):** the v0.2 failure modes and a frozen 17-case retrieval benchmark (`retrieval-benchmark/`). The main findings:
  - restriction text was scored as evidence (Mobile First for a desktop-first task);
  - identity roles were always filled, regardless of preservation instructions;
  - prohibited words became query terms;
  - backend tasks received themes.
- **Benchmark (v0.2 → v0.3)**, measured on 16 scored cases:

  | Metric | v0.2 | v0.3 |
  |---|---|---|
  | Useful queries | 9 | 15 |
  | Useful on original frozen judgments alone | 8 | 15 |
  | Cases with a directly actionable result | 5 | 12 |
  | Conflicting results | 9 of 39 | 0 of 50 |

  The expected abstention (SYN-09) is now correct.
- **Fresh evaluation:** seven withheld Prompt Agent queries, run once against the frozen UIUX-03 candidate (`retrieval-benchmark/fresh-evaluation-specialist-uiux-03/`). Two preservation-versus-prohibition defects (PA-02, PA-05) were corrected for v0.3, along with related phrasings found in PR review. The rerun is in `retrieval-benchmark/experiments/specialist-uiux-04/correction-results.json`. Only PA-02 and PA-05 changed, and none of the 17 benchmark cases changed.
- Reports:
  - `2026-11-24-url-activity-scanner-uiux-pilot.md`
  - `2026-11-24-specialist-uiux-02-retrieval-experiment.md`
  - `2026-11-24-specialist-uiux-03-refinement.md`

### Known limitations

- One evaluator wrote the benchmark cases and graded most results. All benchmark cases and the seven fresh queries have now been seen during development, so no held-out evidence remains.
- The interpretation rules are lexical. They miss negations outside the supported pattern ("shouldn't", "can't"), unlisted interface contexts for "help" and "support", and visual intent that is expressed indirectly.
- Some UI requests return empty or weak shortlists. Examples:
  - a support console critique that preserves the brand (PA-03);
  - first-run onboarding;
  - "do not introduce new colours or fonts" redesigns;
  - a repair task whose palette matched the backend word "database" (PA-07).
- A negated phrase can absorb trailing words ("avoid neon colours in this new fitness app" also prohibits "fitness").
- A protected identity word can still act as matching evidence. In PA-05, Focus Appearance matched on "appearance".
- At v0.3, the plural "colours" mapped to "colors" and could miss singular catalog terms. Addressed in the accepted QUALITY-01 candidate; the original v0.3 limitation remains historical.
- Manual search ranking is unchanged, so the HIST-05 follow-up search remains weak.
- Retrieval quality is not proof of better rendered design.

### Rollback

v0.2 is commit `481bb188453b14108890ef0b803249759c5363f4`. v0.3 is integrated by a merge commit, so it can be reverted through a normal PR:

```bash
git switch main && git pull
git switch -c revert/ui-ux-specialist-v0.3
git revert -m 1 <v0.3 merge commit>
git push -u origin revert/ui-ux-specialist-v0.3   # then open and merge a PR
```

To inspect or use v0.2 without changing `main`, run `git switch --detach 481bb188`.
