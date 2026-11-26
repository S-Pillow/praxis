# Technology and cost

Original conditional decision guidance; apply only within approved project intent. Source keys link to [source register](../SOURCES.md). No claim of current provider facts or project-specific acceptance.

## A10
**Decision:** Should we retain the existing stack?
- **Use when:** A new feature or system problem suggests another language/framework/library.
- **Disqualifiers / stop:** Do not migrate merely for familiarity, popularity or hypothetical performance. Check compatibility and approved environment.
- **Alternatives and consequences:** Retain known stack when it meets requirements; add narrow dependency for clear value; replace only with evidence of constraint gap and feasible transition.
- **Implementation implications:** Compare supported versions, required ecosystem, maintenance skills, security/lifecycle, licensing, operational footprint and migration cost. Pin only what project policy requires.
- **Verification / revisit:** Check supported target and contract using a minimal representative exercise; baseline before/after on actual workload if performance is driver.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** version-sensitive.

## A11
**Decision:** Build, reuse, buy or do without?
- **Use when:** A capability has internal/external alternatives and material maintenance or cost consequences.
- **Disqualifiers / stop:** Do not assume an advertised feature, integration permission or license covers your use. Do not add a service if no capability needed.
- **Alternatives and consequences:** Existing components or local implementation offer control; maintained library can reduce effort; managed service can transfer some operational work but creates trust, cost and exit dependencies.
- **Implementation implications:** Compare total cost including upgrades, monitoring, migration, limits and downtime; record permissions/rights and failure mode. Keep an exit route for critical dependency.
- **Verification / revisit:** Verify decisive capability, compatibility and permissions with qualified evidence; exercise failure/absence locally when possible.
- **Provenance:** P1,P2,F0 (original synthesis; no upstream content copied). **Maintenance:** version-sensitive.

## A12
**Decision:** How does a fixed budget affect the design?
- **Use when:** A real operating cost ceiling, free-only requirement or resource constraint matters.
- **Disqualifiers / stop:** Never infer free operation from marketing, estimated average usage or budget alerts. Unknown hard-stop behavior is a gap.
- **Alternatives and consequences:** No service/existing infrastructure/local are first-class. Hosted option may be viable when terms, quotas, worst-case behavior and operational costs are qualified.
- **Implementation implications:** Model expected and peak usage against verified billing units, reset/overage, account scope and enforced ceiling. Design explicit degraded behavior; do not enable billing.
- **Verification / revisit:** Test boundary and exhaustion without paid calls; distinguish estimates from observed terms and enforced caps.
- **Provenance:** P1,P2,F0 (original synthesis; no upstream content copied). **Maintenance:** volatile-at-use.

