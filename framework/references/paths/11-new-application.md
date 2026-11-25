# **PART 2 — PATH CHAPTERS**

Each chapter contains its path-specific activation, rules, playbook, and template or template references. For copying and use, apply the portable path package definition in How to Use This Document. Universal rules from Part 1 apply everywhere. Shared blocks B1-B5, templates T1-T8, Preflight Templates, and Project Control Record Templates are defined in Part 3.

# **Chapter 11 — New Application Path**

When to use: a new app, product, automation, or major feature with no existing system at risk.

Companion chapters when applicable: Ch. 20 at release; Ch. 16/17/18 per application type; Ch. 21 only when Section 8 Execution mechanism activates Platform Capability controls or Two-Agent Orchestration.

Playbook. 1. Classify project mode, decision owner, maintainer, and technical level (Phase -1). 2. Run planning/feasibility and problem-fit discovery (Phase 0). 3. Establish the requirements/MVP/non-goals/glossary/success criteria/release-blocker baseline (Phase 1); re-baseline later only when authorized evidence or decisions change it. 4. Confirm only material platform, architecture, capacity, persistence, deployment/release/update, and maintenance choices needed for dependent work (Phase 2). 5. Map material workflows, lifecycle states, data model, field purposes, record lifecycle policy, risks, and failure paths (Phases 3-5). 6. Establish a proportionate project-state/durability/version model before meaningful implementation grows (Phase 5A); create source control only when selected or required by consequence. 7. Break work into bounded authorization units or demonstrably independent workstreams. Apply Section 4.1 progression/reuse and Section 5 Decision-changing work test; phase order does not require separate owner stops, artifacts, or re-discovery of still-valid facts.

Authorization form: use the T1 operational boundary fields (Part 3). When a separate Builder exists, T1 is the canonical orchestrated form and the example below is the transported Builder Payload; the Prompt Agent substitutes verified project-specific paths, commands, and closure details before issuance. In direct single-agent execution, record the same operational fields before mutation and execute them directly; derivation partition, transport, and handoff are N/A.

Authorization-unit ID: EXAMPLE-NEW-01  
Objective: create the first read-only task list screen.  
Context and targets: confirmed project root /workspace/task-app; task fixture src/data/tasks.json; editable screen src/TaskList.tsx; tests src/TaskList.test.tsx. These paths and the existing test/build scripts are accessible. The fixture supplies status, owner, dueDate, and priority; an empty fixture array means no tasks.  
Authorized actions: read the project; edit only the screen and its tests; run npm test -- --run and npm run build. Preserve the existing styling and fixture data. No dependency installation, create/edit/delete task actions, backend integration, authentication, advanced filtering, or theme redesign.  
Expected automatic behavior: build writes dist/ and test/build commands may write local caches; these outputs are disposable and MUST NOT be published. No other automatic source or configuration changes are expected.  
Acceptance and verification: fixture tasks show status, owner, due date, and priority; an empty array shows an empty state; the screen is usable at 1280px and 375px viewport widths; no browser-console errors; tests and build exit 0. Check the rendered screen and record commands, results, and viewport observations; unavailable visual inspection is reported as pending, never passed.  
Closure: save authorized source edits to disk and read them back to confirm persistence. No commit, synchronization, integration, publication, or deployment is authorized.  
Stop: stop on missing or conflicting inputs, unexpected mutations, required work outside the allowed targets, or after verification and saved-state confirmation.  
Result record (Builder Handoff only when a distinct Builder exists): changed files; acceptance results and evidence; saved-state confirmation; unexpected effects; unresolved checks and stop reason.

