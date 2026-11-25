# **Chapter 16 — Desktop and Packaged Applications Path**

When to use: standalone desktop apps, packaged executables, installers, app bundles, portable builds, and hybrid local/remote desktop apps. A local desktop app is production-relevant even with no remote server, no web deployment, and no push target.

Companion chapters when applicable: Ch. 19 for CI/remote builds; Ch. 17 for update delivery; Ch. 20 at release.

## **16.1 Term Mapping**

| **AIPF term**               | **Desktop app meaning**                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Source/version state        | Git commit, platform version, or other approved durable source state; a remote is optional unless sharing/release requires one.   |
| Remote sync / push          | N/A until a remote/shared state exists. Reports state N/A rather than pretending synchronization occurred.                        |
| Integration                 | Merge or accepted-version transition only when the project model uses it; do not invent an integration stage for a local tool.    |
| Deploy / release            | Rebuild the executable/app bundle/installer and copy/distribute the release artifact.                                             |
| Production verification     | Test the rebuilt release artifact — not just source-mode commands (python app.py, npm dev, dotnet run, java -jar, or equivalent). |
| Staging/source verification | Run from source with mocked/local tests and test-local output paths.                                                              |
| Runtime/generated files     | Output folders, generated reports, workbooks, build/dist artifacts, installers, logs, and caches.                                 |

## **16.2 Packaging Rules**

Packaging cadence. Do not rebuild the packaged artifact after every source authorization unit. Normal source units stop after source-mode verification and durable source/version closure under the confirmed project-state controls. Rebuild/package only during a packaging/release authorization unit or when artifact-level verification is explicitly part of the same authorized unit. Release closure reports Block B2 durability/closure as independent source, shared, artifact, release, and finalization facts, and reports evidence as achieved evidence plus any pending required observation; do not collapse these into one scalar state.

CI-first packaging. Do not force local packaging onto a nontechnical operator when likely failures are environment issues (PATH, SDK versions, DLLs/shared libraries, disk space, signing tools, native compilers, architecture, installer tooling) rather than source correctness. Prefer CI or a controlled build runner. CI-first packaging does not remove verification responsibility: still record source revision/version, build run, terminal state, artifact path, checksum or provenance stamp, and the operator-target artifact test. If local packaging is required, classify failures as source failure, environment failure, missing dependency, artifact failure, or verification gap.

Cross-platform gate parity. Tests gating a platform-specific artifact must avoid accidental development-OS assumptions or state them explicitly: path separators, shell behavior, case sensitivity, encodings, line endings, filesystem limits, permissions, locale, dependency versions, standard-library differences. Passing tests on the development OS do not automatically prove the target artifact — test on the target platform/runner or document why the source-mode gate is representative and what remains unverified.

Release retry and tag rules. Release tags, release pages, workflow runs, and published artifact metadata are release claims to reconcile, not automatic truth. Use immutable tags when feasible. A failed-build retry may reuse the same version or tag only when the earlier run failed before publishing usable artifacts, or when the decision owner accepts a controlled replacement; if artifacts were published or consumed, prefer a new version or a formal replacement/rollback notice. After a tag move, retry, or replacement, verify that authoritative source/version/state, release-page claim, build input identity, artifact-embedded identity, checksum/manifest, and downloaded artifact agree where applicable — or record the accepted mismatch and operator impact. When provenance matters, re-derive truth from authoritative version/state records, build metadata, checksums, and the artifact itself, not the release page.

Operator payload and evidence bundle. When operator-consumable software and CI/test/diagnostic evidence have different consumers, package or present them so the operator entry point and required runtime files are unambiguous and unnecessary evidence clutter does not become part of normal use. Separate operator and evidence artifacts when that materially improves usability, size, security, or supportability; a single clearly structured artifact is acceptable when separation adds no value.

Playbook. 1. Classify the app: source-only, packaged desktop, installer-based, portable executable, or hybrid. 2. Confirm project root, source/version authority, current stable source state, ignored generated artifacts, packaging tool, output directory, and whether a remote/shared state exists (Section 6). 3. Map AIPF terms per 16.1 and record them in the project rules. 4. For normal source authorization units: implement the source-level objective, run source tests with temp/local output paths, close the required durable source state, and stop without rebuilding the package unless packaging is explicitly in the same unit. 5. For packaging/release units: rebuild from a known source revision/version (prefer CI when appropriate), verify the packaged artifact in its target use mode, then distribute under active authorization. Close release evidence per Chapter 20.

## **16.3 Desktop Release Template**

Application type: source-only / portable executable / installer / app bundle / hybrid Source revision/version: — \| Stable source state/branch: — \| Remote/sync status: available / unavailable / n-a Packaging tool/command: — \| Build location: local / CI runner / controlled host CI workflow/run ID or URL (if applicable): — Terminal status and exit code: — Artifact path and filename: — \| Operator payload/evidence-bundle disposition when material: combined-unambiguous / separate / n-a \| Artifact checksum (SHA-256 or n-a): — Artifact provenance stamp and its source: — Runtime/generated folders protected: — Source verification performed (commands/results): — Packaged-artifact verification performed (target machine / operator workflow / results): — Cross-platform assumptions stated or tested: — Release retry/tag events (prior target, new target, reason, approver, artifacts consumed): — / none Rollback artifact/path: — Known source-vs-artifact gaps: none / list Status (Block B2): execution outcome - ; durability/closure state - ; evidence state - ; control disposition -

