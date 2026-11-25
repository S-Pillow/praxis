"""Static contract and scenario coverage checks, not live prompt quality tests."""
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding='utf-8')


class PayloadContractTests(unittest.TestCase):
    def test_entry_uses_progressive_payload_reference(self):
        skill = read('skills/praxis/SKILL.md')
        ref = 'skills/praxis/references/builder-payload.md'
        self.assertIn(ref, skill)
        guidance = read(ref)
        self.assertIn('passed Preflight', guidance)
        self.assertIn('canonical issuance gate', guidance)
        self.assertIn('not as a mandatory additional report', guidance)

    def test_role_contract_across_active_surfaces(self):
        for path in ('skills/praxis/SKILL.md', '.agents/skills/praxis/SKILL.md',
                     'AGENTS.md', 'PRAXIS.md', 'docs/ARCHITECTURE.md', 'docs/PRD.md', 'README.md'):
            with self.subTest(path=path):
                text = read(path).lower()
                self.assertIn('optional', text)
                self.assertIn('authority', text)
                self.assertNotIn('builder access to praxis and prd is helpful', text)
        self.assertIn('no artificial transport', read('skills/praxis/SKILL.md'))

    def test_quality_rubric_and_decision_links(self):
        text = read('docs/TESTING.md')
        weights = (25, 20, 20, 15, 10, 10)
        for label, weight in zip(('Operational completeness', 'Clarity and lack of ambiguity',
                                  'Scope and authority precision', 'Token efficiency',
                                  'Builder portability', 'Verification and stop conditions'), weights):
            self.assertIn(f'| {label} | {weight} |', text)
        self.assertEqual(sum(weights), 100)
        self.assertIn('no weighted score overrides it', text)
        for name in ('PRAXIS-DEC-002-builder-context-independence.md', 'PRAXIS-DEC-003-quality-first-prompts.md'):
            self.assertIn(name, read('docs/DEVELOPMENT-BASELINE.md'))
            self.assertTrue((ROOT / 'docs/decisions' / name).is_file())

    def test_scenarios_cover_portable_optional_and_failure_modes(self):
        cases = json.loads(read('tests/fixtures/praxis_prompt_scenarios.json'))['cases']
        self.assertEqual(len({c['id'] for c in cases}), len(cases))
        self.assertEqual({c['expected_disposition'] for c in cases}, {'issue', 'stop', 'direct'})
        self.assertTrue({'hidden_context', 'missing_requirements', 'authority_expansion',
                         'forbidden_effect', 'false_orchestration', 'weaker_evidence',
                         'unnecessary_scope'} <= {c['negative_reason'] for c in cases})
        self.assertTrue(any('no governing resources' in c['context'] for c in cases))
        self.assertTrue(any('optional Praxis/PRD access' in c['context'] for c in cases))
        for case in cases:
            self.assertTrue(all(case[k].strip() for k in ('request', 'context', 'expected_behavior', 'negative_example')))

    def test_compact_proportionality_and_observed_example(self):
        guidance = read('skills/praxis/references/builder-payload.md')
        self.assertIn('without making each a separate heading', guidance)
        self.assertIn('repeat only when it materially improves execution reliability', guidance)
        self.assertIn('PASS / PASS WITH NOTES / PARTIAL / FAIL / BLOCKED', guidance)
        self.assertIn('do not impose a universal prohibition', guidance)
        self.assertIn('Quality and correctness precede token efficiency', guidance)
        cases = json.loads(read('tests/fixtures/praxis_prompt_scenarios.json'))['cases']
        case = next(c for c in cases if c['id'] == 'P09')
        self.assertEqual(case['negative_reason'], 'overexpanded_compact')
        evidence = case['observed_example']
        # Check canonical LF content, independent of Git checkout line endings.
        # The archive verification separately establishes exact byte identity.
        raw = read(evidence['path']).encode('utf-8')
        self.assertEqual(hashlib.sha256(raw).hexdigest(), evidence['derived_sha256'])
        self.assertEqual(evidence['source_sha256'], 'c2d3493c105b04c3d7c33aaebc15a51b020c6f377afc928e8019546cd2217ccd')
        self.assertEqual(raw.count(b'<APP_ROOT>'), 3)
        self.assertIn('not an executable authorization', evidence['transformation'])
        self.assertIn('no hard length threshold', case['expected_behavior'])
