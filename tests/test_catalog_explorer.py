"""Full-catalog contract and local HTTP checks for The Design Index."""
import importlib.util
import json
import threading
import unittest
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
SERVER = ROOT / 'ui' / 'catalog-explorer' / 'server.py'
spec = importlib.util.spec_from_file_location('aipf_design_index', SERVER)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class FullCatalogExplorerTests(unittest.TestCase):
    def test_real_catalog_and_no_preview_fallback(self):
        self.assertEqual(len(mod.ROWS), 5500)
        self.assertEqual(len(mod.INDEX), 5500)
        self.assertEqual(sum(mod.COUNTS.values()), 5500)
        self.assertEqual(mod.search()['dataset'], 'full')
        self.assertNotIn('sample-entries.json', SERVER.read_text())

    def test_all_catalog_records_are_browsable_without_omissions(self):
        ids = []
        for offset in range(0, len(mod.ROWS), 48):
            page = mod.search(limit=48, offset=offset)
            self.assertEqual(page['total'], 5500)
            self.assertEqual(page['matches'], 5500)
            ids.extend(row['catalog_id'] for row in page['results'])
            self.assertEqual(page['has_more'], offset + len(page['results']) < 5500)
        self.assertEqual(len(ids), 5500)
        self.assertEqual(len(set(ids)), 5500)
        self.assertFalse(mod.search(offset=5500)['has_more'])
        self.assertEqual(mod.search(offset=5500)['results'], [])

    def test_preferred_default_and_real_provenance(self):
        rows = mod.search(limit=12)['results']
        self.assertEqual(len(rows), 12)
        self.assertEqual(rows[0]['catalog_id'], 'hallmark:theme:editorial')
        for row in rows:
            self.assertIn(row['source_ref'], row['source_url'])
            self.assertNotEqual(row['redistribution_status'], 'approved_for_bundle')
            self.assertIn(row['evidence_status'], ('source_inspected', 'candidate_unverified', 'reported_by_upstream'))

    def test_search_matches_and_category_pagination(self):
        page = mod.search(query='financial dashboard', category='palette', limit=2)
        self.assertGreater(page['matches'], 0)
        self.assertTrue(all(row['entry_type'] == 'palette' for row in page['results']))
        all_palettes = mod.search(category='palette', limit=48)
        self.assertEqual(all_palettes['matches'], mod.COUNTS['palette'])
        other = mod.search(query='financial dashboard', category='palette', offset=2, limit=2)
        self.assertFalse(set(x['catalog_id'] for x in page['results']) & set(x['catalog_id'] for x in other['results']))

    def test_every_source_type_can_be_filtered(self):
        for entry_type, count in mod.COUNTS.items():
            with self.subTest(entry_type=entry_type):
                page = mod.search(category=entry_type, limit=8)
                self.assertEqual(page['matches'], count)
                self.assertTrue(page['results'])
                self.assertTrue(all(x['entry_type'] == entry_type for x in page['results']))

    def test_saved_records_beyond_original_eighty_limit(self):
        keys = list(mod.INDEX)[:150]
        ids = ','.join(keys)
        first = mod.search(ids=ids, limit=48)
        rest = mod.search(ids=ids, limit=48, offset=96)
        self.assertEqual(first['matches'], 150)
        self.assertEqual(rest['matches'], 150)
        self.assertEqual(first['results'][0]['catalog_id'], keys[0])
        self.assertEqual(rest['results'][0]['catalog_id'], keys[96])
        self.assertEqual(mod.search(ids='')['matches'], 0)
        self.assertEqual(mod.search(query='zzzzunlikely987654321')['matches'], 0)

    def test_design_tokens_preserved_in_relevant_details(self):
        row = mod.search(ids='uupm:colors:6')['results'][0]
        self.assertEqual(row['original_name'], 'Financial Dashboard')
        self.assertEqual(row['design_tokens']['Background'], '#020617')
        self.assertEqual(row['source_ref'], 'f2cc36555984fbfb08f1dca037da2467578f33d2')

    def test_http_local_api_and_static_assets(self):
        server = ThreadingHTTPServer(('127.0.0.1', 0), mod.Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        addr = f'http://127.0.0.1:{server.server_port}'
        try:
            with urlopen(addr + '/api/catalog?q=financial%20dashboard&type=palette&limit=3') as response:
                data = json.loads(response.read())
                self.assertEqual(response.headers.get('X-Content-Type-Options'), 'nosniff')
                self.assertEqual(data['dataset'], 'full')
                self.assertTrue(data['results'])
            for resource in ('/', '/index.html', '/app.js', '/styles.css'):
                with urlopen(addr + resource) as response:
                    self.assertEqual(response.status, 200)
                    self.assertGreater(len(response.read()), 500)
            with self.assertRaises(HTTPError) as ctx:
                urlopen(addr + '/private/path')
            self.assertEqual(ctx.exception.code, 404)
            with self.assertRaises(HTTPError) as ctx:
                urlopen(addr + '/api/catalog?offset=nope')
            self.assertEqual(ctx.exception.code, 400)
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=3)


if __name__ == '__main__':
    unittest.main()
