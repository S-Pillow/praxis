# The Design Index — local catalog browser

**Status:** usable local prototype; not deployed, installed or merged into the default branch.

The Design Index uses the Specialist Suite's **existing** catalog and search script. It shows all 5,500 source-linked entries via search, category filters and **Show more references** pagination, with original source links, available design tokens, and locally saved references. It creates no new catalog, database, dependencies, or AIPF rules.

## Open it

In a checkout of `S-Pillow/aipf-specialist-suite` containing these files, run:

```bash
python ui/catalog-explorer/server.py --port 8765
```

Then visit **http://127.0.0.1:8765/** in a browser on that same computer.

The server uses only Python's standard library and binds to **127.0.0.1**. It is a local research tool, **not** a publicly hosted service. There is no account system, shared storage, or remote write operation. Saved references stay in the current browser's local storage. If the full catalog or its search script is unavailable, startup fails clearly instead of pretending that a small sample is the full catalog.

## How to use it

Search by product or style, choose one of the common category chips or the *Other types* selector, inspect a record to see the exact original-source metadata and available tokens, and save references using the bookmark icon. **Show more references** retrieves the next page rather than dropping matches after the first twelve.

Records may be reference-only or metadata-only. Links to third-party sources and displayed token values are not permission to redistribute photographs, fonts, icon files, examples or branded assets. Art on cards is original CSS illustration, not copied upstream media. The optional UI/UX specialist remains subordinate to AIPF v8.10.1 and approved project scope.

## Tests and evidence

From the repository root:

```bash
python -m unittest discover -s tests -v
```

`tests/test_catalog_explorer.py` verifies all 5,500 IDs can be reached through pagination, category filtering covers all catalog entry types, search and saved references behave, real source metadata and tokens remain intact, and local HTTP routes serve correctly. The existing GitHub Actions catalog-validation workflow runs those tests on the draft pull request.

Automated tests prove the tested functionality only. Responsive screenshots and browser behavior should be inspected using an actual running copy on desktop and mobile. No design-quality advantage over AIPF alone or a different model has been established.
