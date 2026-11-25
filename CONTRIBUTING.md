# Contributing to Praxis

Praxis is a quality-first AI development system. Contributions should improve its practical usefulness without weakening the incorporated AIPF governance or conflating evidence with claims.

## Boundaries

- Read [AGENTS.md](AGENTS.md), the [approved product requirements](docs/PRD.md), and the [architecture](docs/ARCHITECTURE.md) before changing behavior. Load the applicable AIPF path through the unified entry.
- Keep work within the current authorization. A specialist, a repository permission, a green test, or an AI recommendation is not authority to expand scope or release.
- Preserve the standalone AIPF product and the exact incorporated framework projection unless an explicitly approved framework-integration change establishes a new identity.
- Preserve existing tests and historical evidence. Add targeted positive and negative regression scenarios for changed behavior; do not weaken assertions or overwrite the original evidence to obtain a pass.
- Do not include credentials, private application data, unreviewed personal paths, or third-party materials without appropriate rights. See [third-party notices](THIRD_PARTY_NOTICES.md).

## Review workflow

Use a branch from the verified accepted repository baseline for authorized changes. Keep changes reviewable and separate implementation, verification and release. Submit changes for owner review before merging; follow the actual repository permissions and release authorization.

From the full repository root:

```bash
python -m unittest discover -s tests -v
```

See [testing strategy](docs/TESTING.md) for impact-triggered tests and independent agent/browser observations. Optional browser tests use existing development tooling; they are not a new product dependency. A missing observer or capability must remain explicit, not be replaced with a fabricated success.

### Catalog enrichment

The four enrichment workflows are manually dispatched verification jobs. They check out the pinned upstream source, regenerate metadata in an ephemeral checkout, run the regression suite, and fail if tracked content differs. They do not commit or push. A drift failure is a review signal, not authorization to update catalog data. Reproduce the relevant enrichment script locally using the pinned upstream checkout specified in its workflow, review provenance, rights, the exact diff and regression results, and submit any intended catalog changes through a pull request. No automatic enrichment writes to `main` are permitted.

## Documentation and history

Update the appropriate in-repository guide when behavior changes. Keep approved historical requirements, decisions and release evidence identifiable; distinguish current state from historical checkpoints. Do not invent future specialists, native host support, or release status. See [release preparation](docs/releases/1.0.0.md).

For suspected security issues, see [SECURITY.md](SECURITY.md). This guide does not create new access, publication or licensing permission.
