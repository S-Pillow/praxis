# The Design Index — local catalog browser

**Status:** local research tool in the Praxis repository; not deployed or installed as a service.

The Design Index uses the **existing** Praxis catalog and search script. It shows all 5,500 source-linked entries via search, category filters and **Show more references** pagination, with original source links, available design tokens, and locally saved references. It creates no new catalog, database, dependencies, or AIPF rules.

## Open it

In a pinned Praxis checkout containing these files, run:

```bash
python ui/catalog-explorer/server.py --port 8765
```

Then visit **http://127.0.0.1:8765/** in a browser on that same computer.

The server uses only Python's standard library and binds to **127.0.0.1**. It is a local research tool, **not** a publicly hosted service. There is no account system, shared storage, or remote write operation. Saved references stay in the current browser's local storage. If the full catalog or its search script is unavailable, startup fails clearly instead of pretending that a small sample is the full catalog.

## How to use it

Search by product or style, choose one of the common category chips or the *Other types* selector, inspect a record to see the exact original-source metadata and available tokens, and save references using the bookmark icon. **Show more references** retrieves the next page rather than dropping matches after the first twelve.

### Use saved references with an AI

Open **Saved references**, describe your actual UI task, and click **Copy instructions for AI**. Paste the brief into an AI coding conversation with access to your application. The brief includes up to the first three saved catalog references, exact provenance and a small set of available source tokens; it retains redistribution limits and makes no changes automatically. If clipboard permission is unavailable, the same brief appears in a selectable text field for manual copy. This is a local export, **not** an AI connection, skill installation, or permission to reuse third-party assets.

Records may be reference-only or metadata-only. Links to third-party sources and displayed token values are not permission to redistribute photographs, fonts, icon files, examples or branded assets. Art on cards is original CSS illustration, not copied upstream media. The optional UI/UX specialist remains subordinate to AIPF v8.10.1 and approved project scope.

## Tests and evidence

From the repository root:

```bash
python -m unittest discover -s tests -v
```

`tests/test_catalog_explorer.py` verifies all 5,500 IDs can be reached through pagination, category filtering covers all catalog entry types, search and saved references behave, real source metadata and tokens remain intact, and local HTTP routes serve correctly. The GitHub Actions catalog-validation workflow is configured to run the test suite on matching changes; remote workflow execution for the accepted candidate remains unverified.

Automated tests prove the tested functionality only. Responsive screenshots and browser behavior should be inspected using an actual running copy on desktop and mobile. No design-quality advantage over AIPF alone or a different model has been established.
