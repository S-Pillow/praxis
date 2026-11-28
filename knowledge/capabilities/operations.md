# Operational and repository-quality candidates

No service or tool selected. Use existing/local or no new tool first. Apply [qualification](QUALIFICATION.md) and [DevOps sources](../../skills/devops-reliability/SOURCES.md). Existing CAP-B01 GitHub Actions, CAP-V01 OpenTelemetry and CAP-B07 EvalView remain the canonical records; use their existing links in the [index](INDEX.md). Langfuse, MLflow, Opik, Deepchecks, Forgejo and other leads remain decision-specific references in DevOps guides. No deployment or installation implied.

## CAP-R01
**Name:** OpenSSF Scorecard
- **Tags:** repository security, findings
- **Candidate use:** Assess individual repository/supply-chain practice findings when material.
- **Constraints to check:** Use existing targeted controls first. Heuristic checks have scope/false positives/unknowns. Experimental conformance/MCP at pin not stable or live unreleased scan. Qualify exact version, access, maintenance, scoring data license, runner/token/data and cost. No automatic publish or score gate.
- **Official documentation pointer(s):** https://github.com/ossf/scorecard/tree/4c48271472229429091d1e65621856a377c13982
- **Pricing / terms / licensing pointer(s):** https://github.com/ossf/scorecard/blob/4c48271472229429091d1e65621856a377c13982/LICENSE
- **Observation / verification state:** 2026-11-27 discovery DO-S19/21; Apache-2.0 root inspected for core, public data and action separately governed; source observations only, runtime, current price, account and actual access/usage unqualified.
- **Origin and redistribution:** Original Praxis record; reference-only upstream, no code, assets or templates copied. Qualify exact rights, notices and operational terms before reuse.

## CAP-R02
**Name:** Actionlint
- **Tags:** workflow static validation, local
- **Candidate use:** Optional GitHub Actions syntax, expression and action interface checks.
- **Constraints to check:** Existing native checks first; qualify exact runner/platform, optional ShellCheck/Pyflakes, action metadata and untrusted input. Static check not actual workflow, permission or release proof.
- **Official documentation pointer(s):** https://github.com/rhysd/actionlint/tree/011a6d15e749bb3f2d771eed9c7aa0e7e3e10ee7
- **Pricing / terms / licensing pointer(s):** https://github.com/rhysd/actionlint/blob/011a6d15e749bb3f2d771eed9c7aa0e7e3e10ee7/LICENSE.txt
- **Observation / verification state:** 2026-11-27 discovery DO-S32; MIT text inspected; source observations only, runtime, current price, account and actual access/usage unqualified.
- **Origin and redistribution:** Original Praxis record; reference-only upstream, no code, assets or templates copied. Qualify exact rights, notices and operational terms before reuse.

## CAP-R03
**Name:** Lychee
- **Tags:** documentation links, local
- **Candidate use:** Optional bounded relative/external link verification.
- **Constraints to check:** Use deterministic local paths/anchors first. Confirm cache, redirects, fragment handling, retries, timeout, credential/URL data, actual destination semantics and network authority. Does not prove rendering, first use or claims.
- **Official documentation pointer(s):** https://github.com/lycheeverse/lychee/tree/f10ac2774dac100dfdbf014647487520a8ffe08d
- **Pricing / terms / licensing pointer(s):** https://github.com/lycheeverse/lychee/blob/f10ac2774dac100dfdbf014647487520a8ffe08d/LICENSE-APACHE
- **Observation / verification state:** 2026-11-27 discovery DO-S33; Apache-2.0 and MIT license texts inspected, qualify exact components; source observations only, runtime, current price, account and actual access/usage unqualified.
- **Origin and redistribution:** Original Praxis record; reference-only upstream, no code, assets or templates copied. Qualify exact rights, notices and operational terms before reuse.

## CAP-R04
**Name:** OpenTofu
- **Tags:** infrastructure as code, plan/state
- **Candidate use:** Candidate for repeatable approved infrastructure when provider-native or manual mechanisms insufficient.
- **Constraints to check:** Qualify backend locking, workspace/provider version, dependencies, state/key protection and recovery, plan-sensitive fields and actual costs. Plan not apply permission; no destroy, force unlock or secret upload.
- **Official documentation pointer(s):** https://github.com/opentofu/opentofu/tree/b71d43c2b4cbb781189feb3bd8d4df5aece1924d
- **Pricing / terms / licensing pointer(s):** https://github.com/opentofu/opentofu/blob/b71d43c2b4cbb781189feb3bd8d4df5aece1924d/LICENSE
- **Observation / verification state:** 2026-11-27 discovery DO-S26/45–47; MPL-2.0 root inspected; source observations only, runtime, current price, account and actual access/usage unqualified.
- **Origin and redistribution:** Original Praxis record; reference-only upstream, no code, assets or templates copied. Qualify exact rights, notices and operational terms before reuse.

## CAP-R05
**Name:** Ansible
- **Tags:** configuration, automation
- **Candidate use:** Candidate for repeatable approved host configuration.
- **Constraints to check:** Use existing/provider-native first; qualify modules/platform, inventory, access, privilege, secret diff, partial check mode, idempotency, recovery and actual service behavior. GPL source reference-only.
- **Official documentation pointer(s):** https://github.com/ansible/ansible/tree/cd313f0a8650ded36707a24e2bad61375f1214ce
- **Pricing / terms / licensing pointer(s):** https://github.com/ansible/ansible/blob/cd313f0a8650ded36707a24e2bad61375f1214ce/COPYING
- **Observation / verification state:** 2026-11-27 discovery DO-S27/48; GPL-3.0 root and GPL-3.0+ module headers inspected; source observations only, runtime, current price, account and actual access/usage unqualified.
- **Origin and redistribution:** Original Praxis record; reference-only upstream, no code, assets or templates copied. Qualify exact rights, notices and operational terms before reuse.

## CAP-R06
**Name:** Restic
- **Tags:** backup, recovery
- **Candidate use:** Candidate local or approved repository backup and isolated recovery.
- **Constraints to check:** Use adequate native backup first; qualify backend credentials/encryption and key recovery, snapshot/filter/retention semantics, consistency, storage transfer cost and actual restore. Forget/prune are separate destructive actions.
- **Official documentation pointer(s):** https://github.com/restic/restic/tree/e63cb63ba646722feda730d44210b3361e6f9dcc
- **Pricing / terms / licensing pointer(s):** https://github.com/restic/restic/blob/e63cb63ba646722feda730d44210b3361e6f9dcc/LICENSE
- **Observation / verification state:** 2026-11-27 discovery DO-S30; BSD-2-Clause inspected; source observations only, runtime, current price, account and actual access/usage unqualified.
- **Origin and redistribution:** Original Praxis record; reference-only upstream, no code, assets or templates copied. Qualify exact rights, notices and operational terms before reuse.

## CAP-R07
**Name:** Prometheus
- **Tags:** metrics, alerting
- **Candidate use:** Candidate for user-impact metrics and actionable alerts where existing signals insufficient.
- **Constraints to check:** Verify scrape/query, absent vs zero, labels/privacy, alert pending/firing and notification routing, storage/head/WAL overhead, retention, access and cost. No uptime claim from config.
- **Official documentation pointer(s):** https://github.com/prometheus/prometheus/tree/ccdfcea89903f5966d3f6b73631f1b37f907dbeb
- **Pricing / terms / licensing pointer(s):** https://github.com/prometheus/prometheus/blob/ccdfcea89903f5966d3f6b73631f1b37f907dbeb/LICENSE
- **Observation / verification state:** 2026-11-27 discovery DO-S28; Apache-2.0 inspected; source observations only, runtime, current price, account and actual access/usage unqualified.
- **Origin and redistribution:** Original Praxis record; reference-only upstream, no code, assets or templates copied. Qualify exact rights, notices and operational terms before reuse.

## CAP-R08
**Name:** Argo CD
- **Tags:** declarative delivery, GitOps
- **Candidate use:** Candidate for an existing justified Kubernetes delivery model.
- **Constraints to check:** Do not introduce Kubernetes for this tool. Exact cluster/namespace/source, controller version, automatic sync/self-heal/prune/allow-empty, repeat hooks, migration/recovery and user outcome. No live sync permission.
- **Official documentation pointer(s):** https://github.com/argoproj/argo-cd/tree/26f602893cec74cbd13f47341f240237f98dfe3c
- **Pricing / terms / licensing pointer(s):** https://github.com/argoproj/argo-cd/blob/26f602893cec74cbd13f47341f240237f98dfe3c/LICENSE
- **Observation / verification state:** 2026-11-27 discovery DO-S31; Apache-2.0 inspected; source observations only, runtime, current price, account and actual access/usage unqualified.
- **Origin and redistribution:** Original Praxis record; reference-only upstream, no code, assets or templates copied. Qualify exact rights, notices and operational terms before reuse.

## CAP-R09
**Name:** Infracost
- **Tags:** cost estimate, infrastructure
- **Candidate use:** Optional comparison of estimated infrastructure changes if manual/provider data insufficient.
- **Constraints to check:** Verify chosen CLI vs Plan JSON API data path, plan sensitivity, exact pricing/region/assumptions/credentials, current terms and actual bill. No plan upload, paid call or zero-cost guarantee; forecast vs actual, alert vs cap.
- **Official documentation pointer(s):** https://github.com/infracost/cli/tree/6771a36b9c34a3fc1d147d74e65bb1823c945c92
- **Pricing / terms / licensing pointer(s):** https://github.com/infracost/cli/blob/6771a36b9c34a3fc1d147d74e65bb1823c945c92/LICENSE
- **Observation / verification state:** 2026-11-27 discovery DO-S34–35/54–55; Apache-2.0 roots inspected; documented vendor API claims not executed; source observations only, runtime, current price, account and actual access/usage unqualified.
- **Origin and redistribution:** Original Praxis record; reference-only upstream, no code, assets or templates copied. Qualify exact rights, notices and operational terms before reuse.
