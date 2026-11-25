"""Executable quality regressions and static instruction contracts; not live agent proof."""
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest

from scripts.check_contrast import check
from scripts.recommend_design import analyse_task, query_terms, recommend
from scripts.search_catalog import load_catalog

ROOT = Path(__file__).resolve().parents[1]
UI = ROOT / 'ui/catalog-explorer'


def read(path):
    return (ROOT / path).read_text(encoding='utf-8')


class QualityCorrectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = load_catalog()
        spec = importlib.util.spec_from_file_location('quality_explorer', UI / 'server.py')
        cls.explorer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.explorer)

    def test_q01_description_is_safe_yaml_scalar(self):
        # This scalar deliberately uses JSON-compatible double quotes, a YAML subset.
        # Full native discovery is a separate live observation, not claimed here.
        header = read('.agents/skills/aipf-ui-ux/SKILL.md').split('---', 2)[1]
        description = re.search(r'^description: (.*)$', header, re.M).group(1)
        self.assertIn('repository: create', json.loads(description))

    def test_q02_ci_triggers_cover_executable_and_discovery_inputs(self):
        workflow = read('.github/workflows/catalog-validation.yml')
        expected = {'catalog/**', 'ui/**', 'skills/**', '.agents/**', 'AGENTS.md',
                    'scripts/**', 'framework/**', 'tests/**', '.github/workflows/catalog-validation.yml'}
        for event in ('pull_request', 'push'):
            section = re.search(rf'^  {event}:\n((?:    .*\n)+)', workflow, re.M).group(1)
            self.assertIn('branches: [main]', section)
            self.assertTrue(expected <= set(re.findall(r"- '([^']+)'", section)))

    def test_q03_q04_ui_handler_contract(self):
        # The separate browser check executes these handlers on the actual DOM.
        app = read('ui/catalog-explorer/app.js')
        self.assertIn("'input, textarea, select, [role=\"textbox\"]'", app)
        self.assertIn('target.isContentEditable', app)
        self.assertIn('!isEditableTarget(e.target)', app)
        self.assertIn("$('clearSearch').addEventListener('click',clearSearch)", app)
        clear = re.search(r'function clearSearch\(\)\{([^}]+)\}', app).group(1)
        self.assertIn("state.query=''", clear)
        self.assertNotIn('state.type', clear)
        self.assertNotIn('state.view', clear)
        self.assertNotIn('showView', clear)

    def test_q05_q06_mobile_navigation_contract(self):
        html = read('ui/catalog-explorer/index.html')
        css = read('ui/catalog-explorer/styles.css')
        self.assertRegex(html, r'data-view="explore" aria-label="Explore library"')
        self.assertRegex(html, r'data-view="saved" aria-label="Saved references"')
        self.assertIn('.nav-item{position:relative;', css)
        self.assertIn('.nav-item[data-view=saved]{padding-right:', css)

    def refs(self, task, mode='build', platform='web'):
        return recommend(task, self.rows, mode=mode, platform=platform)['references']

    def test_q07_commerce_aliases_share_results(self):
        queries = ('shop', 'ecommerce', 'e-commerce')
        self.assertEqual([query_terms(q, analyse_task(q)) for q in queries], [['commerce']]*3)
        found = [self.refs(q) for q in queries]
        self.assertTrue(found[0])
        self.assertEqual(found[0], found[1])
        self.assertEqual(found[0], found[2])
        self.assertTrue(any(r['catalog_id'] == 'uupm:colors:3' for r in found[0]))

    def test_q08_focused_accessibility_correction_vs_creation(self):
        for task in ('Make keyboard focus visible', 'Update keyboard navigation', 'Fix keyboard navigation'):
            with self.subTest(task=task):
                result = recommend(task, self.rows, platform='web')
                self.assertEqual(result['selection_scope'], 'focused_accessibility_correction')
                self.assertTrue(result['references'])
                self.assertEqual({r['entry_type'] for r in result['references']}, {'guideline'})
        for task in ('Make a dashboard with keyboard navigation', 'Build a new dashboard with keyboard navigation',
                     'Update the theme and keyboard navigation'):
            with self.subTest(task=task):
                result = recommend(task, self.rows, platform='web')
                self.assertEqual(result['selection_scope'], 'normal')
                self.assertIn('direction', {r['role'] for r in result['references']})
        self.assertIn('uupm:app-interface:28', {r['catalog_id'] for r in self.refs('Audit safe area insets', 'audit', 'mobile')})

    def test_q09_saved_search_matches_explore_with_stable_saved_order(self):
        m = self.explorer
        hits = m.search('dashboard financial', limit=12)['results']
        self.assertEqual(len(hits), 12)
        keys = [r['catalog_id'] for r in reversed(hits)]
        ids = ','.join(keys + [keys[0], 'unknown-id'])
        actual = m.search('dashboard financial', ids=ids, limit=5, offset=2)
        self.assertEqual(actual['matches'], 12)
        self.assertEqual([r['catalog_id'] for r in actual['results']], keys[2:7])
        self.assertTrue(actual['has_more'])
        category = hits[0]['entry_type']
        expected = [r['catalog_id'] for r in reversed(hits) if r['entry_type'] == category]
        filtered = m.search('dashboard financial', category, ids=ids, limit=48)
        self.assertEqual([r['catalog_id'] for r in filtered['results']], expected)
        self.assertEqual(m.search('zzzzunlikely987654321', ids=ids)['matches'], 0)

    def test_q10_color_aliases_share_guidelines(self):
        queries = ('colour', 'colours', 'color', 'colors')
        found = [self.refs(q, 'audit') for q in queries]
        self.assertTrue(found[0])
        self.assertTrue(all(r == found[0] for r in found))
        self.assertTrue(any('color' in r['original_name'].lower() for r in found[0]))

    def test_q11_contrast_math_and_historical_failure(self):
        self.assertEqual(check('#000000', '#ffffff')['ratio'], 21)
        self.assertEqual(check('#ffffff', '#ffffff')['ratio'], 1)
        for color, white, selected in [('#DC2626', 4.829, 4.397), ('#EA580C', 3.560, 3.241),
                                       ('#CA8A04', 2.938, 2.675), ('#64748B', 4.759, 4.333)]:
            with self.subTest(color=color):
                self.assertAlmostEqual(check(color, '#FFFFFF')['ratio'], white, places=2)
                self.assertAlmostEqual(check(color, '#DCFCE7')['ratio'], selected, places=2)
                self.assertFalse(check(color, '#DCFCE7')['passed'])
        for color in ('#991B1B', '#9A3412', '#854D0E', '#475569'):
            for background in ('#FFFFFF', '#DCFCE7'):
                self.assertTrue(check(color, background)['passed'])
        for bad in ('#fff', 'rgba(0,0,0,.4)', '#00000080'):
            with self.assertRaises(ValueError):
                check(bad, '#ffffff')
        for bad in (float('nan'), 0, 22):
            with self.assertRaises(ValueError):
                check('#000000', '#ffffff', bad)

    def test_q11_contrast_cli_exit_status(self):
        script = ROOT / 'scripts/check_contrast.py'
        for fg, status in (('#000000', 0), ('#EA580C', 1), ('#fff', 2)):
            result = subprocess.run([sys.executable, str(script), fg, '#ffffff'], capture_output=True, text=True)
            self.assertEqual(result.returncode, status)
            if status < 2:
                self.assertEqual(json.loads(result.stdout)['passed'], status == 0)

    def test_q11_q12_q13_instruction_and_scenario_contracts(self):
        specialist = read('skills/aipf-ui-ux/SKILL.md')
        guidance = read('skills/praxis/references/builder-payload.md')
        entry = read('skills/praxis/SKILL.md')
        self.assertIn('one initial recommendation lookup', specialist)
        self.assertIn('one targeted follow-up', specialist)
        self.assertIn('Count actual command invocations', specialist)
        self.assertIn('each applicable foreground/background pair', specialist)
        self.assertIn('actual retrieval invocation count and applicable contrast pairs/thresholds before issuance', guidance)
        self.assertIn('projection_full_markdown_sha256', entry)
        self.assertIn('actual `framework/projection-manifest.json` file', entry)
        cases = json.loads(read('tests/fixtures/praxis_prompt_scenarios.json'))['cases']
        self.assertEqual({c['negative_reason'] for c in cases if c['id'] in ('P10','P11','P12')},
                         {'unverified_contrast','retrieval_budget_exceeded','wrong_artifact_identity'})
