"""Controlled, dependency-free illustrative technique exercises; not product runtime/agent tests."""
import hashlib
import json
from pathlib import Path
import re
import runpy
from threading import Thread
from http.server import ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import build_opener, ProxyHandler
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


    def test_examples_first_action_and_heading_hierarchy(self):
        for name in ("CLI.md", "SERVICE.md"):
            with self.subTest(name=name):
                doc = (EXAMPLES / name).read_text(encoding="utf-8")
                self.assertEqual(len(re.findall(r"(?m)^# ", doc)), 1)
                self.assertLess(doc.index("Run " + chr(96) + "python"),
                                doc.index(chr(96)*3 + "python"))
                # Source hierarchy oracle only; not proof of host viewport geometry.
                first_secondary = re.search(r"(?m)^## ", doc)
                self.assertIsNotNone(first_secondary)
                self.assertLess(doc.index("Run " + chr(96) + "python"), first_secondary.start())
                self.assertIn("Illustrative only;", doc[:first_secondary.start()])

    def test_service_profile_and_boundary_headings(self):
        doc = (EXAMPLES / "SERVICE.md").read_text(encoding="utf-8")
        self.assertIn("constant readiness response", doc)
        self.assertIn("\n## Operating boundary\n", doc)
        self.assertIn("\n### If the service is AI-backed\n", doc)
        self.assertIn("not features of Status Echo", doc)

    def test_service_actual_unknown_route_is_not_ready(self):
        doc = (EXAMPLES / "SERVICE.md").read_text(encoding="utf-8")
        code, = re.findall(r"(?s)\x60\x60\x60python\n(.*?)\n\x60\x60\x60", doc)
        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "status_echo.py"
            script.write_text(code + "\n", encoding="utf-8")
            handler = runpy.run_path(str(script))["Handler"]
            with ThreadingHTTPServer(("127.0.0.1", 0), handler) as server:
                worker = Thread(target=server.serve_forever, daemon=True)
                worker.start()
                try:
                    opener = build_opener(ProxyHandler({}))
                    url = f"http://127.0.0.1:{server.server_port}/unknown"
                    with self.assertRaises(HTTPError) as caught:
                        opener.open(url, timeout=3)
                    with caught.exception as response:
                        self.assertEqual(response.code, 404)
                        self.assertEqual(json.loads(response.read()), {"status": "not_found"})
                finally:
                    server.shutdown()
                    worker.join(timeout=3)
                self.assertFalse(worker.is_alive())


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

    def test_resolving_link_does_not_establish_semantic_parity(self):
        """RQ03: both local targets exist, only one supports the claimed function."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "delivery.md").write_text("# Deployment\nRelease a build.\n", encoding="utf-8")
            (root / "recovery.md").write_text("# Recovery\nRestore a backup.\n", encoding="utf-8")
            for target, expected in (("delivery.md", False), ("recovery.md", True)):
                with self.subTest(target=target):
                    index = f"[Backup recovery]({target})"
                    label, dest = re.fullmatch(r"\[([^]]+)\]\(([^)]+)\)", index).groups()
                    self.assertEqual(label, "Backup recovery")
                    self.assertTrue((root / dest).is_file())
                    title = (root / dest).read_text(encoding="utf-8").splitlines()[0]
                    self.assertEqual(title == "# Recovery", expected)

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
