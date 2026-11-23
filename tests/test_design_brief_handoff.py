"""Lightweight contract checks for the local copy-to-AI handoff."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UI = ROOT / 'ui' / 'catalog-explorer'


class DesignBriefHandoffTests(unittest.TestCase):
    def test_accessible_handoff_controls_present(self):
        html = (UI / 'index.html').read_text(encoding='utf-8')
        self.assertIn('id="aiHandoff"', html)
        self.assertIn('id="copyBrief"', html)
        self.assertIn('id="designTask"', html)
        self.assertIn('maxlength="600"', html)
        self.assertIn('id="copyStatus" role="status" aria-live="polite"', html)
        self.assertIn('id="briefOutput"', html)

    def test_export_is_bounded_and_preserves_provenance(self):
        script = (UI / 'app.js').read_text(encoding='utf-8')
        for expected in (
            'function buildDesignBrief(task, entries)',
            '[...saved].slice(0,3)',
            "entry.catalog_id", "entry.source_ref", "entry.source_url",
            "entry.redistribution_status", "entry.asset_license_status",
            "'designTask'", "navigator.clipboard.writeText(text)",
            "out.hidden=false;out.focus();out.select()",
        ):
            self.assertIn(expected, script, expected)
        self.assertNotIn('https://api.openai.com', script)


if __name__ == '__main__':
    unittest.main()