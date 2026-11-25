import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
from scripts.praxis_context import ROOT, resolve, retrieve, verify_framework


class PraxisIntegrationTests(unittest.TestCase):
    def test_complete_canonical_projection(self):
        self.assertEqual(verify_framework(), '8.10.1')
        manifest = json.loads((ROOT/'framework/projection-manifest.json').read_text(encoding="utf-8"))
        self.assertEqual(len(manifest['files']), 22)
        self.assertEqual([e['first_line'] for e in manifest['files']][0], 1)
        for previous, following in zip(manifest['files'], manifest['files'][1:]):
            self.assertEqual(previous['last_line']+1, following['first_line'])

    def test_new_application_ui(self):
        result = resolve('ui-build', [11,14])
        self.assertEqual(result['status'], 'consult')
        self.assertEqual(result['specialists'][0]['mode'], 'build')
        self.assertEqual(result['specialists'][0]['version'], '0.3')

    def test_existing_redesign(self):
        self.assertEqual(resolve('ui-build', [12,14])['specialists'][0]['id'], 'aipf-ui-ux')

    def test_critique_and_audit_distinct(self):
        for task,mode in [('ui-critique','critique'),('ui-audit','audit')]:
            self.assertEqual(resolve(task,[14])['specialists'][0]['mode'], mode)

    def test_minor_and_backend_skip_retrieval(self):
        with patch('scripts.praxis_context.subprocess.run') as runner:
            for task, chapters in [('minor-ui',[12,14]),('non-ui',[12])]:
                result = retrieve(resolve(task,chapters),'A task')
                self.assertEqual(result['status'],'not_needed')
                self.assertEqual(result['specialists'],[])
            runner.assert_not_called()

    def test_requires_canonical_path(self):
        self.assertEqual(resolve('ui-build',[11])['status'],'recheck_framework_path')

    def test_actual_lookup(self):
        result = retrieve(resolve('ui-build',[11,14]),'Build a financial dashboard with readable tables','web')
        lookup = result['specialists'][0]
        self.assertEqual(lookup['lookup_status'],'completed')
        self.assertEqual(lookup['lookup']['catalog_records_searched'],5500)
        self.assertLessEqual(len(lookup['lookup']['references']),3)
        self.assertTrue(all(r['source_ref'] in r['source_url'] for r in lookup['lookup']['references']))

    def test_unavailable_skill_and_corrupt_core_are_different(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            shutil.copytree(ROOT/'framework',root/'framework')
            (root/'skills').mkdir()
            shutil.copy(ROOT/'skills/specialists.json', root/'skills/specialists.json')
            self.assertEqual(resolve('ui-build',[14],root)['status'],'specialist_unavailable')
            (root/'framework/references/paths/14-ui.md').write_text('corrupt')
            with self.assertRaises(ValueError):
                resolve('ui-build',[14],root)

    def test_runner_unavailable(self):
        with patch('scripts.praxis_context.subprocess.run', side_effect=OSError('not available')):
            result=retrieve(resolve('ui-audit',[14]),'Audit keyboard focus')
        self.assertEqual(result['specialists'][0]['lookup_status'],'unavailable')
        self.assertNotIn('lookup',result['specialists'][0])

    def test_entrypoint_and_role_boundaries(self):
        entry=(ROOT/'skills/praxis/SKILL.md').read_text(encoding="utf-8")
        adapter=(ROOT/'.agents/skills/praxis/SKILL.md').read_text(encoding="utf-8")
        self.assertIn('skills/praxis/SKILL.md',adapter)
        for path in ('overview.md','how-to-use.md','core/sections-1-4.md','core/sections-5-10.md'):
            self.assertIn('framework/references/'+path,entry)
        self.assertIn('transport only the authorized Builder Payload',entry)
        self.assertIn('no artificial transport',entry)
        self.assertIn('Chapter 14 integration point',entry)


if __name__ == '__main__':
    unittest.main()
