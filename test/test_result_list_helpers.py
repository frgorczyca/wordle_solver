import unittest
from solvers.game_manager import LetterStates
from solvers.result_list_helpers import update_taboo_list, update_correct_list, update_misplaced_list

class GameManagerTest(unittest.TestCase):
    def test_update_taboo_list(self):
        result = [('p', LetterStates.WRONG),
            ('h', LetterStates.MISPLACED),
            ('o', LetterStates.MISPLACED),
            ('t', LetterStates.WRONG),
            ('o', LetterStates.WRONG)]

        taboo_list = []

        taboo_list = update_taboo_list(result, taboo_list)
        self.assertEqual(taboo_list, ['p','t'])

        result = [('s', LetterStates.WRONG),
            ('a', LetterStates.MISPLACED),
            ('s', LetterStates.WRONG),
            ('s', LetterStates.PROPER),
            ('y', LetterStates.WRONG)]

        taboo_list = update_taboo_list(result, taboo_list)
        self.assertEqual(taboo_list, ['p','t','y'])

    def test_update_misplaced_list(self):
        result = [('p', LetterStates.WRONG),
            ('h', LetterStates.MISPLACED),
            ('o', LetterStates.MISPLACED),
            ('t', LetterStates.WRONG),
            ('o', LetterStates.WRONG)]

        misplaced_list = []

        misplaced_list = update_misplaced_list(result, misplaced_list)
        self.assertEqual(misplaced_list, [(1,'h'),(2,'o')])

    def test_update_correct_list(self):
        result = [('p', LetterStates.PROPER),
            ('h', LetterStates.MISPLACED),
            ('o', LetterStates.MISPLACED),
            ('t', LetterStates.WRONG),
            ('o', LetterStates.PROPER)]

        correct_list = []

        correct_list = update_correct_list(result, correct_list)
        self.assertEqual(correct_list, [(0,'p'),(4,'o')])

if __name__ == '__main__':
    unittest.main()
