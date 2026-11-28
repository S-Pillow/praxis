# Git and repository lifecycle

Use only applicable cards. Examples are synthetic and unexecuted. Source IDs resolve through [SOURCES](../SOURCES.md); provider facts must be verified at use.

## DO-D01 — Which source, branch and release are authoritative?

**Applicability / context:** Existing repository, change, or release; identify actual editable root, active branch/head, accepted commit/tree, release tag and whether integration is required. A branch name is not an identity.

**Decision and alternatives:** Read the controlling refs and compare trees before choosing a change base. Distinguish an unreleased candidate, tested commit, tag and published release. Preserve approved history and known-good selectable recovery; a documentation-only delta still needs impact analysis. Do not move an existing tag or rewrite history as a convenience. If divergent work is present, reconcile rather than overwrite. Prefer no new branch model when existing controls suffice.

**Counterexample:** A green PR from a previous commit and a tag with the desired name do not establish that the currently selected artifact is tested. A README date is not evidence of a publication.

**Observable verification:** Record actual ref-to-SHA, tree/changed paths, tested SHA and release metadata; identify applicable source/remote guards and unchanged protected paths. A missing ref or conflicting authoritative state stops dependent work.

**Sources and limits:** DO-S01, DO-S08–13, DO-S19–23; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D02 — What repository controls and review permissions matter?

**Applicability / context:** Collaborative, public or delivery-critical repo; know actors, forks, workflow event context, protected targets and actual provider capabilities.

**Decision and alternatives:** Prefer existing protection and least privilege. Inspect branch/ruleset settings when authorized, required-check binding and bypass roles; distinguish declared config from enforcement and unobservable settings. Avoid untrusted contributions running with privileged secrets, shared runner access or writable tokens. Require action-specific authority for settings, workflow enablement or merges; do not impose protected branch rules on a local disposable project.

**Counterexample:** A SECURITY.md and passing badge do not show who can push, whether required review applies, or whether the reported vulnerability path works.

**Observable verification:** Inspect actual settings and allowed/denied behavior where authorized; if admin access is absent disclose unknown. Record actor, permission, event and target for a negative control.

**Sources and limits:** DO-S03, DO-S08–13, DO-S19–21, DO-S25; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D03 — Hosted or self-hosted forge and runners?

**Applicability / context:** Consider moving only for actual ownership, residency, reliability, integration or cost needs; know repository count, CI load, admin capacity and recovery objective.

**Decision and alternatives:** Compare current service, local Git, managed forge and self-hosted Forgejo. Include issue/PR metadata, identities, Git LFS/attachments, database, packages, configuration, TLS and backups. Runner host/container isolation is configuration-dependent; avoid host execution of untrusted code, broad credential sharing and privileged container assumptions. Verify compatibility rather than assuming GitHub syntax works unchanged.

**Counterexample:** Copying .git alone cannot restore issues or accounts; an ephemeral job on a shared privileged host is not proof of isolation.

**Observable verification:** Show actual compatible workflow in a disposable target, runner credential/network isolation, restore full relevant state and user access. No upstream pin for Forgejo; verify selected version and license.

**Sources and limits:** DO-S42–44 (official docs; upstream inaccessible), prior QA-S23 / XR-04; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.
