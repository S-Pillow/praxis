"""Controlled, dependency-free illustrative technique exercises; not product runtime/agent tests."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "knowledge/repository-quality/examples"


class DocumentationFirstUse(unittest.TestCase):
    def run_example(self, name, code_file, args=(), prepare=None):
        doc = (EXAMPLES / name).read_text(encoding="utf-8")
        code, = re.findall(r"(?s)\x60\x60\x60python\n(.*?)\n\x60\x60\x60", doc)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script = root / code_file
            script.write_text(code + "\n", encoding="utf-8")
            if prepare:
                prepare(root)
            before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in root.iterdir()}
            result = subprocess.run([sys.executable, "-B", script.name, *args], cwd=root,
                                    capture_output=True, text=True, timeout=15)
            after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in root.iterdir()}
            self.assertEqual(after, before, "documented read-only first use mutated fixture")
            return result

    def test_cli_documented_example_actual_first_success(self):
        result = self.run_example("CLI.md", "count.py", ("input.txt",),
                                  lambda root: (root / "input.txt").write_text("one\n\ntwo\n", encoding="utf-8"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "2")

    def test_cli_missing_file_is_not_success(self):
        result = self.run_example("CLI.md", "count.py", ("missing.txt",))
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("FileNotFoundError", result.stderr)

    def test_service_documented_example_actual_loopback_first_success(self):
        result = self.run_example("SERVICE.md", "status_echo.py")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"status": "ready"})


class OperationalNegativeControls(unittest.TestCase):
    def test_backup_integrity_is_not_recovery(self):
        """DQ10: correct checksum and archive integrity can miss critical state."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            expected = {"data.json": b'{"records":[1,2]}', "config.json": b'{"mode":"safe"}'}
            for case, contents in (("incomplete", {"data.json": expected["data.json"]}),
                                   ("complete", expected)):
                with self.subTest(case=case):
                    archive = root / (case + ".zip")
                    with zipfile.ZipFile(archive, "w") as out:
                        for name, data in contents.items():
                            out.writestr(name, data)
                    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
                    restored = root / case
                    restored.mkdir()
                    with zipfile.ZipFile(archive) as incoming:
                        self.assertIsNone(incoming.testzip())  # weak oracle accepts both
                        self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(), digest)
                        # Extract only fixture-owned known paths; no external archive.
                        for name in incoming.namelist():
                            self.assertIn(name, expected)
                            (restored / name).write_bytes(incoming.read(name))
                    actual = {p.name: p.read_bytes() for p in restored.iterdir()}
                    if case == "incomplete":
                        self.assertNotEqual(actual, expected)
                        self.assertNotIn("config.json", actual)
                    else:
                        self.assertEqual(actual, expected)
                        self.assertEqual(json.loads(actual["data.json"])["records"], [1, 2])
                        self.assertEqual(json.loads(actual["config.json"])["mode"], "safe")

    def test_green_status_does_not_establish_test_execution(self):
        """DQ03: run two local synthetic commands; both exit zero but only one runs an oracle."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            weak = subprocess.run([sys.executable, "-c", "print('tests skipped; build successful')"],
                                  cwd=root, text=True, capture_output=True, timeout=5)
            good = subprocess.run([sys.executable, "-c",
                                   "import unittest\nclass Contract(unittest.TestCase):\n def test_effect(self):\n  self.assertEqual(2 + 2, 4)\nunittest.main()"],
                                  cwd=root, text=True, capture_output=True, timeout=5)
            self.assertEqual(weak.returncode, 0)
            self.assertEqual(good.returncode, 0, good.stderr)
            self.assertNotIn("Ran 1 test", weak.stderr)
            self.assertIn("Ran 1 test", good.stderr)

    def test_zero_and_missing_samples_distinct(self):
        """DQ08: demonstrate a lossy fallback vs an explicit missing observation."""
        observed_zero = {"errors": 0, "samples": 3}
        absent = {"samples": 0}
        self.assertEqual(observed_zero.get("errors", 0), absent.get("errors", 0))
        self.assertIsNone(absent.get("errors"))
        self.assertEqual(observed_zero["errors"], 0)
        self.assertGreater(observed_zero["samples"], 0)


if __name__ == "__main__":
    unittest.main()
