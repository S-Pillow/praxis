"""Regression of agent-selected routes, not a natural-language path classifier test."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import shutil
import unittest
from unittest.mock import patch

from scripts.praxis_context import ROOT, resolve, retrieve

CORPUS = json.loads((Path(__file__).parent / 'fixtures/praxis_scenarios.json').read_text(encoding='utf-8'))


class PraxisScenarioTests(unittest.TestCase):
    def test_retained_scenario_helper_routes(self):
        for case in CORPUS['scenarios']:
            with self.subTest(case=case['id']):
                if case['expected'] == 'bypass':
                    # A reasoning-only scenario: no helper call or execution claimed.
                    self.assertEqual(case['chapters'], [])
                    continue
                result = resolve(case['task'], case['chapters'])
                self.assertEqual(result['status'], case['expected'])
                if case['expected'] == 'not_needed':
                    with patch('scripts.praxis_context.subprocess.run') as runner:
                        self.assertEqual(retrieve(result, case['request'])['status'], 'not_needed')
                        runner.assert_not_called()

    def test_retained_material_scenarios_lookup(self):
        for case in CORPUS['scenarios']:
            if case['expected'] != 'consult':
                continue
            with self.subTest(case=case['id']):
                result = retrieve(resolve(case['task'], case['chapters']), case['request'], 'web')
                specialist = result['specialists'][0]
                self.assertIn(specialist['lookup_status'], {'completed', 'empty'})
                self.assertEqual(specialist['lookup']['catalog_records_searched'], 5500)

    def test_unknown_task_fails_closed(self):
        for task in ('ui-buid', '', 'future-specialist', 'UI-build'):
            with self.subTest(task=task):
                with self.assertRaisesRegex(ValueError, 'Unknown task identifier'):
                    resolve(task, [11, 14])
        proc = subprocess.run([sys.executable, str(ROOT/'scripts/praxis_context.py'), '--task', 'ui-buid', '--chapter', '14'], capture_output=True, encoding='utf-8')
        self.assertEqual(proc.returncode, 2)
        self.assertIn('Unknown task identifier', proc.stderr)
        self.assertEqual(proc.stdout, '')

    def test_missing_catalog_vs_required_framework(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT/'framework', root/'framework')
            shutil.copytree(ROOT/'skills', root/'skills')
            (root/'scripts').mkdir()
            for name in ('recommend_design.py','search_catalog.py'):
                shutil.copyfile(ROOT/'scripts'/name, root/'scripts'/name)
            result = retrieve(resolve('ui-build', [11, 14], root), 'Build a dashboard', root=root)
            self.assertEqual(result['specialists'][0]['lookup_status'], 'unavailable')
            self.assertNotIn('lookup', result['specialists'][0])
            (root/'framework/references/paths/14-ui.md').unlink()
            with self.assertRaises(OSError):
                resolve('ui-build', [11,14], root)
