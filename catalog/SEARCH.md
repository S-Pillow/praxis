# Read-only catalog search

The unified catalog contains **5,500 source-preserving records** and supports concise retrieval without loading all entries into an AI context.

Run from the repository root:

```bash
python scripts/search_catalog.py "financial dashboard" --type palette --limit 5
python scripts/search_catalog.py "glassmorphism" --type style --limit 8
python scripts/search_catalog.py "riso" --limit 5 --include-tokens
python scripts/search_catalog.py "navigation accessibility" --specialist-use audit
```

Outputs JSON including original source ID, pinned commit, original location, license/redistribution status, and compatibility restrictions. `--include-tokens` returns exact imported source values where present; omit it for a concise shortlist.

**AIPF Prompt Agent / Builder Agent:**
- The Prompt Agent chooses an authorized unit, approved direction and relevant catalog findings.
- If a distinct Builder exists, the Prompt Agent includes the **necessary operational details** in that specific Builder Payload. Do not assume Builder can read this repository or upstream files; when it cannot, transport selected exact tokens/constraints in the payload.
- The Builder uses the supplied guidance, verifies against acceptance criteria, returns evidence and stops at the current boundary. The catalog never authorizes changes.
- For direct single-agent execution, distinct Builder transport is N/A; the same bounded authorization/evidence intent applies.

**Quality boundary:** search relevance is a heuristic, not a quality or legal clearance score. Results can have stale, source-incomplete or unverified rights metadata. The owner-approved design system takes precedence over catalog recommendations. Anti-generic diagnostics remain optional. Critique and technical audit remain distinct.
