# SPECIALIST-UIUX-03 — bounded retrieval refinement

**Prepared:** 2026-11-24 (AIPF v8.10.1, Builder Agent)
**Status:** frozen local candidate on `experiment/specialist-uiux-03-refinement`. Unreleased; no version is assigned. Awaiting the separate fresh evaluation.
**Base:** SPECIALIST-UIUX-02 preservation commit `4ebee2648b49de22ef102100d0d4ff9eee9cf489`, on top of `951c0930` (benchmark) and `481bb188` (v0.2)
**Results:** [`retrieval-benchmark/experiments/specialist-uiux-03/`](retrieval-benchmark/experiments/specialist-uiux-03/)

## 1. Outcome

The five corrections were addressed with small changes to `scripts/recommend_design.py`. Every acceptance criterion held on the 17 benchmark cases:

- Useful queries: 13 → 15 of 16 scored cases against SPECIALIST-UIUX-02 (9 for v0.2). Both new useful cases, SYN-01 and SYN-07, are useful on frozen judgments alone.
- Cases with a directly actionable result: 9 → 12.
- Relevant results returned: 25 → 31 (frozen only: 23 → 28).
- Conflicts: 0 of 50 returned results. No case regressed against UIUX-02 or v0.2.

**All 17 cases were development evidence here, so these figures are not an independent evaluation.** SYN-04, SYN-07 and SYN-11 were used for refinement and are no longer reserved. Release readiness depends on the separate fresh evaluation.

## 2. Corrections, demonstrated causes and effects

Effects were attributed by disabling one correction at a time in-process on the final candidate. Records were inspected for every claimed cause.

| ID | Demonstrated cause | Change | Effect on the benchmark |
|---|---|---|---|
| R01 negation and reliance | "without relying on colour alone" was parsed as a colour prohibition. That marked the palette as preserved and removed "colour" from the query. Separately, "colour" never matched the catalog's American "color" | A negated part containing an exclusivity marker (alone, only, solely, exclusively, sole) becomes a reliance limit (`task_signals.not_sole_reliance`), not a prohibition. A part starting with "only" ("…, only flat surfaces") is a stated alternative and is skipped. Query alias colour/colours → color/colors | SYN-11: Color Only (grade 3) rises to first and Color Contrast (2) replaces Easing Functions (0). Disabling either the parse or the alias reverts this |
| R02 critique references | The critique design-reference role was always filled. SYN-11 got Sticker on the single word "order" | Critique keeps the theme or style role only when the request expresses visual-direction intent (style, aesthetic, theme, brand, identity, palette, typography and similar). Any design reference must share at least two query terms. A guideline-only shortlist fills to `--limit` (previously only audit and `preserve_identity`), except in the focused accessibility-correction scope | SYN-11 returns three guidelines instead of a guideline and an unrelated style (Gradient Mesh without R02). SYN-07, which asks about "the calm aesthetic", keeps Coral. With a style cue, the two-term rule still blocks Sticker for "Critique the visual style of the trading blotter order table" (regression test) |
| R03 platform terms | "web" matched Shopify Polaris's "web components" keyword in SYN-07 | "web" is excluded from query terms. Platform fit stays with `--platform`; priority detection is unchanged | SYN-07 design reference: Shopify Polaris (0) → Coral (1) |
| R04 ambiguous name matches | Investigated: the matches came from guideline names and keywords colliding with domain words, not from record weight. "support" (a verb in SYN-07, "support agents" in SYN-01) matched Autofill Support (8.34 of 8.36 in SYN-07). "help" in "help-desk" matched Consistent Help. "first" in "first-run" matched Mobile First (SYN-07) and Voice-First Multimodal | (a) "help" and "support" count only next to an interface noun (help center, support chat, inline help). (b) A word appearing only inside a hyphenated compound counts only for records containing the whole phrase. "desktop-first" and "mobile-first" stay priority signals | SYN-01: Autofill Support (0) → Bulk Actions (2), Keyboard Navigation (3), Submit Feedback (0). SYN-07: Heading Hierarchy (3) first. SYN-06: Form Labels (0) → Readable Font Size (2). SYN-08: two grade-3 records swap order |
| R05 stop words | "does", "can", "whether" were scored (for example "can" added 2.51 to Table Handling in SYN-11) | Added conservatively: does, did, can, may, might, whether, how, what, why, when, who, forms of be and have, they, them, without, never, rely, relying, relies. Negation and reliance are parsed from raw text before stop-word removal | No benchmark output depends on R05 alone in the final candidate. It removes grammatical score noise |

## 3. Rejected or limited corrections

- **General discount on name-only matches (rejected).** Many partial name matches are relevant: Heading Hierarchy, Contrast Readability, the charity palette (3), Loading Buttons (3), Inline Validation. A global discount would remove legitimate results, so record-name weighting is unchanged.
- **Global removal of help or support terminology (rejected, per scope).** Help-center, support-chat and inline-help requests keep the words, and "Critique the help center article page and its search" still returns Consistent Help.
- **Platform-word removal beyond "web" (not done).** "mobile" and "desktop" also carry interface priority, so removing them would weaken the protected desktop-first and mobile-first distinction.
- **Compound rule side effect (accepted, documented).** "Critique the first-run onboarding of a meditation app" now returns nothing. UIUX-02 returned Mobile First and Voice-First Multimodal, both matched only on "first". No inspected guideline or style matches the remaining words, so the empty result is honest but unhelpful. Not tuned further.

## 4. Comparative results (all 17 cases, identical judgment sets)

Judgments are frozen, then UIUX-01 post-hoc, UIUX-02 (`post_hoc_uiux02`) and UIUX-03 (`post_hoc_uiux03`). Every returned result in all three runs is graded. Denominators exclude the expected-empty case SYN-09.

| Metric | v0.2 | UIUX-02 | UIUX-03 |
|---|---|---|---|
| Useful queries, expanded (historical / development / formerly reserved) | 1/5, 6/8, 2/3 | 4/5, 7/8, 2/3 | 4/5, 8/8, 3/3 |
| Useful queries, frozen judgments only | 1/5, 5/8, 2/3 | 4/5, 7/8, 2/3 | 4/5, 8/8, 3/3 |
| Cases with a directly actionable result | 1, 3, 1 | 3, 5, 1 | 3, 6, 3 |
| Relevant results returned, total (frozen only) | 12 (10) | 25 (23) | 31 (28) |
| Conflicting / returned results | 9/39 | 0/48 | 0/50 |
| Follow-up usefulness (HIST-04, HIST-05, SYN-12) | 1/3 | 2/3 | 2/3 |
| SYN-09 abstention | incorrect | correct | correct |

Returned counts per case are within one of UIUX-02, so the gains do not come from returning more. Only SYN-01 (2 → 3) and SYN-11 (2 → 3) return more, and both add relevant results.

**Runtime:** a full 17-command run took 3.1 to 3.9 s for UIUX-03 and 2.9 to 3.5 s for UIUX-02 over three runs each. This is within noise, and no performance change is claimed.

## 5. Case-level changes against UIUX-02

**Newly useful**
- SYN-01: Bulk Actions (2), Keyboard Navigation (3) and Submit Feedback (0) replace Autofill Support (0) and Consistent Help (0).
- SYN-07: Heading Hierarchy (3) and Coral (1) replace Autofill Support (0) and Shopify Polaris (0).

**Improved**
- SYN-11: Color Only (3), Table Handling (2) and Color Contrast (2) replace Table Handling and Sticker (0).
- SYN-06: Readable Font Size (2) replaces Form Labels (0).

**Neutral**
- SYN-08: Disabled States and Focus States (both 3) swap order.

**Unchanged:** the other 12 cases, including HIST-03 (Keyboard Navigation first), SYN-09 (correct abstention) and HIST-05 (manual search ranking unchanged by design).

**Regressions:** none under the benchmark rules (lost usefulness, more conflicts, a lost or worse first actionable result, lost abstention, or a failure). Remaining weak results: SYN-01 Submit Feedback (0), and Coral in SYN-07, which is only tangential (1).

## 6. Acceptance criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | All five corrections addressed or dispositioned | Met | Sections 2 and 3 |
| 2 | "Without relying on colour alone" is not a colour prohibition | Met | `test_reliance_limits_are_not_prohibitions` (six phrasings, US and UK); SYN-11 signals |
| 3 | Genuine prohibitions remain effective | Met | `test_genuine_prohibitions_remain_effective`; SYN-10 and SYN-05 still conflict-free |
| 4 | Critique no longer fills a role with an unrelated theme | Met | SYN-11; `test_operational_critique_returns_guidelines_without_a_theme`; `test_style_critique_rejects_a_single_word_theme_match` |
| 5 | Legitimate visual-direction critique still works | Met | SYN-07 Coral; `test_style_critique_still_retrieves_a_visual_reference` |
| 6 | Incidental platform and grammatical terms do not justify recommendations | Met | SYN-07 Polaris removed; `test_platform_word_does_not_drive_matching` |
| 7 | Ambiguous name matches improve without suppressing legitimate matches | Met | SYN-01 and SYN-07; help-center, support-chat and inline-help tests |
| 8 | No new explicit conflicts | Met | 0/50 |
| 9 | UIUX-02 coverage preserved, no material case regressions | Met | 13 → 15 useful; none regressed |
| 10 | Keyboard guidance and correct abstention preserved | Met | HIST-03 rank 1; SYN-09 empty; backend test |
| 11 | CLI, catalog, provenance, licensing and manual-search compatibility | Met | Section 7 |
| 12 | Full regression suite passes | Met | Section 7 |

## 7. Verification and compatibility

- Complete suite: 90 tests pass. That is the 74 from SPECIALIST-UIUX-02, 13 new refinement tests in `tests/test_recommend_refinement.py`, and 3 new benchmark tests (17 → 20):
  - New: UIUX-03 judgment separation, pinned UIUX-02 hashes, and pinned UIUX-02 reproduction.
  - Repointed (not added): working-tree reproduction now targets the UIUX-03 results instead of UIUX-02's, which the pinned replay now covers.
- Pinned v0.2 still reproduces `baseline-v0.2-481bb18.json` and the retained historical outputs. Pinned UIUX-02 (`reference-specialist-uiux-02/`, hashes equal its freeze) reproduces `experiments/specialist-uiux-02/candidate-results.json` field for field. The only adjustment is its `implementation` label, recorded as `working-tree` when frozen.
- CLI: arguments, defaults (limit 3), the 1–5 limit, exit codes and all UIUX-02 output keys are unchanged. `task_signals` gains `not_sole_reliance`. Provenance, restriction, licence and token-excerpt fields are produced by the unchanged `reference()` function.
- Manual search and Design Index ranking are unchanged. `scripts/search_catalog.py` is byte-identical to UIUX-02, and the existing manual-ranking test against pinned v0.2 passes.
- Catalog entries are unchanged: 30 files, 5,500 records, sha256 `e3ae82ff…`.
- Output is deterministic: repeated runs are byte-identical.
- The UIUX-01 test-design defect (`test_full_run_reproduces_frozen_baseline` comparing the git revision, which failed at `951c0930`) and its UIUX-02 correction remain documented in the UIUX-02 report. `951c0930` was not amended.

## 8. Remaining limitations

- All 17 cases were used for refinement, and one evaluator wrote the cases, the frozen judgments and every post-hoc grade. The UIUX-03 grades (`post_hoc_uiux03`, 3 records) were assigned after seeing the output. No independent or blind evidence exists until the fresh evaluation.
- The reliance and visual-intent rules are lexical. Negations outside the existing pattern ("shouldn't", "can't") and reliance limits without the listed markers ("colour can't carry meaning by itself") are not recognised as reliance limits. In those cases colour stays in the query and nothing is prohibited. Visual intent expressed indirectly ("does it feel premium?") gets no design reference.
- "help" and "support" rely on a fixed interface-noun list, and unlisted interface contexts lose the term.
- The compound rule can leave a UI request with no matching terms, giving an empty result (first-run onboarding probe).
- Build-mode quality for weakly specified tasks is not addressed. For example, a reliance-only status board returns loosely related identity records.
- HIST-05 (manual search) remains not useful, because manual ranking is deliberately unchanged.
- Judgment coverage for SYN-11's pre-freeze Easing Functions result is retained in `post_hoc_uiux03` although the frozen candidate no longer returns it.

## 9. Recommendation

Hold at the frozen-candidate evaluation gate. The candidate meets every criterion on development evidence, but release readiness depends on the separate fresh evaluation set.
