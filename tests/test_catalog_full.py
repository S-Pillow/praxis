"""Read-only validation of the populated AIPF Unified Design Catalog.

This verifies structure and provenance, NOT content quality, visual acceptance,
font/image licenses, legal clearance, or upstream asset rights.
"""
import json
import pathlib
import re
import unittest
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "entries"
SCHEMA = json.loads((ROOT / "catalog/schema/entry.schema.json").read_text())
PINNED = {
    "Nutlope/hallmark": "04977e15f3dfd6ee4b74c887dac3eb52665d6c92",
    "nextlevelbuilder/ui-ux-pro-max-skill": "f2cc36555984fbfb08f1dca037da2467578f33d2",
    "feimacode/open-design-agent-kit": "1b3832c3452720f028a96b1bdab805ecc1aa3213",
    "pbakaus/impeccable": "d41d9860b0094dcb68030657da63461212835aaa",
    "MengTo/Skills": "3cc93458c4949c39a04e938ea7892a1d6d3d40bf",
}
EXPECTED_DATASET_COUNTS = {
    "hallmark-themes.json": 50,
    "uupm-styles.json": 89,
    "uupm-colors.json": 192,
    "uupm-typography.json": 74,
    "uupm-landing.json": 34,
    "uupm-products.json": 192,
    "uupm-ux-guidelines.json": 120,
    "uupm-motion.json": 17,
    "uupm-charts.json": 25,
    "uupm-ui-reasoning.json": 192,
    "uupm-icons.json": 105,
    "uupm-app-interface.json": 32,
    "uupm-react-performance.json": 44,
    "open-design-design-systems.json": 198,
    "open-design-templates.json": 114,
    "open-design-examples.json": 193,
    "open-design-skills.json": 197,
    "mengto-illustration.json": 14,
    "impeccable-knowledge.json": 45,
    "uupm-font-families-01.json": 400,
    "uupm-font-families-02.json": 400,
    "uupm-font-families-03.json": 400,
    "uupm-font-families-04.json": 400,
    "uupm-font-families-05.json": 334,
    "uupm-phosphor-icons-01.json": 400,
    "uupm-phosphor-icons-02.json": 400,
    "uupm-phosphor-icons-03.json": 400,
    "uupm-phosphor-icons-04.json": 312,
}
# starter.json deliberately excluded: illustrative, non-production examples
def load():
    data = []
    for filename, expected in EXPECTED_DATASET_COUNTS.items():
        path = CATALOG / filename
        rows = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(rows, list) or len(rows) != expected:
            raise AssertionError(f"{filename}: expected {expected}, got {len(rows)}")
        data.extend(rows)
    return data

class PopulatedCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = load()
        cls.by_id = {x["catalog_id"]: x for x in cls.entries}

    def test_source_inventory_count(self):
        self.assertEqual(len(self.entries), sum(EXPECTED_DATASET_COUNTS.values()))
        self.assertEqual(len(self.entries), 5373)

    def test_unique_ids_and_pinned_sources(self):
        self.assertEqual(len(self.by_id), len(self.entries))
        for x in self.entries:
            self.assertEqual(x["source_ref"], PINNED[x["source_repo"]], x["catalog_id"])
            self.assertIn(x["source_ref"], x["source_url"], x["catalog_id"])

    def test_required_fields_and_values(self):
        required = SCHEMA["required"]
        props = SCHEMA["properties"]
        for x in self.entries:
            self.assertTrue(set(required) <= set(x), x.get("catalog_id"))
            self.assertTrue(re.fullmatch(props["catalog_id"]["pattern"], x["catalog_id"]), x["catalog_id"])
            for field in ["entry_type","asset_license_status","redistribution_status","evidence_status","specialist_use"]:
                self.assertIn(x[field], props[field]["enum"], (x["catalog_id"],field))
            self.assertTrue(x["original_name"], x["catalog_id"])
            self.assertTrue(x["source_path_or_key"], x["catalog_id"])
            self.assertIn(x["source_repo"], x["source_url"])
            self.assertTrue(x["license_evidence_url"].startswith("https://github.com/"))

    def test_no_unreviewed_redistribution(self):
        for x in self.entries:
            self.assertNotEqual(x["redistribution_status"], "approved_for_bundle", x["catalog_id"])
        self.assertFalse(list((ROOT / "catalog").rglob("*.ttf")), "bundled fonts not reviewed")
        self.assertFalse(list((ROOT / "catalog").rglob("*.webp")), "bundled image not reviewed")
        self.assertFalse(list((ROOT / "catalog").rglob("*.svg")), "bundled SVG not reviewed")

    def test_overlaps_preserve_both_source_entries(self):
        rel = json.loads((ROOT / "catalog/relations/overlaps.json").read_text())
        for r in rel:
            self.assertIn(r["left_id"], self.by_id)
            self.assertIn(r["right_id"], self.by_id)
            self.assertNotEqual(r["left_id"], r["right_id"])
            self.assertFalse(r["should_merge"])
            self.assertIn(r["review_status"], ["unreviewed", "source_compared", "candidate_explained"])

    def test_license_manifest_is_not_claimed_as_independent_verification(self):
        h = json.loads((ROOT / "catalog/provenance/hallmark-photo-manifest.json").read_text())
        m = json.loads((ROOT / "catalog/provenance/mengto-illustration-assets.json").read_text())
        self.assertEqual(len(h["items"]), 755)
        self.assertEqual(len(m["assets"]), 42)
        self.assertTrue(all(x["redistribution"] == "BLOCKED" for x in h["items"]))
        self.assertTrue(all(x["redistribution"] == "blocked_pending_review" for x in m["assets"]))

    def test_catalog_provenance_gaps_are_not_silenced(self):
        states = Counter(e["evidence_status"] for e in self.entries)
        self.assertGreater(states["source_inspected"], 0)
        self.assertGreater(states["candidate_unverified"], 0)
        # This is expected until source-level enrichment and license review are complete.

if __name__ == "__main__":
    unittest.main()
