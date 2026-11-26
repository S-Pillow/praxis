# Security and privacy capability candidates

Discovery only; no integration, approved dependency or execution. Compare existing/no-tool alternatives. Apply [QUALIFICATION.md](QUALIFICATION.md), exact version/plan, data boundary, rights, permission, cost ceiling and failure checks.

## CAP-S01

**Name:** Safe Anything

**Tags:** static source / secret / dependency review

**Candidate use:** Manual source review, existing checks or no scanner first. Candidate pattern-based local review.

**Constraints to check:** Qualify language/rules, skipped files, path scope, redaction and report sensitivity. Pinned privacy doc reports package/ecosystem/version metadata to OSV; offline omits that dependency check and reduces coverage. No actual network/redaction proof. Reject prohibited transfer; check runtime/failure and resource cost.

**Official documentation pointer(s):** [Pinned source](https://github.com/erkamyaman/safe-anything/tree/09a7269eac49000f6cee64af2f94d2ce05da64be).

**Pricing / terms / licensing pointer(s):** [Source/terms](https://github.com/erkamyaman/safe-anything/blob/09a7269eac49000f6cee64af2f94d2ce05da64be/LICENSE); verify current commercial eligibility, data policy, prices and enforceable limits if material.

**Observation / verification state:** 2026-11-25 project-local. MIT root verified; privacy doc 03b0e23cf4fc08a93a6f3798e46ca4904c59c874 reread. Provider statement only; runtime, accuracy, pricing/terms, OSV availability, execution not qualified.

**Origin and redistribution:** Original Praxis record, reference-only. No code, executable, assets or rules imported. See [security source register](../../skills/security-privacy/SOURCES.md).

## CAP-S02

**Name:** DevToys

**Tags:** local developer data

**Candidate use:** Existing standard library/local utility first; candidate transformation utility.

**Constraints to check:** Qualify exact utility and OS, clipboard, logs/temp, extension/update source and actual egress. Extension trust is separate. Local processing not blanket no-network proof. No installation or real sensitive input; check cost/terms and failure behavior.

**Official documentation pointer(s):** [Pinned source](https://github.com/DevToys-app/DevToys/tree/2dbbc8aa594978d11165a0e8112243c96a277dbc).

**Pricing / terms / licensing pointer(s):** [Source/terms](https://github.com/DevToys-app/DevToys/blob/2dbbc8aa594978d11165a0e8112243c96a277dbc/EXTENSIONS-TERM-AND-CONDITIONS.md); verify current commercial eligibility, data policy, prices and enforceable limits if material.

**Observation / verification state:** 2026-11-25 project-local. MIT root per checkpoint; extension terms blob 352553f8efd65f493477ba687ac1d9b9d2cc27ae reread. Runtime, edition, extension rights, costs and availability unqualified.

**Origin and redistribution:** Original Praxis record, reference-only. No code, executable, assets or rules imported. See [security source register](../../skills/security-privacy/SOURCES.md).

## CAP-S03

**Name:** Umami

**Tags:** analytics and privacy

**Candidate use:** No analytics, aggregate-only counts or existing approved metrics first.

**Constraints to check:** Pinned schema has session and distinct identifiers; qualify actual collection, replay/masking, logs, recipients, permissions, retention/export/delete/backup, residency, plan and costs. Self-hosted and cloud responsibilities differ. Reject if prohibited identifiers cannot be excluded; no setup or transfer.

**Official documentation pointer(s):** [Pinned source](https://github.com/umami-software/umami/tree/dbb8d606fbd4e99220fb83bcb4abad3e0f97f42a).

**Pricing / terms / licensing pointer(s):** [Source/terms](https://github.com/umami-software/umami/blob/dbb8d606fbd4e99220fb83bcb4abad3e0f97f42a/LICENSE); verify current commercial eligibility, data policy, prices and enforceable limits if material.

**Observation / verification state:** 2026-11-25 project-local. MIT root per checkpoint; Session/SessionLink schema blob ba94dbceaab7617b8554450a119f3716703a1dff reread. No live deployment, collection, replay, deletion, plan/terms or hard spend control observed.

**Origin and redistribution:** Original Praxis record, reference-only. No code, executable, assets or rules imported. See [security source register](../../skills/security-privacy/SOURCES.md).

## CAP-S04

**Name:** OpenRewrite

**Tags:** targeted remediation

**Candidate use:** Small reviewed patch or existing migration first; deterministic transformation candidate.

**Constraints to check:** Qualify parser/recipe version and rights independently, source/metadata transfers, execution permissions, resource and commercial cost, failure/exit. Preview exact delta and recovery; reject uncontrolled bulk modification. No automatic execution.

**Official documentation pointer(s):** [Pinned source](https://github.com/openrewrite/rewrite/tree/4d2110dbbf7098a3185b6eb0e94c7f5f55a20d35).

**Pricing / terms / licensing pointer(s):** [Source/terms](https://docs.openrewrite.org/licensing/openrewrite-licensing); verify current commercial eligibility, data policy, prices and enforceable limits if material.

**Observation / verification state:** 2026-11-25 project-local. Root Apache-2.0 blob 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64 reread; actual module/recipe/runtime and commercial terms unqualified.

**Origin and redistribution:** Original Praxis record, reference-only. No code, executable, assets or rules imported. See [security source register](../../skills/security-privacy/SOURCES.md).
