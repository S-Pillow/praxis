# SEND TO BUILDER — Builder Payload only

Transfer this entire document to the Builder. The Builder executes only what is written here, using the application files it can access. Do not load Praxis, AIPF, PRDs, catalogs, specialist guidance, or Prompt-Agent derivation notes. Optional access to those resources confers no extra authority.

---

## Authorization-unit ID

**PV03-FIX-01**

## Objective

Fix reopened tasks disappearing from active tabs by correcting task completion classification so a task is completed only when it has a completion timestamp. Preserve all behavior outside that approved correction.

## Exact operational context and accepted baseline

**Application root (confirmed):**  
`<APP_ROOT>`

**Authoritative files for this unit:**
- `task_visibility.py` — defines `tab_for(task)`
- `test_task_visibility.py` — unittest suite for `tab_for`

**Current helper behavior (observed defect):**  
`tab_for` returns `"completed"` when `task["completedAt"] is not None` **or** when `all(task["steps"])` is true. That hides reopened tasks (`completedAt` cleared to `None` while every step remains `True`). The same `all(steps)` rule also marks tasks with `completedAt is None` and an empty `steps` list as `"completed"` because `all([])` is true in Python.

**Accepted interface baseline (must preserve):**
- Function name: `tab_for`
- Input: a `task` mapping with at least `completedAt` and `steps`
- Return values: exactly `"active"` or `"completed"` (same vocabulary)
- No change to callers’ data shape beyond what the helper already expects

**Environment baseline:**
- Python 3 available locally
- Tests use the Python standard-library `unittest` module only
- No third-party packages, no network calls

## Authorized actor / actions / targets

**Actor:** Distinct Builder Agent for this payload only.

**Authorized actions (in order):**
1. Inspect `task_visibility.py` and `test_task_visibility.py` under the application root above.
2. Modify `task_visibility.py` so `tab_for` implements the required completion rule below.
3. Modify `test_task_visibility.py` so tests lock the required behaviors (keep existing still-valid cases; add or adjust coverage for the approved correction cases).
4. Run the local unittest suite from the application root.
5. Save changes to disk and read the two authorized files back to confirm persistence.
6. Return the Compact Handoff and stop.

**Targets:** only  
`<APP_ROOT>\task_visibility.py`  
and  
`<APP_ROOT>\test_task_visibility.py`

## Required behavior (governing rules for this unit)

1. A task is **completed** if and only if `completedAt` is not `None`.
2. A reopened task (`completedAt` is `None`) remains **active** even when every step is checked / `True`.
3. A task with no completion timestamp and no steps (`completedAt` is `None`, `steps` empty) remains **active**.
4. Preserve the existing function interface, data structure expectations, and return values (`"active"` / `"completed"`).
5. Modify only the disposable helper and its tests.
6. Use the Python standard library only; do not add dependencies or perform network activity.

## Shared allowed / forbidden boundary and constraints

**Allowed:**
- Edits to the two target files listed above
- Running local `unittest` (may create/update `__pycache__` / `.pyc` as a normal side effect)

**Forbidden:**
- Any other file under the application root or elsewhere in the workspace
- Schema, persistence, API, UI, configuration, packaging, or dependency changes
- Installing packages, using non-stdlib libraries, or network access
- Git commit, push, merge, tag, publish, deploy, or release actions
- Expanding scope to unrelated refactors, renames, or “improvements”
- Changing return labels, adding new tab names, or altering the `tab_for` calling convention

**Governing intent / protected invariant:**  
Completion classification must remain timestamp-based (`completedAt`), not step-checklist-based. Do not “fix” visibility by treating checked steps as completion.

## Planned transitions / conditional gates

1. **Inspect** authorized files → if root or files are missing/wrong, stop and report.
2. **Correct** `tab_for` to the required rule → if another module must change to meet acceptance, stop and report (do not expand targets).
3. **Update tests** for the acceptance cases below.
4. **Verify** with unittest → on failure, you may adjust only the authorized files to meet the stated rules; if still failing without leaving that boundary, stop and report.
5. **Persist and read back** the two files → then handoff and stop.

No batch items. Single workstream; no independent continuation of other work.

## Expected automatic effects / closure signals

- Expected: unittest may write `__pycache__` / `.pyc` under the app root.
- Not expected: any other source, config, lockfile, or project mutation.
- Closure signals: unittest exit code 0 for the required suite; both authorized files saved and readable with the corrected behavior; Compact Handoff returned.

## Deterministic acceptance and verification

Named observer: **Builder** (local Python + unittest). Evidence purpose: prove the corrected classification and non-regression of still-valid cases. Feasibility: confirmed (Builder has the app). Fallback: none — if unittest cannot run, stop and report blocked verification.

**Acceptance criteria (all required):**

| Case | Input | Required `tab_for` result |
|---|---|---|
| Completed with timestamp | `{"completedAt": <non-None timestamp>, "steps": [True, True]}` (or equivalent non-None `completedAt`) | `"completed"` |
| Unfinished partial steps | `{"completedAt": None, "steps": [True, False]}` | `"active"` |
| Reopened, all steps checked | `{"completedAt": None, "steps": [True, True, True]}` | `"active"` |
| No timestamp, no steps | `{"completedAt": None, "steps": []}` | `"active"` |

**Verification command (from application root):**

```text
python -m unittest test_task_visibility.py -v
```

(or `python -m unittest discover -s . -v` limited to this app’s tests)

**Pass rules:**
- Command exit code **0**
- Assertions cover at least the four cases above (existing green cases may remain; reopened and empty-steps cases must be present after your edit)
- Read-back of both authorized files shows the saved correction on disk

**Fail / stop without expanding scope** if acceptance cannot be met inside the allowed files.

## Durability closure

Write `task_visibility.py` and `test_task_visibility.py` to disk. Re-open/read both files and confirm the intended correction and tests are present. Do not claim success from an unsaved editor buffer alone.

## Binding stop conditions and stop scope

Stop this unit (local / workstream stop — do not start other work) when any of the following is true:
- Application root or authorized targets are missing, mismatched, or not writable as assumed
- Meeting acceptance would require changing a forbidden surface
- An unexpected mutation occurs outside authorized files (other than normal `__pycache__` / `.pyc`)
- Verification is blocked or cannot pass within authorized scope
- Authorized edits, verification, and saved-state confirmation are complete (success path)

On stop: do not commit, deploy, or begin a follow-up authorization unit.

## Compact handoff requirements

Return a Compact Handoff with at least:
- Authorization-unit ID received: `PV03-FIX-01`
- Executor-reported outcome: success / failure / blocked (and brief factual reason)
- Changed surfaces (paths)
- Actor-initiated mutations vs expected automatic effects (`__pycache__` / `.pyc` if any)
- Unexpected or forbidden changes: none or list
- Deterministic verification: exact command(s), exit code(s), and pass/fail per acceptance case
- Durability: confirmation that both files were saved and read back
- Unresolved issues / escalations, if any
- Stop respected: yes/no

Suggestions, if any, are observations only — they do not authorize further work.
