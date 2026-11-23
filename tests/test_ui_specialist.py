"""Small smoke checks for the optional, dependency-free UI/UX specialist."""
import json
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "aipf-ui-ux" / "SKILL.md"
SEARCH = ROOT / "scripts" / "search_catalog.py"


class UISpecialistSmokeTests(unittest.TestCase):
    def search(self, *args):
        result = subprocess.run(
            [sys.executable, str(SEARCH), *args],
            cwd=ROOT, capture_output=True, text=True, check=True, timeout=45
        )
        return json.loads(result.stdout)

    def test_skill_has_discoverable_identity(self):
        content = SKILL.read_text(encoding="utf-8")
        self.assertTrue(content.startswith("---\nname: aipf-ui-ux\n"))
        self.assertIn("description:", content.split("---", 2)[1])
        self.assertIn("AIPF v8.10.1", content)
        self.assertIn("not another development framework", content)

    def test_build_query_preserves_provenance_and_tokens(self):
        data = self.search("financial dashboard", "--type", "palette",
                           "--limit", "4", "--include-tokens")
        self.assertTrue(data["results"])
        self.assertLessEqual(len(data["results"]), 4)
        for candidate in data["results"]:
            self.assertEqual(candidate["entry_type"], "palette")
            self.assertIn(candidate["source_ref"], candidate["source_url"])
            self.assertIn("redistribution_status", candidate)
            self.assertNotEqual(candidate["redistribution_status"], "approved_for_bundle")
        self.assertTrue(any(x.get("design_tokens") for x in data["results"]))

    def test_audit_query_does_not_select_build_only_entries(self):
        data = self.search("active state navigation", "--specialist-use", "audit", "--limit", "4")
        self.assertTrue(data["results"])
        self.assertTrue(all(x["specialist_use"] in {"audit", "multiple"} for x in data["results"]))
        self.assertTrue(all("design_tokens" not in x for x in data["results"]))


if __name__ == "__main__":
    unittest.main()
