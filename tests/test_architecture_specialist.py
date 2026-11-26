"""Architecture candidate: isolated mechanism, local knowledge, and real checkout tests."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch, Mock
from scripts import praxis_context as ctx

ROOT = Path(__file__).resolve().parents[1]
ARCH = ROOT/'skills/architecture'
CAP = ROOT/'knowledge/capabilities'
REGISTRY = ROOT/'skills/specialists.json'

class ArchitectureMechanismTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for rel in ['skills/aipf-ui-ux/SKILL.md','scripts/recommend_design.py','skills/architecture/SKILL.md']:
            p=self.root/rel; p.parent.mkdir(parents=True,exist_ok=True); p.write_text('test double')
        shutil.copy(REGISTRY,self.root/'skills/specialists.json')
        self.addCleanup(patch.stopall)
        patch.object(ctx,'verify_framework',return_value='8.10.1').start()

    def resolve(self,task,chapters): return ctx.resolve(task,chapters,self.root)

    def test_modes_and_alternative_paths(self):
        for mode in ('design','evolve','critique'):
            for chapters in ([11],[12],[11,12,14]):
                with self.subTest(mode=mode,chapters=chapters):
                    r=self.resolve('architecture-'+mode,chapters)
                    self.assertEqual(r['status'],'consult')
                    self.assertEqual(r['authority'],'advisory_only')
                    self.assertEqual(r['specialists'],[dict(id='aipf-architecture',version='0.1',skill='skills/architecture/SKILL.md',mode=mode,status='available')])

    def test_wrong_paths_and_no_execution(self):
        with patch.object(ctx.subprocess,'run') as run:
            for chapters in ([14],[13,15],[]):
                r=self.resolve('architecture-design',chapters)
                self.assertEqual(r['status'],'recheck_framework_path')
                self.assertEqual(ctx.retrieve(r,'request',root=self.root),r)
            run.assert_not_called()

    def test_no_lookup_for_architecture(self):
        with patch.object(ctx.subprocess,'run') as run:
            r=self.resolve('architecture-evolve',[12])
            self.assertNotIn('lookup_status',r['specialists'][0])
            s=ctx.retrieve(r,'request',platform='web',root=self.root)['specialists'][0]
            self.assertEqual(s['lookup_status'],'not_applicable')
            self.assertNotIn('lookup',s)
            self.assertNotIn('retrieval_script',s)
            run.assert_not_called()

    def test_missing_architecture_skill(self):
        (self.root/'skills/architecture/SKILL.md').unlink()
        with patch.object(ctx.subprocess,'run') as run:
            r=self.resolve('architecture-design',[11]); self.assertEqual(r['status'],'specialist_unavailable')
            self.assertEqual(ctx.retrieve(r,'request',root=self.root),r)
            run.assert_not_called()

    def test_skip_and_unknown(self):
        with patch.object(ctx.subprocess,'run') as run:
            for task in ('non-ui','minor-ui'):
                r=self.resolve(task,[11,12,14]); self.assertEqual(r['status'],'not_needed')
                self.assertEqual(ctx.retrieve(r,'request',root=self.root),r)
            with self.assertRaises(ValueError): self.resolve('unknown',[12])
            run.assert_not_called()

    def test_blank_request(self):
        with patch.object(ctx.subprocess,'run') as run:
            with self.assertRaises(ValueError): ctx.retrieve(self.resolve('architecture-design',[11]),' ',root=self.root)
            run.assert_not_called()

    def test_ui_legacy_result(self):
        r=self.resolve('ui-build',[12,14]); self.assertEqual(r['status'],'consult')
        self.assertEqual(r['specialists'],[dict(id='aipf-ui-ux',version='0.3',skill='skills/aipf-ui-ux/SKILL.md',mode='build',retrieval_script='scripts/recommend_design.py',status='available')])
        self.assertEqual(self.resolve('ui-build',[12])['status'],'recheck_framework_path')

    def test_legacy_lookup_outcomes(self):
        for code,out,want in [(0,'{"references":[{"id":"x"}]}','completed'),(0,'{"references":[]}','empty'),(1,'','unavailable'),(0,'invalid','unavailable'),(0,'{"references":null}','unavailable')]:
            with self.subTest(want=want,out=out),patch.object(ctx.subprocess,'run',return_value=Mock(returncode=code,stdout=out)) as run:
                r=ctx.retrieve(self.resolve('ui-audit',[14]),'task','web',self.root)['specialists'][0]
                self.assertEqual(r['lookup_status'],want)
                self.assertEqual(run.call_args.args[0],[ctx.sys.executable,str(self.root/'scripts/recommend_design.py'),'task','--mode','audit','--platform','web'])
                self.assertEqual(run.call_args.kwargs['cwd'],self.root)
                self.assertEqual('lookup' in r,want!='unavailable')

    def test_legacy_lookup_timeout(self):
        with patch.object(ctx.subprocess,'run',side_effect=subprocess.TimeoutExpired('lookup',45)):
            self.assertEqual(ctx.retrieve(self.resolve('ui-build',[14]),'task',root=self.root)['specialists'][0]['lookup_status'],'unavailable')

    def test_missing_legacy_script_still_unavailable(self):
        (self.root/'scripts/recommend_design.py').unlink()
        self.assertEqual(self.resolve('ui-build',[14])['status'],'specialist_unavailable')

    def test_invalid_chapter_contract(self):
        for spec in ({},{'chapter':14,'chapters_any':[11]}, {'chapters_any':[]},{'chapters_any':'11'},{'chapters_any':[True]},{'chapters_any':[99]},{'chapter':'14'}):
            with self.subTest(spec=spec), self.assertRaises(ValueError): ctx.applicable_chapters(spec)

class ArchitectureKnowledgeTests(unittest.TestCase):
    def test_registry_paths(self):
        registry=json.loads(REGISTRY.read_text(encoding="utf-8"))
        a=next(s for s in registry['specialists'] if s['id']=='aipf-architecture')
        self.assertNotIn('retrieval_script',a)
        for p in [a['skill'],*a['knowledge_sources']]: self.assertTrue((ROOT/p).is_file(),p)

    def check_links(self,folder,local_only=True):
        for f in folder.rglob('*.md'):
            for dest in re.findall(r'\]\(([^)]+)\)',f.read_text(encoding="utf-8")):
                if '://' in dest: continue
                path,_,frag=dest.partition('#'); target=(f.parent/path).resolve() if path else f
                if local_only and not any(target.is_relative_to(base) for base in (ARCH,CAP)):
                    continue  # actual project-source links checked on full checkout below
                self.assertTrue(target.is_file(),(f,dest))
                if frag:
                    headings=re.findall(r'^#+\s+(.+)$',target.read_text(encoding="utf-8"),re.M)
                    self.assertIn(frag,[re.sub(r'[^\w -]','',s.lower()).replace(' ','-') for s in headings],(f,dest))

    def test_internal_navigation(self): self.check_links(ARCH); self.check_links(CAP)

    def test_cards_index_unique_and_complete(self):
        ids=[]
        for f in (ARCH/'references').glob('*.md'):
            t=f.read_text(encoding="utf-8"); cards=re.split(r'^## (A\d+)\n',t,flags=re.M)
            for id,body in zip(cards[1::2],cards[2::2]):
                ids.append(id)
                for field in ('Decision','Use when','Disqualifiers / stop','Alternatives and consequences','Implementation implications','Verification / revisit','Provenance','Maintenance'):
                    self.assertIn('**'+field+':**',body,(id,field))
        self.assertTrue(ids); self.assertEqual(len(ids),len(set(ids)))
        self.assertEqual(set(ids),set(re.findall(r'\[(A\d+) —', (ARCH/'INDEX.md').read_text(encoding="utf-8"))))

    def test_capability_index_unique_and_complete(self):
        ids=[]
        for f in CAP.glob('*.md'):
            cards=re.split(r'^## (CAP-[A-Z]\d+)\n',f.read_text(encoding="utf-8"),flags=re.M)
            for id,body in zip(cards[1::2],cards[2::2]):
                ids.append(id)
                for field in ('Name','Tags','Candidate use','Constraints to check','Official documentation pointer(s)','Pricing / terms / licensing pointer(s)','Observation / verification state','Origin and redistribution'):
                    self.assertIn('**'+field+':**',body,(id,field))
        self.assertTrue(ids); self.assertEqual(len(ids),len(set(ids)))
        self.assertEqual(set(ids),set(re.findall(r'\[(CAP-[A-Z]\d+) —',(CAP/'INDEX.md').read_text(encoding="utf-8"))))

class ArchitectureIntegratedTests(unittest.TestCase):
    def test_project_source_navigation(self):
        checker=ArchitectureKnowledgeTests()
        checker.check_links(ARCH,local_only=False)
        checker.check_links(CAP,local_only=False)

    def test_actual_framework_and_registered_architecture(self):
        self.assertEqual(ctx.verify_framework(ROOT),'8.10.1')
        for chapter in (11,12):
            r=ctx.resolve('architecture-design',[chapter],ROOT)
            self.assertEqual(r['status'],'consult')
            with patch.object(ctx.subprocess,'run') as run:
                self.assertEqual(ctx.retrieve(r,'actual task',root=ROOT)['specialists'][0]['lookup_status'],'not_applicable')
                run.assert_not_called()

if __name__=='__main__': unittest.main()
