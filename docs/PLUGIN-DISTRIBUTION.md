# Praxis plugin distribution

Praxis is maintained in one Git repository. The v1.4.1 packaging-only source adds Claude and ChatGPT distribution without changing the AIPF v8.10.1 framework, five specialist capabilities, design catalog or shared engineering knowledge. Check [published releases](https://github.com/S-Pillow/praxis/releases) before using a release label; a candidate branch, manifest version or successful build is not a published release.

## Choose an installation path

**Claude Code, current marketplace:** after the marketplace is integrated into `main`, run these commands in Claude Code:

```text
/plugin marketplace add S-Pillow/praxis
/plugin install praxis@praxis
```

This uses the repository-root marketplace and its current source, not a permanently pinned tag. Check installed version and source before making reproducibility claims. For a pinned installation, clone the verified published tag, then add that local checkout as the marketplace using its actual absolute path and install `praxis@praxis`. Use a clean plugin test profile if an existing marketplace with that name is present. See [Claude marketplace creation](https://code.claude.com/docs/en/plugins/create-marketplace) and [manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference).

**Claude app / Cowork:** download `Praxis_Claude_v1.4.1.plugin` from the published v1.4.1 release and verify its SHA-256. Where custom plugins are permitted, open Customize → Plugins and use the custom plugin upload option. The archive uses the repository-root Claude layout. See [Claude plugin usage](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

**ChatGPT:** download `Praxis_ChatGPT_Plugin_v1.4.1.zip` and verify its SHA-256. Use the custom plugin import mechanism only if your ChatGPT environment provides one and its policy permits it. There is no public-directory dependency, no bundled app, and no MCP server. A download does not install anything. If custom upload is unavailable, use a compatible repository-aware assistant or provide accessible canonical resources and explicitly select Praxis. Do not assume the host can run scripts or access repositories.

Both plugins are skills-based packages. Explicitly ask Praxis to guide the actual task. Confirm the framework, specialist registry and resource access before governed work. A distinct Builder follows its authorized payload; neither installation nor knowledge access grants external action authority. Ranked catalog retrieval requires actual Python and filesystem access; a host without those capabilities must disclose the gap and follow the canonical fallback. A missing required framework dependency blocks affected governed work.

## Build and verify

Use Git and Python 3.12 (the standing CI runtime). From the repository root, build from an exact published tag, using a new output directory outside the checkout:

```bash
python scripts/package_plugins.py --ref v1.4.1 --out ../praxis-dist-v1.4.1
```

For candidate validation, use a full authorized commit ID or `HEAD` and add `--candidate`; the resulting filenames carry `candidate-<commit>` and are not release assets:

```bash
python scripts/package_plugins.py --ref HEAD --candidate --out ../praxis-candidate
```

The builder resolves the selected Git commit and tree, reads raw `git cat-file --batch` objects without checkout or archive filters and verifies every blob against `git ls-tree`, validates the complete framework projection and registry/catalog counts, renders the ChatGPT templates from that same commit, and checks the generated ZIP inventories and contents. It does not read untracked or modified worktree files as package inputs, create tags, upload assets, install plugins, or run external services. Run the builder from the reviewed version of this repository. Both archives include the exact complete tracked source, including passive test and historical documentation files, preserving relative links and licensing provenance. Claude uses that source directly at its archive root; ChatGPT adds its original host-specific adapter, resource map, manifest, icon, and generated identity outside the snapshot.

ZIP members use fixed timestamps, lexical order, regular-file permissions and no compression so reproducibility does not depend on host zlib versions. The files are larger than compressed predecessors. Build twice from the same commit and compare SHA-256. Candidate and tag-bound output are intentionally distinguishable; the final merge commit identity is not the candidate commit identity even if the trees match. For the final assets, rerun from the verified release tag after authorized integration and tag creation.

The output includes both native package files and `SHA256SUMS.txt`, with exact source commit/tree comments. On Linux, run `sha256sum -c SHA256SUMS.txt` from that output directory. On Windows, use `Get-FileHash -Algorithm SHA256 <file>` and compare the printed hash to its listed value. A checksum proves file identity against the supplied expected checksum, not publisher authenticity; obtain expected hashes from the trusted GitHub release. The ChatGPT package's `skills/praxis/references/PACKAGE-IDENTITY.json` also records every selected source path, Git blob SHA-1, size and SHA-256. The Claude archive consists exclusively of the selected Git tree's files, so its source identity can be checked against that commit.

## Release qualification and recovery

Use [v1.4.1 scope and qualification](releases/1.4.1.md). Native Claude marketplace validation, local test installation and host resource loading must be observed on the candidate; ChatGPT import/activation must be observed only where an authorized custom installation is available. Source/archive checks alone do not prove native host behavior. The v1.4.0 release remains the unchanged recovery anchor. Removing or disabling a plugin is host-specific; no automatic account or repository changes are performed by the package. Preserve release tags, prior evidence, third-party notices and asset restrictions.
