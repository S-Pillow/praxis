# Prompt Agent and Builder Agent — catalog consumption

The governing standard is AIPF v8.10.1. This is a non-normative interface note.

**Prompt Agent:** selects applicable AIPF path, maintains authoritative project baseline, controls the current authorization unit, selects approved design intent and source references, defines evidence and stop conditions, reconciles Builder results. If a distinct Builder exists, transport only the operational Builder Payload, not internal framework-routing metadata.

**Builder Agent (when distinct):** executes only the current transported payload, reads only actually accessible pinned catalog/reference materials, uses catalog recommendations without changing authority/design intent, reports actual evidence and stops. It must not choose the next authorization unit.

**No Phantom Context:** if the Builder cannot access a source file or repository artifact at the named pin, the Prompt Agent distills necessary exact design tokens, reference details, constraints and evidence tests into the Builder Payload. A URL or catalog ID does not imply Builder access.

**Brand truth:** existing approved design system first, then authorized verified source extraction, then owner-approved catalog recommendations; speculative choices cannot silently replace approved identity.

**Modes:** build-time expertise is primary. Critique is design-quality judgment based on rendered evidence where claimed. Audit is technical checks with actual tool results. Optional anti-generic diagnostics are nonbinding unless separately authorized; no additional mandatory degraded-review wording. Never claim unavailable capabilities or independent review.

**Licensing stop:** unresolved photo/font/example rights bar bundling/distribution of those assets. Source metadata is not a license to rehost.

If the AI is operating alone without a distinct Builder, the AIPF Chapter 21 two-agent transport clauses are not active; the one executor still observes its authorized scope and evidence contract.
