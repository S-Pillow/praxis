# Test-suite effectiveness

Original conditional QA guidance. Examples below are illustrative, not executed qualification. Source IDs resolve via [SOURCES](../SOURCES.md); use current official evidence for material volatile facts. AIPF and approved requirements govern.

## QA-D32 — Can the suite detect the defect we care about?

**Applicability / context:** Passing tests with risk of weak assertions or material new correction.

**Decision and alternatives:** Create original disposable known-bad and known-good cases with same inputs and oracle. Run original weak checks, then independently authored stronger test targeting actual invariant; ensure failure reason is correct and good case passes. Keep actual logs. Do not insert defect in accepted source.

**Counterexample:** Test merely checks key exists; buggy normalizer replaces explicit false with default true.

**Observable verification:** Show weak pass on bad, strong failure on bad, strong plus weak pass on good, and unrelated invariant preserved. Independence requires real distinct reviewer where required.

**Sources and limits:** QA-S03, QA-S25, QA-S33. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D33 — What do mutant results mean?

**Applicability / context:** Targeted change to disposable implementation to assess test sensitivity, not mandated full mutation tooling.

**Decision and alternatives:** Select material predicate/branch/side-effect change. Distinguish killed intended failure, survivor needing assessment, equivalent behavior, invalid/unexecutable and untested. Use native manual mutation when enough; optional framework if suitable. No arbitrary score target or acceptance by percentage.

**Counterexample:** Mutant fails compilation or changes unreachable code; neither demonstrates required assertion strength.

**Observable verification:** Verify mutant executes relevant path and fails exact meaningful assertion; classify equivalent or invalid separately. Preserve fixture, raw outputs and candidate identity.

**Sources and limits:** QA-S25, QA-S03. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

## QA-D34 — Can coverage or reruns establish confidence?

**Applicability / context:** Review passing suite, coverage gaps or flaky failures.

**Decision and alternatives:** Map assertions to required behavior and failure modes; coverage tells what executed, not what was checked. Investigate first failed run and cause; repeated pass can reduce uncertainty only within controlled conditions. Prefer high-impact negative and independent oracle over more trivial checks.

**Counterexample:** 100% branch execution with no result assertion or ignored side effects; retry masks race.

**Observable verification:** Show one material counterexample and expected failure, existing unchanged behavior and scope; retain all required raw failed/skipped/retry records.

**Sources and limits:** QA-S25, QA-S32, QA-S30. Reference-only observations; no upstream runtime, benchmark or blanket rights claim. See source register.

