#!/usr/bin/env python3
"""Read-only integration helper; path selection and task judgment remain agent-owned."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
NON_SPECIALIST_TASKS = frozenset({"non-ui", "minor-ui"})


def verify_framework(root=ROOT):
    """Validate the complete canonical projection before consulting specialists."""
    manifest = json.loads((root / 'framework/projection-manifest.json').read_text(encoding="utf-8"))
    if manifest['framework_version'] != '8.10.1':
        raise ValueError('Unexpected framework version')
    full = hashlib.sha256()
    for entry in manifest['files']:
        data = (root / 'framework/references' / entry['path']).read_bytes()
        if hashlib.sha256(data).hexdigest() != entry['sha256']:
            raise ValueError('Framework reference integrity failure: ' + entry['path'])
        full.update(data)
    if full.hexdigest() != 'b11dfa2c12deb4d5b90833af4f10a02b5daf5e26d143469560b896fe9c85e0fd':
        raise ValueError('Canonical projection integrity failure')
    return manifest['framework_version']


def applicable_chapters(specialist):
    """Legacy singular chapter, or a nonempty list of alternative canonical paths."""
    if 'chapter' in specialist:
        if 'chapters_any' in specialist:
            raise ValueError('Ambiguous specialist chapter contract')
        paths = [specialist['chapter']]
    else:
        paths = specialist.get('chapters_any')
        if not isinstance(paths, list):
            raise ValueError('Specialist requires chapter or chapters_any')
    if not paths or any(type(p) is not int or p not in range(11, 22) for p in paths):
        raise ValueError('Invalid specialist chapter contract')
    return set(paths)


def resolve(task, chapters, root=ROOT):
    version = verify_framework(root)
    registry = json.loads((root / 'skills/specialists.json').read_text(encoding="utf-8"))
    registered = {name for specialist in registry['specialists'] for name in specialist['tasks']}
    if task not in registered | NON_SPECIALIST_TASKS:
        raise ValueError(f'Unknown task identifier: {task!r}; expected one of '
                         + ', '.join(sorted(registered | NON_SPECIALIST_TASKS)))
    matches = [s for s in registry['specialists'] if task in s['tasks']]
    result = {'framework_version': version, 'task': task, 'chapters': sorted(set(chapters)),
              'authority': 'advisory_only', 'specialists': []}
    if not matches:
        return dict(result, status='not_needed')
    if any(not applicable_chapters(s).intersection(chapters) for s in matches):
        return dict(result, status='recheck_framework_path')
    for s in matches:
        # A declared legacy lookup remains part of that specialist's availability
        # contract. An omitted lookup is valid for file-based guidance.
        accessible = (root / s['skill']).is_file()
        if 'retrieval_script' in s:
            accessible = accessible and (root / s['retrieval_script']).is_file()
        entry = {'id': s['id'], 'version': s['version'], 'skill': s['skill'],
                 'mode': s['tasks'][task]}
        if 'retrieval_script' in s:
            entry['retrieval_script'] = s['retrieval_script']
        entry['status'] = 'available' if accessible else 'unavailable'
        result['specialists'].append(entry)
    return dict(result, status='consult' if all(s['status']=='available' for s in result['specialists']) else 'specialist_unavailable')


def retrieve(result, request, platform=None, root=ROOT):
    """Run a declared legacy lookup unchanged; report absent lookup without execution."""
    if not request.strip():
        raise ValueError('A nonblank actual task is required')
    if result['status'] != 'consult':
        return result
    for s in result['specialists']:
        if 'retrieval_script' not in s:
            s['lookup_status'] = 'not_applicable'
            continue
        command = [sys.executable, str(root / s['retrieval_script']), request, '--mode', s['mode']]
        if platform:
            command.extend(['--platform', platform])
        try:
            proc = subprocess.run(command, cwd=root, capture_output=True, encoding="utf-8", timeout=45,
                                  env={**os.environ, "PYTHONIOENCODING": "utf-8"})
            if proc.returncode:
                raise ValueError(f'Lookup exited {proc.returncode}')
            payload = json.loads(proc.stdout)
            if not isinstance(payload, dict) or not isinstance(payload.get('references'), list):
                raise ValueError('Malformed lookup result')
            s['lookup'] = payload
            s['lookup_status'] = 'completed' if payload['references'] else 'empty'
        except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
            s['lookup_status'] = 'unavailable'
            s['lookup_error'] = str(exc)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--task', required=True, help='Agent-selected registered task type, or non-ui/minor-ui')
    parser.add_argument('--chapter', type=int, action='append', required=True, choices=range(11,22))
    parser.add_argument('--request', help='Actual task; omit to resolve only. Read the selected skill before retrieval.')
    parser.add_argument('--platform', choices=['web','mobile','desktop'])
    args = parser.parse_args()
    try:
        result = resolve(args.task, args.chapter)
        if args.request is not None:
            result = retrieve(result, args.request, args.platform)
    except (OSError, ValueError, KeyError) as exc:
        parser.exit(2, f'Praxis context unavailable: {exc}\n')
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 2 if result['status']=='recheck_framework_path' else 0


if __name__ == '__main__':
    raise SystemExit(main())
