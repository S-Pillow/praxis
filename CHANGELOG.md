# Changelog

## Unreleased — Praxis v1.0.0 release preparation

Initial integrated Praxis product release, based on the accepted QUALITY-01 implementation. The product version is independent of AIPF v8.10.1 and the retained UI/UX v0.3 component identity.

- Unified entry, incorporated canonical framework, context-aware specialist registry and support for direct and distinct-agent execution.
- Portable Builder Payload guidance, quality-first synthesis and permanent scenario regressions.
- Cross-platform portability corrections, evidence attribution and independent workflow validation.
- Accepted QUALITY-01 baseline: 134 regression tests passed on Linux and Windows; VALIDATION-05 operator acceptance with notes. Native Codex discovery is unverified; later R4 PR and main CI both passed 136/136.
- Repository renamed to `S-Pillow/praxis`; Apache-2.0 approved for original Praxis and AIPF materials. R4 integrated and merged privately; tag and publication remain separate actions.

- Public-release safeguards: manual read-only enrichment verification, no bot commits to main, explicit source attribution and upstream content-manifest provenance.

- Final release correction: enforce canonical LF checkout bytes for framework references and frozen retrieval evidence, with a Git CRLF checkout regression. No framework version or catalog content changes.

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
