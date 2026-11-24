# URL Activity Scanner UI/UX Specialist pilot — evaluation record

**Prepared:** 2026-11-24 (unit SPECIALIST-UIUX-01-BENCHMARK, AIPF v8.10.1, Builder Agent)
**Specialist measured:** `aipf-ui-ux` prototype v0.2 at `481bb188453b14108890ef0b803249759c5363f4`
**Benchmark:** [`retrieval-benchmark/`](retrieval-benchmark/README.md)
**Status:** research record. It does not amend canonical AIPF, the specialist instructions or the catalog.

## 1. Summary

The optional UI/UX Specialist was used during a real, owner-accepted UI improvement to an existing production application, the URL Activity Scanner. The interface improved by the pilot's own measures: weighted critique score 3.15 → 4.00, a 100-result batch 15,242 → 7,292 px tall at 1280 px, and focus and completion behaviour fixed. The owner approved the visual result and accepted the deployed release.

The specialist's **procedure** (separate critique from audit, inherit the existing identity, make the smallest useful change, verify against the rendered interface, do not claim unverified checks) visibly shaped how the work was done. Its **catalog retrieval** contributed one useful audit checklist item, Keyboard Navigation. It contributed no design decision, and two of its five pilot queries returned records that conflicted with the project, one of them contradicting explicit owner direction. Most substantive findings came from rendered measurements, source inspection, owner direction and general UI and accessibility knowledge.

This was not a controlled comparison. It shows that the specialist could be used on a real project without harm when its output was critically assessed. It does not show that the specialist produces better results than ordinary AIPF development.

## 2. Evidence sources

All evidence is retained outside this repository, in the scanner pilot evidence directories, each sealed with a SHA-256 manifest that verified on 2026-11-24. Only the five raw specialist outputs were copied here (`retrieval-benchmark/historical/`), because they contain catalog data only. No server logs, credentials, keys, operational archives or production configuration are reproduced.

| Unit | Content used | Seal |
|---|---|---|
| UIUX-PILOT-01-BASELINE | Specialist commands, exit codes, raw outputs, `specialist/assessment.md`; `critique/critique.md` (scorecard, R1–R8); `validation/exit-codes.txt` (411/411 tests) | 72 files, verified |
| UIUX-PILOT-02 | Specialist commands and outputs, `specialist/assessment.md` (attribution table); `critique/after-evaluation.md` (acceptance matrix, measurements, scorecard) | 152 files, verified |
| UIUX-PILOT-03 | Production-build verification, mocked private owner review; 463/463 tests | 90 files, verified |
| UIUX-PILOT-04-INTEGRATION | Integration with concurrent backend work; `validation/test-count-reconciliation.txt` | 99 files, verified |
| UIUX-PILOT-05-REPOSITORY, 05A-SYNC | Local commits; [PR #1](https://github.com/S-Pillow/url-activity-scanner/pull/1) merged as `3cf2d2a0` | 23 files, verified (05A has no separate directory) |
| UIUX-PILOT-06-DEPLOYMENT | Staged build, backup, cutover and verification of `3cf2d2a0` | 162 files, verified |

**Owner statements**, conveyed by the Prompt Agent in the pilot conversation and not stored as evidence files:

- About 98% of scans are performed on PCs.
- Approval to move the complete result key below populated results.
- Approval of the UIUX-PILOT-03 implementation.
- On 2026-11-24: "PILOT-06-OWNER: PASS. Live interface, real scan and CSV export verified. No exceptions."

## 3. Evaluation design

- **Real application:** an existing Next.js production tool, not a fixture or demo.
- **Before and after:** UIUX-PILOT-01 measured the unchanged interface; UIUX-PILOT-02 implemented and re-measured with the same method and weights.
- **Actual activation:** the specialist skill was read and its commands were run by the same agent doing the work, with raw output retained.
- **Desktop-first:** the owner's 98% PC figure made this a desktop-first web interface. Mobile layouts had to keep working (verified at 375 and 320 px), but were not the design target.
- **Identity and protected requirements:** the existing GitHub-dark-style tokens, monospace data values, "no images" rule, complete always-visible result key and all result meanings were protected.
- **Not a controlled independent-agent A/B.** There was no parallel run without the specialist, no blinded evaluator and no control for effort, time or cost.

## 4. Outcomes

| Measure | Before | After | Source |
|---|---|---|---|
| Weighted critique score (1–5) | 3.15 | 4.00 | PILOT-01 `critique.md`; PILOT-02 `after-evaluation.md` |
| Desktop-first suitability (reported separately) | 2 | 4 | PILOT-02 `after-evaluation.md` |
| 100-result section height, 1280 px | 15,242 px | 7,292 px (−52%) | same |
| Average row height, 100 results | 142 px | 70 px | same |
| Results heading after completion (1280 / 375 / 320) | 1021 / 1343 / 1092 px from top (off-screen) | 23 / 11 / 11 px | same |
| Lowest text contrast | 2.57:1 | 4.63:1 | same |
| Lowest focus-ring contrast | 1.95:1 | 3.73:1 (controls 6.85:1) | same |
| Export control | 109×26 px, top only | 129×40 px, sticky in results | same |

**Tests.** The baseline UI had 411 tests in 9 suites. The UI change set (PILOT-02/03) brought this to 451 and then 463 in 11 suites. Separately, concurrent backend development had produced a pre-UI integration base of 456 tests. Integrating the UI work with it gave 508 tests in 14 suites (PILOT-04). The backend work is **not** a specialist outcome: it was pre-existing development merged alongside.

**Owner and release.** The owner approved the PILOT-03 implementation visually through a private, mocked review session, approved moving the result key, and on 2026-11-24 accepted the deployed release `3cf2d2a0` after verifying the live interface, a real scan and CSV export. Deployment (PILOT-06) was ordinary operational work. No scan in any pilot unit except the owner's was a real production scan.

**Attribution.** These outcomes belong to the bounded UI change set as a whole. The PILOT-02 attribution table assigns each implementation decision to its sources. Owner direction and general UI and accessibility knowledge appear in almost every row. Catalog content appears only as a rejected direction (Mobile First, Midnight) or as a verification checklist (Keyboard Navigation). The score change cannot be attributed to the specialist.

## 5. Specialist findings

### Positive

- **Procedural guidance was useful.** Keeping judgment (critique) separate from observable checks (audit) structured the baseline report. "Inherit the existing identity" and "smallest useful intervention" matched the owner's constraints. The required rendered audit with a bounded correction and recheck found two real defects in the R5 layout (wrapping row labels and a disproportionate Meaning column at mid-desktop widths), which were fixed and re-verified.
- **Audit retrieval worked.** Keyboard Navigation (`uupm:ux-guidelines:41`) was directly actionable. It was applied as a checklist to the running preview: visible focus on every control, logical tab order, no traps, and focus never covered by the sticky toolbar. It changed what was verified, not the code.
- **Provenance was transparent.** Every reference carried its source repository, pinned commit, row, evidence status, redistribution status and asset licence. This made it straightforward to reject Midnight's fonts and photography as not cleared for redistribution.
- **Fallback was safe.** When retrieval was weak, the instructions allowed falling back to project requirements and general craft. No weak reference was adopted merely because it was retrieved.

### Negative

- **Build-mode retrieval contradicted owner direction.** The only build reference was Mobile First, recommending mobile-first design for a 98%-desktop tool. It was rejected as a direction and kept only as a "do not break mobile" check.
- **Critique retrieval was off-target.** "No Results" addresses empty search results, which the scanner never produces. Midnight is a full replacement theme that conflicts with the established identity.
- **Follow-ups added nothing.** The critique follow-up returned zero results. The build follow-up returned four irrelevant records and one tangential one (`open-design:skills:app-table`, whose filters and selection were outside the authorization).
- **No catalog-derived design decision.** The baseline assessment states that no critique finding depends on catalog content.

### Rejected recommendations

| Reference | Mode | Reason | What was kept |
|---|---|---|---|
| `uupm:ux-guidelines:64` Mobile First | build | Contradicts the owner's desktop-first direction | Mobile non-breakage check (0 px overflow at 375 and 320 px) |
| `hallmark:theme:midnight` Midnight | critique | Replaces the identity; fonts and photography not cleared for redistribution | The idea of an opaque, light focus ring, implemented with the app's own `--accent` |
| `open-design:skills:app-table` | build follow-up | Filtering, sort and selection not authorized | Its state list matched coverage already planned; no decision attributed |

## 6. Why retrieval failed in the historical cases

These mechanisms were demonstrated by per-term BM25 breakdowns against the unchanged v0.2 code and catalog. They are causes of these specific results, not a general diagnosis.

- **Negated text matched positively (HIST-02).** Mobile First scored 11.33, made up entirely of "desktop" (4.54) and "first" (6.79). Both terms come from its restriction text, "Avoid: Desktop-first causing mobile issues". The query's desktop-first intent therefore retrieved the record that warns against it. Keyboard Navigation scored 7.28 in the same pool of 110 guidelines (the focused accessibility-correction scope).
- **Stop-word gap and lexical collisions (HIST-01).** Midnight scored 10.70, of which "its" contributed 3.89 ("its" is not a stop word), "technical" 3.76 and "dark" 3.05. No Results scored 7.45, entirely from the word "results" matching a heavily weighted record name.
- **Filter cardinality (HIST-04).** `--specialist-use critique` admits only 2 of 5,500 records (`specialist_use` values: build 5,260, audit 199, reference 39, critique 2, multiple 0), so the critique follow-up was empty. Without the filter, the same query surfaces Data-Dense Dashboard and app-table; with the audit filter it surfaces Table Handling first.
- **Relevant records existed but were not returned.** Table Handling (71), Long Token Wrapping (111), Focus Not Obscured (100), Color Contrast (36) and Data-Dense Dashboard are in the catalog and address actual pilot findings.

## 7. Benchmark baseline

The benchmark reruns the five historical queries and twelve synthetic ones (three held out) through the unchanged scripts. Every command exited 0 with empty stderr. All five historical reruns are byte-identical to the retained pilot outputs, and two full runs produced byte-identical results files. Relevance grades are evaluator judgments. Status, reproduction and conflict-rule matching are objective given the frozen fixture.

| Split | Cases | Useful (≥ 2) | Actionable result (3) | Conflicting results / returned | Notes |
|---|---|---|---|---|---|
| Historical | 5 | 1 (HIST-03) | 1, at rank 1 | 2 / 9 (HIST-01 Midnight, HIST-02 Mobile First) | HIST-04 empty and judged unacceptable; follow-ups 0 of 2 useful |
| Development (synthetic) | 9, of which 8 relevance-scored | 6 (5 using frozen grades only) | 3 (SYN-03 rank 3, SYN-08 rank 1, SYN-12 rank 2) | 7 / 25 (SYN-01 2, SYN-05 3, SYN-10 2) | Abstention case SYN-09 incorrect (a theme returned for a backend rename) |
| Held-out (synthetic) | 3 | 2 (SYN-04, SYN-11) | 1 (SYN-04 rank 1) | 0 / 5 | SYN-07 critique not useful |

Patterns visible in these cases (not general claims):

- **Audit mode was the strongest.** HIST-03, SYN-04 and SYN-08 each returned a directly actionable guideline at rank 1.
- **Build mode with an existing identity produced conflicts.** Build mode always fills direction, palette and typography roles. In SYN-01 (keep the light theme and component library) and SYN-05 (no new colours or fonts), every direction, palette or typography result conflicted with that constraint.
- **Prohibitions were not respected.** SYN-10 ("do not use dark mode, glassmorphism or decorative animation") returned a dark, glassmorphic, animated style as the top direction, a pattern similar to HIST-02.
- **No abstention.** SYN-09, a non-visual backend change, still received a visual theme.
- **Critique mode was mixed.** SYN-11 returned Table Handling (relevant). HIST-01 and SYN-07 returned nothing useful.

## 8. Limitations

- **Superiority is unproven.** There was no without-specialist control. The same agent ran the specialist, did the work and evaluated it.
- **Scores are subjective.** The critique scorecard and its weights were set by the evaluator. The 3.15 → 4.00 change measures the change set against its own rubric.
- **Effort, time and cost were not controlled or recorded** comparably.
- **Browser coverage was limited.** Chromium automation only; no screen-reader output, OS forced colours or real browser zoom was verified.
- **No causal catalog benefit.** The single useful catalog item shaped verification, not design.
- **Benchmark limits.** One evaluator, synthetic cases written with knowledge of the catalog and failure modes, 20 of 30 synthetic results graded post hoc, and small denominators. See the benchmark README.

## 9. Process observation

In UIUX-PILOT-05-REPOSITORY, an exhaustive investigation of hypothetical GitHub automation (installed apps, event subscriptions and agents that might act on a push or merge) could not rule out every hypothetical consequence, so the push, PR and merge gates were reported as blocked even though no concrete risk had been found. In UIUX-PILOT-05A-SYNC the owner superseded this with a proportionate manual workflow: push, open the PR, merge with a standard merge commit, and confirm production unchanged. That resolved the stage, and the observed app activity (review comments and a stalled or empty check suite) had no deployment effect. It is recorded as an observation about proportionality in this pilot, not as a proposed change to AIPF governance.

## 10. Improvement hypotheses (not implemented, not demonstrated)

The mechanisms in section 6 are demonstrated for specific results. The fixes below are hypotheses. None has been tested, and each could introduce new failures, which the benchmark is designed to detect.

1. Exclude or down-weight negated restriction text ("Avoid: …", "Avoid for: …") in ranking, which might remove the HIST-02 and SYN-10 conflicts.
2. Add common function words such as "its" to the stop-word list.
3. Reduce lexical collisions from heavily weighted record names on generic words ("results", "component library").
4. Make critique mode usable: retag records as `critique` or `multiple`, or let the critique filter fall back to audit and reference records.
5. Normalise platform labels ("iOS/Android/React Native", "Mobile", "Web") so `--platform` matches the intended records.
6. Recognise desktop-first and preserve-identity constraints, and suppress direction, palette and typography roles when the task forbids a new identity.
7. Add an abstention path for tasks without visual design content.
