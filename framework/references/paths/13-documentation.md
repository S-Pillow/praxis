# **Chapter 13 — Documentation and Content Integrity Path**

When to use: docs-only updates of any risk level and published or public content defects, including source links, citations, factual dates, body copy, release notes, user documentation, and metadata. In-application interface copy, labels, controls, and workflow text route through Chapter 14 unless the surface is documentation or help content.

Companion chapters when applicable: Ch. 20 for hotfix release evidence; Ch. 18 when the live surface is builder-managed.

## **13.1 Documentation Change Classification**

| **Classification**                 | **Examples**                                                                                            | **Minimum process**                                                                                                                                                                                                        |
|------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Low-risk documentation             | Typos, README wording, setup clarification, screenshots, examples matching current behavior.            | Confirm docs-only changes; no secrets/runtime/build files; verify durable project-state closure through the confirmed mechanism; synchronize only when required and authorized. No build/deploy unless docs are published. |
| Operational documentation          | Deployment, packaging, rollback, environment variables, runtime paths, quota handling, troubleshooting. | Verify accuracy, exclude secrets, review commands, and update the authoritative project state through the confirmed durability mechanism.                                                                                  |
| Product-scope documentation        | PRD changes, acceptance criteria, feature claims, workflow expectations.                                | Decision-owner review; update backlog and authorization units when execution is planned.                                                                                                                                   |
| Security/compliance documentation  | Data retention, access, privacy, audit, incident response.                                              | Formal review proportional to risk.                                                                                                                                                                                        |
| Published/user-facing docs         | Public docs, in-app help, release notes, user instructions.                                             | Verify against live behavior or packaged artifact; update as part of release/handoff.                                                                                                                                      |
| Production content/citation hotfix | Live copy, citation/link, factual date, or metadata defect with no workflow change.                     | Hotfix procedure in 13.4.                                                                                                                                                                                                  |

## **13.2 Rendered Copy and Semantic Invariant Rules**

Copy-audit acceptance must be based on the rendered user-facing surface, not only raw source text. Distinguish literal source characters, escaped characters that render visibly, ordinary visible body copy, protected visible labels/titles, metadata, and comments or other non-visible source. Source-only counts support diagnosis but do not replace rendered acceptance.

Copy-only changes must preserve semantic qualifiers, not just numbers: figures/units, actor or population qualifiers, time qualifiers, uncertainty terms, comparison basis, cause-and-effect relationships, and environmental/operational/scope caveats. For each materially changed factual sentence, identify the qualifiers present before the edit and where each survives afterward. A generic claim that “meaning is unchanged” is not sufficient when a qualifier was removed or weakened.

For broad copy-heavy work where voice or tone is acceptance-relevant, use the smallest representative review that can establish the direction, then a final whole-surface review by an observer capable of judging that criterion. A literal/deterministic correction does not require two human voice gates. Any approved style constraints discovered by the representative review become scoped protections for the remaining work.

## **13.3 Source and Citation Parity Rules**

Source label–target parity. For evidence-backed content, verify together: visible source label, destination URL, destination title, publication year/date, and the claim or figure actually supported by that destination. A source register or test is not verified merely because the href exists — internal consistency can faithfully preserve the wrong destination. Verify every newly added or modified source; recheck high-impact sources on content, citation, maintenance, or release triggers.

Prerequisite source rule. When approved copy introduces an unregistered source or evidence dependency that can materially change the claim or acceptance decision, block only the dependent work until source verification/registration is resolved. Use Section 5.3 Authorization-unit coherence to decide whether the prerequisite can be resolved inside the current authority or needs a separate authorization unit. Do not invent a source or treat it as verified without evidence. If the missing source cannot change the current decision, record it as non-material and continue.

Verification stamps. A verification stamp represents the latest meaningful factual verification of the cited claims — not automatically the build, commit, publish, or deployment date. Record scope, source set, verifier, and date when the stamp changes. If facts were not re-verified, preserve the prior stamp and disclose the narrower release verification that occurred.

## **13.4 Production Content/Citation Hotfix Playbook**

1\. Confirm the live defect and external source of truth. Classify as copy, citation/link, factual date, or metadata; do not expand it into a feature or workflow change.

2\. Identify the accepted baseline, exact affected strings/files, semantic qualifiers, protected labels, destination properties, expected files, and forbidden files.

3\. Run a narrow scan for every occurrence, distinguishing source, generated artifact, metadata, comments, and rendered output.

4\. Implement the smallest durable source correction. Do not patch generated output alone unless explicitly temporary and separately tracked.

5\. Run targeted tests with raw command status (Section 7), the applicable build, and rendered-copy/source-parity checks against the registered test baseline.

6\. Make the correction durable in the approved source/version state, preserve the known-good recovery anchor, perform one authorized release attempt, and verify the live destination, rendered copy, and artifact identity. If the release attempt fails, reconcile the failure before retrying or issuing new release authorization; do not treat "once" as a prohibition on a controlled retry.

7\. Record only affected evidence-ledger rows (Chapter 20); carry forward unaffected evidence. Stop after live verification and documentation closure.

## **13.5 Template - Rendered Copy, Semantic Invariant, and Citation Parity**

Applicability: not required for a literal low-risk typo or formatting correction unless the change affects factual meaning, citations, protected visible labels, or a published rendered surface. Complete only the fields that govern the changed claim; do not create empty ledgers for inapplicable categories.

Surface/page/report: - Audit scope: body copy / protected labels / metadata / comments / generated artifact. Occurrence counts: literal source - ; escaped-rendering - ; ordinary visible - ; protected labels - ; metadata - ; non-visible - ; total rendered - . Semantic invariant ledger, when applicable: numbers/units - ; actor/population - ; time - ; uncertainty - ; comparison basis - ; cause/effect - ; caveats - . Changed sentences: qualifiers before -\> preserved location after - . Early voice sample: pass / fail / n-a; locked style protections - . Final whole-surface review: pass / fail / partial; notes - . Source parity per changed source: label - ; URL - ; title - ; publication date - ; supported claim - ; evidence/date - . Verification-stamp decision: changed / preserved / n-a; basis - . Status (Block B2): execution outcome - ; durability/closure state - ; evidence state - ; control disposition - .

