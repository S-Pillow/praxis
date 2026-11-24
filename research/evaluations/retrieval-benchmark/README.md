# UI/UX Specialist retrieval benchmark

**Created:** 2026-11-24 (unit SPECIALIST-UIUX-01-BENCHMARK)
**Baseline measured:** `481bb188453b14108890ef0b803249759c5363f4` (prototype v0.2), unchanged retrieval code and catalog
**Companion report:** [`../2026-11-24-url-activity-scanner-uiux-pilot.md`](../2026-11-24-url-activity-scanner-uiux-pilot.md)

This directory holds a small, reproducible benchmark of the catalog lookup used by the optional UI/UX Specialist (`scripts/recommend_design.py` and its follow-up `scripts/search_catalog.py`). It measures retrieval quality only. It does not measure whether the specialist improves the work of an agent, and it is not an independent evaluation.

## Files

| File | Purpose |
|---|---|
| `cases.json` | Frozen case fixture: 17 cases, rubric, conflict rules and relevance judgments. SHA-256 `6b6dda63eac336f2ee6078550f82f3175d0a1e440fd8a666a8de324b0d6038d2`, recorded before any synthetic query was run. |
| `historical/HIST-0*.json` | Byte-exact copies of the raw specialist outputs retained by the URL Activity Scanner pilot (UIUX-PILOT-01 and UIUX-PILOT-02 evidence). They contain catalog data only, with no paths, hosts or credentials. |
| `post-hoc-judgments.json` | Grades for 20 synthetic results that the frozen judgments did not anticipate. Assigned after viewing the baseline output; weaker evidence. |
| `baseline-v0.2-481bb18.json` | Frozen baseline: environment, exact commands, exit codes, stderr size, raw stdout, returned IDs, scores, grades, conflicts, provenance fields and metrics. |
| `reference-v0.2/` | Pinned v0.2 retrieval scripts used for replay (see below). |
| `experiments/specialist-uiux-02/` | SPECIALIST-UIUX-02 retrieval experiment results (see the experiment report). |
| `../../../scripts/retrieval_benchmark.py` | Standard-library runner. |
| `../../../tests/test_retrieval_benchmark.py` | Fixture integrity, scoring behaviour and baseline-reproduction tests. |

## Cases

- **Historical (5):** the only specialist queries actually issued during the scanner pilot, with the same arguments. HIST-01 (critique), HIST-02 (build), HIST-03 (audit) and their follow-ups HIST-04 and HIST-05. No other historical queries are included.
- **Synthetic (12), labelled `origin: synthetic`:** desktop operational and dense-dashboard interfaces (SYN-01, SYN-02, SYN-11), an explicit mobile-first contrast case (SYN-03), native mobile audit (SYN-04), brand preservation (SYN-05) and new identity (SYN-06), critique, build and audit modes, keyboard and interaction states (SYN-08, SYN-12), an abstention case (SYN-09) and prohibited characteristics (SYN-10).
- **Held-out (3):** SYN-04, SYN-07 and SYN-11. Report them separately and do not tune retrieval against them. If a future change is tuned using any held-out case, move that case to `development` and state it.

Each case records the task, the constraints, the interface purpose, platform semantics (for example, "a desktop-first web interface" is not "a mobile web app"), whether an empty result is expected or acceptable, which conflict rules apply, frozen judgments and the evidence or reasoning behind them. Exact IDs are not required for credit: any record judged 2 or 3 counts.

## Judgment model

- **Relevance (0–3):** 0 irrelevant, 1 tangential, 2 relevant, 3 directly actionable. Unlisted returned records are `unjudged` unless graded in `post-hoc-judgments.json`.
- **Conflict (independent of relevance):** derived mechanically from frozen rules in `cases.json` (for example `mobile_first_direction`, `replacement_identity`, `dark_ground`). A record can be relevant and still conflict.
- **Provenance and licence (independent of both):** `evidence_status`, `redistribution_status` and `asset_license_status` are copied from the tool output and reported, never scored.

## Metrics

All metrics are reported per split (`historical`, `development`, `held_out`), with denominators and contributing case IDs. Expected-empty (abstention) cases are excluded from relevance denominators. SYN-09 is the only such case, so relevance metrics use 11 of the 12 synthetic cases (8 development and 3 held-out); SYN-09 is reported only under abstention, and `useful_query_coverage.excluded_expected_empty` names it.

| Metric | Definition | Kind |
|---|---|---|
| Status | `ok`, `empty`, `command_failed` (non-zero exit) or `malformed` (invalid JSON, missing result list, missing or empty `catalog_id`, non-numeric or non-finite `relevance_score`) | Objective |
| Relevant in top 3 | Results ranked 1–3 graded ≥ 2 | Judgment |
| First actionable rank | Rank of the first result graded 3 | Judgment |
| Constraint conflicts | Results matching an applicable conflict rule, over results returned | Rule-based; the rules themselves are judgment |
| Useful-query coverage | Cases with at least one result graded ≥ 2; also reported using frozen grades only | Judgment |
| Abstention | Expected-empty case: `correct` only when status is `empty`; `incorrect` if results are returned; `not_assessable` on command failure or malformed output. Unexpected empty results are `acceptable_empty` or `unacceptable_empty`. | Objective given the frozen expectation |
| Follow-up usefulness | Useful-query coverage restricted to follow-up cases | Judgment |
| Judgment coverage | Returned results graded frozen, post-hoc or unjudged | Objective |
| Historical reproduction | Rerun stdout byte-identical to retained output | Objective |

## Reproduce

From the repository root, with Python 3.12 (the CI version) and no dependencies:

```bash
# v0.2, from the pinned copies in reference-v0.2/ against this checkout's catalog
python3 scripts/retrieval_benchmark.py --implementation v0.2 --raw --check-historical --output /tmp/v02.json
# SPECIALIST-UIUX-02, from the pinned copies in reference-specialist-uiux-02/
python3 scripts/retrieval_benchmark.py --implementation specialist-uiux-02 --raw --judgments research/evaluations/retrieval-benchmark/experiments/specialist-uiux-02/judgments.json --output /tmp/uiux02.json
# the scripts in this working tree
python3 scripts/retrieval_benchmark.py --raw --judgments research/evaluations/retrieval-benchmark/experiments/specialist-uiux-02/judgments.json --judgments research/evaluations/retrieval-benchmark/experiments/specialist-uiux-03/judgments.json --output /tmp/current.json
# case-level comparison
python3 scripts/retrieval_benchmark.py --compare /tmp/v02.json /tmp/current.json --output /tmp/comparison.json
python3 -m unittest discover -s tests
```

`--split` (repeatable) restricts the run. `--check-historical` exits 1 if a historical rerun differs from the retained pilot output; it is meaningful only for `--implementation v0.2`. `--scripts-dir DIR` runs copies of `recommend_design.py` and `search_catalog.py` from another directory, such as a saved experimental stage. `--judgments FILE` adds a labelled judgment set consulted after the frozen and post-hoc judgments. The runner writes no timestamps, so identical code, catalog and judgments produce byte-identical output.

A rerun reproduces a results file when every field of that file is present and equal in the rerun. New fields are allowed, and the recorded checkout revision and Python patch version are ignored (`reproduction_differences` in the runner). The original v0.2 baseline file is never rewritten.

## Pinned implementations

`reference-v0.2/` holds byte-exact copies of `scripts/recommend_design.py` and `scripts/search_catalog.py` at `481bb188`. Their hashes equal those recorded in `baseline-v0.2-481bb18.json`, and a test checks this. The v0.2 replay tests run these copies, so the working-tree scripts may change without losing the ability to reproduce v0.2 or the retained pilot outputs.

`reference-specialist-uiux-02/` holds byte-exact copies of the SPECIALIST-UIUX-02 candidate scripts (commit `4ebee264`). Their hashes equal those in `experiments/specialist-uiux-02/candidate-freeze.json`, and `--implementation specialist-uiux-02` reproduces `experiments/specialist-uiux-02/candidate-results.json` (whose `implementation` field reads `working-tree`, because it was frozen from the working tree). `reference-specialist-uiux-03/` likewise holds the frozen SPECIALIST-UIUX-03 candidate (commit `cd3ef156`), reproduced by `--implementation specialist-uiux-03`.

## Experiments

Each retrieval experiment gets its own directory under `experiments/`. It holds a labelled judgment file for newly returned records (separate from `cases.json` and `post-hoc-judgments.json`), any intermediate stage results, a freeze record written before the reserved cases are run, the candidate's full results, a same-judgment v0.2 rerun and a comparison. `cases.json` is never edited.

In SPECIALIST-UIUX-03 (`experiments/specialist-uiux-03/`) all 17 cases are development and regression evidence. SYN-04, SYN-07 and SYN-11 keep the `held_out` split label and their recorded SPECIALIST-UIUX-02 reserved results, but they were used for refinement and are no longer reserved. That directory compares v0.2, pinned SPECIALIST-UIUX-02 and the refinement candidate under identical judgment sets.

`fresh-evaluation-specialist-uiux-03/` preserves, unchanged, the seven withheld Prompt Agent queries (PA-01 to PA-07) run once against the frozen UIUX-03 candidate. `experiments/specialist-uiux-04/` holds the v0.3 preservation-versus-prohibition correction: the 17-case results (no case changed), a comparison with UIUX-03, and `correction-results.json`, which reruns PA-01 to PA-07 as regression evidence (only PA-02 and PA-05 changed). Those queries are no longer held-out evidence. A future fixture version should be added alongside it, so the freeze hash stays meaningful.

## Limitations

- One evaluator wrote the cases, froze the judgments and graded the post-hoc results. No inter-rater agreement exists.
- Synthetic cases were written with knowledge of the catalog and of the pilot failure modes, so they are not a random sample of real tasks.
- Frozen judgments covered all 9 historical results but only 10 of the 30 synthetic results; the other 20 were graded post hoc. Frozen-only coverage figures are reported alongside.
- Seventeen cases is a small denominator. The metrics describe these cases, not general retrieval quality.
- Conflict rules are regular expressions over catalog text; they can miss conflicts or flag negated mentions.
