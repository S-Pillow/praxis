# Read-only catalog search

The unified catalog contains **5,500 source-preserving records** and supports concise retrieval without loading all entries into an AI context.

### Agent-initiated shortlist (preferred for normal UI requests)

When the UI/UX skill is loaded and the repository is accessible to the coding agent, it runs this **itself**, not the end user:

```bash
python scripts/recommend_design.py "Build a financial dashboard with clear data tables" --mode build --platform web
python scripts/recommend_design.py "Audit keyboard focus and navigation" --mode audit
```

The output is a small set of source-linked **candidates**, not automatic design approval. It includes evidence, license restrictions and a short exact-token excerpt where available; it does not create files or execute a build. The existing `search_catalog.py` remains the deeper, read-only search tool.

**Selection behaviour (SPECIALIST-UIUX-02, released in v0.3).** The shortlist reads explicit constraints in the request; `task_signals` in the output shows what it detected.
- Only a record's name, type, keywords and description count as matching evidence. `compatibility_restrictions` ("Avoid: …", "Avoid for: …") are returned unchanged but never scored.
- A stated interface priority ("desktop-first", or desktop or mobile mentioned alone) excludes records that advocate the opposite priority or discourage the stated one. This is separate from `--platform`: a web interface can be desktop-first or mobile-first.
- Explicitly prohibited items ("do not use dark mode or glassmorphism") are removed from the query and exclude matching theme, style, palette, font and motion records.
- An explicit instruction to keep an identity ("keep the current theme", "do not introduce new colours or fonts") suppresses replacement direction, palette or typography unless that part is explicitly requested. When every identity role is suppressed, `selection_scope` is `preserve_identity` and the shortlist contains usability guidelines.
- Audit and `preserve_identity` shortlists add further guidelines up to `--limit` when each scores at least half of the best match.
- Platform labels are normalized ("iOS/Android/React Native" counts as mobile). Framework-labelled guidance ("React/Next.js") requires the framework to be named in the request.
- Clearly non-visual work (backend cues and no interface cues) returns no references, with `selection_scope: non_visual_task`. A missing catalog or empty request is an error, never an empty result.

**Refinements (SPECIALIST-UIUX-03, released in v0.3).**
- A limit on exclusive reliance ("without relying on colour alone", "don't rely solely on color", "no colour-only indicators") is not a prohibition. Colour stays in the query and palettes stay eligible; `task_signals.not_sole_reliance` lists such items. Genuine prohibitions ("do not use red") still apply.
- A critique includes a theme or style reference only when the request asks about visual direction (style, aesthetic, theme, brand, identity, palette, typography and similar), and only when the reference shares at least two query terms. Other critiques return guidelines and fill up to `--limit` as audits do.
- The delivery-platform word "web" is not matching evidence; platform fit comes from `--platform`.
- "help" and "support" count only next to an interface noun ("help center", "support chat", "inline help"), not as domain words or verbs ("help-desk", "support agents", "browsers that support").
- A word that appears only inside a hyphenated compound ("first-run", "long-form") counts only for records containing the whole phrase. "desktop-first" and "mobile-first" are interpreted as interface priorities.
- The shortlist normalizes "colour", "colours", "color" and "colors" to a common concept, and "shop", "ecommerce" and "e-commerce" to a common commerce concept. Matching positive catalog fields uses the same aliases for the requested concepts; manual search is unchanged.

**Preservation versus prohibition (SPECIALIST-UIUX-04, released in v0.3).** A negated change ("without changing its established appearance", "do not alter the current theme") protects the existing identity and prohibits nothing. A prohibition implies preservation only when it names a bare identity part ("no new colours or fonts"). A qualified prohibition ("avoid saturated accent colors") constrains a new design and leaves the palette eligible. A preservation instruction in the same sentence no longer cancels a prohibition ("avoid glassmorphism and keep the current palette"). Preserve and request cues apply to their own part of a sentence ("keep the palette and choose a new font pairing").

Benchmark evidence and limits: `research/evaluations/2026-11-24-specialist-uiux-02-retrieval-experiment.md` and `research/evaluations/2026-11-24-specialist-uiux-03-refinement.md`.

Focused accessibility corrections such as "Make keyboard focus visible" and "Update keyboard navigation" return guideline-only shortlists; explicit new-design or identity-change cues remain eligible for visual direction. This is a lexical heuristic, not authorization to redesign.

### Manual targeted search (optional)

Run from the repository root:

```bash
python scripts/search_catalog.py "financial dashboard" --type palette --limit 5
python scripts/search_catalog.py "glassmorphism" --type style --limit 8
python scripts/search_catalog.py "riso" --limit 5 --include-tokens
python scripts/search_catalog.py "navigation accessibility" --specialist-use audit
```

Outputs JSON including original source ID, pinned commit, original location, license/redistribution status, and compatibility restrictions. Ranking is unchanged for manual search (including the Design Index). `--specialist-use critique` also admits audit-tagged guidelines, because only two records are tagged `critique`. `--include-tokens` returns exact imported source values where present; omit it for a concise shortlist.

**AIPF Prompt Agent / Builder Agent:**
- The Prompt Agent chooses an authorized unit, approved direction and relevant catalog findings.
- If a distinct Builder exists, the Prompt Agent includes the **necessary operational details** in that specific Builder Payload. Do not assume Builder can read this repository or upstream files; when it cannot, transport selected exact tokens/constraints in the payload.
- The Builder uses the supplied guidance, verifies against acceptance criteria, returns evidence and stops at the current boundary. The catalog never authorizes changes.
- For direct single-agent execution, distinct Builder transport is N/A; the same bounded authorization/evidence intent applies.

**Quality boundary:** search relevance is a heuristic, not a quality or legal clearance score. Results can have stale, source-incomplete or unverified rights metadata. The owner-approved design system takes precedence over catalog recommendations. Anti-generic diagnostics remain optional. Critique and technical audit remain distinct.
