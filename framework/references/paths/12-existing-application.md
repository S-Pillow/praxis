# **Chapter 12 — Existing Application and Corrections Path**

When to use: any existing app, repo, deployed site, packaged executable, working tool, or current workflow — including new or major features, bug fixes, and production changes to one.

Companion chapters when applicable: Ch. 20 at release; Ch. 16/17/18 per application type; Ch. 21 only when Section 8 Execution mechanism activates Platform Capability controls or Two-Agent Orchestration.

**Rules.**

**Existing-system trigger.** Before the first dependent change, establish or reuse a valid Phase -2 baseline and perform any delta discovery its impact triggers require (Section 4.1, Phase -2). No valid baseline or required delta check means no dependent implementation authorization. Wrong-directory signs require an immediate stop of affected work and confirmation of the correct project root. Do not scaffold a new app as a workaround for not finding the existing one.

Correction authorization units. Before implementation, confirm the app root and the project-state/release facts material to the correction. Use T3 fields proportionately: a compact low-risk correction may carry only the applicable state, durability, verification, and recovery fields; require the full Project-State and Release Plan when managed work, release/state transitions, significant recovery needs, or other material project-state consequences activate it. Classify risk severity and disposition separately, then define the bounded correction unit with allowed/forbidden surfaces, acceptance, tests, planned transitions, and stop condition.

Playbook. 1. Establish or reuse the Phase -2 baseline; run only required delta discovery and do not initiate project changes during discovery. 2. Confirm only material app/project root, source/version authority, release relationship, runtime/data surfaces, APIs/routes/artifacts, and known working behavior for the current change. 3. Update the Phase -2A Risk and Decision Register only for new or affected findings. 4. Resolve or disposition findings that can change the current authorization/acceptance boundary. 5. Create focused correction/enhancement authorization units with proportional state fields, risk carryover, allowed/forbidden surfaces, acceptance criteria, tests, planned transitions, and stop condition. 6. Execute coherent units; independent units may proceed in parallel only when authority/state/risk/evidence/release boundaries are independent. Integration, deploy, package, or release may share a unit only when Section 6 permits pre-authorization; otherwise stop at the changed boundary. Close release evidence per Chapter 20 only when it activates.

Authorization form: use the T1 operational boundary fields and the Risk Register (T2). When a separate Builder exists, T1 is the canonical orchestrated form and the example below is the transported Builder Payload; substitute verified project-specific values before issuance. In direct single-agent execution, record the same operational fields before mutation and execute them directly; derivation partition, transport, and handoff are N/A.

Authorization-unit ID: EXAMPLE-FIX-01  
Objective: fix reopened tasks disappearing from active tabs.  
Context and targets: confirmed project root /workspace/task-app; editable helper src/taskVisibility.ts and tests src/taskVisibility.test.ts; existing test/build scripts are accessible. Observed backend behavior: completedAt = null returns a task in the active query. The frontend also treats all checked steps as completion, hiding reopened tasks. The approved completion rule is completedAt != null; checked steps alone do not imply completion.  
Authorized actions: inspect the project; correct only the helper and its tests; run npm test -- --run and npm run build. Preserve other task types, existing UI, completed-task behavior, and exports. No schema, backend lifecycle, runtime-data, secret, dependency, or configuration changes.  
Expected automatic behavior: build writes dist/ and test/build commands may write local caches; no other automatic source/configuration mutation is expected. Do not publish generated outputs.  
Acceptance and verification: test completion followed by reopening with completedAt cleared and all steps still checked; the reopened task appears in active tabs; completed tasks remain in Completed; displayed counts match lists; existing tests and build exit 0. Report each test result and inspect the affected UI; unavailable UI inspection remains pending.  
Closure: save the helper/tests to disk and read them back to confirm persistence. No commit, synchronization, integration, publication, or deployment is authorized.  
Stop: stop if observed backend behavior differs, another target must change, an unexpected mutation occurs, or verification and saved-state confirmation finish.  
Result record (Builder Handoff only when a distinct Builder exists): changed files; criterion-level results and evidence; saved-state confirmation; unexpected effects; unresolved checks and stop reason.

