# Praxis — Architecture & Engineering Design Specialist
## Build plan v1.0 | Final planning specification

**Date:** 2026-11-25  
**Workstream:** PRAXIS-ARCH-01 (proposed identifier)  
**State:** finalized planning copy accompanying PRD v1.2; implementation not authorized by this plan  
**Target:** proposed Praxis v1.1.0 (version subject to owner approval); AIPF v8.10.1 unchanged  
**Source baseline observed:** `S-Pillow/praxis` main `66138bd1c1249d004d94e9e4877eb55a2e7cd955`, protected. Roadmap PR #14 remains open at `478796b0946847575382b94b1c0ed83f2ac5f373`. The earlier Word PRD v1.1 was a review draft; final PRD v1.2 is the consolidated product planning reference. Published v1.0.0 remains immutable.

## 1. Decision and product boundary

Build an advisory specialist that helps a Prompt Agent or direct agent choose suitable architecture, technology and external engineering capabilities for the actual task. The specialist will contribute decision knowledge, not a second framework, a mandatory review pipeline, or a new authorization mechanism. The existing AIPF and approved target requirements govern. Keep the specialist usable from plain local files, with no required network, cloud account, external API, package installation, background service, or separately installed Builder skill.

**Deliverable:** one registered specialist with design/evolve/critique modes, progressive architecture guides and original decision cards; a shared, source-linked discovery index of external capabilities; an official-source qualification method for decision-sensitive provider facts; compatibility extension to current Praxis entry/registry/helper; focused regression and practical workflow validation; documentation. The index should be useful later to QA, Security and DevOps, but none of those specialists is implemented here.

The service index is not a marketplace or a catalog of approved dependencies. No promise that providers remain free, that a host can use an advertised integration, or that advertised capabilities have been independently validated. Review Parity remains experimental; Claude Ship and Interfere are candidates to know about, not required runtime components. No import of third-party code/content without item-specific redistribution qualification.

## 2. Consolidated research decisions

| Evidence | Decision for this build |
|---|---|
| Architecture discovery report, sections 3–5 | Original guides informed by system architecture, module design, quality attributes and conditional tradeoffs. Do not clone whole skills or methods. |
| Discovery sections 6–7 | Minimal registry compatibility change; optional retrieval and multi-path applicability; one agent synthesizes specialist guidance. |
| PRD v1.1 AR-01–14 | Context, useful alternatives, simplicity, portable instructions, provenance, truthful fallback and compatibility drive acceptance. |
| Free-for-Dev | Use to discover candidate services and missing capability categories. Do not ingest the directory or its descriptions wholesale. |
| Interfere | Optional error investigation/release evidence provider; teach privacy, telemetry and actual access boundaries. No MCP installation or telemetry export in this unit. |
| Claude Ship | Optional external PR review, correction and policy-based approval capability; respect cost, permissions, existing branch policies and independent acceptance. No enablement in this unit. |
| Review Parity | Design evidence-friendly outputs: identifiable source state, observation requirements and unresolved assumptions. No Go helper import, receipt protocol, governance DSL or resumed benchmark program. |

## 3. Knowledge architecture

### 3.1 Core guidance and progressive navigation

Use `skills/architecture/` (proposed ID `aipf-architecture`, specialist version `0.1`). Initial guide coverage:

| Guide | Decision cards / questions to cover |
|---|---|
| Drivers and constraints | Significant requirements; quality scenarios; hard constraint vs preference; reversibility and uncertain assumptions |
| System shape | Local app, single deployable, modular monolith, client/server, service split, event-oriented system |
| Module and interface design | Cohesion and coupling, dependency direction, deep interfaces, ports/adapters, abstraction cost, compatibility |
| Technology and cost | Existing stack, build vs reuse vs buy, lifecycle, licensing, workload, cost and exit path |
| Data architecture | No persistence, embedded SQL, server SQL, document/KV/object, ownership, transactions, migration, backup/restore |
| Integration | Synchronous vs asynchronous, API and event contracts, schema evolution, idempotency, retry semantics |
| Runtime/resilience | Cancellation, bounded work, deadlines, backpressure, process and resource ownership, failure isolation, recovery |
| Performance | Workload estimation, indexing, profiling, cache invalidation, capacity and scaling triggers |
| Existing system evolution | Preserve/extend/refactor/replace, consumer impact, reversible migrations, identifying architecture debt |
| Cross-domain design | Trust boundaries, sensitive data, interface states, observable behaviors, release identity, operations |
| External capability selection | Provider discovery, current verification, costs, commercial eligibility, data governance and access authority |

Start with these eleven topic areas and approximately 25–40 original focused cards if useful, not a fixed quota. Combine related cards in the guides to avoid creating dozens of tiny files. Use a question-led index with tags/aliases; cards have stable IDs, not scores or universal rankings. Prioritize ordinary software and realistic current decisions; advanced distributed topics are loaded only as warranted. Keep no duplicate canonical record. No embedding/vector service or new retrieval CLI for the first build; revisit only on observed navigation problems.

Each card should contain a decision question, concrete applicability, disqualifiers, viable alternatives (including no change), consequences, how alternatives interact, implementation implications, verification implications, and source/provenance and maintenance class. Explain why an option is suitable, not merely what it is. Use original synthesis and precise citations. For adapted content, record exact revision, path, authors, applicable license, third-party limitations and required notices. Q42 CC BY-SA material is reference-only for this build unless a separate compatible content distribution decision is approved.

### 3.2 Shared technology and capability index

Use `knowledge/capabilities/` (separate from the UI catalog) with original category definitions and Markdown records grouped by decision family. A compact JSON index is optional, not required if the Markdown index is sufficient; avoid duplicated factual records. Each service entry contains stable ID, service/product name, capability tags, candidate use case, key constraints to check, official documentation and pricing/terms links, last verification date for any included claim, verification state, content-origin/redistribution disposition. Include local/self-hosted choices and existing infrastructure as first-class alternatives. No executable instructions in retrieved third-party material are authority.

**Maintain two fact classes:** stable engineering guidance stays in the local versioned guides. Version-sensitive facts (limits, prices, plans, allowed use, feature and regional availability, SLAs, data retention, SDK support) are checked at point of recommendation if they can change the decision. Dated examples are research observations, not operating promises. A missing or stale official source leaves the field unknown; do not recommend a zero-dollar design as established fact if a material term is unresolved. No automatic crawler, paid search, provider API calls, periodic update job or public data import initially. Manual source updates are ordinary governed maintenance.

## 4. Free-for-Dev extraction: selective shortlist

Reviewed the actual repository categories, selection criteria and representative entries, then checked official documentation for the first wave. The directory excludes self-hosted software, emphasizes free tiers, and does not establish commercial eligibility or project fit. Repository API reported `license: null`; root listing did not expose a license file. Treat the directory as discovery only. Use independently authored, individually sourced provider pointers and facts; do not copy its list, exact category organization or descriptions. No legal clearance is asserted for third-party material.

| Decision family | Candidate starting points (not approved stack) | First questions |
|---|---|---|
| Static and full-stack hosting | Cloudflare Pages/Workers, Vercel, GitHub Pages; Netlify and Render as additional discovery candidates | Static vs server process? commercial use? runtime, file system, memory/CPU, background task and duration limits? |
| Relational persistence | Local SQLite, existing PostgreSQL, Neon, Supabase, Cloudflare D1 | Is storage required? writer concurrency, transactions, data residency, backups, idle behavior and cost? |
| Object/media storage | Local files if appropriate, Cloudflare R2; S3-compatible alternatives | Egress vs requests, data lifecycle, ACLs, backups, portability |
| Authentication/backend | Existing identity provider, Supabase Auth; Clerk/Firebase as discovery candidates | Tenant isolation, MFA/SSO, export, MAU definition, account recovery, session and data policy |
| Cache/rate limiting | In-process cache, existing Redis, Upstash Redis | Shared state actually required? cache correctness, eviction, atomic operations, network latency and quota |
| Async work/scheduling | In-process bounded work, durable SQL jobs, Cloudflare Queues; QStash as discovery candidate | Delivery guarantees, deduplication, backpressure, retries, cancellation and dead-letter behavior |
| Messaging/email | Resend; Postmark and existing approved mail service as alternatives | Transactional need, sending limits, verified domains, retry, privacy and deliverability |
| DNS/CDN/security perimeter | Existing DNS/CDN, Cloudflare; deSEC as discovery candidate | DNS hosting vs resolver, TLS, DNSSEC, migration and management boundaries |
| Observability | Existing logs, OpenTelemetry, Sentry, Interfere; UptimeRobot/Grafana Cloud as discovery candidates | Required signal, sensitive fields, sampling, retention, release correlation, read-only access and actual coverage |
| Build/review/quality | Existing GitHub Actions, GitLab CI if appropriate, provider-native checks, Claude Ship | CI runners, artifact retention, spend caps, independent review, approval boundaries |

The initial index needs enough useful alternatives for these decisions, not every product name in Free-for-Dev. Candidate names marked discovery-only need primary-source qualification before factual entry creation. Explicitly defer general productivity tools, fonts, design tools, education, resume builders, unrelated low-code products, mass marketing, generic AI APIs and niche APIs until a use case warrants them. No requirement for any particular provider to appear in a project's selected architecture.

### 4.1 Why live qualification is essential (observed 2026-11-25)

| Service | Directory/primary-source observation | Consequence |
|---|---|---|
| Neon | Directory reported 0.5 GB per project; official pricing showed 1 GB per project and 100 CU-hours/month per project on Free. | Directory is not a reliable current quota authority. Recheck actual plan and region before selection. |
| Upstash Redis | Directory reported 256 MB; official price page showed 250 MB, 500K commands/month and 10 GB monthly bandwidth on Free. | Check units, command counts and network limits; no free-tier capacity assumption. |
| Supabase | Official Free pricing showed 500 MB database, two active projects and inactivity pausing after one week. | A dormant but always-available production app may not fit; evaluate backup/restore and support separately. |
| Cloudflare Workers | Official Free pricing showed 100,000 requests/day and 10 ms CPU/invocation. | Requests alone cannot determine suitability; CPU and runtime behavior matter. |
| Cloudflare R2 | Official free allowance applies to Standard storage; requests and stored amount have separate dimensions. | No egress charge does not imply zero bill; model requests and storage class. |
| Vercel | Official terms and pricing restrict Hobby to personal/non-commercial use. | Exclude Hobby when commercial use is established; assess paid plan or alternatives. |
| Resend | Official sending comparison showed 100/day Free limit. | Peak day volume matters independently of monthly allowance. |

These are dated illustrations; not a comprehensive provider comparison or a determination of all terms. See section 10 for primary sources. Never encode these as permanent limits or advertise an architecture as guaranteed free.

### 4.2 Practical selection method

1. Start with the required behavior, user/workload scale, existing assets, budget and constraints. Ask only unknowns that can change the decision.
2. Consider no service, existing component, local/self-hosted and hosted alternatives. Exclude anything that violates hard constraints (commercial terms, offline, data residency, incompatible API or runtime, unacceptable cost).
3. For the small remaining set, verify the material official plan features, terms and technical limits. Include account/project scopes, billable units, burst/peak behavior, quota reset, what happens after exhaustion, billing controls, egress, minimum charges, idle/retention behavior, region and export where relevant. Treat an alert as distinct from an enforced spending cap.
4. Estimate expected and peak demand with explicit assumptions; include non-provider costs (maintenance, backups, incident response, migration). Do not use a cost formula without a verified billing basis. No numeric score is required; explain the recommendation and tradeoffs.
5. If a zero-spend constraint is binding, establish an enforceable resource ceiling or documented hard-stop behavior; otherwise label cost safety unestablished and return to the decision owner where needed. Never provision, enable billing, install, grant scopes or transfer data based on discovery alone.
6. Communicate selected provider only after the applicable authorization/decision, the specific limits and design assumptions, accessible implementation inputs, required configuration boundaries, degraded/failure behavior, and verification implications. Keep credentials out of payloads and records. Revisit facts when the plan, usage or material environment changes.

## 5. Optional external tools: scope for this release

Interfere exposes separate read-only and read/write MCP endpoints. Its documentation connects errors with traces/logs, sessions and releases. Include a capability record describing what evidence may be available, not a preconfigured connection. Prefer existing project observability and vendor-neutral instrumentation such as OpenTelemetry where warranted. Record data categories, redaction, retention, environment/release identity, sampling and known blind spots; a provider's suspected cause is not proof. Read-only does not make sensitive reads or third-party data transfer authorized. No session replay by default. Interfere pricing/free tier not confirmed in this pass. [E1–E3]

Claude Ship has review, PR correction and policy-based approval components, with beta features and usage-based cost; observe-only approval can still incur review/classifier charges. Record as an optional candidate. Don't create automatic fixes, approval policy, agent workflow, merge permissions or spending. AIPF remains authoritative. [E4]

Review Parity: retain design compatibility with future read-only release evidence auditing (claim, source identity, observation, freshness, limitations). Do not require its helper, schemas or receipts. Do not imply testing/integrating experimental software was authorized. No MCP client or generic tool execution abstraction in this build.

## 6. Integration design and file-level plan

Proposed paths; verify the actual repository before implementation. Existing framework, UI/UX data and recommendation interfaces are protected.

```text
skills/architecture/
  SKILL.md                     # activation, modes, decision synthesis, fallback
  INDEX.md                     # question -> relevant guide/card
  references/*.md              # original progressive guides with cards
  SOURCES.md                   # source/rights register
knowledge/capabilities/
  INDEX.md                     # question -> decision family/provider candidates
  *.md                         # grouped independently authored records
  SOURCES.md                   # official references, provenance, maintenance
skills/specialists.json        # additive architecture registration
skills/praxis/SKILL.md          # multi-specialist integration guidance
scripts/praxis_context.py      # backward-compatible path/optional lookup handling
PRAXIS.md, skills/README.md     # usage and integration guidance
README.md, docs/PRD.md, docs/ARCHITECTURE.md, docs/TESTING.md, CHANGELOG.md
  # align with accepted design and actual availability; preserve release evidence
research/                      # discovery/build record as approved, no private data
 tests/                        # affected routing/compatibility/reference tests
```

Add repository-local discovery adapter only if appropriate for the existing host layout. Update `AGENTS.md` only if needed to keep discovery coherent. No second routing engine. No placeholder for unimplemented specialists. Don't treat proposal PR #14 as merged; resolve roadmap and PRD once, integrating accepted planning content without conflicting duplicate PRs.

**Registry proposal:** retain UI/UX v0.3 entry as-is and extend reader to accept `chapters_any: [11,12]` for architecture. Existing singular `chapter` means the same one required chapter. Any additional applicable paths remain selected canonically by AIPF; path overlap alone is not activation. Architecture task IDs `architecture-design`, `architecture-evolve`, `architecture-critique` map to the corresponding modes, with explicit agent selection. Omit `retrieval_script` for architecture. Resolve checks skill availability independently of optional lookup. Legacy UI tasks keep exact task names, `--mode`, `--platform` and JSON shape. Existing UI lookup error/empty/completed and no-activation/path-recheck status semantics preserved. If architecture lookup requested via helper, report explicitly `lookup_status: not_applicable` and do not execute a process. An architecture result is not evidence that an agent read its guides. Consider schema v2 plus v1 compatibility only if the actual consumers require it; proposed wire changes must be documented and tested, not silently made.

**Composition:** a material user-facing system design may consult both existing UI/UX and architecture separately in the same agent; synthesize once. Do not require a multi-task CLI or new orchestration service solely to achieve composition. Existing single task helper remains optional; direct consultation works without Python. No fake retrieval command or mandatory external search.

**CI impact:** existing workflow already covers skills/scripts/tests; check path filters for the proposed new `knowledge/**` and relevant docs. Extend only as needed for regression coverage of new files. Do not alter existing manual enrichment permissions or execution triggers. Keep frozen UI output and existing test expectations unchanged unless a genuine authorized interface change requires explicit reconciliation.

## 7. Build sequence

One coherent development authorization may cover B1–B4 with explicit gates and stop boundary; do not demand separate owner approval for each mechanical step. This plan is a proposal, not authorization. Integrate/merge/publication only if explicitly covered in later execution authority.

| Unit | Work | Exit / evidence |
|---|---|---|
| B1 — establish design baseline | Recheck repo, reconcile the final PRD v1.2 and roadmap documentation, choose exact files and compatibility contract, select source rights policy; freeze relevant acceptance scenarios and source baseline. | Approved bounded scope; no unclear material architecture or licensing decisions. No code mutation before applicable authority. |
| B2 — build original knowledge | Write skill, topic guides, conditional cards and source registers; create shared discovery index with priority families and official pointers, include verified snapshots only where useful. | Coverage of initial decision families; useful counterexamples; every selected reference traceable; no unqualified copied material. |
| B3 — integrate and protect existing behavior | Implement additive registry/helper, entry, conditional discovery and docs; update affected tests and CI filter where needed. | Architecture consultation and non-activation correct; missing skill/lookup fallback truthful; v1 UI contract intact; no external dependencies. |
| B4 — qualify and correct | Run focused tests and full standing regression once for integrated candidate; run practical scenarios below, using direct and distinct-agent observations; fix actual defects only with targeted reruns. | Requirement-level evidence, honest limits, preserved invariants and exact candidate identity. No comparative research requirement. |
| B5 — delivery | Record observed behavior and final diff; prepare versioned docs and private/local or branch candidate; review/merge and release only under explicit authority. | Source identity, CI and actual workflow evidence reconciled; v1.0.0 tag unchanged; proposed v1.1.0 published only if authorized. |

### 7.1 Practical test/acceptance matrix

| Scenario | Proposed evidence / PRD mapping |
|---|---|
| Local import/report utility; offline, bounded workload | Select simple design; explicit durability, repeat import identity, failure behavior, no hosted services. AR-02–05,09; AS-AC02 |
| New small commercial web app; fixed operating budget | Compare existing/local/hosted where viable, detect Hobby commercial-use conflict, verify terms, establish unknowns and safe quota/overage behavior. AR-03,04,10,14; AS-AC02,07 |
| Existing URL Activity Scanner; request for historical results | Identify conflict with no persistence; preserve existing intent unless owner authorizes change. No production scan or mutation. AR-02,06,08; AS-AC03,06 |
| Existing API operation with uncertain completion | Explain retry/idempotency/compatibility and observable verification, not default broker. AR-05,06,09; AS-AC03,06 |
| Combined UI and data-driven dashboard | Both specialists contribute coherent interface, data and failure states; avoid duplicate governance. AR-07,13; AS-AC05 |
| Distinct Builder receives only authorized payload + target inputs | Meaningful implementation without hidden Praxis/AIPF/PRD/specialist context; exact requirements and evidence. AR-07; AS-AC04 |
| Direct task; unrelated small change | Same capability without artificial handoff; no activation for immaterial task. AR-01,07,13; AS-AC01,05 |
| Unavailable provider/source or lookup | Do not fabricate pricing, access or retrieval; continue with qualified alternatives or identify real decision gap. AR-10,11,14; AS-AC07,08 |
| Registry / existing UI regressions | Multi-path applicability, invalid task, missing skill, no process execution, optional retrieval, source links, legacy schema, unchanged UI output and framework integrity. AR-12,14; AS-AC09 |
| Actual candidate / final documentation | Observer and source-bound evidence, acceptance decisions and known limitations before release. AS-AC10 |

Combine scenarios into 2–3 practical exercises where they naturally cover multiple criteria; use a disposable local app for implementation, a read-only existing-system architecture exercise, and focused service selection/negative cases. Use actual tools and observable outcomes where applicable. Fresh independent Builder exercise where necessary; don't create agents solely to satisfy a role label. Record material rationale and failures, not artificially scored preference tables. Test deterministic helper behavior separately from semantic advice. If source or environment is unavailable, mark the corresponding evidence unestablished; no invented test pass. Do not run paid calls, live integrations or Docker benchmark harnesses.

## 8. Scope exclusions and recovery

No standalone AIPF edits, change to released UI design catalog/engine, production app changes, Review Parity integration, second specialist, mandatory API/MCP, provider accounts, deployment or paid usage. No automatic import/enrichment crawler or vector store. No independent comparative testing requirement. No release tag or visibility change under planning authority. Preserve baseline commit and release tag; branch-based changes allow ordinary revert or PR closure before merge. If an actual defect/rights issue requires a material new boundary, stop the affected portion and resolve it; don't expand work into unrelated cleanup. Carry forward historical limitations without re-proving unaffected evidence.

## 9. Decisions recommended for owner approval

Approve proposed architecture scope, modes and file-based knowledge model; approve independently authored provider discovery index and point-of-use qualification, with no copied directory content or services installed; approve minimal registry compatibility change and practical validation scope; reconcile the draft PRD/roadmap into the governing documentation. Recommended product version v1.1.0 once the feature is accepted; PRD revision is independent. Later future specialists may reuse capability index without coupling to architecture module. Future Review Parity evidence auditing can consume existing evidence; no protocol commitment today.

**Stop:** this document is a proposed build plan, not a Builder Payload or release authority. Owner may authorize a coherent implementation unit covering these decisions and gates without authorizing public publication. Produce a durable candidate and evidence, not an endless series of approval requests.

## 10. Source register and verification notes

Access date for new web observations: 2026-11-25. Earlier detailed research source register remains in the discovery report, section 11. New primary links below support the examples; links are not redistribution licenses.

- P1: [PRD v1.2](PRD.md) — consolidated AR-01–14, KI-01–08, NFR-01–10 and AS-AC01–10; target requirements, not implementation authority.
- P2: `Praxis_Architecture_Specialist_Discovery_2026-11-25.md` — research basis, pinned skill candidates and licenses, guidance and integration analysis.
- P3: [Praxis registry](https://github.com/S-Pillow/praxis/blob/66138bd1c1249d004d94e9e4877eb55a2e7cd955/skills/specialists.json), [context helper](https://github.com/S-Pillow/praxis/blob/66138bd1c1249d004d94e9e4877eb55a2e7cd955/scripts/praxis_context.py), [roadmap PR #14](https://github.com/S-Pillow/praxis/pull/14); baseline rechecked via GitHub, no changes made.
- F1: [Free-for-Dev](https://free-for.dev/), [actual repository README](https://github.com/ripienaar/free-for-dev) and repository metadata (`license: null`). Public list discovery only; selected entries inspected, not every entry qualified.
- F2: [Neon pricing](https://neon.com/pricing); [Supabase pricing](https://supabase.com/pricing); [Upstash Redis pricing](https://upstash.com/pricing/redis). Official pages compared with selected directory entries.
- F3: [Cloudflare Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/); [R2 pricing](https://developers.cloudflare.com/r2/pricing/). Check actual plan and product-specific terms at selection.
- F4: [Vercel terms](https://vercel.com/legal/terms) and [pricing](https://vercel.com/pricing); [Resend pricing](https://resend.com/pricing); [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions); [Sentry pricing](https://sentry.io/pricing/).
- K1: [SQLite appropriate uses](https://www.sqlite.org/whentouse.html); [PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html). Use actual version documentation when selected.
- E1: [Interfere documentation](https://interfere.com/docs); [MCP](https://interfere.com/docs/integrations/mcp). Documented capabilities only, no live access or integration validation.
- E2: [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/). Optional standards-based instrumentation reference, not required implementation.
- E3: [Interfere documentation index](https://interfere.com/docs/llms.txt). Product release/session/observability references.
- E4: [Anthropic, Introducing Claude Ship](https://claude.com/resources/articles/introducing-claude-ship), November 23, 2026. Provider-stated features and limitations, not independent performance evidence.

**Limitations:** this is a design, not a working implementation. Selected public sources and provider pages were inspected; complete terms, region/plan/account-specific limits, all candidate license chains and live provider behavior have not been qualified. No candidate code or external service executed. No runtime or implementation changes were made in the research. This publication of planning documentation is not a release or implementation authorization. Proposed paths, registry extension, initial knowledge volume, scenario grouping, version and feature boundary are design decisions for review. No claim of demonstrated superiority or actual release readiness.
