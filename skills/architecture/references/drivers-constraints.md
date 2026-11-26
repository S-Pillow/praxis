# Drivers and constraints

Original conditional decision guidance; apply only within approved project intent. Source keys link to [source register](../SOURCES.md). No claim of current provider facts or project-specific acceptance.

## A01
**Decision:** Which requirements actually change architecture?
- **Use when:** A new decision or disputed tradeoff has material consequences for behavior, cost or reliability.
- **Disqualifiers / stop:** Do not promote a preference, guess or unapproved behavior into a hard requirement.
- **Alternatives and consequences:** Keep existing design if it satisfies drivers; otherwise rank competing options by actual constraints, not pattern popularity. A cheaper option may sacrifice availability or reversibility.
- **Implementation implications:** Name the actor, stimulus, operating conditions, expected response and measurable bound where meaningful. Separate confirmed constraints, assumptions and unresolved owner choices.
- **Verification / revisit:** Exercise a representative scenario and boundary; identify which assumption would invalidate the decision.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A02
**Decision:** How much uncertainty warrants a spike?
- **Use when:** An unresolved technical assumption could reverse a decision or cause costly rework.
- **Disqualifiers / stop:** Skip a proof when no plausible result changes action; never test production or use paid services without authority.
- **Alternatives and consequences:** Use inspection or authoritative docs first; choose a small disposable experiment only if project fit remains unknown. Keep a reversible fallback; defer irreversible selection when key evidence is missing.
- **Implementation implications:** State a falsifiable question, controlled inputs, observable threshold, time/resource ceiling and no-mutation limits.
- **Verification / revisit:** Capture command/result, environment and limitations; distinguish evidence of feasibility from acceptance.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

## A03
**Decision:** When should a decision be recorded or revisited?
- **Use when:** An architectural choice affects multiple consumers, expensive dependencies, data policy or long-term maintenance.
- **Disqualifiers / stop:** Do not mandate an ADR for routine implementation detail or claim approval merely by writing one.
- **Alternatives and consequences:** Use concise decision record for durable rationale; retain an accepted design if constraints unchanged; revisit when workload, dependencies, cost or authority changes.
- **Implementation implications:** Record alternatives, selected conditions, rejected reasons, invariants, owner decision status, source identity and revisit triggers in the project’s existing record.
- **Verification / revisit:** Check consumers can trace constraints and a later change has a clear trigger; avoid duplicate canonical project state.
- **Provenance:** P1,P2 (original synthesis; no upstream content copied). **Maintenance:** stable.

