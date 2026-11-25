# **Chapter 17 — Update Delivery Path**

When to use: any application that will download, import, replace, install, trigger, or otherwise apply updates to code, artifacts, content, configuration, rules, models, plugins, or data/schema after release. If update handling is not needed, record “not applicable” with the reason — never build an updater by default (Section 5, No implicit updater).

Companion chapters when applicable: Ch. 16 for packaged/installed artifact verification; Ch. 20 at release. Ordinary user file exchange uses template T7, not this chapter — see the T7 boundary note in Part 3.

## **17.1 Update Model Rules**

An application does not need to regenerate all source code to receive an update. Define what an update changes: source code, build/release artifact, configuration/content, data/schema, plugin/rule/model package, or the installed/running system.

Before implementing update logic, the update delivery model must state: artifact type, approved update source/location, who can initiate the update, integrity/version/compatibility checks, control-plane change/audit evidence, rollback, and operator instructions. The evidence may live in project records, platform logs, release tooling, or another approved control mechanism; do not add product-facing audit storage solely to satisfy AIPF.

By application type. Standalone desktop/packaged apps may use an installer, app bundle, zip, patch package, plugin/model/rule/content package, local folder, network share, managed software system, or remote release location - rebuilding the executable is a build/release step (Chapter 16), not a per-authorization-unit update mechanism. Web/hosted apps should flow code updates through an approved deployment, CI/CD, container, hosting, or release pipeline; an admin surface may show version/update status, import approved packages, or trigger an approved deployment only if intentionally designed, authorized, audited, and secured for that purpose. Mobile apps, browser extensions, embedded systems, and managed enterprise apps use the appropriate store, device-management, signed-package, or controlled distribution model unless a different channel is explicitly approved.

Integrity. Update sources must not be arbitrary or unverified. Use checksums, signatures, provenance stamps, allowlists, permissions, and rollback/recovery steps where feasible and proportional.

**Playbook.** 1. Decide whether update delivery is in scope, optional, future, or not applicable — record the reason. 2. Separate source changes, build/release artifacts, update package/source, and the installed/running application. 3. Define the full model per 17.1. 4. When update behavior is in scope for packaged apps, verify the packaged or installed artifact update flow (Chapter 16 verification rules). 5. Test the approved success path and at least one rejection path: unauthorized, tampered, incompatible, wrong-version, missing artifact, or unreachable source (Section 7, Semantic gate and Negative-action verification).

## **17.2 Update Delivery Template**

Update need: required / optional / future / not applicable with reason  
Application type: web / website / desktop / mobile / packaged executable / server / automation / plugin system / other  
Update target: source / deployed service / static bundle / executable / installer / app bundle / configuration / content / data schema / plugin / rule pack / model package / other  
Update artifact/package (filename, type, version, manifest, checksum): -  
Approved update source/location: -  
Initiator and permission model: admin / operator / CI-CD / installer / self-update / end user / managed device system  
Admin/operator surface: none / status only / import package / trigger approved deployment / self-update controls  
Authorization and control-plane change evidence: roles, credentials, logs, approvals, change record  
Integrity/provenance checks: checksum / signature / version stamp / manifest / allowlist / compatibility rule  
Apply/install steps: -  
Positive verification: -  
Negative verification (tampered / unauthorized / incompatible / wrong-version / missing-source): -  
Rollback/recovery path and operator instructions: -  
Out of scope: -

