# AIPF Specialist Suite — continuation handoff

**Prepared:** 2026-11-23 (America/Kentucky/Louisville; some GitHub merges are dated 2026-11-24 UTC)  
**Repository:** https://github.com/S-Pillow/aipf-specialist-suite  
**Purpose:** Transfer verified project context to a new chat without treating this narrative as a new governing framework, a new authorization unit, or a substitute for current repository state.

## Start here in the new chat

Read this handoff, verify the live repository and relevant uploaded source artifacts, and apply **canonical AIPF v8.10.1**. Do not assume the prior chat's observations are still current. The next user-facing milestone is a **controlled real-project UI/UX Specialist effectiveness comparison**. The user said a suitable project now exists but has **not yet supplied its repository/ZIP or target UI task in this conversation**. First establish that target's baseline, scope, execution model, and approval. Do not build, merge, deploy, install an external plugin, or invent a Builder run from this handoff alone.

## 1. Authority and workflow

- **Canonical framework:** `Neutral_AIPF_v8_10_1.docx`, SHA-256 `8e66028c8ebf60ea87180be1c23933273d8a597c425d3a1595ae81d9a720b8e6`. The installed `aipf-framework` skill is a progressively loaded projection of this canonical text. **No AIPF v8.10.1 rule changes were approved or made in this workstream.**
- **AIPF routing:** Apply Section 8, not a substitute workflow. An existing application/repository uses Chapter 12 as its baseline; add Chapter 14 for UI changes, Chapter 13 for documentation when applicable, Chapter 19 for qualifying remote/CI execution, Chapter 20 at applicable release/reconciliation gates, and Chapter 21 only when its two-agent or platform-capability activation conditions hold. Apply Section 9 Compact or Managed treatment, current preflight, authorization, Project Control Record, evidence, stop, and reconciliation controls.
- **Prompt Agent / Builder Agent distinction:** In a *genuine two-agent execution model*, the Prompt Agent owns routing, current state, preflight and T1 derivation, sends only the operational **Builder Payload** through an authorized handoff, receives the **Builder Handoff**, and reconciles it. The distinct Builder executes only the payload and cannot choose the next route/unit. A Builder cannot be assumed to have the Prompt Agent's files or catalog access; transport necessary exact tokens and constraints when needed. If human-mediated, label **SEND TO BUILDER** and stop until the handoff returns.
- **Clarification accepted by the user:** It was **fine for one assistant to act as both planner and builder during isolated prototype testing**. A strict instruction mandating a separate Builder Agent for *all* work was proposed during a misunderstanding and **was not adopted**. When there is no distinct Builder, canonical AIPF allows properly authorized **direct single-agent execution**, without a fictional self-handoff. For the next experiment, agree on actual agent/runtime and independent-run setup rather than assume a Builder exists.
- **Instruction status:** An expanded project-instructions draft was discussed; it has **not been confirmed as installed in persistent Project settings or GitHub**. Do not describe it as governing. This handoff is informational; do not turn it into competing AIPF rules.

## 2. Verified repository baseline (before this handoff update)

- `main` at `22b813d558665b8e58042b64e17cd4c0e511b49d`, verified via GitHub connector. No open pull requests at that check. Refresh both in the next chat.
- [PR #5](https://github.com/S-Pillow/aipf-specialist-suite/pull/5), merged: usable optional UI/UX skill, full 5,500-entry Design Index/browser, search infrastructure and tests.
- [PR #6](https://github.com/S-Pillow/aipf-specialist-suite/pull/6), merged: optional **Copy instructions for AI** handoff from saved references. The user manually tested it and said it works.
- [PR #7](https://github.com/S-Pillow/aipf-specialist-suite/pull/7), merged: agent-initiated `scripts/recommend_design.py` catalog lookup, instructions, real-catalog tests, and bounded Design Index keyboard-focus CSS correction. Final branch CI: **37 tests passed**. Its read-only lookup is heuristic, not permission or acceptance.
- [PR #8](https://github.com/S-Pillow/aipf-specialist-suite/pull/8), merged: repository-scoped Codex discovery via `.agents/skills/aipf-ui-ux/SKILL.md` and `AGENTS.md`. Final branch CI: **40 tests passed**. Tests verify layout/invocation, **not actual live Codex auto-selection**.
- **Capability boundary:** The skill can initiate lookup when loaded by a compatible coding agent with access to this repository and a command runner. This is **not a global installation**, an always-on ChatGPT capability, or proof of live deployment. The user should not have to run Python, browse 5,500 items, or copy a prompt for the intended normal workflow; the optional Design Index/copy prompt remain useful.

## 3. Catalog and specialist decisions to preserve

- Original **AIPF Unified Design Catalog**: 5,500 production source-linked records from Hallmark, UI UX Pro Max, Open Design Agent Kit, Impeccable, and MengTo. Not 5,500 fully built templates. Keep upstream identities/overlaps and source provenance; use concise retrieval rather than context dumps.
- Preserve original source commit/path, evidence depth, actual token values if present, platform fit, and rights status. **Metadata/reference is not a license to bundle** photos, fonts, icons, screenshots, demos, logos, or branded assets. Asset redistribution remains blocked until file-level clearance.
- The specialist must **improve the interface while building**, and subsequently perform distinct **design critique** (judgment) and **technical UI audit** (observable tests). Existing approved brand/product requirements win over catalog suggestions; optional anti-generic diagnostics are not universal aesthetic bans. Do not claim independent reviewers or visual inspections that did not occur.
- The older `research/catalog-import-status.md` documents a historical **5,373-record** import snapshot; the current production count and tests show **5,500**. Do not treat that older count as current or silently rewrite its historical evidence.
- Key repo documents: [skill](../../skills/aipf-ui-ux/SKILL.md), [catalog retrieval](../../catalog/SEARCH.md), [existing agent guide](../../AGENTS.md), [Prompt/Builder interface](../prompt-agent-builder-interface.md), [source-rights register](../licensing/independent-evidence-pass.md), [accepted research decisions](../decisions/2026-11-18.md).

## 4. Completed design comparison — useful, not a proven advantage

**Task:** Improve mobile labels/touch usability for **Explore library** and **Saved references** in the Design Index, preserve existing branding/behavior/desktop. Two isolated HTML/CSS *variants* were produced in one assistant session against the same snapshot, with a three-record simulated catalog API:

| Evidence | A — ordinary guidance | B — source-linked catalog guidance |
|---|---|---|
| Mobile navigation labels | Visible | Visible |
| Target height at 375px | 40 CSS px | 46 CSS px |
| Overflow at 320/375/1280px | None observed | None observed |
| View switch/search/keyboard focus | Passed scoped browser checks | Passed scoped browser checks |
| JavaScript exceptions | None observed | None observed |

B used source-inspected `uupm:ux-guidelines:23` (Touch Spacing), `:40` (ARIA Labels), `:41` (Keyboard Navigation) and `:66` (Touch Friendly). Both designs looked good to the user. **No preference for B was expressly selected**, no Design Index code from the A/B was merged, and no measurable specialist superiority was established. Both variants came from the **same assistant session**, so this was not independent-agent evaluation. The archived local test bundle is `AIPF_UIUX_Specialist_AB_Test_2026-11-23.zip` (not in this GitHub repository); its `REPORT.md` documents the browser method and limits. If it matters later, attach the ZIP in the new chat.

## 5. Other experiment / parked research state

- An earlier paired **QA specialist pilot** (separate from the UI design experiment) graded two small synthetic tasks. AIPF-only and specialist-guided submissions **tied**: Task A 14/14 per condition; Task B 10/10 per condition, or 24/24 per condition total. It did **not** establish added benefit. Evidence did not independently prove separate matched model runs, timing, cost, or tool settings. Local report: `AIPF_QA_Pilot_Graded_2026-11-23/GRADE_REPORT.md`; this evidence has not been added to the repo as part of this handoff.
- Ralph Starter **native-runtime acceptance remains separately blocked/unverified**; do not treat the QA pilot as a native Ralph test or authorize its integration by association. Earlier workstream notes and evaluation registers are historical research, not proof of installed runtime features.
- Continue to treat future source enrichment/licensing and QA specialist experiments as **separate** from the immediate real-project UI/UX effectiveness gate unless reauthorized.

## 6. Next meaningful test (not yet started)

**Goal:** Compare AIPF-only vs AIPF + optional UI/UX Specialist on the user's **actual project**, using matched requirements and independent coding-agent contexts, and determine whether the specialist improves an observable outcome without introducing regressions.

1. **Identify target:** Obtain the existing project/repo/ZIP, target screen or specific design outcome, accepted baseline and branch, user-approved change scope, protected behaviors/design tokens, target platform, and actual coding-agent/runtime availability. The user said a project exists; the target has not yet been supplied. Do not assume it is the Design Index.
2. **Apply AIPF:** Verify current project state and authority; route Section 8 (usually Ch. 12 + 14 plus applicable wrappers), choose Section 9 treatment, perform applicable preflight, define a bounded authorization unit and stop/release conditions. Establish whether a *distinct Builder Agent* exists. If yes, prepare T1 and transport correctly; if no, use authorized single-agent execution or identify needed setup.
3. **Freeze comparison:** Same starting commit, task statement, acceptance criteria, time/effort/tool budget and evaluation plan. Use isolated worktrees/branches and fresh agent contexts. Arm A: canonical AIPF + project requirements, without UI/UX Specialist. Arm B: same plus skill and source-linked retrieval. Ensure the B agent actually has the skill/repository available; independently observe whether retrieval/selection happened rather than infer activation from configuration. Do not leak B's knowledge into A. Record model/settings/environment where available.
4. **Execute within bounds:** No production deployment, public release, unsolicited merge, unlicensed asset bundling, or changes to canonical AIPF. Capture changed files, raw test results, diffs, runtime evidence, and Builder Handoffs when distinct agents are used.
5. **Evaluate the same surfaces:** Functional regression, responsive desktop/mobile views, keyboard focus, accessibility/readability, interaction and edge states, product fit, visual hierarchy and coherent identity. Use actual rendered screenshots and named observation methods; distinguish objective checks from aesthetic judgment. Capture time/cost only if observed; ask user for qualitative visual preference.
6. **Reconcile:** Produce a side-by-side evidence table with provenance and limitations. Do not declare B better solely because it is more elaborate. Owner decides whether an approach merits integration; release/merge is a **separate AIPF authorization gate**.

**Immediate next action:** Request the real project link/ZIP and bounded target task if not already provided in the next chat; then perform read-only baseline discovery and the AIPF preflight. Avoid another Design Index polish pass. Do not promise an independent-agent run without a real accessible agent runtime.

## 7. Explicitly not decided / not done

- No globally installed UI/UX Specialist or publicly distributed plugin; no demonstrated live Codex automatic discovery outside repository-scoped file checks.
- No real-project A/B outcome or measured UI/UX Specialist benefit. No decision to prefer B or ship either Design Index A/B variant.
- No change to canonical AIPF v8.10.1, no strict project-wide mandatory two-agent amendment, and no confirmed persistent Project instruction update.
- No completed third-party asset redistribution clearance, public deployment, or production acceptance.

## 8. New-chat kickoff prompt

> Resume the AIPF Specialist Suite from the repository handoff at `research/handoffs/2026-11-23-aipf-specialist-suite.md`. Read canonical AIPF v8.10.1 and verify the current repo state first. Preserve the Prompt Agent / Builder Agent distinction only when a distinct Builder is actually part of the execution model. The next objective is a controlled, matched AIPF-only vs AIPF + UI/UX Specialist test on my real project. Do not change the Specialist Suite, install anything, or claim an independent test until the project baseline, target task, runtime, authorization, and evidence gates are established.
