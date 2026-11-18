import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ENTRIES = ROOT / "catalog" / "entries" / "starter.json"
SCHEMA = ROOT / "catalog" / "schema" / "entry.schema.json"

class CatalogStarterTests(unittest.TestCase):
    def test_json_readable(self):
        self.assertIsInstance(json.loads(ENTRIES.read_text()), list)
        self.assertEqual(json.loads(SCHEMA.read_text())["type"], "object")

    def test_unique_provenance_and_required_fields(self):
        data = json.loads(ENTRIES.read_text())
        schema = json.loads(SCHEMA.read_text())
        ids = [r["catalog_id"] for r in data]
        self.assertEqual(len(ids), len(set(ids)))
        for entry in data:
            self.assertTrue(set(schema["required"]) <= set(entry))
            self.assertTrue(re.match(schema["properties"]["catalog_id"]["pattern"], entry["catalog_id"]))
            self.assertIn(entry["entry_type"], schema["properties"]["entry_type"]["enum"])
            self.assertIn(entry["redistribution_status"], schema["properties"]["redistribution_status"]["enum"])
            self.assertIn(entry["asset_license_status"], schema["properties"]["asset_license_status"]["enum"])
            self.assertTrue(entry["source_url"].startswith("https://github.com/"))
            self.assertTrue(entry["source_path_or_key"])

    def test_no_unreviewed_bundle_claims(self):
        for entry in json.loads(ENTRIES.read_text()):
            self.assertNotEqual(entry["redistribution_status"], "approved_for_bundle")

if __name__ == "__main__":
    unittest.main()
