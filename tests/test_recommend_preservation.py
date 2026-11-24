"""Preservation versus prohibition (SPECIALIST-UIUX-04) against the real catalog."""
import unittest

from scripts.recommend_design import IDENTITY_GROUPS, analyse_task, conflicts_with_task, recommend
from scripts.search_catalog import load_catalog


class PreservationVersusProhibitionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = load_catalog()
        cls.index = {row['catalog_id']: row for row in cls.rows}

    def roles(self, data):
        return [r['role'] for r in data['references']]

    def test_unchanged_established_appearance_is_protected(self):
        for task in (
            "Improve a help centre's article navigation and search discoverability without changing its "
            "established appearance.",
            'Refine the settings flow without altering its established look and feel.',
            'Improve the article navigation while keeping the current appearance.',
        ):
            with self.subTest(task=task):
                data = recommend(task, self.rows, platform='web')
                self.assertEqual(data['task_signals']['prohibited'], [])
                self.assertEqual(data['task_signals']['preserved_identity'], list(IDENTITY_GROUPS))
                self.assertEqual(data['selection_scope'], 'preserve_identity')
                self.assertTrue(set(self.roles(data)) <= {'usability_reference'})
        help_centre = recommend("Improve a help centre's article navigation and search discoverability without "
                                "changing its established appearance.", self.rows, platform='web')
        self.assertTrue(help_centre['references'])

    def test_qualified_prohibition_constrains_a_new_design(self):
        task = 'Create a monochrome inventory interface. Avoid gradients and saturated accent colors.'
        signals = analyse_task(task)
        self.assertEqual(signals['prohibited'], [('gradients',), ('saturated', 'accent', 'colors')])
        self.assertFalse(signals['preserved'])
        data = recommend(task, self.rows, platform='desktop')
        self.assertIn('palette', self.roles(data))
        self.assertEqual(data['task_signals']['preserved_identity'], [])
        for ref in data['references']:
            self.assertFalse(conflicts_with_task(self.index[ref['catalog_id']], signals), ref['catalog_id'])
        self.assertFalse(analyse_task('Design a new booking app. Avoid neon colours and heavy fonts.')['preserved'])

    def test_bare_identity_prohibition_still_preserves(self):
        signals = analyse_task('Redesign the settings page. Do not introduce new colours or fonts.')
        self.assertEqual(signals['preserved'], {'palette', 'typography'})
        self.assertEqual(analyse_task('Avoid changing the established brand.')['prohibited'], [])
        self.assertEqual(analyse_task('Avoid changing the established brand.')['preserved'], set(IDENTITY_GROUPS))

    def test_prohibition_survives_a_preservation_instruction_in_scope(self):
        task = 'Build a dashboard. Avoid glassmorphism and keep the current palette.'
        signals = analyse_task(task)
        self.assertEqual(signals['prohibited'], [('glassmorphism',)])
        self.assertEqual(signals['preserved'], {'palette'})
        data = recommend(task, self.rows, platform='web')
        for ref in data['references']:
            self.assertFalse(conflicts_with_task(self.index[ref['catalog_id']], signals), ref['catalog_id'])

    def test_negated_change_preserves_without_prohibiting(self):
        for task in ('Refine the settings page without changing its look and feel.',
                     'Refine the settings page without changing the existing appearance.',
                     'Do not alter the current theme.',
                     'Its brand colours and fonts must be preserved; improve the table layout.'):
            with self.subTest(task=task):
                signals = analyse_task(task)
                self.assertEqual(signals['prohibited'], [])
                self.assertEqual(signals['preserved'], set(IDENTITY_GROUPS))

    def test_preservation_and_request_apply_to_their_own_parts(self):
        signals = analyse_task('Keep our current palette and choose a new font pairing for the editorial blog.')
        self.assertEqual(signals['preserved'], {'palette'})
        self.assertEqual(signals['requested'], {'typography'})
        data = recommend('Keep our current palette and choose a new font pairing for the editorial blog.',
                         self.rows, platform='web')
        self.assertIn('typography', self.roles(data))
        self.assertNotIn('palette', self.roles(data))
        self.assertEqual(analyse_task('Keep the current light theme and component library.')['preserved'],
                         set(IDENTITY_GROUPS))
        self.assertEqual(analyse_task('Redesign the look and feel of the app.')['requested'], set(IDENTITY_GROUPS))
        kept = analyse_task('Keep the current theme and design system.')
        self.assertEqual(kept['preserved'], set(IDENTITY_GROUPS))
        self.assertFalse(kept['requested'])
        self.assertEqual(analyse_task('Create a new design system for the app.')['requested'], set(IDENTITY_GROUPS))

    def test_ordinary_ui_terms_are_not_negated_changes(self):
        for task in ('Avoid large touch targets in this new theme.', 'Do not use a touch-first theme.'):
            with self.subTest(task=task):
                signals = analyse_task(task)
                self.assertFalse(signals['preserved'])
                self.assertTrue(signals['prohibited'])

    def test_redesign_and_genuine_prohibition_remain_distinct(self):
        redesign = analyse_task('Redesign the dashboard with a new appearance and a fresh palette.')
        self.assertEqual(redesign['requested'], set(IDENTITY_GROUPS))
        self.assertFalse(redesign['preserved'])
        prohibition = analyse_task('Build a pricing page. Do not use red.')
        self.assertEqual(prohibition['prohibited'], [('red',)])
        self.assertFalse(prohibition['preserved'])


if __name__ == '__main__':
    unittest.main()
