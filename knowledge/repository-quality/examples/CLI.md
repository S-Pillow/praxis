# Line Count — synthetic CLI README example

Count nonempty lines in a local UTF-8 file. Illustrative only; not a released tool.

Save the code below as `count.py` and create `input.txt` with two nonempty lines and a blank line. Run `python count.py input.txt` → expected `2`.

## Setup and implementation

Use an available Python 3.12+ interpreter in a disposable directory. If your host names the interpreter `python3` or `py`, substitute that verified command. No network, account or installation.

```python
from pathlib import Path
import sys

text = Path(sys.argv[1]).read_text(encoding="utf-8")
print(sum(bool(line.strip()) for line in text.splitlines()))
```

Invalid path or encoding raises an error; no claim of graceful handling. This reads only the specified local file. License and support are not asserted for this fictional repository; use actual project facts in a real README.

## Faulty contrast

“Enterprise-grade, cross-platform AI analytics. Install the latest global package and connect your API key. Passing badge.” This invents capability, dependency and verification while omitting a first useful action. A local utility does not need architecture diagrams, SaaS onboarding or release automation.

## Verification plan

With approved Python, create a synthetic input and run the exact code. Observe exit status, stdout, absence of writes to input, and malformed/missing file behavior. Inspect actual target rendering, reader comprehension, links and rights. Illustrative output is not a universal runtime or compatibility claim.
