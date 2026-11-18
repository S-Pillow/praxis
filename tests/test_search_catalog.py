import unittest

from scripts.search_catalog import load_catalog, rank_entries, reference

class SearchCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = load_catalog()

    def test_all_populated_entries_available(self):
        self.assertEqual(len(self.rows), 5373)

    def test_financial_dashboard_palette(self):
        matches = rank_entries("financial dashboard", self.rows, limit=8, entry_type="palette")
        self.assertTrue(matches)
        self.assertTrue(any("Financial Dashboard" in x["original_name"] for _, x in matches))

    def test_style_query_does_not_return_unrelated_assets(self):
        matches = rank_entries("glassmorphism", self.rows, limit=8, entry_type="style")
        self.assertTrue(matches)
        self.assertTrue(all(e["entry_type"] == "style" for _, e in matches))

    def test_distinct_source_variants_remain_available(self):
        matches = rank_entries("neumorphism", self.rows, limit=10)
        ids = {entry["catalog_id"] for _, entry in matches}
        self.assertTrue(any(x.startswith("uupm:styles:neumorphism") for x in ids))
        self.assertTrue(any(x.startswith("open-design:design-systems:neumorphism") for x in ids))

    def test_no_asset_licensing_claim_or_hidden_tokens(self):
        results = rank_entries("riso", self.rows, limit=3)
        selected = reference(results[0][1], results[0][0], include_tokens=False)
        self.assertNotIn("design_tokens", selected)
        self.assertIn("asset_license_status", selected)
        self.assertNotEqual(selected["redistribution_status"], "approved_for_bundle")

if __name__ == "__main__":
    unittest.main()
