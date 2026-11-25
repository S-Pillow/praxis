"""Targeted portability regression checks; actual Windows suite is a separate gate."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from scripts import retrieval_benchmark as benchmark
from scripts.praxis_context import resolve, retrieve


class PraxisPortabilityTests(unittest.TestCase):
    def test_pinned_replay_requires_no_symlink_privilege(self):
        with patch.object(Path, 'symlink_to', side_effect=OSError('WinError 1314')) as link:
            with benchmark.Implementation('v0.2') as impl:
                self.assertFalse((impl.workdir/'catalog').is_symlink())
                self.assertEqual(benchmark.catalog_identity(impl.workdir), benchmark.catalog_identity())
                for name, (path, _) in benchmark.TOOLS.items():
                    self.assertEqual(benchmark.sha256_file(impl.workdir/path), benchmark.sha256_file(benchmark.REFERENCE_V02/Path(path).name))
                workspace = impl.workdir
            self.assertFalse(workspace.exists())
            link.assert_not_called()

    def test_utf8_and_crlf_transcript_contract(self):
        case = {'tool':'recommend','query':'test','args':[]}
        text = '{"references": [], "note": "café — \\r\\n"}\n'
        proc = subprocess.CompletedProcess([], 0, text.replace('\n','\r\n').encode('utf-8'), b'')
        with patch.object(benchmark.subprocess, 'run', return_value=proc) as run:
            result = benchmark.run_command(case)
        self.assertEqual(result['stdout'], text)
        self.assertEqual(run.call_args.kwargs['env']['PYTHONIOENCODING'], 'utf-8')
        self.assertEqual(json.loads(result['stdout'])['note'], 'café — \r\n')
        self.assertEqual(benchmark.reproduction_differences({'raw_stdout':{'case':text}}, {'raw_stdout':{'case':text.replace('café','changed')}}), [('raw_stdout','case')])

    def test_helper_utf8_transport(self):
        result = resolve('ui-build',[11,14])
        proc = subprocess.CompletedProcess([],0,json.dumps({'references':[{'name':'café —'}]},ensure_ascii=False),'')
        with patch('scripts.praxis_context.subprocess.run',return_value=proc) as run:
            actual = retrieve(result,'Build a UI')
        self.assertEqual(actual['specialists'][0]['lookup']['references'][0]['name'],'café —')
        self.assertEqual(run.call_args.kwargs['encoding'],'utf-8')
        self.assertEqual(run.call_args.kwargs['env']['PYTHONIOENCODING'],'utf-8')
