# Claims, links, first use and rendering

Examples are illustrative; use actual approved project facts, not invented placeholders or results.

## RQ-D04 — What supports each material README claim?

**Applicability / decision and alternatives:** Map material capability, support, security, performance, version, count and badge claims to actual source, accepted artifact or separately attributed runtime/owner evidence. Preserve numeric units, population, time, uncertainty and caveats under Chapter 13. Verify visible source label, actual destination title/version/date and supported claim; HTTP 200 or correct anchor alone is not enough. Distinguish tag, tested commit/tree, publication and working state. Reuse valid evidence, do not rewrite release history.

**Counterexample:** Project index says backup lab but target describes deployment; badge from stale run appears green; example claims current Linux/Windows support without actual evidence.

**Observable verification and sources:** Read target content/version, source/CI and release identity; map material changed claims and qualifiers; flag wrong target even if link resolves. DO-S01, DO-S06–13, DO-S19–25. See [source register](SOURCES.md); no tool execution or rights clearance inferred.

## RQ-D05 — How do local and external link checks differ?

**Applicability / decision and alternatives:** Use deterministic local relative path, anchor, reference-definition and case checks from appropriate checkout; inspect actual renderer-generated anchors for complex headings. External links require authorized bounded network checks, exact destination identity, timeout/redirect/caching and status handling; local syntax cannot prove semantic parity. Use existing tooling first; Lychee optional at qualified version, never transmit secrets in URL/headers.

**Counterexample:** Redirect to generic homepage returns success; fragment doesn't exist; private path leaks in an external checker; cached response masks changed target.

**Observable verification and sources:** Check valid and deliberately broken path/anchor and wrong-destination fixture; confirm actual external destination only where authorized. Report untested/denied/timeout separately. DO-S08–11, DO-S33. See [source register](SOURCES.md); no tool execution or rights clearance inferred.

## RQ-D06 — How do we verify first use and visual quality?

**Applicability / decision and alternatives:** Follow documented safe commands in clean appropriate host with actual prerequisites, versions, files and expected output; do not install, provision, call live or spend unless authorized. If no runtime/observer, state unavailable, do not imply execution. For material presentation inspect actual GitHub/equivalent rendered page with wide/narrow, relevant dark/light, heading/nav, alt text, overflow, contrast and useful first-screen content. Distinguish equivalent render from actual target. Record host chrome as part of the viewport: GitHub navigation, breadcrumbs and file controls reduce the usable content area. A command visible in an isolated Markdown preview may be below the fold on the real host. Prefer a concise purpose, status and first action before secondary headings or long code; verify on the intended host when accessible, and disclose when platform chrome prevents a first-screen result. A fixed pixel threshold is not a universal acceptance rule. Owner design feedback applies at product scope only.

**Counterexample:** A sample output is authored, not executed; syntax looks valid but screenshot is clipped or contrast fails. Demo uses a secret or disallowed data.

**Observable verification and sources:** Retain actual command/exit/output, source identity, renderer/viewport/theme, observer and limitations. Verify meaningful scope, not number of badges. DO-S04–11, DO-S32–33. See [source register](SOURCES.md); no tool execution or rights clearance inferred.
