# Build, verification and engineering review

**No new service / existing / local first:** Use local tests and existing CI/review before adding a product. Distinguish automated review findings from independent acceptance or authorization. Review Parity remains deferred.

The following are independently authored discovery candidates. Verify decisive facts at use; none grants installation, access, data transfer, billing or release permission.

## CAP-B01
**Name:** GitHub Actions
- **Tags:** existing, CI
- **Candidate use:** Existing or candidate CI for source-bound deterministic tests.
- **Constraints to check:** Runner environment, permissions, triggers, artifact retention, quota/spend, independent review and exact commit.
- **Official documentation pointer(s):** https://docs.github.com/en/actions
- **Pricing / terms / licensing pointer(s):** https://docs.github.com/en/actions/concepts/billing-and-usage
- **Observation / verification state:** 2026-11-25 official billing documentation search located pointer; no claim of free runs for a given repository or plan.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

## CAP-B02
**Name:** Claude Ship
- **Tags:** hosted, PR review
- **Candidate use:** Optional provider-stated PR review/correction/approval candidate, not installed.
- **Constraints to check:** Beta features, review/classifier charges even observe-only, data exposure, permissions, policy and actual evidence, no auto-merge.
- **Official documentation pointer(s):** https://claude.com/resources/articles/introducing-claude-ship
- **Pricing / terms / licensing pointer(s):** https://claude.com/resources/articles/introducing-claude-ship
- **Observation / verification state:** P2 provider announcement dated 2026-11-23; not independently validated; pricing and actual workspace eligibility unqualified. No enablement.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

## QA v0.1 discovery additions

No new dependencies or services selected. These original candidate records are usable by all specialists. Check [qualification](QUALIFICATION.md) and exact point-of-use facts; unknown rights, access or spend remain unselected. See [QA sources](../../skills/qa-engineering-quality/SOURCES.md).

## CAP-B03
**Name:** Playwright
- **Tags:** browser, local verification
- **Candidate use:** Browser interaction and bounded local observation.
- **Constraints to check:** Use existing browser/manual observer first; verify exact installed version, executable, host, isolation, data traces, network and rights; no install. Pinned Playwright license inspected QA-S12, official best practices QA-S27; actual compatibility not inferred.
- **Official documentation pointer(s):** https://playwright.dev/docs/best-practices
- **Pricing / terms / licensing pointer(s):** https://github.com/microsoft/playwright/blob/81f985211281bf435a112eaf6532293d3c7523fb/LICENSE
- **Observation / verification state:** 2026-11-26 discovery sources QA-S12, QA-S27; no runtime, price, account or installation qualification.
- **Origin and redistribution:** Original Praxis discovery record; no upstream code, prompts, fixtures or assets imported.

## CAP-B04
**Name:** Hypothesis
- **Tags:** property, state testing
- **Candidate use:** Property and state tests when explicit examples insufficient.
- **Constraints to check:** Existing standard-library examples and seeded sequences first. Exact Python/package compatibility, license, generation/replay scope and CI time unknown at use; no install. Documentation only.
- **Official documentation pointer(s):** https://hypothesis.readthedocs.io/en/latest/stateful.html
- **Pricing / terms / licensing pointer(s):** https://github.com/HypothesisWorks/hypothesis
- **Observation / verification state:** 2026-11-26 discovery sources QA-S24; no runtime, price, account or installation qualification.
- **Origin and redistribution:** Original Praxis discovery record; no upstream code, prompts, fixtures or assets imported.

## CAP-B05
**Name:** Stryker
- **Tags:** mutation, test effectiveness
- **Candidate use:** Targeted mutation testing.
- **Constraints to check:** Hand-authored material mutant first. Check target-language runner, dependency/license/version, execution cost and equivalent/invalid mutants; no numeric score waiver. Docs reference only.
- **Official documentation pointer(s):** https://stryker-mutator.io/docs/
- **Pricing / terms / licensing pointer(s):** https://github.com/stryker-mutator
- **Observation / verification state:** 2026-11-26 discovery sources QA-S25; no runtime, price, account or installation qualification.
- **Origin and redistribution:** Original Praxis discovery record; no upstream code, prompts, fixtures or assets imported.

## CAP-B06
**Name:** Pact
- **Tags:** contracts, integration
- **Candidate use:** Consumer/provider contract testing.
- **Constraints to check:** Local actual serialized seam and existing tests first. Check exact protocol/implementation version, rights, provider/broker access, data and service cost; mocks do not prove provider. Docs reference only.
- **Official documentation pointer(s):** https://docs.pact.io/getting_started/how_pact_works
- **Pricing / terms / licensing pointer(s):** https://docs.pact.io/
- **Observation / verification state:** 2026-11-26 discovery sources QA-S26; no runtime, price, account or installation qualification.
- **Origin and redistribution:** Original Praxis discovery record; no upstream code, prompts, fixtures or assets imported.

## CAP-B07
**Name:** EvalView
- **Tags:** agent evaluation, trace
- **Candidate use:** Agent trace and interface-contract comparison.
- **Constraints to check:** Existing deterministic allowed-action assertions and minimal redacted events first. Pinned telemetry configuration defaults on and retains installation ID; model/API, outbound data, access and spend unknown. Do not infer offline by disabling telemetry. Apache-2.0 root inspected at discovery pin; no run.
- **Official documentation pointer(s):** https://github.com/hidai25/eval-view/blob/ed2d312d812f4fd82bb7881b29432f752b02823e/evalview/core/diff.py
- **Pricing / terms / licensing pointer(s):** https://github.com/hidai25/eval-view/blob/ed2d312d812f4fd82bb7881b29432f752b02823e/LICENSE
- **Observation / verification state:** 2026-11-26 discovery sources QA-S02; no runtime, price, account or installation qualification.
- **Origin and redistribution:** Original Praxis discovery record; no upstream code, prompts, fixtures or assets imported.

## CAP-B08
**Name:** Promptfoo
- **Tags:** AI evaluation, assertions
- **Candidate use:** Declarative AI scenarios and assertions.
- **Constraints to check:** Use native deterministic checks/domain reviewer first. Pinned MIT root inspected; actual provider/model/hosted/red-team paths, telemetry, data retention/access, current plan and spend unknown; no provider call or live red team.
- **Official documentation pointer(s):** https://www.promptfoo.dev/docs/configuration/expected-outputs/
- **Pricing / terms / licensing pointer(s):** https://github.com/promptfoo/promptfoo/blob/485074451bd3c77a0abf000bc9a960499a86f286/LICENSE
- **Observation / verification state:** 2026-11-26 discovery sources QA-S04, QA-S28; no runtime, price, account or installation qualification.
- **Origin and redistribution:** Original Praxis discovery record; no upstream code, prompts, fixtures or assets imported.
