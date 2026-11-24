"""Experimental retrieval refinements (SPECIALIST-UIUX-03) against the real catalog."""
import unittest

from scripts.recommend_design import (
    IDENTITY_GROUPS, analyse_task, conflicts_with_task, query_terms, recommend,
)
from scripts.search_catalog import load_catalog

COLOR_ONLY = 'uupm:ux-guidelines:37'
KEYBOARD = 'uupm:ux-guidelines:41'
CONSISTENT_HELP = 'uupm:ux-guidelines:105'
MOBILE_FIRST_GUIDELINE = 'uupm:ux-guidelines:64'


class RecommendRefinementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = load_catalog()

    def ids(self, data):
        return [r['catalog_id'] for r in data['references']]

    def roles(self, data):
        return [r['role'] for r in data['references']]

    def test_reliance_limits_are_not_prohibitions(self):
        for task in (
            'Review status chips so they work without relying on colour alone',
            "Don't rely solely on color to show errors",
            'Do not use colour as the only indicator of state',
            'Make sure states are not conveyed by color only',
            'Status must never depend on colour alone',
            'No color-only status indicators',
        ):
            with self.subTest(task=task):
                signals = analyse_task(task)
                self.assertEqual(signals['prohibited'], [])
                self.assertFalse(signals['preserved'])
                self.assertTrue(any({'color', 'colour'} & set(item) for item in signals['reliance']))
                self.assertTrue({'color', 'colour'} & set(query_terms(task, signals)))

    def test_genuine_prohibitions_remain_effective(self):
        self.assertEqual(analyse_task('Do not use red')['prohibited'], [('red',)])
        mixed = analyse_task('Do not use gradients or colour alone')
        self.assertEqual(mixed['prohibited'], [('gradients',)])
        self.assertEqual(mixed['reliance'], [('colour',)])
        alternative = analyse_task('Do not use glassmorphism, only flat surfaces')
        self.assertEqual(alternative['prohibited'], [('glassmorphism',)])
        self.assertEqual(alternative['reliance'], [])
        task = 'Design a fitness tracking dashboard. Avoid dark mode and neon colours.'
        signals = analyse_task(task)
        self.assertIn(('neon', 'colours'), signals['prohibited'])
        data = recommend(task, self.rows, platform='web')
        self.assertTrue(data['references'])
        for ref in data['references']:
            entry = next(row for row in self.rows if row['catalog_id'] == ref['catalog_id'])
            self.assertFalse(conflicts_with_task(entry, signals), ref['catalog_id'])

    def test_not_colour_alone_keeps_colour_guidance_and_palette(self):
        for task in ('Critique the alert badges: can states be distinguished without relying on color alone?',
                     'Critique the alert badges: can states be distinguished without relying on colour alone?'):
            with self.subTest(task=task):
                data = recommend(task, self.rows, mode='critique', platform='web')
                self.assertIn(COLOR_ONLY, self.ids(data))
                self.assertEqual(data['task_signals']['prohibited'], [])
        build = recommend('Design an order status board for a warehouse team that works without relying '
                          'on colour alone', self.rows, platform='web')
        self.assertIn('palette', self.roles(build))
        self.assertEqual(build['task_signals']['preserved_identity'], [])
        self.assertEqual(build['task_signals']['not_sole_reliance'], ['colour'])

    def test_operational_critique_returns_guidelines_without_a_theme(self):
        data = recommend('Critique the checkout form usability and error recovery', self.rows,
                         mode='critique', platform='web')
        self.assertNotIn('design_reference', self.roles(data))
        self.assertGreaterEqual(len(data['references']), 2)
        self.assertEqual(set(self.roles(data)), {'usability_reference'})

    def test_style_critique_still_retrieves_a_visual_reference(self):
        data = recommend('Critique the visual style and typography of this editorial magazine landing page',
                         self.rows, mode='critique', platform='web')
        self.assertIn('design_reference', self.roles(data))

    def test_style_critique_rejects_a_single_word_theme_match(self):
        data = recommend('Critique the visual style of the trading blotter order table', self.rows,
                         mode='critique', platform='web')
        self.assertNotIn('hallmark:theme:sticker', self.ids(data))
        self.assertNotIn('design_reference', self.roles(data))

    def test_protected_identity_is_not_replaced_in_critique(self):
        data = recommend('Critique the visual style of our checkout; keep the existing brand colours and '
                         'typography', self.rows, mode='critique', platform='web')
        self.assertEqual(data['selection_scope'], 'preserve_identity')
        self.assertTrue(data['references'])
        self.assertEqual(set(self.roles(data)), {'usability_reference'})
        self.assertFalse(set(self.roles(data)) & set(IDENTITY_GROUPS))

    def test_platform_word_does_not_drive_matching(self):
        task = 'Design a web dashboard for warehouse inventory'
        self.assertNotIn('web', query_terms(task, analyse_task(task)))
        data = recommend(task, self.rows, platform='web')
        self.assertIn('uupm:colors:102', self.ids(data))
        self.assertIn('mobile', query_terms('Design a mobile banking app', analyse_task('Design a mobile banking app')))

    def test_help_and_support_interface_requests_remain_eligible(self):
        for task, term in (('Critique the help center article page and its search', 'help'),
                           ('Add a support chat widget to the account settings page', 'support'),
                           ('Add inline help tooltips to the billing form', 'help')):
            with self.subTest(task=task):
                self.assertIn(term, query_terms(task, analyse_task(task)))
        data = recommend('Critique the help center article page and its search', self.rows,
                         mode='critique', platform='web')
        self.assertIn(CONSISTENT_HELP, self.ids(data))

    def test_incidental_help_and_support_words_are_not_evidence(self):
        for task in ('Refine the desktop help-desk console so support agents can scan queues',
                     'Make sure the layout works in browsers that support container queries',
                     'Help me tidy the settings page spacing'):
            with self.subTest(task=task):
                found = set(query_terms(task, analyse_task(task)))
                self.assertFalse(found & {'help', 'support'})

    def test_hyphenated_compounds_need_the_phrase(self):
        first_run = recommend('Critique the first-run onboarding of a meditation app', self.rows,
                              mode='critique', platform='web')
        self.assertNotIn(MOBILE_FIRST_GUIDELINE, self.ids(first_run))
        task = 'Build a mobile-first checkout with large touch targets'
        signals = analyse_task(task)
        self.assertEqual(signals['priority'], 'mobile')
        self.assertEqual(signals['compounds'], {})
        self.assertTrue({'mobile', 'first'} <= set(query_terms(task, signals)))

    def test_ambiguous_ui_request_is_not_backend_only(self):
        data = recommend('Improve the support queue so agents can find tickets faster', self.rows,
                         platform='web')
        self.assertNotEqual(data['selection_scope'], 'non_visual_task')
        self.assertTrue(data['references'])

    def test_existing_successful_retrieval_remains(self):
        data = recommend('Audit keyboard navigation and focus order of the settings page', self.rows,
                         mode='audit', platform='web')
        self.assertEqual(self.ids(data)[0], KEYBOARD)
        backend = recommend("Rename the CSV export column header in the backend serializer.", self.rows)
        self.assertEqual(backend['selection_scope'], 'non_visual_task')
        self.assertEqual(backend['references'], [])


if __name__ == '__main__':
    unittest.main()
