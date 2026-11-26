"""Security candidate mechanism and knowledge regression; not semantic or audit evidence."""
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest
from unittest.mock import patch
from scripts import praxis_context as ctx

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / 'skills/security-privacy'
CAP = ROOT / 'knowledge/capabilities'
REG = ROOT / 'skills/specialists.json'


class SecurityMechanismTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        for rel in ('skills/aipf-ui-ux/SKILL.md', 'scripts/recommend_design.py',
                    'skills/architecture/SKILL.md', 'skills/security-privacy/SKILL.md'):
            p = self.root / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text('test double', encoding='utf-8')
        shutil.copy(REG, self.root / 'skills/specialists.json')
        mock = patch.object(ctx, 'verify_framework', return_value='8.10.1')
        mock.start()
        self.addCleanup(mock.stop)

    def resolve(self, task, chapters):
        return ctx.resolve(task, chapters, self.root)

    def test_modes_across_paths(self):
        for mode in ('design', 'harden', 'review'):
            for chapters in ([11], [12], [12, 13], [12, 14, 15],
                             [12, 16, 17], [12, 18, 19, 20], [12, 21]):
                with self.subTest(mode=mode, chapters=chapters):
                    r = self.resolve('security-' + mode, chapters)
                    self.assertEqual(r['status'], 'consult')
                    self.assertEqual(r['authority'], 'advisory_only')
                    self.assertEqual(r['specialists'], [{
                        'id': 'aipf-security-privacy', 'version': '0.1',
                        'skill': 'skills/security-privacy/SKILL.md', 'mode': mode,
                        'status': 'available'}])

    def test_no_lookup_process(self):
        with patch.object(ctx.subprocess, 'run') as run:
            for mode in ('design', 'harden', 'review'):
                r = self.resolve('security-' + mode, [12, 15])
                self.assertNotIn('lookup_status', r['specialists'][0])
                s = ctx.retrieve(r, 'actual task', platform='web', root=self.root)['specialists'][0]
                self.assertEqual(s['lookup_status'], 'not_applicable')
                self.assertNotIn('lookup', s)
                self.assertNotIn('retrieval_script', s)
            run.assert_not_called()

    def test_missing_skill_and_path(self):
        with patch.object(ctx.subprocess, 'run') as run:
            self.assertEqual(self.resolve('security-review', [])['status'], 'recheck_framework_path')
            (self.root / 'skills/security-privacy/SKILL.md').unlink()
            r = self.resolve('security-review', [12, 15])
            self.assertEqual(r['status'], 'specialist_unavailable')
            self.assertEqual(ctx.retrieve(r, 'actual task', root=self.root), r)
            run.assert_not_called()

    def test_skip_unknown_and_blank(self):
        with patch.object(ctx.subprocess, 'run') as run:
            for task in ('non-ui', 'minor-ui'):
                r = self.resolve(task, [12, 14, 15, 21])
                self.assertEqual(r['status'], 'not_needed')
                self.assertEqual(r['specialists'], [])
                self.assertEqual(ctx.retrieve(r, 'minor task', root=self.root), r)
            with self.assertRaises(ValueError):
                self.resolve('security-unknown', [12])
            with self.assertRaises(ValueError):
                ctx.retrieve(self.resolve('security-design', [12]), ' ', root=self.root)
            run.assert_not_called()

    def test_legacy_entries(self):
        for task, mode in [('ui-build', 'build'), ('ui-critique', 'critique'), ('ui-audit', 'audit')]:
            self.assertEqual(self.resolve(task, [12, 14])['specialists'], [{
                'id': 'aipf-ui-ux', 'version': '0.3', 'skill': 'skills/aipf-ui-ux/SKILL.md',
                'mode': mode, 'retrieval_script': 'scripts/recommend_design.py', 'status': 'available'}])
        for mode in ('design', 'evolve', 'critique'):
            self.assertEqual(self.resolve('architecture-' + mode, [12])['specialists'], [{
                'id': 'aipf-architecture', 'version': '0.1',
                'skill': 'skills/architecture/SKILL.md', 'mode': mode, 'status': 'available'}])
        self.assertEqual(self.resolve('ui-build', [12])['status'], 'recheck_framework_path')
        self.assertEqual(self.resolve('architecture-design', [14])['status'], 'recheck_framework_path')


class SecurityKnowledgeTests(unittest.TestCase):
    def test_unique_card_index_fields_sources(self):
        index = (SEC / 'INDEX.md').read_text(encoding='utf-8')
        sources = (SEC / 'SOURCES.md').read_text(encoding='utf-8')
        ids = []
        guides = list((SEC / 'references').glob('*.md'))
        self.assertEqual(len(guides), 9)
        for guide in guides:
            cards = re.split(r'^## (SD\d+)\n', guide.read_text(encoding='utf-8'), flags=re.M)
            for card, body in zip(cards[1::2], cards[2::2]):
                ids.append(card)
                for field in ('Decision', 'Context / use when', 'Alternatives and tradeoffs',
                              'Constraints / unsuitable conditions', 'Verification / revisit',
                              'Provenance and limits'):
                    self.assertIn('**' + field + ':**', body, (card, field))
                self.assertIn(f'(references/{guide.name}#{card.lower()})', index)
                for ref in re.findall(r'\b(?:PS|SR)-\d{2}\b', body):
                    self.assertIn('**' + ref + ' —', sources)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), {f'SD{i:02d}' for i in range(1, 37)})
        self.assertEqual(set(ids), set(re.findall(r'\[(SD\d+) —', index)))

    def test_links_and_registry_contract(self):
        registry = json.loads(REG.read_text(encoding='utf-8'))
        security = next(s for s in registry['specialists'] if s['id'] == 'aipf-security-privacy')
        self.assertEqual(security['chapters_any'], list(range(11, 22)))
        self.assertNotIn('retrieval_script', security)
        self.assertEqual(security['tools'], [])
        tasks = [t for s in registry['specialists'] for t in s['tasks']]
        self.assertEqual(len(tasks), len(set(tasks)))
        for path in (security['skill'], *security['knowledge_sources']):
            self.assertTrue((ROOT / path).is_file(), path)
        for source in list(SEC.rglob('*.md')) + [CAP / 'security-privacy.md']:
            for dest in re.findall(r'\]\(([^)]+)\)', source.read_text(encoding='utf-8')):
                if '://' in dest:
                    continue
                path, _, frag = dest.partition('#')
                target = (source.parent / path).resolve() if path else source
                self.assertTrue(target.is_file(), (source, dest))
                if frag:
                    heads = re.findall(r'^#+\s+(.+)$', target.read_text(encoding='utf-8'), re.M)
                    self.assertIn(frag, [re.sub(r'[^\w -]', '', h.lower()).replace(' ', '-') for h in heads])

    def test_actual_framework_and_no_lookup(self):
        self.assertEqual(ctx.verify_framework(ROOT), '8.10.1')
        with patch.object(ctx.subprocess, 'run') as run:
            for mode in ('design', 'harden', 'review'):
                r = ctx.resolve('security-' + mode, [12, 15], ROOT)
                self.assertEqual(r['status'], 'consult')
                self.assertEqual(ctx.retrieve(r, 'actual task', root=ROOT)['specialists'][0]['lookup_status'], 'not_applicable')
            run.assert_not_called()


if __name__ == '__main__':
    unittest.main()
