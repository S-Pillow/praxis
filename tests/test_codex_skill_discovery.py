"""Check project-scoped Codex skill discovery without asserting a real agent activation."""
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / ".agents" / "skills" / "aipf-ui-ux" / "SKILL.md"
SKILL = ROOT / "skills" / "aipf-ui-ux" / "SKILL.md"
GUIDANCE = ROOT / "AGENTS.md"
COMMAND = ROOT / "scripts" / "recommend_design.py"


class CodexDiscoveryTests(unittest.TestCase):
    def test_discoverable_skill_and_single_authoritative_source(self):
        loader = ADAPTER.read_text(encoding="utf-8")
        self.assertTrue(loader.startswith("---\nname: aipf-ui-ux\ndescription:"))
        self.assertIn("skills/aipf-ui-ux/SKILL.md", loader)
        self.assertTrue(SKILL.is_file())
        self.assertIn("AIPF v8.10.1", SKILL.read_text(encoding="utf-8"))
        self.assertLess(len(loader), len(SKILL.read_text(encoding="utf-8")))

    def test_specialist_version_is_consistent(self):
        version = re.search(r"^# AIPF UI/UX Specialist — (v\d+\.\d+)$", SKILL.read_text(encoding="utf-8"), re.M)
        self.assertIsNotNone(version)
        self.assertIn(f"({version.group(1)})", ADAPTER.read_text(encoding="utf-8").splitlines()[5])
        self.assertIn(f"UI/UX specialist ({version.group(1)})", (ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertIn(f"## {version.group(1)}", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))

    def test_scope_does_not_claim_global_install(self):
        guidance = GUIDANCE.read_text(encoding="utf-8")
        self.assertIn(".agents/skills/aipf-ui-ux/SKILL.md", guidance)
        self.assertIn("project-scoped", guidance)
        loader = ADAPTER.read_text(encoding="utf-8").replace("*", "")
        self.assertIn("not a global install", loader)

    def test_agent_side_lookup_works_with_full_catalog(self):
        process = subprocess.run(
            [sys.executable, str(COMMAND),
             "Build a financial dashboard with readable tables", "--mode", "build"],
            cwd=ROOT, capture_output=True, text=True, check=True, timeout=45,
        )
        payload = json.loads(process.stdout)
        self.assertEqual(payload["catalog_records_searched"], 5500)
        self.assertTrue(payload["references"])
        self.assertLessEqual(len(payload["references"]), 3)
        self.assertTrue(all(item["source_ref"] in item["source_url"]
                            for item in payload["references"]))


if __name__ == "__main__":
    unittest.main()
