# Audience, profile and README information architecture

Examples are illustrative; use actual approved project facts, not invented placeholders or results.

## RQ-D01 — Which profile and first action fit?

**Applicability / decision and alternatives:** Determine actual audience, released vs candidate status, supported platform, first useful task and owner identity. For local end-user app use real install/first task; CLI/library use supported runtime and minimal working example with expected output; API use safe local request/auth and response; IaC use read-only plan and cost/authority; AI/agent explain activation, role/host/tool and evidence limits; research/internal explain scope, method, access and reproducibility. A small project may need only purpose, first success, scope and license. Place a concise purpose, status and first useful action early; separate supporting implementation, limitations and optional profile details so readers do not need to traverse several headings before finding the task. Preserve accepted style; no generic sections.

**Counterexample:** A CLI README starts with generic feature hero and six badges, no runnable example; an AI skill claims every host auto-discovers it. Adapt content, not just layout.

**Observable verification and sources:** Ask a fresh reader to state purpose/status/first action; actual safe first-use result where feasible; distinguish illustrative from observed. DO-S04–07, DO-S08–11. See [source register](SOURCES.md); no tool execution or rights clearance inferred.

## RQ-D02 — What sections and visual hierarchy belong?

**Applicability / decision and alternatives:** Use meaningful title, concise purpose and supported state, quick start, usage/result; add real design assets, navigation, architecture, examples, compatibility, support/security/contributing/release/license only when helpful. Choose existing brand, readable hierarchy, alt text/text equivalent, restrained badges bound to actual evidence, mobile/wide and dark/light legibility; locally versioned rights-cleared asset if needed. Link canonical deep docs, don't duplicate policy. No empty sections, fake screenshots or claims; avoid universally banning visual choices.

**Counterexample:** A logo sourced from a curated list has no reuse rights; dynamic badge points at another branch; dark-mode logo unreadable. A formal enterprise profile is excessive for a one-file utility.

**Observable verification and sources:** Review actual rendered surface and relevant viewport/theme; inspect source/license of actual visuals and links; reader judgment is not static lint. DO-S04–07, DO-S08–11. See [source register](SOURCES.md); no tool execution or rights clearance inferred.

## RQ-D03 — How to use examples rather than a compulsory template?

**Applicability / decision and alternatives:** Select modular section patterns: purpose and audience; supported prerequisites and safe install; runnable first task with observed/illustrative status; reference and limits; contribution/support; release/license. Keep original content, omit inapplicable sections and fill every value with actual approved facts. See original [examples](examples/CLI.md) and [service example](examples/SERVICE.md); neither is a ready-to-publish universal template. Verify command and expected effect before claiming it works.

**Counterexample:** Template ships dummy domain, API key or nonexistent feature; copy-paste global latest install changes host unexpectedly. A one-line correction becomes a full redesign.

**Observable verification and sources:** Check no unresolved placeholders or secret-bearing examples, actual files and safe first use, preserved qualifiers and scope. DO-S04–07, DO-S33. See [source register](SOURCES.md); no tool execution or rights clearance inferred.
