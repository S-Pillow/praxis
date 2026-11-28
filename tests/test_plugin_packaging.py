"""Package qualification: real Git snapshots and extracted helper execution."""
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

from scripts import package_plugins as p

ROOT = Path(__file__).resolve().parents[1]
BASE_TREES = {
    'framework': '96a9afea7d74aee6157ab838fcb9255a65af99f3',
    'catalog': '28386249deaf49a4877d1dd533d7a894426bb057',
    'knowledge': '08acb62f03ea4a1858e038218dffab8293966fd4',
    'research': 'e876719e2ddcd4666c37df4347eac5587a43a2a2',
    'skills/specialists.json': 'd612f41ca025915060acba0aa34410288bdc01de',
    'docs/PRD.md': '36e7805c78d800e11220002d4e40002f66996a3c',
}
BASE_SKILLS = {
    'aipf-ui-ux': '84a15c2dd5ed6ff0397ab36fcff404cc174711fa',
    'architecture': 'ff11535640d893eef5b90b27636b5de90b8fa117',
    'devops-reliability': '29fc332c369fb3278f8728c69736fcc85406f0d1',
    'praxis': '2014914e9b68e6c8be2fc54421c3feb868f9cd0a',
    'qa-engineering-quality': 'b96f8b14b524124b966267bf52a7ad7a0270ef33',
    'security-privacy': '18fcf3dc2073b3da74cf85dc1cf2e3e7af74236f',
}


class ArchiveSafety(unittest.TestCase):
    def test_path_guard(self):
        for name in ('../x', '/x', 'a/../b', 'a\\b', 'C:/x', '.git/config', 'a//b', 'a\0b'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                p.safe_path(name)

    def test_duplicate_casefold_and_symlink_members_rejected(self):
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, 'w') as z:
            z.writestr('A.txt', 'first')
            z.writestr('a.txt', 'second')
        with self.assertRaises(ValueError):
            p.read_zip(stream.getvalue())
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, 'w') as z:
            entry = zipfile.ZipInfo('link')
            entry.create_system = 3
            entry.external_attr = 0o120777 << 16
            z.writestr(entry, '../target')
        with self.assertRaises(ValueError):
            p.read_zip(stream.getvalue())

    def test_corrupt_member_rejected(self):
        data = p.archive_bytes({'data': b'original payload'})
        corrupted = data.replace(b'original payload', b'altered! payload', 1)
        self.assertNotEqual(data, corrupted)
        with self.assertRaises(zipfile.BadZipFile):
            p.read_zip(corrupted)

    def test_snapshot_excludes_dirty_and_untracked_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            p.git(repo, 'init', '-q')
            (repo / 'tracked.txt').write_bytes(b'approved\n')
            p.git(repo, 'add', 'tracked.txt')
            p.git(repo, '-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'fixture')
            (repo / 'tracked.txt').write_bytes(b'dirty\n')
            (repo / 'untracked.txt').write_bytes(b'not approved\n')
            _, _, files = p.snapshot(repo, 'HEAD')
            self.assertEqual(files, {'tracked.txt': b'approved\n'})


class CommittedPackageQualification(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            top = Path(p.git(ROOT, 'rev-parse', '--show-toplevel').decode().strip()).resolve()
        except subprocess.CalledProcessError:
            raise unittest.SkipTest('Commit-bound package tests require the Git checkout, not an extracted source snapshot')
        if top != ROOT:
            raise unittest.SkipTest('Commit-bound package tests require the Praxis Git checkout')
        cls.identity, cls.assets = p.package(ROOT, 'HEAD', candidate=True)
        cls.commit, cls.tree, cls.source = p.snapshot(ROOT, 'HEAD')
        cls.claude_name = next(k for k in cls.assets if k.endswith('.plugin'))
        cls.chatgpt_name = next(k for k in cls.assets if k.endswith('.zip'))
        cls.claude = p.read_zip(cls.assets[cls.claude_name])
        cls.chatgpt = p.read_zip(cls.assets[cls.chatgpt_name])

    def test_protected_source_and_skill_bodies(self):
        for path, sha in BASE_TREES.items():
            with self.subTest(path=path):
                self.assertEqual(p.git(ROOT, 'rev-parse', self.commit + ':' + path).decode().strip(), sha)
        for skill, sha in BASE_SKILLS.items():
            data = self.source['skills/' + skill + '/SKILL.md']
            lines = data.splitlines(keepends=True)
            notes = [i for i, line in enumerate(lines) if line.startswith(b'> **Praxis resource root:**')]
            self.assertEqual(len(notes), 1, skill)
            i = notes[0]
            self.assertEqual(lines[i+1], b'\n')
            self.assertEqual(p.blob_sha(b''.join(lines[:i] + lines[i+2:])), sha, skill)

    def test_exact_archive_inventory_and_identity(self):
        self.assertEqual(self.claude, self.source)
        self.assertEqual({k[len(p.PREFIX):]: v for k, v in self.chatgpt.items() if k.startswith(p.PREFIX)}, self.source)
        meta = json.loads(self.chatgpt['praxis/skills/praxis/references/PACKAGE-IDENTITY.json'])
        self.assertEqual(meta, self.identity)
        self.assertEqual(meta['source_commit'], self.commit)
        self.assertEqual(meta['source_git_tree_sha1'], self.tree)
        self.assertEqual(meta['source_file_count'], len(self.source))
        self.assertEqual(len(meta['source_files']), len(self.source))
        for row in meta['source_files']:
            data = self.source[row['path']]
            self.assertEqual((row['bytes'], row['git_blob_sha1'], row['sha256']), (len(data), p.blob_sha(data), p.digest(data)))
        self.assertEqual(meta['catalog_unique_records'], 5500)
        self.assertEqual(meta['illustrative_starter_records'], 9)
        self.assertEqual(meta['framework_version'], '8.10.1')
        self.assertEqual(len(meta['specialists']), 5)

    def test_two_builds_match_and_checksums_verify(self):
        _, again = p.package(ROOT, self.commit, candidate=True)
        self.assertEqual(self.assets, again)
        for name in (self.claude_name, self.chatgpt_name):
            self.assertIn('-candidate-' + self.commit[:12], name)
            self.assertIn(p.digest(self.assets[name]) + '  ' + name, self.assets['SHA256SUMS.txt'].decode())
            with zipfile.ZipFile(io.BytesIO(self.assets[name])) as z:
                self.assertEqual(z.namelist(), sorted(z.namelist()))
                self.assertTrue(all(i.date_time == (1980, 1, 1, 0, 0, 0) and i.compress_type == zipfile.ZIP_STORED for i in z.infolist()))

    def test_manifest_versions_and_discovery_boundary(self):
        claude = json.loads(self.claude['.claude-plugin/plugin.json'])
        market = json.loads(self.claude['.claude-plugin/marketplace.json'])
        chat = json.loads(self.chatgpt['praxis/plugin.json'])
        self.assertEqual(claude['version'], '1.4.1')
        self.assertEqual(claude['version'], market['plugins'][0]['version'])
        self.assertEqual(claude['version'], chat['version'])
        self.assertEqual(market['plugins'][0]['source'], './')
        self.assertEqual({k for k in self.chatgpt if k.startswith('praxis/skills/') and len(k.split('/')) == 4 and k.endswith('/SKILL.md')}, {'praxis/skills/praxis/SKILL.md'})
        self.assertEqual(len([k for k in self.claude if k.startswith('skills/') and len(k.split('/')) == 3 and k.endswith('/SKILL.md')]), 6)
        for name in ('praxis/mcp.json', 'praxis/.app.json'):
            self.assertNotIn(name, self.chatgpt)
        self.assertIn(b'allow_implicit_invocation: false', self.chatgpt['praxis/skills/praxis/agents/openai.yaml'])
        self.assertIn(self.commit.encode(), self.chatgpt['praxis/skills/praxis/SKILL.md'])

    def test_untagged_commit_not_a_release(self):
        with self.assertRaisesRegex(ValueError, 'exact matching version tag'):
            p.package(ROOT, self.commit)

    def test_framework_and_real_lookup_from_both_extracted_roots(self):
        observations = []
        for name, files, prefix in [('Claude', self.claude, ''), ('ChatGPT', self.chatgpt, p.PREFIX)]:
            with self.subTest(host=name), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                for path, data in files.items():
                    target = root / path
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(data)
                checkout = root / prefix
                result = subprocess.run([sys.executable, str(checkout / 'scripts/praxis_context.py'), '--task', 'ui-build', '--chapter', '14', '--request', 'Build a financial dashboard with clear data tables', '--platform', 'web'], cwd=checkout, capture_output=True, check=True, timeout=90)
                payload = json.loads(result.stdout)
                self.assertEqual(payload['framework_version'], '8.10.1')
                self.assertEqual(payload['status'], 'consult')
                specialist = payload['specialists'][0]
                self.assertEqual(specialist['lookup_status'], 'completed')
                refs = specialist['lookup']['references']
                self.assertTrue(0 < len(refs) <= 3)
                observations.append([x['catalog_id'] for x in refs])
        self.assertEqual(observations[0], observations[1])
        print('Packaged lookup (both source roots):', observations[0])


if __name__ == '__main__':
    unittest.main()
