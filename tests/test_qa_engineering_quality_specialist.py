"""QA v0.1 additive integration and knowledge checks; not agent/Builder qualification."""
import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch
from scripts import praxis_context as ctx

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT / 'skills/qa-engineering-quality'
CAP = ROOT / 'knowledge/capabilities'
MODES = ('plan', 'diagnose', 'review')
SKILL = 'skills/qa-engineering-quality/SKILL.md'
LEGACY = json.loads("[{\"id\":\"aipf-ui-ux\",\"version\":\"0.3\",\"chapter\":14,\"skill\":\"skills/aipf-ui-ux/SKILL.md\",\"retrieval_script\":\"scripts/recommend_design.py\",\"tasks\":{\"ui-build\":\"build\",\"ui-critique\":\"critique\",\"ui-audit\":\"audit\"},\"purpose\":\"Practical UI/UX design, improvement, visual critique and technical UI audit\",\"authority\":\"Advisory; AIPF, approved requirements and current authorization govern\",\"domain\":\"UI/UX\",\"activation\":\"Material user-facing UI design, improvement, critique or technical audit after canonical Chapter 14 routing; not unrelated coding or trivial edits.\",\"knowledge_sources\":[\"catalog/entries/\",\"catalog/SEARCH.md\"],\"tools\":[\"scripts/recommend_design.py\",\"scripts/search_catalog.py\"],\"output\":\"Source-linked candidate references and applied guidance; distinguish observations from recommendations and respect licensing.\",\"fallback\":\"Use approved project context and available craft when sufficient; disclose unavailable guidance or retrieval; never fabricate references.\"},{\"id\":\"aipf-architecture\",\"version\":\"0.1\",\"chapters_any\":[11,12],\"skill\":\"skills/architecture/SKILL.md\",\"tasks\":{\"architecture-design\":\"design\",\"architecture-evolve\":\"evolve\",\"architecture-critique\":\"critique\"},\"purpose\":\"Context-grounded software architecture and engineering design decisions, evolution and critique\",\"authority\":\"Advisory; AIPF, approved requirements and current authorization govern\",\"domain\":\"Software Architecture & Engineering Design\",\"activation\":\"Material architecture decision, structural diagnosis, change to boundaries/data/contracts, or technology evaluation after canonical AIPF routing; not incidental code edits or chapter presence alone.\",\"knowledge_sources\":[\"skills/architecture/INDEX.md\",\"knowledge/capabilities/INDEX.md\"],\"tools\":[],\"output\":\"Suitable options including no change, tradeoffs, assumptions, implementation constraints and verification implications, source-linked when material.\",\"fallback\":\"Disclose missing guides or facts; use verified project context and qualified alternatives only where sufficient, otherwise identify the material decision gap.\"},{\"id\":\"aipf-security-privacy\",\"version\":\"0.1\",\"chapters_any\":[11,12,13,14,15,16,17,18,19,20,21],\"skill\":\"skills/security-privacy/SKILL.md\",\"tasks\":{\"security-design\":\"design\",\"security-harden\":\"harden\",\"security-review\":\"review\"},\"purpose\":\"Context-grounded defensive security and privacy design, hardening and source assessment\",\"authority\":\"Advisory; AIPF, approved requirements and current authorization govern\",\"domain\":\"Security & Privacy\",\"activation\":\"Material security/privacy intent or trust/data boundary change after canonical AIPF routing; not chapter presence or minor unrelated work.\",\"knowledge_sources\":[\"skills/security-privacy/INDEX.md\",\"knowledge/capabilities/INDEX.md\"],\"tools\":[],\"output\":\"Conditional controls, alternatives, trust/data invariants, positive/negative verification and source-bound findings with evidence limits.\",\"fallback\":\"Disclose unavailable guidance or facts; continue only with sufficient verified approved context, otherwise identify decision or observation gap.\"}]")
PRIOR_CAPS = ["CAP-H01","CAP-H02","CAP-H03","CAP-D01","CAP-D02","CAP-D03","CAP-D04","CAP-D05","CAP-O01","CAP-I01","CAP-C01","CAP-C02","CAP-Q01","CAP-M01","CAP-N01","CAP-V01","CAP-V02","CAP-V03","CAP-B01","CAP-B02","CAP-S01","CAP-S02","CAP-S03","CAP-S04"]
FAMILIES = ["risk-impact.md","test-design.md","unit-property-state.md","contracts-integration.md","browser-ux.md","failure-resilience.md","diagnosis-regression.md","maintainability.md","data-quality.md","ai-agent-quality.md","test-effectiveness.md","capability-selection.md"]
SOURCE_REGISTER = ROOT / 'research/qa-engineering-quality/QA-SOURCE-REGISTER-01.md'
CROSS = ROOT / 'research/CROSS-SPECIALIST-RESEARCH-REGISTER.md'


class QAMechanismTests(unittest.TestCase):
    def test_modes_and_path_eligibility(self):
        for mode in MODES:
            for chapter in range(11, 22):
                with self.subTest(mode=mode, chapter=chapter):
                    result = ctx.resolve('qa-' + mode, [chapter], ROOT)
                    self.assertEqual(result['status'], 'consult')
                    self.assertEqual(result['authority'], 'advisory_only')
                    self.assertEqual(result['specialists'], [dict(
                        id='aipf-qa-engineering-quality', version='0.1',
                        skill=SKILL, mode=mode, status='available')])

    def test_no_subprocess(self):
        with patch.object(ctx.subprocess, 'run') as run:
            for mode in MODES:
                result = ctx.resolve('qa-' + mode, [12], ROOT)
                self.assertNotIn('lookup_status', result['specialists'][0])
                result = ctx.retrieve(result, 'material test decision', root=ROOT)
                self.assertEqual(result['specialists'][0]['lookup_status'], 'not_applicable')
            run.assert_not_called()

    def test_missing_skill_and_path(self):
        registry = (ROOT / 'skills/specialists.json').read_text(encoding='utf-8')
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'skills').mkdir()
            (root / 'skills/specialists.json').write_text(registry, encoding='utf-8')
            with patch.object(ctx, 'verify_framework', return_value='8.10.1'):
                for mode in MODES:
                    missing = ctx.resolve('qa-' + mode, [12], root)
                    self.assertEqual(missing['status'], 'specialist_unavailable')
                    self.assertEqual(missing['specialists'][0]['status'], 'unavailable')
                    for paths in ([], [10], [22]):
                        self.assertEqual(ctx.resolve('qa-' + mode, paths, root)['status'],
                                         'recheck_framework_path')

    def test_skip_unknown_blank(self):
        with patch.object(ctx.subprocess, 'run') as run:
            for task in ('non-ui', 'minor-ui'):
                self.assertEqual(ctx.resolve(task, [12], ROOT)['status'], 'not_needed')
            for task in ('qa', 'qa-verify', ''):
                with self.assertRaises(ValueError):
                    ctx.resolve(task, [12], ROOT)
            with self.assertRaises(ValueError):
                ctx.retrieve(ctx.resolve('qa-plan', [12], ROOT), '  ', root=ROOT)
            run.assert_not_called()

    def test_prior_registry_and_outputs(self):
        reg = json.loads((ROOT / 'skills/specialists.json').read_text(encoding='utf-8'))
        self.assertEqual(reg['schema_version'], 1)
        self.assertEqual(reg['specialists'][:3], LEGACY)
        self.assertEqual(len(reg['specialists']), 5)  # approved additive DevOps entry
        for legacy in LEGACY:
            chapter = legacy.get('chapter') or legacy['chapters_any'][0]
            for task, mode in legacy['tasks'].items():
                expected = dict(id=legacy['id'], version=legacy['version'],
                                skill=legacy['skill'], mode=mode, status='available')
                if 'retrieval_script' in legacy:
                    expected['retrieval_script'] = legacy['retrieval_script']
                self.assertEqual(ctx.resolve(task, [chapter], ROOT)['specialists'], [expected])
        self.assertEqual(ctx.verify_framework(ROOT), '8.10.1')


class QAKnowledgeTests(unittest.TestCase):
    def test_question_index_and_card_contract(self):
        guides = sorted((QA / 'references').glob('*.md'))
        self.assertEqual(sorted(p.name for p in guides), sorted(FAMILIES))
        index = (QA / 'INDEX.md').read_text(encoding='utf-8')
        indexed = re.findall(r'\[(QA-D\d{2}) —', index)
        found = []
        for guide in guides:
            for card in re.split(r'(?m)^## (?=QA-D\d{2} —)', guide.read_text(encoding='utf-8'))[1:]:
                found.append(card.split()[0])
                for field in ('Applicability / context', 'Decision and alternatives',
                              'Counterexample', 'Observable verification', 'Sources and limits'):
                    self.assertIn('**' + field + ':**', card)
        self.assertEqual(len(found), len(set(found)))
        self.assertEqual(sorted(found), sorted(indexed))
        self.assertTrue(all(found.count(x) == 1 for x in indexed))
        self.assertTrue(all(re.search(r'QA-D\d{2}', p.read_text(encoding='utf-8')) for p in guides))

    def test_source_ids_and_deferred_research(self):
        original = SOURCE_REGISTER.read_text(encoding='utf-8')
        sources = set(re.findall(r'^\| (QA-S\d{2}) \|', original, re.M))
        self.assertEqual(sources, {f'QA-S{i:02d}' for i in range(1, 30)})
        extra = set(re.findall(r'^\| (QA-S\d{2}) \|',
                               (QA / 'SOURCES.md').read_text(encoding='utf-8'), re.M))
        self.assertEqual(extra, {f'QA-S{i:02d}' for i in range(30, 34)})
        self.assertEqual(set(re.findall(r'^\| (XR-\d{2}) \|',
                         CROSS.read_text(encoding='utf-8'), re.M)),
                         {f'XR-{i:02d}' for i in range(1, 15)})
        for path in (QA / 'references').glob('*.md'):
            ids = set(re.findall(r'QA-S\d{2}', path.read_text(encoding='utf-8')))
            self.assertTrue(ids, path)
            self.assertTrue(ids <= sources | extra, (path, ids - sources - extra))

    def test_internal_links(self):
        for source in list(QA.rglob('*.md')) + [CAP / 'engineering-quality.md']:
            for dest in re.findall(r'\]\(([^)]+)\)', source.read_text(encoding='utf-8')):
                if '://' in dest:
                    continue
                path, _, frag = dest.partition('#')
                target = (source.parent / path).resolve() if path else source
                self.assertTrue(target.is_file(), (source, dest))
                if frag:
                    heads = re.findall(r'^#+\s+(.+)$', target.read_text(encoding='utf-8'), re.M)
                    slugs = [re.sub(r'[^\w -]', '', h.lower()).replace(' ', '-') for h in heads]
                    self.assertIn(frag, slugs, (source, dest))

    def test_shared_capability_index(self):
        index = (CAP / 'INDEX.md').read_text(encoding='utf-8')
        ids = re.findall(r'\[(CAP-[A-Z]\d{2}) —', index)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(set(PRIOR_CAPS) <= set(ids))
        additions = {f'CAP-B{i:02d}' for i in range(3, 9)}
        devops_additions = {f'CAP-R{i:02d}' for i in range(1, 10)}
        self.assertEqual(set(ids) - set(PRIOR_CAPS) - devops_additions, additions)
        records = (CAP / 'engineering-quality.md').read_text(encoding='utf-8')
        self.assertTrue(additions <= set(re.findall(r'^## (CAP-[A-Z]\d{2})$', records, re.M)))

    def test_registration_sources_and_unique_tasks(self):
        reg = json.loads((ROOT / 'skills/specialists.json').read_text(encoding='utf-8'))
        qa = next(s for s in reg['specialists'] if s['id'] == 'aipf-qa-engineering-quality')
        self.assertEqual(qa['tasks'], {'qa-' + mode: mode for mode in MODES})
        self.assertEqual(qa['chapters_any'], list(range(11, 22)))
        self.assertEqual(qa['tools'], [])
        self.assertNotIn('retrieval_script', qa)
        tasks = [task for item in reg['specialists'] for task in item['tasks']]
        self.assertEqual(len(tasks), len(set(tasks)))
        for path in [qa['skill'], *qa['knowledge_sources']]:
            self.assertTrue((ROOT / path).is_file(), path)


if __name__ == '__main__':
    unittest.main()
