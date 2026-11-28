#!/usr/bin/env python3
"""Build and verify Praxis distribution archives from a committed Git snapshot."""
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'praxis/skills/praxis/references/release/'
TEMPLATES = {
    'plugin.json.in': 'praxis/plugin.json',
    'README.md.in': 'praxis/README.md',
    'SKILL.md.in': 'praxis/skills/praxis/SKILL.md',
    'RESOURCE-MAP.md.in': 'praxis/skills/praxis/references/RESOURCE-MAP.md',
    'openai.yaml': 'praxis/skills/praxis/agents/openai.yaml',
    'praxis-icon.svg': 'praxis/assets/praxis-icon.svg',
}
VERSION = re.compile(r'[0-9]+\.[0-9]+\.[0-9]+')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(root, *args):
    return subprocess.check_output(['git', *args], cwd=root, stderr=subprocess.PIPE)


def safe_path(path):
    p = PurePosixPath(path)
    if (not path or p.is_absolute() or '\\' in path or ':' in path or
            any(part in ('', '.', '..', '.git') for part in path.split('/')) or
            any(ord(c) < 32 for c in path)):
        raise ValueError('Unsafe archive path: ' + repr(path))
    return path


def blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()


def read_zip(data):
    """Reject unsafe/duplicate paths and nonregular members; validate CRC on read."""
    files = {}
    seen = set()
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        for info in archive.infolist():
            name = safe_path(info.filename.rstrip('/'))
            if info.orig_filename != info.filename or name.casefold() in seen:
                raise ValueError('Ambiguous archive member: ' + name)
            seen.add(name.casefold())
            kind = (info.external_attr >> 16) & 0o170000
            if info.is_dir():
                if kind not in (0, 0o040000):
                    raise ValueError('Invalid directory member: ' + name)
                continue
            if kind not in (0, 0o100000):
                raise ValueError('Nonregular archive member: ' + name)
            files[name] = archive.read(info)
    return files


def snapshot(root, ref):
    if not ref or ref.startswith('-'):
        raise ValueError('Provide a Git commit or ref, not an option')
    commit = git(root, 'rev-parse', '--verify', '--end-of-options', ref + '^{commit}').decode().strip()
    tree = git(root, 'rev-parse', commit + '^{tree}').decode().strip()
    expected = {}
    for item in git(root, 'ls-tree', '-r', '-z', commit).split(b'\0'):
        if not item:
            continue
        meta, raw_path = item.split(b'\t', 1)
        mode, kind, sha = meta.decode('ascii').split()
        path = safe_path(raw_path.decode('utf-8'))
        if mode != '100644' or kind != 'blob':
            raise ValueError('Unsupported Git entry: ' + path)
        expected[path] = sha
    # git archive can apply CRLF/export attributes, even when reading a commit.
    # Read the raw object database without filters, using one binary batch.
    request = ('\n'.join(expected.values()) + '\n').encode('ascii')
    stream = io.BytesIO(subprocess.check_output(
        ['git', 'cat-file', '--batch'], cwd=root, input=request, stderr=subprocess.PIPE))
    files = {}
    for path, sha in expected.items():
        header = stream.readline().decode('ascii').rstrip('\n').split()
        if len(header) != 3 or header[:2] != [sha, 'blob']:
            raise ValueError('Unexpected Git object header: ' + path)
        size = int(header[2])
        if size < 0:
            raise ValueError('Invalid Git object size: ' + path)
        data = stream.read(size)
        if len(data) != size or stream.read(1) != b'\n' or blob_sha(data) != sha:
            raise ValueError('Raw Git blob does not match the selected tree: ' + path)
        files[path] = data
    if stream.read(1):
        raise ValueError('Unexpected trailing Git object data')
    return commit, tree, files


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=True, sort_keys=True) + '\n').encode('utf-8')


def source_identity(files, commit, tree, version, state):
    framework = json.loads(files['framework/projection-manifest.json'])
    full = hashlib.sha256()
    for part in framework['files']:
        data = files['framework/references/' + part['path']]
        if digest(data) != part['sha256']:
            raise ValueError('Framework reference integrity mismatch: ' + part['path'])
        full.update(data)
    if full.hexdigest() != framework['projection_full_markdown_sha256']:
        raise ValueError('Framework projection integrity mismatch')
    registry = json.loads(files['skills/specialists.json'])['specialists']
    for specialist in registry:
        if specialist['skill'] not in files:
            raise ValueError('Missing registered specialist: ' + specialist['id'])
    catalog = [row['catalog_id'] for path, data in files.items()
               if path.startswith('catalog/entries/') and path.endswith('.json')
               and path != 'catalog/entries/starter.json' for row in json.loads(data)]
    starter = json.loads(files['catalog/entries/starter.json'])
    if len(set(catalog)) != len(catalog):
        raise ValueError('Duplicate production catalog IDs')
    if (framework['framework_version'], len(registry), len(catalog), len(starter)) != ('8.10.1', 5, 5500, 9):
        raise ValueError('Update distribution adapters for changed framework or inventory')
    return {
        'distribution': 'Praxis GitHub-distributed skills-only package',
        'package_state': state, 'plugin_version': version, 'source_release': 'v' + version,
        'source_repository': 'https://github.com/S-Pillow/praxis',
        'source_commit': commit, 'source_git_tree_sha1': tree,
        'source_root': 'references/release/', 'source_file_count': len(files),
        'source_uncompressed_bytes': sum(map(len, files.values())),
        'framework_version': framework['framework_version'],
        'framework_canonical_docx_sha256_recorded': framework['source_sha256'],
        'framework_full_projection_sha256_verified': full.hexdigest(),
        'framework_projection_manifest_sha256_verified': digest(files['framework/projection-manifest.json']),
        'specialists': [{k: s[k] for k in ('id', 'version', 'skill')} for s in registry],
        'catalog_unique_records': len(catalog), 'illustrative_starter_records': len(starter),
        'source_files': [{'path': p, 'bytes': len(data), 'git_blob_sha1': blob_sha(data),
                          'sha256': digest(data)} for p, data in sorted(files.items())],
    }


def archive_bytes(files):
    """Portable deterministic ZIP: no platform/zlib-dependent compression metadata."""
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_STORED) as archive:
        for path, data in sorted(files.items()):
            info = zipfile.ZipInfo(safe_path(path), date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    payload = stream.getvalue()
    if read_zip(payload) != files:
        raise ValueError('Generated ZIP inventory or bytes differ from expected files')
    return payload


def package(root, ref, candidate=False):
    commit, tree, files = snapshot(root, ref)
    claude = json.loads(files['.claude-plugin/plugin.json'])
    market = json.loads(files['.claude-plugin/marketplace.json'])
    version = claude['version']
    if (not VERSION.fullmatch(version) or claude['name'] != 'praxis' or market['name'] != 'praxis' or
            len(market['plugins']) != 1 or any(market['plugins'][0].get(k) != v for k, v in
            {'name': 'praxis', 'version': version, 'source': './'}.items())):
        raise ValueError('Claude marketplace and plugin identity mismatch')
    if not candidate:
        tag = 'refs/tags/v' + version
        if ref not in (tag, 'v' + version) or git(root, 'rev-parse', '--verify', tag + '^{commit}').decode().strip() != commit:
            raise ValueError('Release build requires the exact matching version tag; use --candidate for evaluation')
    state = 'candidate' if candidate else 'tag-bound (publication not asserted)'
    identity = source_identity(files, commit, tree, version, state)
    chatgpt = {PREFIX + p: data for p, data in files.items()}
    replacements = {'@VERSION@': version, '@COMMIT@': commit, '@FILE_COUNT@': str(len(files)), '@STATE@': state}
    for source, target in TEMPLATES.items():
        data = files['packaging/chatgpt/' + source]
        if source.endswith('.in'):
            rendered = data.decode('utf-8')
            for placeholder, value in replacements.items():
                rendered = rendered.replace(placeholder, value)
            if re.search(r'@[A-Z_]+@', rendered):
                raise ValueError('Unresolved package template: ' + source)
            data = rendered.encode('utf-8')
        chatgpt[target] = data
    manifest = json.loads(chatgpt['praxis/plugin.json'])
    if (manifest['$schema'] != 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json' or
            manifest['name'] != 'praxis' or manifest['version'] != version or
            'apps' in manifest or 'mcpServers' in manifest or
            'apps' in manifest.get('extensions', {}).get('com.openai', {})):
        raise ValueError('ChatGPT plugin identity or skills-only contract mismatch')
    interface = manifest['extensions']['com.openai']['interface']
    if len(interface['shortDescription']) > 30 or any('praxis/' + interface[k].removeprefix('./') not in chatgpt for k in ('logo', 'composerIcon')):
        raise ValueError('ChatGPT plugin listing or icon reference mismatch')
    chatgpt['praxis/skills/praxis/references/PACKAGE-IDENTITY.json'] = json_bytes(identity)
    suffix = '-candidate-' + commit[:12] if candidate else ''
    assets = {
        'Praxis_ChatGPT_Plugin_v' + version + suffix + '.zip': archive_bytes(chatgpt),
        'Praxis_Claude_v' + version + suffix + '.plugin': archive_bytes(files),
    }
    sums = ['# Praxis v' + version + ' | ' + state, '# Source commit: ' + commit, '# Git tree: ' + tree]
    sums.extend(digest(data) + '  ' + name for name, data in sorted(assets.items()))
    assets['SHA256SUMS.txt'] = ('\n'.join(sums) + '\n').encode('ascii')
    return identity, assets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ref', required=True, help='Exact release tag, or candidate Git ref with --candidate')
    parser.add_argument('--out', required=True, type=Path, help='New output directory (never overwrite)')
    parser.add_argument('--candidate', action='store_true', help='Build evaluation assets, not release-labeled files')
    args = parser.parse_args()
    try:
        identity, assets = package(ROOT, args.ref, args.candidate)
        args.out.mkdir(parents=True, exist_ok=False)
        for name, data in assets.items():
            with (args.out / name).open('xb') as target:
                target.write(data)
        print(assets['SHA256SUMS.txt'].decode('ascii'), end='')
        print('Verified source files:', identity['source_file_count'])
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError, zipfile.BadZipFile) as exc:
        parser.exit(2, 'Packaging failed: ' + str(exc) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
