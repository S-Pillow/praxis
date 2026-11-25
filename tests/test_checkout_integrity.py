"""Regression for raw-byte integrity under Git CRLF checkout conversion."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from scripts.praxis_context import verify_framework

ROOT = Path(__file__).resolve().parents[1]


class CheckoutIntegrityTests(unittest.TestCase):
    def test_autocrlf_preserves_canonical_bytes(self):
        paths = [ROOT / 'framework/projection-manifest.json']
        for pattern in ('framework/references/**/*', 'catalog/entries/*.json',
                        'research/evaluations/retrieval-benchmark/**/*',
                        'scripts/recommend_design.py', 'scripts/search_catalog.py'):
            paths.extend(p for p in ROOT.glob(pattern) if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc')
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            def git(*args):
                subprocess.run(['git', '-c', 'core.autocrlf=true', *args], cwd=repo,
                               check=True, capture_output=True)
            git('init', '-q')
            shutil.copyfile(ROOT / '.gitattributes', repo / '.gitattributes')
            for source in paths:
                target = repo / source.relative_to(ROOT)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
            control = repo / 'control.txt'
            control.write_bytes(b'control\n')
            git('add', '--all')
            for source in paths:
                (repo / source.relative_to(ROOT)).unlink()
            control.unlink()
            git('checkout-index', '-a', '-f')
            self.assertEqual(control.read_bytes(), b'control\r\n')
            self.assertEqual(verify_framework(repo), '8.10.1')
            for source in paths[1:]:
                with self.subTest(path=source.relative_to(ROOT)):
                    self.assertEqual((repo / source.relative_to(ROOT)).read_bytes(), source.read_bytes())
