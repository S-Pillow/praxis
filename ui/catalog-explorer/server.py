#!/usr/bin/env python3
"""Local-only read-only browser of the repository's real unified design catalog."""
from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter
from functools import lru_cache
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SEARCH = ROOT / 'scripts' / 'search_catalog.py'
CATALOG = ROOT / 'catalog' / 'entries'
PREFERRED = [
    'hallmark:theme:editorial',
    'uupm:colors:6',
    'open-design:design-systems:warm-editorial',
    'hallmark:theme:atelier',
    'uupm:styles:minimalism-and-swiss-style',
    'uupm:typography:4',
    'uupm:colors:7',
    'open-design:design-systems:trading-terminal',
    'uupm:ux-guidelines:28',
]


def load_data():
    """Never silently replace an unavailable full catalog with preview records."""
    if not SEARCH.is_file() or not CATALOG.is_dir():
        raise RuntimeError('Repository catalog or search script missing: run from an actual Specialist Suite checkout')
    spec = importlib.util.spec_from_file_location('aipf_catalog_search', SEARCH)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot import repository search script')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load_catalog(), mod.rank_entries


ROWS, RANKER = load_data()
INDEX = {row['catalog_id']: row for row in ROWS}
TYPES = frozenset({row['entry_type'] for row in ROWS})
COUNTS = dict(sorted(Counter(row['entry_type'] for row in ROWS).items()))
FIELDS = (
    'catalog_id', 'entry_type', 'original_name', 'description', 'design_tokens',
    'source_repo', 'source_url', 'source_ref', 'source_path_or_key',
    'redistribution_status', 'asset_license_status', 'evidence_status', 'specialist_use',
)


@lru_cache(maxsize=24)
def ranked_ids(query, category):
    """Full ranked match list, cached for the next-page request of the same search."""
    matches = RANKER(query, ROWS, limit=len(ROWS), entry_type=category or None)
    return tuple(row['catalog_id'] for _, row in matches)


def search(query='', category='', ids=None, limit=12, offset=0):
    """Return a bounded page, with actual match totals and no hidden truncation."""
    category = category if category in TYPES else ''
    query = query.strip()[:160]
    limit = max(1, min(int(limit), 48))
    offset = max(0, min(int(offset), len(ROWS)))

    if ids is not None:
        # Saved references have an explicit stable user order, no recommendations.
        chosen_ids = dict.fromkeys(part for part in ids.split(',') if part in INDEX)
        eligible = set(ranked_ids(query, category)) if query else None
        matched = [INDEX[key] for key in chosen_ids
                   if (not category or INDEX[key]['entry_type'] == category)
                   and (eligible is None or key in eligible)]
        page = matched[offset:offset + limit]
        total_matches = len(matched)
    elif query:
        keys = ranked_ids(query, category)
        total_matches = len(keys)
        page = [INDEX[key] for key in keys[offset:offset + limit]]
    else:
        # Default browsing is deterministic and exposes all entries via paging.
        preferred = [INDEX[key] for key in PREFERRED if key in INDEX and (not category or INDEX[key]['entry_type'] == category)]
        already = {x['catalog_id'] for x in preferred}
        all_ids = [x['catalog_id'] for x in preferred]
        all_ids.extend(x['catalog_id'] for x in ROWS if x['catalog_id'] not in already
                       and (not category or x['entry_type'] == category))
        total_matches = len(all_ids)
        page = [INDEX[key] for key in all_ids[offset:offset + limit]]

    return {
        'total': len(ROWS), 'dataset': 'full', 'matches': total_matches,
        'offset': offset, 'has_more': offset + len(page) < total_matches,
        'types': COUNTS,
        'results': [{key: row.get(key) for key in FIELDS} for row in page],
    }


class Handler(BaseHTTPRequestHandler):
    def send_bytes(self, data, content_type, status=200):
        if isinstance(data, str):
            data = data.encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Security-Policy', "default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; script-src 'self'; connect-src 'self'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        url = urlsplit(self.path)
        if url.path == '/api/catalog':
            params = parse_qs(url.query, keep_blank_values=True)
            try:
                limit = int(params.get('limit', ['12'])[0])
                offset = int(params.get('offset', ['0'])[0])
            except (ValueError, OverflowError):
                self.send_bytes('Invalid pagination', 'text/plain; charset=utf-8', 400)
                return
            result = search(
                query=params.get('q', [''])[0],
                category=params.get('type', [''])[0],
                ids=params['ids'][0] if 'ids' in params else None,
                limit=limit,
                offset=offset,
            )
            self.send_bytes(json.dumps(result, ensure_ascii=False), 'application/json; charset=utf-8')
            return
        files = {'/': 'index.html', '/index.html': 'index.html', '/styles.css': 'styles.css', '/app.js': 'app.js'}
        if url.path not in files:
            self.send_bytes('Not found', 'text/plain; charset=utf-8', 404)
            return
        path = HERE / files[url.path]
        content_type = 'text/html' if path.suffix == '.html' else 'text/css' if path.suffix == '.css' else 'text/javascript'
        self.send_bytes(path.read_bytes(), content_type + '; charset=utf-8')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--port', type=int, default=8765)
    args = p.parse_args()
    print(f'Full catalog: {len(ROWS)} source entries', flush=True)
    print(f'Local address: http://127.0.0.1:{args.port}', flush=True)
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
