"""Experimental retrieval behaviour (SPECIALIST-UIUX-02) against the real catalog."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from scripts.recommend_design import (
    IDENTITY_GROUPS, analyse_task, compatible, conflicts_with_task, recommend,
)
from scripts.search_catalog import entry_fields, load_catalog, positive_fields, rank_entries

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts' / 'recommend_design.py'
REFERENCE = ROOT / 'research' / 'evaluations' / 'retrieval-benchmark' / 'reference-v0.2'

DESKTOP_FIRST = ('Improve the existing desktop-first URL Activity Scanner results experience for technical '
                 'users reviewing batches of up to 100 URLs. Prioritize information hierarchy, dense readable '
                 'results, status summaries, keyboard accessibility, contrast, export accessibility and '
                 'responsive usability while preserving the existing dark technical identity.')
MOBILE_FIRST = 'Design a mobile-first fitness tracker web app'
PRESERVED = ('Refine the existing desktop help-desk console: make queue rows quicker to scan and keep row '
             'actions reachable from the keyboard. Keep the current light theme and component library.')
NEGATED = ("Redesign the donation landing page for a children's hospital charity. Do not use dark mode, "
           "glassmorphism or decorative animation; prioritise legibility for older donors.")
BACKEND = "Rename the CSV export column header from 'Checked' to 'Checked at' in the backend serializer."


def load_reference_search():
    spec = importlib.util.spec_from_file_location('reference_search_catalog', REFERENCE / 'search_catalog.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_cli(*args, cwd=ROOT, script=SCRIPT):
    return subprocess.run([sys.executable, str(script), *args], cwd=cwd, text=True,
                          capture_output=True, timeout=60)


class RecommendConstraintTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = load_catalog()
        cls.index = {row['catalog_id']: row for row in cls.rows}

    def ids(self, data):
        return [r['catalog_id'] for r in data['references']]

    def test_restrictions_are_not_positive_evidence_but_are_returned(self):
        mobile_first = self.index['uupm:ux-guidelines:64']
        self.assertIn('desktop', entry_fields(mobile_first))
        self.assertNotIn('desktop', positive_fields(mobile_first))
        data = recommend(MOBILE_FIRST, self.rows, platform='web')
        ref = next(r for r in data['references'] if r['catalog_id'] == 'uupm:ux-guidelines:64')
        self.assertEqual(ref['compatibility_restrictions'], mobile_first['compatibility_restrictions'])

    def test_desktop_first_excludes_mobile_first_guidance(self):
        data = recommend(DESKTOP_FIRST, self.rows, mode='build', platform='web')
        self.assertEqual(data['task_signals']['interface_priority'], 'desktop')
        self.assertNotIn('uupm:ux-guidelines:64', self.ids(data))
        self.assertTrue(data['references'])
        self.assertTrue(conflicts_with_task(self.index['uupm:ux-guidelines:64'], analyse_task(DESKTOP_FIRST)))
        self.assertTrue(conflicts_with_task(self.index['uupm:styles:flat-design-mobile-touch-first'],
                                            analyse_task(DESKTOP_FIRST)))

    def test_mobile_first_keeps_mobile_first_guidance(self):
        data = recommend(MOBILE_FIRST, self.rows, mode='build', platform='web')
        self.assertEqual(data['task_signals']['interface_priority'], 'mobile')
        self.assertIn('uupm:ux-guidelines:64', self.ids(data))
        self.assertFalse(conflicts_with_task(self.index['uupm:ux-guidelines:64'], analyse_task(MOBILE_FIRST)))

    def test_preserved_identity_suppresses_replacement_identity(self):
        data = recommend(PRESERVED, self.rows, mode='build', platform='web')
        self.assertEqual(data['selection_scope'], 'preserve_identity')
        self.assertEqual(data['task_signals']['preserved_identity'], list(IDENTITY_GROUPS))
        self.assertTrue(data['references'])
        self.assertTrue(all(r['entry_type'] == 'guideline' for r in data['references']))

    def test_requested_identity_is_still_recommended(self):
        data = recommend("Create a visual identity for an independent bookshop's events website: warm, "
                         "literary and editorial. No existing brand exists.", self.rows, platform='web')
        self.assertEqual(data['task_signals']['preserved_identity'], [])
        self.assertIn('direction', [r['role'] for r in data['references']])
        partial = recommend('Keep our brand colours but choose a new typography pairing for the blog',
                            self.rows, platform='web')
        self.assertEqual(partial['task_signals']['requested_identity'], ['typography'])
        self.assertEqual([r['role'] for r in partial['references']], ['typography'])

    def test_negated_styles_are_excluded_but_positive_styles_remain(self):
        data = recommend(NEGATED, self.rows, mode='build', platform='web')
        self.assertEqual(data['task_signals']['prohibited'], ['dark mode', 'glassmorphism', 'decorative animation'])
        for ref in data['references']:
            text = ' '.join([ref['original_name'], ref['description'],
                             ' '.join(self.index[ref['catalog_id']].get('keywords', []))]).lower()
            self.assertNotIn('glass', text)
            self.assertNotIn('dark', text)
        self.assertNotIn('uupm:styles:modern-dark-cinema-mobile', self.ids(data))
        positive = recommend('Build a SaaS landing page with a bold dark theme', self.rows, platform='web')
        self.assertIn('uupm:styles:dark-mode-oled', self.ids(positive))
        self.assertEqual(positive['task_signals']['prohibited'], [])

    def test_absent_identity_is_not_a_prohibition(self):
        signals = analyse_task('Design a new dashboard. There is no existing brand to follow.')
        self.assertEqual(signals['prohibited'], [])
        self.assertEqual(signals['preserved'], set())

    def test_critique_search_filter_includes_audit_guidelines(self):
        query = 'dense data table status results readability scanning batch'
        matches = rank_entries(query, self.rows, limit=5, specialist_use='critique')
        self.assertEqual(matches[0][1]['catalog_id'], 'uupm:ux-guidelines:71')
        self.assertTrue(all(e['specialist_use'] in {'critique', 'audit', 'multiple'} for _, e in matches))
        build = rank_entries('data table', self.rows, limit=5, specialist_use='build')
        self.assertTrue(all(e['specialist_use'] in {'build', 'multiple'} for _, e in build))

    def test_manual_search_ranking_is_unchanged(self):
        reference = load_reference_search()
        for query, kind in (('financial dashboard', 'palette'), ('glassmorphism', None),
                            ('data table', None), ('desktop first', None), ('keyboard focus', 'guideline')):
            new = [(s, e['catalog_id']) for s, e in rank_entries(query, self.rows, limit=25, entry_type=kind)]
            old = [(s, e['catalog_id']) for s, e in reference.rank_entries(query, self.rows, limit=25, entry_type=kind)]
            self.assertEqual(new, old, query)

    def test_platform_labels_are_normalized(self):
        native = self.index['uupm:app-interface:17']
        react = next(r for r in self.rows if r.get('platforms') == ['React/Next.js'])
        mobile_web = next(r for r in self.rows if r.get('platforms') == ['Mobile'])
        self.assertTrue(compatible(native, 'mobile'))
        self.assertFalse(compatible(native, 'web'))
        self.assertFalse(compatible(react, 'web'))
        self.assertTrue(compatible(react, 'web', frameworks=frozenset({'react/next.js'})))
        self.assertFalse(compatible(mobile_web, 'web'))
        self.assertTrue(compatible(mobile_web, 'web', priority='mobile'))
        data = recommend('Audit the iOS app for touch targets and dynamic type', self.rows,
                         mode='audit', platform='mobile')
        self.assertTrue(any(r['catalog_id'].startswith('uupm:app-interface:') for r in data['references']))

    def test_accessibility_guidance_is_preserved(self):
        audit = recommend('Audit the improved URL Activity Scanner results interface for keyboard accessibility, '
                          'focus recovery, contrast, readable technical data, batch summary accuracy, desktop and '
                          'mobile usability, result-key navigation and CSV export accessibility.',
                          self.rows, mode='audit', platform='web')
        self.assertEqual(self.ids(audit)[0], 'uupm:ux-guidelines:41')
        self.assertTrue(all(r['role'] == 'check_reference' for r in audit['references']))
        self.assertLessEqual(len(audit['references']), 3)

    def test_unrelated_task_abstains_but_ui_task_does_not(self):
        data = recommend(BACKEND, self.rows)
        self.assertEqual(data['references'], [])
        self.assertEqual(data['selection_scope'], 'non_visual_task')
        ui = recommend('Show backend validation errors inline on the settings page form', self.rows, platform='web')
        self.assertNotEqual(ui['selection_scope'], 'non_visual_task')
        self.assertTrue(ui['references'])

    def test_provenance_and_license_fields_match_catalog(self):
        for task, mode in ((MOBILE_FIRST, 'build'), (PRESERVED, 'build'), ('Audit keyboard focus', 'audit')):
            for ref in recommend(task, self.rows, mode=mode, platform='web')['references']:
                row = self.index[ref['catalog_id']]
                for field in ('source_repo', 'source_ref', 'source_url', 'source_path_or_key', 'evidence_status',
                              'redistribution_status', 'asset_license_status', 'compatibility_restrictions'):
                    self.assertEqual(ref[field], row.get(field), field)
                self.assertEqual(ref['evidence_status'], 'source_inspected')
                self.assertIn(ref['source_ref'], ref['source_url'])


class RecommendCliTests(unittest.TestCase):
    def test_output_contract_is_a_superset_of_v02(self):
        reference = run_cli('financial dashboard', '--mode', 'build', '--platform', 'web',
                            script=REFERENCE / 'recommend_design.py')
        current = run_cli('financial dashboard', '--mode', 'build', '--platform', 'web')
        self.assertEqual(current.returncode, 0, current.stderr)
        old, new = json.loads(reference.stdout), json.loads(current.stdout)
        self.assertTrue(set(old) <= set(new))
        self.assertLessEqual(len(new['references']), 3)
        for old_ref, new_ref in zip(old['references'], new['references']):
            self.assertTrue(set(old_ref) <= set(new_ref))
        self.assertEqual(new['use_boundary'], old['use_boundary'])
        self.assertEqual(new['selection_method'], old['selection_method'])

    def test_limits_and_arguments_are_unchanged(self):
        self.assertEqual(run_cli('Dashboard', '--limit', '6').returncode, 2)
        self.assertEqual(run_cli('Dashboard', '--limit', '0').returncode, 2)
        self.assertEqual(run_cli('Dashboard', '--mode', 'other').returncode, 2)
        five = json.loads(run_cli('Audit keyboard focus and navigation', '--mode', 'audit', '--limit', '5').stdout)
        self.assertLessEqual(len(five['references']), 5)

    def test_empty_result_is_distinct_from_failure(self):
        empty = run_cli(BACKEND)
        self.assertEqual(empty.returncode, 0)
        self.assertEqual(json.loads(empty.stdout)['references'], [])
        self.assertEqual(run_cli('   ').returncode, 2)
        with tempfile.TemporaryDirectory() as tmp:
            scripts = Path(tmp) / 'scripts'
            scripts.mkdir()
            for name in ('recommend_design.py', 'search_catalog.py'):
                shutil.copyfile(ROOT / 'scripts' / name, scripts / name)
            for script in ('recommend_design.py', 'search_catalog.py'):
                missing = run_cli('dashboard', cwd=tmp, script=scripts / script)
                self.assertEqual(missing.returncode, 1, script)
                self.assertEqual(missing.stdout, '')
                self.assertIn('catalog entries not found', missing.stderr)

    def test_output_is_deterministic(self):
        args = (PRESERVED, '--mode', 'build', '--platform', 'web')
        self.assertEqual(run_cli(*args).stdout, run_cli(*args).stdout)


if __name__ == '__main__':
    unittest.main()
