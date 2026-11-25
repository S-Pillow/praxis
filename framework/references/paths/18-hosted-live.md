# **Chapter 18 - Hosted Builders and Live Surfaces Path**

When to use: hosted no-code/AI-builder pages and apps, builder-managed projects, static-hosted sites, SPAs, custom domains, and public surfaces with SEO, sharing, or crawler requirements. This chapter verifies affected hosted/live states and platform side effects. Chapter 21 Platform Capability controls apply only when the managed platform replaces conventional repository/deployment controls; Two-Agent Orchestration applies only when a distinct Builder is used.

Companion chapters when applicable: Ch. 21 only when Section 8 activates Platform Capability controls or Two-Agent Orchestration; Ch. 20 at release.

## **18.1 Live-Surface Parity and Platform-Mutation Rules**

Hosted platforms can produce several different truths: source/config state, builder preview, generated/built artifact, live custom-domain response, and crawler-visible response. Never collapse them into one status.

**Execution self-audit.** After each authorization unit, the executing agent checks the implemented change against its acceptance criteria and reports evidence. Treat that report as a claim. Use a Builder Handoff only when a distinct Builder exists; otherwise reconcile the direct execution record. Acceptance uses the observer appropriate to each criterion: deterministic tool-observable evidence may be reconciled without a human gate; human/manual verification is required only for criteria that genuinely require human judgment or cannot be observed reliably by available tools.

Relevant-state parity. For a public or reputationally important release, identify the hosted/platform states that actually exist and can change acceptance - source/config, preview, generated/built/published artifact, live/custom-domain response, crawler-visible response, or platform-equivalent states. Verify each material state separately and mark genuinely absent states N/A; do not invent a four-state ceremony for a platform that does not expose those states.

Live-domain parity. When a live/custom domain is part of the accepted release surface, preview success does not prove live-domain success. Verify the direct live URL and only the navigation, static assets, route behavior, device/accessibility behavior, cache/reload behavior, and rollback/recovery checks material to acceptance.

**Route evidence.** HTTP success alone does not prove that the intended page rendered when a catch-all, soft-404, redirect, or fallback can return the same status. Verify at least one unique target sentinel and the absence of the not-found or fallback sentinel, plus the final URL where relevant.

**Crawler and SEO artifacts.** Public pages with search/share requirements verify crawler-visible artifacts, not only rendered browser UI: view-source/raw HTML, canonical URL, robots.txt, sitemap protocol, Open Graph tags, Twitter/social tags, share image, and scraper/debugger behavior. Static/raw HTML proves head metadata and initial markup; it cannot prove hydrated client content. Metadata fetched directly from a server does not prove external crawler, social-share, CDN, or platform-cache freshness - use the external consumer or debugger when cache state is the claim.

**Initial HTML vs hydrated app.** For SPAs and client-hydrated apps, distinguish rendered browser UI, raw server/static HTML, hydrated client state, and crawler-visible metadata.

**Static artifact shadowing.** Check whether public/, dist/, static assets, copied files, CDN or platform-generated files shadow dynamic handlers, routes, metadata, robots.txt, sitemap, images, or updated code.

Platform automatic effects. Apply Section 6 Automatic execution consequences. Hosted execution may trigger route registries, SEO or sitemap synchronization, generated imports, formatting, code generation, platform metadata, version records, CI/review/scan activity, preview builds, notifications, or other automatic effects. When Platform Capability controls are active, the capability profile identifies known material automatic behavior and whether it can be disabled; otherwise use confirmed project-state/platform facts in the Project Control Record. Each authorization unit lists only automatic effects material to its authority, cost/privacy, evidence, state, release, or next-action boundary. An unexpected governed source/config mutation is a scope event: stop affected/dependent work, classify the change, reconcile shared state, and return the appropriate outcome. Other unexpected material automatic consequences are reconciled under Section 6 and the applicable evidence/release rules. Independent work may continue only under Section 5 Scoped stopping. An automatic effect cannot be reported as harmless or PASS merely because the platform caused it.

Source durability. Apply the "Generated fixes must be source-durable" principle (Section 2) to hosted/builder output, bundles, and exports.

**PRD/observed-behavior conflict.** If a PRD or acceptance criterion conflicts with observed production behavior, stop and create a behavior clarification instead of guessing. Preserve existing production behavior unless the decision owner approves the change.

**Release correction mini-loop. Publish verification may reveal release-only defects. Handle them as coherent bounded release-correction work sized under Section 5.3, with acceptance and live checks attributable to each defect. Safely related release-only corrections may share one unit when their control envelope is the same; do not force one unit per symptom, turn the entire release checklist into a monolithic failure, or rerun unrelated release gates.**

## 18.2 Execution State, Completion, and Authorization Rules

Hosted/platform-managed work reports state through the four Block B2 dimensions; composite commit-state tokens are prohibited. Required durability/closure facts are assessed independently. An authorization unit cannot be accepted while any required closure fact remains unsatisfied or finalization is pending. When platform-owned finalization is expected after execution, record finalization = pending and perform a bounded read-only recheck for the required closure signal; do not overwrite already-achieved source/shared/artifact/release facts. Do not create a new T1 unless a distinct Builder requires new execution, corrective mutation, new authority, or a decision requires a new authorization unit.

For assessed outcome, control disposition, achieved evidence, and any pending required observation, apply Block B2 Deterministic outcome assessment and Outcome storage. Do not duplicate classification logic in the platform record.

When AI or automation performs a publish, deployment, release, update, or destructive platform action, require explicit and unambiguous authorization before execution. A direct human action may itself serve as the authorization event only when that human holds decision authority to approve that exact action, target, and scope. A human operator with execution-only authority still requires a prior authorization from the decision owner or authorized delegate; clicking the control does not create approval authority. Record who approved, who acted when different, the active source/version/artifact, the resulting release identifier, and the outcome. A locked phrase is optional; intent, authority, target, and scope are the control.

Playbook. 1. Establish or reuse the material capability profile only when Platform Capability controls are active; otherwise use confirmed project-state/platform facts, the applicable execution-access map, Project Control Record, and matching preflight. 2. Establish one coherent authorization boundary with resolved acceptance-impacting preconditions, expected mutations, criteria, and stop condition; use Builder transport only when a distinct Builder exists. 3. Run execution self-audit and only the named observer checks required by acceptance. 4. Apply Block B2 Deterministic outcome assessment and reconcile mutations. 5. Verify only affected live-surface states. 6. Use a narrow release-correction unit for release-only defects. 7. Record authorization, least-sufficient rollback readiness (Block B4), and Chapter 20 closure when activated. When Chapter 13 source-backed factual-content controls apply, load Section 13.3 and record its verification-stamp decision.

## **18.3 Live Surface Verification Template**

Feature/page: -  
Execution actor/platform: -  
Authorization unit: -  
Execution self-audit: -  
Operator verification: -  
Material hosted/platform states and results (source/config; preview; built/published; live/custom-domain; crawler-visible or equivalents; N/A when absent): -  
Public routes / initial status -\> final status -\> final URL when applicable: -  
Target sentinel / fallback sentinel when applicable: -  
Hard refresh/navigation/static assets when applicable: -  
Raw HTML / crawler-share artifacts / debugger evidence when applicable: -  
Static shadowing check when applicable: -  
Known/expected automatic mutations/evaluations/triggers: -  
Unexpected material automatic effects: none / list  
Mobile/keyboard/accessibility evidence when applicable: -  
Status: Block B2 tuple -  
Authorization event: -  
Rollback readiness: Block B4 required / achieved -  
Release corrections: -  
Evidence attribution: Block B1 -  
Final release acceptance: -

