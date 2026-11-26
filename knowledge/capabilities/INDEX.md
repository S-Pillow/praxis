# Shared technology and service capability index

This independently usable index serves any specialist or agent. It contains original discovery records, not approved dependencies, operational integrations, pricing guarantees or an exhaustive provider directory. Start from the question; no external service is assumed. Read only relevant groups and [QUALIFICATION.md](QUALIFICATION.md) when decision-sensitive facts matter. [SOURCES.md](SOURCES.md) records rights and evidence classes.

## [Application delivery and hosting](hosting.md)
First alternatives: No hosted service for offline/local tools; retain existing approved host or self-managed static/app server if it meets deployment, maintenance and traffic needs. Distinguish static assets from server runtime and background work.

- [CAP-H01 — Cloudflare Pages / Workers](hosting.md#cap-h01)
- [CAP-H02 — Vercel](hosting.md#cap-h02)
- [CAP-H03 — GitHub Pages](hosting.md#cap-h03)

## [Structured data and persistence](relational-data.md)
First alternatives: No persistence if not authorized; in-memory for ephemeral state; existing database before a new one; embedded or self-managed stores where suitable.

- [CAP-D01 — SQLite](relational-data.md#cap-d01)
- [CAP-D02 — PostgreSQL](relational-data.md#cap-d02)
- [CAP-D03 — Neon](relational-data.md#cap-d03)
- [CAP-D04 — Supabase](relational-data.md#cap-d04)
- [CAP-D05 — Cloudflare D1](relational-data.md#cap-d05)

## [Files and object data](object-storage.md)
First alternatives: Keep files local if authorized and usable; use existing object store when already approved; no media store if data not needed.

- [CAP-O01 — Cloudflare R2](object-storage.md#cap-o01)

## [Identity and account services](identity.md)
First alternatives: Avoid accounts for local single-user tools where appropriate. Reuse approved identity provider; consider self-hosted identity only if the team can maintain it. Do not implement bespoke password handling merely to avoid a service.

- [CAP-I01 — Supabase Auth](identity.md#cap-i01)

## [Caching and admission control](cache-rate.md)
First alternatives: Do not add shared state by default; use bounded in-process cache/rate controls for single process or existing shared store if necessary. Establish staleness and failure policy.

- [CAP-C01 — Redis](cache-rate.md#cap-c01)
- [CAP-C02 — Upstash Redis](cache-rate.md#cap-c02)

## [Deferred work and scheduling](async-work.md)
First alternatives: Direct bounded calls, in-process workers or durable SQL work records may suffice. Keep existing scheduler/queue if it fits. No queue solely for retries.

- [CAP-Q01 — Cloudflare Queues](async-work.md#cap-q01)

## [Outbound notifications](messaging.md)
First alternatives: No email when in-app/local notification is sufficient. Reuse existing approved mail relay; self-host only if deliverability, abuse and operations are sustainable.

- [CAP-M01 — Resend](messaging.md#cap-m01)

## [Network naming, delivery and perimeter](network-boundary.md)
First alternatives: Keep existing authoritative DNS/CDN/security policy where fit; local/offline apps may need none. DNS hosting and recursive resolution are distinct decisions.

- [CAP-N01 — Cloudflare DNS / CDN](network-boundary.md#cap-n01)

## [Diagnostic signals and operations evidence](observability.md)
First alternatives: Use existing application logs and local tracing first. Choose signals from actual incident/release questions; no collection or export solely because available.

- [CAP-V01 — OpenTelemetry](observability.md#cap-v01)
- [CAP-V02 — Sentry](observability.md#cap-v02)
- [CAP-V03 — Interfere](observability.md#cap-v03)

## [Build, verification and engineering review](engineering-quality.md)
First alternatives: Use local tests and existing CI/review before adding a product. Distinguish automated review findings from independent acceptance or authorization. Review Parity remains deferred.

- [CAP-B01 — GitHub Actions](engineering-quality.md#cap-b01)
- [CAP-B02 — Claude Ship](engineering-quality.md#cap-b02)
- [CAP-B03 — Playwright](engineering-quality.md#cap-b03)
- [CAP-B04 — Hypothesis](engineering-quality.md#cap-b04)
- [CAP-B05 — Stryker](engineering-quality.md#cap-b05)
- [CAP-B06 — Pact](engineering-quality.md#cap-b06)
- [CAP-B07 — EvalView](engineering-quality.md#cap-b07)
- [CAP-B08 — Promptfoo](engineering-quality.md#cap-b08)

## Other discovery candidates
Netlify, Render, Clerk, Firebase, QStash, Postmark, deSEC, UptimeRobot, Grafana Cloud, GitLab CI and other S3-compatible stores are names from the approved shortlist only. No factual provider record, license or approval asserted. Locate and qualify official sources if a real use case warrants adding one. No full Free-for-Dev import.

## [Security and privacy capabilities](security-privacy.md)

First alternatives: manual scoped review, existing tools, no collection, approved local processing and small reviewed correction. No installation or scanning implied.

- [CAP-S01 — Safe Anything](security-privacy.md#cap-s01)
- [CAP-S02 — DevToys](security-privacy.md#cap-s02)
- [CAP-S03 — Umami](security-privacy.md#cap-s03)
- [CAP-S04 — OpenRewrite](security-privacy.md#cap-s04)

Other security candidates (OSV-Scanner, Semgrep, Gitleaks, GitHub security features, CycloneDX / Dependency-Track and aeo.js) remain discovery only pending concrete need and exact version, rights, data and coverage qualification. See [security source register](../../skills/security-privacy/SOURCES.md).
