"""Optional Chromium DOM regression for Q03–Q06; requires existing Playwright/browser.

Run: python tests/browser/catalog_quality.py --chromium /path/to/chromium
Uses original HTML/CSS/JS in an isolated document with a synthetic API response.
Does not establish real HTTP integration or native skill discovery.
"""
import argparse
from pathlib import Path
import json
from playwright.sync_api import sync_playwright

UI = Path(__file__).resolve().parents[2] / 'ui/catalog-explorer'


def run(chromium, no_sandbox=False):
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chromium, headless=True,
                                    args=['--no-sandbox'] if no_sandbox else [],
                                    chromium_sandbox=not no_sandbox)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})
        # Supply the exact local application source; use no external network.
        page.route('**/*', lambda route: route.abort())
        page.set_content((UI/'index.html').read_text(encoding='utf-8'))
        page.add_style_tag(content=(UI/'styles.css').read_text(encoding='utf-8'))
        page.evaluate('''() => { window.fetch = async () => ({ok:true,json:async()=>({
            total:5500, dataset:'full',matches:0,results:[],has_more:false,types:{theme:100}})}); }''')
        page.add_script_tag(content=(UI/'app.js').read_text(encoding='utf-8'))
        page.get_by_role('button', name='Saved references').click()
        task = page.locator('#designTask')
        task.fill('UI')
        task.press('/')
        assert task.input_value() == 'UI/', 'slash lost from textarea'
        assert task.evaluate('(e) => e === document.activeElement')
        # Readonly output is still an editable-target exclusion; do not jump.
        page.evaluate("$('briefOutput').hidden=false; $('briefOutput').focus()")
        page.keyboard.press('/')
        assert page.locator('#briefOutput').evaluate('(e) => e === document.activeElement')
        page.evaluate('''() => {const e=document.createElement('div'); e.contentEditable='true';
                       e.id='editableProbe';document.body.append(e);e.focus();}''')
        page.keyboard.press('/')
        assert page.locator('#editableProbe').inner_text() == '/'
        page.locator('#editableProbe').evaluate('(e) => e.remove()')
        page.locator('[data-type=theme]').click()
        page.locator('#searchInput').fill('editorial')
        page.locator('#clearSearch').click()
        assert page.locator('[data-view=saved]').get_attribute('aria-current') == 'page'
        assert page.locator('[data-type=theme]').get_attribute('aria-pressed') == 'true'
        assert page.locator('#searchInput').input_value() == ''
        # Global shortcut still works on noneditable controls.
        page.locator('[data-view=explore]').focus()
        page.keyboard.press('/')
        assert page.locator('#searchInput').evaluate('(e) => e === document.activeElement')
        page.locator('[data-view=explore]').click()
        page.locator('#searchInput').fill('editorial')
        page.locator('#clearSearch').click()
        assert page.locator('[data-view=explore]').get_attribute('aria-current') == 'page'
        assert page.locator('[data-type=theme]').get_attribute('aria-pressed') == 'true'
        print('PASS Q03 slash in task, readonly output, contenteditable; global shortcut retained')
        print('PASS Q04 clear search preserves Saved/Explore and category')
        for width in (320, 390, 720, 1280):
            page.set_viewport_size({'width':width,'height':844})
            page.evaluate("window.scrollTo({top:0,left:0,behavior:'instant'})")
            button = page.get_by_role('button', name='Saved references', exact=True)
            assert button.count() == 1
            assert page.get_by_role('button', name='Explore library', exact=True).count() == 1
            for count in ('0','12','5500'):
                page.locator('#savedCount').evaluate('(e,n)=>e.textContent=n',count)
                b, badge = button.evaluate('''e => [e, e.querySelector('#savedCount')].map(el => {
                    const {x,y,width,height}=el.getBoundingClientRect();return {x,y,width,height};})''')
                assert b and badge
                assert badge['x'] >= b['x']-0.5 and badge['y'] >= b['y']-0.5, (width,count,b,badge)
                assert badge['x']+badge['width'] <= b['x']+b['width']+0.5, (width,count,b,badge)
                assert badge['y']+badge['height'] <= b['y']+b['height']+0.5, (width,count,b,badge)
            print('PASS Q05/Q06 viewport',width,'counts 0/12/5500, navigation names',
                  json.dumps(page.locator('nav.nav').aria_snapshot()))
        browser.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--chromium', default=None)
    parser.add_argument('--no-sandbox', action='store_true',
                        help='Only for an isolated root-run browser test environment')
    args = parser.parse_args()
    run(args.chromium, args.no_sandbox)
