# Example: Line Count (synthetic local CLI)

This original instructional example is not a released project or executed command. Adapt sections only after actual source, environment and claims are known.

## Strong sample

# Line Count

Count nonempty lines in a local UTF-8 text file. Offline; no network or account. Example assumes Python 3.12 and the single-file implementation below. It is an illustrative first-success example, not a compatibility or benchmark claim.

```python
from pathlib import Path
import sys

text = Path(sys.argv[1]).read_text(encoding="utf-8")
print(sum(bool(line.strip()) for line in text.splitlines()))
```

Save as count.py in a disposable directory. Create input.txt containing two nonempty lines separated by a blank line. Run `python count.py input.txt`. Expected illustrative stdout: `2`. Invalid path or encoding raises an error; no claim of graceful handling. This only reads the specified local file. No install or service. License/support not asserted for a fictional repo; use actual project files in a real README.

## Faulty contrast

“Enterprise-grade, cross-platform AI analytics. Install the latest global package and connect your API key. Passing badge.” This invents capability, dependency and verification while omitting a first useful action. A plain local utility does not need architecture diagrams, SaaS onboarding or release automation.

## Verification plan

With approved Python, create synthetic file and run exact code; observe exit, stdout, absence of writes to input and malformed/missing file behavior. Check actual rendered hierarchy, reader first action, links and rights. This example's run and rendering are not asserted here.
