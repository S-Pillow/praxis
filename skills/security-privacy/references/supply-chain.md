# Software supply chain

Advisory decisions; examples use dummy inputs and require actual authorization and safe observation. No blanket requirements.

## SD21

**Decision:** Dependency selection and provenance

**Context / use when:** New package, binary, plugin or build tool.

**Alternatives and tradeoffs:** No new dependency or approved existing first; compare maintained candidates for fit, exposure, rights and recovery.

**Constraints / unsuitable conditions:** Inspect publisher, immutable version, lockfile, transitive dependencies, install/build scripts, runtime permission and distribution rights. Popularity not trust.

**Verification / revisit:** Check locked artifact and authorized diff; existing tests after approved selection. Do not install or execute candidate just to inspect it. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-03; SR-07; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD22

**Decision:** Advisory applicability and freshness

**Context / use when:** Scanner warning or dependency advisory.

**Alternatives and tradeoffs:** Use actual inventory; local offline match if freshness adequate; authorized current advisory lookup if needed.

**Constraints / unsuitable conditions:** Separate version/ecosystem match, affected feature/configuration, reachability, existing mitigation and advisory freshness. No blanket exploitable or secure result.

**Verification / revisit:** Synthetic affected/unaffected versions, stale/unknown freshness and verified mitigation. Current advisory and actual path needed for consequential claims. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-03; SR-02; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD23

**Decision:** SBOM and build/release integrity

**Context / use when:** Artifact trust, CI or dependency inventory.

**Alternatives and tradeoffs:** Existing lockfile/build manifest first; add exact-artifact BOM or signing/provenance only if justified.

**Constraints / unsuitable conditions:** Bind components to actual artifact/source, transitive scope and configuration. Protect inventory, minimize CI privilege, verify expected origin/signature where selected.

**Verification / revisit:** Compare dummy manifest to actual resolved components; reject identity mismatch and observe failure in authorized environment. Inventory not coverage/compliance. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-03; PS-07; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.

## SD24

**Decision:** Targeted remediation and rollback

**Context / use when:** Known weakness, package update or proposed recipe.

**Alternatives and tradeoffs:** Small reviewed patch/existing migration first; recipe only with qualified language/version/rights. Avoid bulk refactor.

**Constraints / unsuitable conditions:** Preview exact delta, preserve interfaces and prior known-good anchor, test compatibility; no automatic service/tool execution.

**Verification / revisit:** Positive/negative regressions and changed-path inspection. Stop on unrelated behavior changes; scanner green not acceptance. Revisit when source, threat, data flow, environment or authorization materially changes.

**Provenance and limits:** PS-03; SR-05; original Praxis synthesis, reference-only. See [source register](../SOURCES.md). Qualify exact version/clauses before decision-sensitive use; no claim of completed verification.
