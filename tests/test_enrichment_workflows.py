"""Static safeguards for enrichment CI; live GitHub dispatch is a separate gate."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / '.github/workflows'
EXPECTED = {
    'enrich-hallmark-tokens.yml': 'enrich_hallmark_tokens.py',
    'enrich-mengto-knowledge.yml': 'enrich_mengto_knowledge.py',
    'enrich-open-design-references.yml': 'enrich_open_design_references.py',
    'enrich-open-design.yml': 'enrich_open_design.py',
}


class EnrichmentWorkflowTests(unittest.TestCase):
    def test_enrichment_is_manual_read_only_and_pinned(self):
        self.assertEqual({p.name for p in WORKFLOWS.glob('enrich-*.yml')}, set(EXPECTED))
        for name, script in EXPECTED.items():
            with self.subTest(workflow=name):
                text = (WORKFLOWS / name).read_text(encoding='utf-8')
                self.assertEqual(text.split('on:\n', 1)[1].split('jobs:', 1)[0], '  workflow_dispatch:\n')
                self.assertEqual(re.findall(r'contents:\s*(\S+)', text), ['read'])
                self.assertEqual(text.count('uses: actions/checkout@'), 2)
                self.assertEqual(re.findall(r'persist-credentials:\s*(\S+)', text), ['false', 'false'])
                self.assertRegex(text, r'(?m)^\s+ref: [0-9a-f]{40}$')
                self.assertIn(f'python scripts/{script} --upstream-root ../upstream', text)
                self.assertIn('python -m unittest discover -s tests -v', text)
                self.assertIn('git diff --exit-code -- .', text)
                self.assertNotRegex(text, r'(?m)\b(?:git\s+(?:commit|push|config)|gh\s+pr\s+create)\b')
                self.assertNotIn('continue-on-error:', text)

    def test_validation_covers_enrichment_workflow_edits(self):
        text = (WORKFLOWS / 'catalog-validation.yml').read_text(encoding='utf-8')
        for event in ('pull_request', 'push'):
            section = re.search(rf'^  {event}:\n((?:    .*\n)+)', text, re.M).group(1)
            self.assertIn("- '.github/workflows/enrich-*.yml'", section)
        self.assertIn('persist-credentials: false', text)
        self.assertNotIn('contents: write', text)
