# Repository security posture and workflow automation — discovery 02

Date: 2026-11-27. Owner added OpenSSF Scorecard and Awesome Actions to DevOps discovery. Accepted baseline Praxis v1.3.0 commit `1749f9d3632efd1ab272a69e0738fdd6bd754932`; AIPF v8.10.1 unchanged. Research branch parent `9220dbe47b204ddeba763c182d22e16b333688a5`. Scope: source-bound discovery, candidate selection method, future requirements proposals. No new PRD approval, implementation, scan, publication, service or dependency authorization. [Source register](DEVOPS-SOURCE-REGISTER-01.md#supplement-02--scorecard-and-github-actions) · [Prior DevOps discovery](DEVOPS-RELIABILITY-DISCOVERY-01.md) · [Repository-quality discovery](REPOSITORY-QUALITY-DISCOVERY-01.md).

## 1. Scorecard (DO-S19): posture evidence, not security verdict

The inspected check registry has twenty registered definitions; experimental checks are excluded by default unless activated. README states goals for automated security practice assessment and policy measurements, non-goals for definitive/one-size-fits-all verdicts, false positives/negatives and aggregate ambiguity. Check documentation defines risk, scoring, applicability and remediation. Beginner guidance separates setup, accepting contributions and packaging/release; update-tool detection does not prove it actually runs. Do not impose multiple maintainers, packaging, fuzzing, external services or scanners simply to raise score.

The inspected aggregate-scoring specification weights conclusive scores by risk (critical 10, high 7.5, medium 5, low 2.5). Negative scores including errors/inconclusive are excluded from numerator and denominator; all inconclusive yields -1. A restricted set of checks can score highly despite missing material observations. Example from specification: Binary-Artifacts 10 and Signed-Releases -1 produce aggregate 10, not evidence of release integrity. Preserve check scope, unknowns, dates, target commit, tool version/commit, and raw reasons. Do not equate Scorecard PASS/FAIL or score with AIPF B2/B4/B5 outcome or risk acceptance.

### Experimental conformance: useful evidence method

At pinned main, documented OSPS Baseline v2026.08.28 coverage: 6/64 full, 16/64 partial, 38/64 gap, 4/64 not observable. Experimental conformance evaluates eleven mapped requirements, not full coverage; current hosted HEAD only, not arbitrary local or historical commit. Actual mapping code BR01 yields FAIL on known injection/untrusted checkout patterns, NEEDS_REVIEW if no known pattern, UNKNOWN for missing workflows in this mapping. Probe no-workflows outcome is not applicable but mapping interprets as unknown since other CI may exist. AC03 uses default branch findings; classic bypass/admin visibility limited. VM02 returns NEEDS_REVIEW when policy exists, FAIL when absent, unknown on insufficient data; link does not prove valid reporting route. The implementation uses source location/snippet findings; preserve redaction. Distinguish PASS, FAIL, UNKNOWN, NOT_APPLICABLE and NEEDS_REVIEW with explicit applicability; use canonical AIPF result meanings for governed acceptance. No certification claim.

Gaps include actual released user guides, bug reporting and contribution process, secret storage detection, and organization MFA/permissions visibility. This is precisely why repository documentation/semantic verification and security review complement Scorecard. Do not claim full baseline compliance. Preserve native evidence/owner observations for admin-only settings, do not demand elevated token merely for score.

### Usage methods and information boundaries

- CLI: optional source-bound scan method; official README notes Linux/macOS, Windows may have issues. Requires verified version and target, supported platform, credential/network/API access and specific authorization; no runtime observation here.
- REST: cached public results, weekly scans omit CI-Tests, Contributors and Dependency-Update-Tool per README; actual result missing_checks governs, do not assume completeness. Public data CDLA Permissive 2.0, separate from Apache code.
- MCP: experimental stdio server documented as cached REST provider, not on-demand scanner. Offline list/explain check vs network get/compare; exposes target SHA, tool SHA/version, date, source, missing_checks and completeness. Date formats vary; -1 inconclusive and error string not defect proof. Live scans/hosted transport roadmap only. No MCP installation, result request or private target export.
- Action DO-S21: manifest defaults publish_results false; own DO-S19 workflow explicitly true, uses full-SHA action refs, read-all top-level, job security-events/id-token writes, SARIF and five-day artifact retention. Manifest uses Docker image tag internally, so action SHA alone does not pin all executable inputs. Public result publication is an external disclosure requiring separate permission. Readme says public repo action free, private support with Advanced Security, private without use CLI; plan/cost verification at selection. OIDC required when publishing; do not grant indiscriminate permissions. Scan success and publication success distinct: API rejection defaults warning, fail_on_publish_error true still warns on network/408/429/5xx. Inspect results_published, publication_status, actual stored result and retrieval identity. No green-step-only proof.

## 2. Awesome Actions (DO-S20): curated leads, not qualification

Actual index categories official resources, workflow examples, official actions, creating JS/TS/Docker actions; community management, utility/environments/dependencies/versioning, testing/lint/security/coverage, dynamic analysis, monitoring, PRs, Pages, notifications, deployments (Docker/Kubernetes/AWS/Terraform), external services, frontend/ML/build/database/network/localization/tutorials. Contribution rules emphasize concise unique categorized entries and meaningful source links. Own lint YAML uses old checkout v1.0.0 and awesome-lint v2.0.0, not immutable SHA. Some entries automatically approve/merge dependency updates or delete artifacts; these change state and can destroy evidence. No adoption from listing alone.

Direct metadata verification: DO-S24 and DO-S25 are archived despite listed under official automation. DO-S22 and DO-S23 not archived; DO-S21 not archived. No security endorsement. For candidate comparison: existing native GitHub features, current local scripts, gh CLI/API under authorized execution, existing workflow and no automation before adding a dependency. Do not import entire catalog or create duplicate CAP-B01 GitHub Actions record.

### Concrete source observations and future selection

DO-S22 action.yml supports target_commitish, tag, draft, prerelease, body, glob assets, explicit token, repository override, generated notes. Defaults overwrite_files=true and fail_on_unmatched_files=false; Node24 runtime. README describes contents:write and immutable release constraints. A well-designed approved workflow must bind accepted target SHA/tree, independently check existing tag identity and approved notes/asset manifest, prevent unapproved overwrite/missing assets, distinguish draft from publication, verify actual tag/release/download and preserve earlier recovery. No auto-release on arbitrary push or untrusted PR. Existing operator publication remains valid; connector absence not authority for workflow changes.

DO-S23 README describes artifact ID/digest, immutable artifacts v4+, overwrite deletes old ID/creates new, retention default and configurable days, hidden-file risks, compatibility limits for GHES v4+. Preserve exact run/job/attempt/commit, archive digest vs per-file digest, output/retention/access and actual download where required. No blind upload of workspace, secrets or private qualification logs; do not delete retained evidence. Source artifact upload is not release publication.

### Action qualification questions

1. Concrete problem and alternatives: existing built-in step, script, provider feature, no change; scope and actor authority.
2. Exact publisher/repo/revision, archived/maintenance/rights, manifest inputs/defaults, runtime and transitive packages/images, runner OS and hosted/server compatibility, security advisories.
3. Event trust and data flow: PR/fork vs protected release, credentials, secrets, environment, job permissions, OIDC, outbound endpoints, upload/retention/logging, cache poisoning and untrusted artifact handling.
4. Repeatability and evidence: full SHA where feasible, exact versions/digests and update strategy, fail/skip/timeout/retry/cancel/concurrency, no silent missing outputs, expected negative test.
5. State changes, cost/quota/cleanup: approvals, protected refs, deployments, releases, artifact overwrites/deletions, external calls, billing, rollback/forward recovery.
6. Actual observation and independent review where material: safe synthetic fixtures or approved read-only observations first; compare real outputs and side effects. Document limits, never invent missing evidence or claim all hosts.

## 3. Praxis-specific research observations, not approved changes

At released v1.3.0, existing CAP-B01 GitHub Actions already covers general CI discovery. CAP-V01 OpenTelemetry already exists. Do not duplicate. Scorecard is a plausible *new optional shared security/engineering quality record* after qualification; action discovery and release/artifact controls may be original cards and references under existing GitHub Actions capability. No mandatory score threshold.

Actual released .github/workflows/catalog-validation.yml blob `e7900733cbe8615820e3668490e4036de2b72688`: explicit per-job contents:read, persist-credentials:false, Linux + conditional native Windows, Python3.12 and unittest. Uses checkout@v4 and setup-python@v5 mutable major tags; future candidate to review SHA pinning and action runtime maintenance warning, verify compatible releases and tests before alteration. Path filters omit README.md and docs/**; a documentation-only PR against current main may not automatically run this validation even though standing tests check README contract. Earlier B5 release PR contained other triggering changes, so its CI evidence remains valid. Proposed future decision: ensure material doc-only changes get relevant semantic/version/link regression with cost proportionality; do not weaken required checks. Not a live audit or confirmed exploit; no changes.

## 4. Integrate with proposed specialist and shared repository quality

- DevOps: CI/CD execution/trust, artifact and release identity, platform constraints, operational readiness and recovery.
- Security: control requirements, dependency trust, least privilege, disclosure, vulnerability triage.
- QA: test efficacy, actual control/negative tests, missing observation vs failure, false positives and false negatives.
- UI/UX + Architecture: readable, appropriate, truthful README and navigation; accurate onboarding, component/operations boundaries.
- AIPF: sole authority, evidence sufficiency, acceptance and release. Do not add second score-based governance or approval runtime.

Extend DR-02 secure delivery and DR-01 repository quality in prior report with these sources; retain DR-07 Scorecard structured findings/optional CLI, Action, REST/MCP (DO-S19/21); DR-08 source-qualified workflow/release/artifact candidates (DO-S20/22–25). Revisit deferred Review Parity DR-06 for missing-data/identity distinction only under separate authority. Preserve all previous research IDs and requirements.

## 5. Candidate qualification refinements (unexecuted)

Augment existing DV-Q01/02/08/10/11/12 rather than mandatory new counts. Synthetic repository/workflow fixtures: untrusted trigger/input and job permissions, candidate missing check and stale target SHA, partial rule coverage with no known bad pattern, policy with irrelevant link, archived candidate, missing required upload artifact, overwrite existing release asset refused, scan green with publication missing, doc-only verification path. Evaluate known defect vs known good, no unauthorized writes, unknown/inapplicable distinct, actual output/effect. Optional Scorecard tool trial only if approved, pin actual released version, specify supported scope/data destination and compare findings with independent source checks; no arbitrary aggregate target or blanket compliance certification. No actual release/secret access/production probe; no mandatory external dependency. The exact PRD requirements and exercises remain owner decision.

Research stop: source discovery retained; released main, tag, registry, shared capability index, CI, source code and framework untouched.
