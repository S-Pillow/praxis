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

    def test_redesign_and_genuine_prohibition_remain_distinct(self):
        redesign = analyse_task('Redesign the dashboard with a new appearance and a fresh palette.')
        self.assertEqual(redesign['requested'], set(IDENTITY_GROUPS))
        self.assertFalse(redesign['preserved'])
        prohibition = analyse_task('Build a pricing page. Do not use red.')
        self.assertEqual(prohibition['prohibited'], [('red',)])
        self.assertFalse(prohibition['preserved'])


if __name__ == '__main__':
    unittest.main()
