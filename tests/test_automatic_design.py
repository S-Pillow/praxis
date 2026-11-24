"""Real-catalog checks for optional, automatic UI reference lookup."""
import json
from pathlib import Path
import subprocess
import sys
import unittest

from scripts.recommend_design import recommend, exact_tokens, query_terms
from scripts.search_catalog import load_catalog

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts' / 'recommend_design.py'
SKILL = ROOT / 'skills' / 'aipf-ui-ux' / 'SKILL.md'


class AutomaticDesignRetrievalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = load_catalog()

    def test_normal_request_returns_few_source_linked_references(self):
        data = recommend('Build a financial dashboard with readable data tables', self.rows)
        self.assertEqual(data['catalog_records_searched'], 5500)
        refs = data['references']
        self.assertTrue(refs)
        self.assertLessEqual(len(refs), 3)
        self.assertTrue(any(r['catalog_id'] == 'uupm:colors:6' for r in refs))
        for ref in refs:
            self.assertIn(ref['source_ref'], ref['source_url'])
            self.assertEqual(ref['evidence_status'], 'source_inspected')
            self.assertNotEqual(ref['redistribution_status'], 'approved_for_bundle')
            self.assertLessEqual(len(ref.get('source_tokens_excerpt', {})), 10)

    def test_accessibility_guidance_fits_default_result_limit(self):
        data = recommend('Improve keyboard navigation on a financial dashboard', self.rows)
        self.assertTrue(any(r['role'] == 'usability_reference' and
                            r['entry_type'] == 'guideline' for r in data['references']))
        self.assertLessEqual(len(data['references']), 3)

    def test_real_existing_ui_keyboard_correction_does_not_restyle(self):
        request = ('Improve keyboard focus visibility and mobile navigation of the '
                   'Design Index search and category filters without changing their behavior')
        data = recommend(request, self.rows, mode='build', platform='web')
        self.assertEqual(data['selection_scope'], 'focused_accessibility_correction')
        self.assertEqual([item['role'] for item in data['references']], ['usability_reference'])
        self.assertEqual(data['references'][0]['catalog_id'], 'uupm:ux-guidelines:41')
        self.assertIn(data['references'][0]['source_ref'], data['references'][0]['source_url'])

    def test_new_accessible_dashboard_can_retrieve_palette_and_guidance(self):
        data = recommend('Build an accessible financial dashboard', self.rows)
        self.assertEqual(data['selection_scope'], 'normal')
        self.assertIn('palette', [item['role'] for item in data['references']])
        self.assertIn('usability_reference', [item['role'] for item in data['references']])

    def test_audit_returns_guidelines_not_design_systems(self):
        data = recommend('Audit keyboard focus and navigation', self.rows, mode='audit')
        self.assertTrue(data['references'])
        self.assertTrue(all(r['role'] == 'check_reference' and
                            r['entry_type'] == 'guideline' for r in data['references']))

    def test_generic_and_unknown_prompts_do_not_force_a_style(self):
        self.assertEqual(recommend('Make a beautiful modern interface', self.rows)['references'], [])
        self.assertEqual(recommend('Create a zzzyxkpt app', self.rows)['references'], [])
        self.assertEqual(query_terms('Build a finance dashboard'), ['financial', 'dashboard'])

    def test_platform_and_bounded_results(self):
        data = recommend('Create an editorial magazine', self.rows,
                         mode='build', platform='web', limit=2)
        self.assertLessEqual(len(data['references']), 2)
        self.assertTrue(all(not r['platforms'] or
                            any(str(p).lower() in ('web', 'all') for p in r['platforms'])
                            for r in data['references']))
        with self.assertRaises(ValueError):
            recommend('Dashboard', self.rows, limit=6)

    def test_source_token_values_remain_exact(self):
        row = next(e for e in self.rows if e['catalog_id'] == 'uupm:colors:6')
        self.assertEqual(exact_tokens(row)['Background'], '#020617')
        self.assertEqual(exact_tokens({'design_tokens': None}), {})

    def test_cli_and_skill_integration(self):
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), 'financial dashboard',
             '--mode', 'build', '--platform', 'web'],
            cwd=ROOT, text=True, capture_output=True, check=True, timeout=45
        )
        output = json.loads(proc.stdout)
        self.assertEqual(output['catalog_records_searched'], 5500)
        self.assertTrue(output['references'])
        self.assertLess(len(proc.stdout), 9000)
        skill = SKILL.read_text(encoding='utf-8')
        self.assertTrue(skill.startswith('---\nname: aipf-ui-ux\n'))
        self.assertIn('recommend_design.py', skill)


if __name__ == '__main__':
    unittest.main()
