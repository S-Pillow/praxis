# SPECIALIST-UIUX-02 — retrieval improvement experiment

**Prepared:** 2026-11-24 (AIPF v8.10.1, Builder Agent)
**Status:** experimental, unreleased, uncommitted working state on `experiment/specialist-uiux-02-retrieval`. No new specialist version is assigned.
**Base:** benchmark-preservation commit `951c0930444e06a8c811acb17a7d5ac12255eab5` (on top of v0.2 `481bb188`)
**Benchmark:** [`retrieval-benchmark/`](retrieval-benchmark/README.md); results in [`retrieval-benchmark/experiments/specialist-uiux-02/`](retrieval-benchmark/experiments/specialist-uiux-02/)

## 1. Outcome

Bounded, dependency-free changes to `scripts/recommend_design.py` (and an opt-in addition to `scripts/search_catalog.py`) met all ten acceptance objectives on the historical and development cases:

- Historical-query usefulness rose from 1/5 to 4/5, measured with frozen judgments alone.
- Constraint conflicts fell from 9 of 34 returned results to 0 of 41 across the historical and development cases.
- SYN-09 now abstains, and Keyboard Navigation remains first for HIST-03.
- The reserved cases did not regress (useful 2/3 before and after; conflicts 0 before and after). They did not improve on the two critique cases, and they exposed defects that are reported in section 8 and were not tuned.

These results describe retrieval on 17 benchmark cases. They do not establish that the specialist improves design work overall.

## 2. Demonstrated root causes and remaining hypotheses

Demonstrated by per-term BM25 breakdowns against actual source and catalog records:

| Failure | Cause | Evidence |
|---|---|---|
| HIST-02 Mobile First for a desktop-first task | Restriction text "Avoid: Desktop-first causing mobile issues" was scored as positive evidence; "desktop" and "first" supplied the whole score | Score 11.33 = 4.54 + 6.79 from restriction terms |
| HIST-01 Midnight; SYN-01 and SYN-05 replacement identity | Build and critique modes always fill direction, palette, typography or design-reference roles; nothing recognised "keep the current theme" or "do not introduce new colours or fonts" | Role structure in `GROUPS`; v0.2 SYN-05 returned 3 of 3 conflicting records |
| SYN-10 dark glassmorphic style | Prohibited words ("dark mode", "glassmorphism") were positive query terms | Modern Dark (Cinema Mobile) matched on its "dark mode" and "glassmorphism" keywords |
| Grammatical words as evidence | "its" (HIST-01, Midnight 3.89) and "not" (stage 1 SYN-10: Focus Not Obscured scored only on "not") were not stop words | Per-term breakdown |
| HIST-04 empty | `search_catalog.py --specialist-use critique` admits 2 of 5,500 records (1 source-inspected, both `design_knowledge`) | Pool counts below |
| `--platform mobile` missing native guidance | `compatible()` compared the platform string exactly, so "iOS/Android/React Native" (32 guidelines) never matched `mobile` | Pool counts below |
| SYN-09 theme for a backend change | No path for non-visual work | v0.2 returned Newsprint |

**Scope of the critique finding.** The two-record count applies only to the search follow-up filter. In `recommend_design.py` critique mode, the usability role draws on 196 audit-tagged guidelines (110 with `--platform web`, 70 with `mobile`, 62 with `desktop`). The design-reference role draws on 139 themes and styles (89 for mobile or desktop). All of these require `evidence_status = source_inspected`. The real critique weakness is that the design-reference role always returns a replacement theme or style.

**Hypotheses not demonstrated or not addressed:**

- Record-name weight (×8). Lowering it to ×4 or ×2 brought no measurable gain on development cases, so it was kept.
- Domain nouns colliding with guideline names ("help", "support" in SYN-01).
- "Avoid for:" audience clauses as conflicts (for example "children's apps").
- A platform word in the query ("web") acting as a lexical match (exposed by SYN-07; section 8).

## 3. Interventions

All changes are in the agent shortlist (`recommend_design.py`). The shared search module gains only an opt-in field function and a wider critique filter, so manual search and Design Index ranking are unchanged (verified against the pinned v0.2 module).

1. **Restriction semantics.** `positive_fields` scores name, type, keywords and description only. Restrictions are returned unchanged and used only for explicit conflicts. A record conflicts with a stated interface priority if it advocates the opposite ("mobile first", or "mobile" in its name, for a desktop-priority task) or if its "Avoid" text discourages the stated priority.
2. **Explicit negative constraints.** Negated phrases ("do not use…", "without…", "no…") become prohibited items. Statements of absence such as "no existing brand" are excluded. Prohibited items are removed from the query and exclude theme, style, design-system, palette, font and motion records whose positive text contains them. A generic head noun stands for its modifier, so "dark mode" prohibits dark grounds.
3. **Identity intent.** Clause-level cues distinguish protected identity ("keep", "preserve", "established" plus theme, identity, brand, design system, palette, colours, fonts or typography) from explicit requests ("create" or "choose" plus the same objects). Protected roles are suppressed unless explicitly requested. When every identity role is suppressed, the scope is `preserve_identity` and the shortlist contains guidelines.
4. **Eligibility.**
   - Audit and `preserve_identity` shortlists fill up to `--limit` with guidelines scoring at least 50% of the best match. The 50% threshold was set before measurement and not tuned.
   - The focused accessibility-correction scope is unchanged.
   - Platform labels are normalized: "iOS/Android/React Native" and "native" count as mobile, and "Mobile"-labelled guidelines are eligible for a web interface whose priority is mobile.
   - Framework labels ("React/Next.js") require the framework to be named in the request. Admitting them as "web" in an earlier stage-2 attempt let React code-performance rules match incidental words, so it was reverted.
   - The search filter `--specialist-use critique` also admits audit-tagged records, matching the pool `recommend_design.py` already uses for critique.
5. **Ranking.** Grammatical and generic words ("its", "not", "while", "where", "per", "several", "show", "clearly" and others) are excluded from recommendation queries, and "desktop-first" contributes only "desktop".
6. **Abstention and failure.**
   - A request with backend cues and no interface cues returns no references (`selection_scope: non_visual_task`).
   - A blank task exits with status 2.
   - A missing catalog exits with status 1 in both CLIs, instead of producing an empty result.

**Compatibility.** Arguments, defaults, the 1–5 limit and all v0.2 output keys are unchanged. Additions:
- a `task_signals` object;
- new `selection_scope` values (`preserve_identity`, `non_visual_task`);
- errors for a blank task or missing catalog.

The `use_boundary` and `selection_method` texts are identical.

## 4. Intermediate findings (historical and development cases only)

Each stage was run from saved script copies with the same judgment sets.

| Stage | Historical useful | Development useful | Relevant returned (historical + development) | Conflicts / returned | SYN-09 |
|---|---|---|---|---|---|
| v0.2 | 1/5 | 6/8 | 10 | 9/34 | incorrect |
| 1. Restrictions and explicit constraints | 2/5 | 6/8 | 11 | 6/34 | incorrect |
| 2. Intent and eligibility | 4/5 | 7/8 | 21 | 0/43 | incorrect |
| 3. Ranking and abstention (candidate) | 4/5 | 7/8 | 21 | 0/41 | correct |

- **Stage 1** removed Mobile First from HIST-02 (now Color Contrast, grade 3) and the dark glassy style from SYN-10. Identity conflicts in SYN-01 and SYN-05 remained.
- **Stage 2** produced most of the gain:
  - Identity suppression made SYN-05 directly useful and removed Midnight and the SYN-01 conflicts.
  - Guideline filling added relevant checks to HIST-01, HIST-03 and SYN-08.
  - The critique filter made the HIST-04 follow-up useful (Table Handling, grade 3).
  - The reverted React-label attempt is the one intervention observed to harm retrieval.
- **Stage 3** removed incidental matches (Focus Not Obscured on "not") and made SYN-09 abstain. Lowering the name weight was tried and rejected for lack of benefit.

## 5. Before-and-after results

From `comparison-v0.2-vs-candidate.json`. Both runs use identical frozen, post-hoc and experiment judgment sets and the same catalog (5,500 records, sha256 `e3ae82ff…`). Relevance denominators exclude the expected-empty case SYN-09, so they cover 11 of the 12 synthetic cases.

| Metric | Historical | Development | Reserved |
|---|---|---|---|
| Useful queries (expanded judgments) | 1/5 → 4/5 | 6/8 → 7/8 | 2/3 → 2/3 |
| Useful queries (frozen judgments only) | 1/5 → 4/5 | 5/8 → 7/8 | 2/3 → 2/3 |
| Relevant results returned (frozen only) | 1 (1) → 7 (7) | 9 (7) → 14 (12) | 2 (2) → 4 (4) |
| Cases with a directly actionable result | 1/5 → 3/5 | 3/8 → 5/8 | 1/3 → 1/3 |
| Conflicting results / returned | 2/9 → 0/17 | 7/25 → 0/24 | 0/5 → 0/7 |
| Returned results | 9 → 17 | 25 → 24 | 5 → 7 |
| Follow-up usefulness | 0/2 → 1/2 | 1/1 → 1/1 | — |
| Abstention | HIST-04 unacceptable empty → none | SYN-09 incorrect → correct | — |

The improvement is not explained by returning fewer results. Historical returns roughly doubled while relevant results rose from 1 to 7. Development returns fell by one while relevant results rose from 9 to 14 and conflicts fell from 7 to 0.

**Runtime** (17 commands, median of 3 local runs): v0.2 about 159 ms per command, candidate about 174 ms. The difference is within run-to-run noise of the same order. No cost or performance improvement is claimed.

## 6. Case-level differences

**Newly useful:**
- HIST-01: Heading Hierarchy and Contrast Readability replace Midnight.
- HIST-02: Color Contrast replaces Mobile First.
- HIST-04: Table Handling and Contrast Readability replace an empty result.
- SYN-05: Error Placement, Focusable Error Summary and Inline Validation replace three replacement-identity records.

**Improved without changing usefulness:**
- HIST-03 keeps Keyboard Navigation first and adds Color Contrast (grade 3).
- SYN-08 adds Disabled States (3) and Loading Indicators (2).
- SYN-04 (reserved) goes from one directly actionable guideline to three, including two native-app guidelines.
- SYN-10 gains a directly actionable charity palette and loses all conflicts.
- SYN-01 loses both conflicts.
- SYN-09 abstains.

**Unchanged:** HIST-05 (manual search ranking deliberately unchanged), SYN-02, SYN-06 and SYN-12.

**No case met the regression rules**: lost usefulness, more conflicts, a lost or lower first actionable result, lost abstention, or a failure. Smaller negatives:
- SYN-10 no longer returns Continuous Animation (post-hoc 2) and returns no direction, because no theme or style matches the task's remaining terms.
- SYN-07 swaps Coral (1) for Shopify Polaris (0).
- SYN-11 swaps Halftone (0) for Sticker (0), caused by the negation misparse described in section 8.
- SYN-03 swaps Touch Friendly for Mobile First (both grade 3).
- SYN-01 remains not useful.

## 7. Judgment limitations

- Historical results are graded entirely by frozen judgments except one record (HIST-03 Focusable Error Summary, experiment grade 1).
- Of the candidate's 48 returned results, 33 have frozen grades, 9 have SPECIALIST-UIUX-01 post-hoc grades and 6 have SPECIALIST-UIUX-02 grades (`judgments.json`, label `post_hoc_uiux02`). Four of those six were graded in the development phase and two after the reserved run.
- All non-frozen grades were assigned by the same Builder Agent after seeing output. Each was assigned after inspecting the record, and none was graded 0 merely for being absent from earlier judgments.
- Frozen-only metrics are reported beside expanded ones, and every headline improvement above holds on frozen judgments alone.
- There is no independent evaluator and no inter-rater agreement.

## 8. Reserved evaluation integrity

SYN-04, SYN-07 and SYN-11 were not used for diagnosis, thresholds, rules or variant choice. The candidate was frozen at 2026-11-24T15:36:32Z (`candidate-freeze.json`; recommend `3da35bf6…`, search `f3a5c885…`) before their first experimental run. Their v0.2 outputs were already known, so they are reserved evaluation cases, not a blind test.

The reserved run exposed these defects, which were recorded and **not** tuned:

1. **SYN-07.** Removing restriction text also removed an incidental "web" match. Coral had ranked first partly through its "Web-oriented theme" restriction. The query word "web" now matches Shopify Polaris's "web components" keyword. The delivery-platform word should probably not be a query term when `--platform` is given (hypothesis).
2. **SYN-07 and SYN-11.** Without a preservation cue, the critique design-reference role still returns an unrelated replacement theme or style. Both are graded 0.
3. **SYN-11.** The stop-word list is incomplete: "does", "can" and "whether" remain as query terms.
4. **SYN-11.** The negation parser read "without relying on colour alone", an accessibility requirement, as a colour prohibition. A read-only check with negation parsing disabled shows it alone caused the design-reference swap from Halftone to Sticker (both graded 0), so the parse error changed output but not usefulness.

Fixing any of these and re-running these cases would make them development cases. A later unit would need new reserved cases.

## 9. Verification

- Complete suite: 74 tests pass. That is the original 40 unchanged, 17 benchmark tests and 17 new candidate tests in `tests/test_recommend_constraints.py`.
  - Of the 17 benchmark tests, 13 are from SPECIALIST-UIUX-01. Three of those were repointed to the pinned v0.2 copies:
    - historical replay;
    - script-hash check;
    - full baseline reproduction, which now ignores the checkout revision.
  - Four benchmark tests are new: experiment judgments, candidate reproduction, reproduction-check sensitivity and comparison.
- The pinned v0.2 copies hash to the baseline's recorded values, and their rerun reproduces every field of `baseline-v0.2-481bb18.json`.
- The candidate run is byte-deterministic, and regrading did not change its retrieval output.
- Catalog entries are unchanged (30 files, 5,500 records, same hash). `catalog/SEARCH.md` gained documentation only.
- At the preservation commit itself, `test_full_run_reproduces_frozen_baseline` failed. It compared the recorded git revision, which changes with any commit. This was a SPECIALIST-UIUX-01 test-design defect, fixed here by the reproduction rule above.

## 10. Recommendation

**Revise.** Keep the three intervention groups: they met every objective on frozen judgments and caused no measured regression. Before any release, address the reserved-evaluation defects and the remaining failures (SYN-01 lexical collisions, and the critique design-reference role), then evaluate against new reserved cases.
