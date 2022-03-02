import unittest
from solvers.game_manager import GameManager, LetterStates

class GameManagerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.game_manager = GameManager()

    def test_verify_solution(self):
        self.game_manager.set_password('paser')

        self.assertEqual(self.game_manager.verify_solution('paser'), [(letter, LetterStates.PROPER) for letter in 'paser'])
        self.assertEqual(self.game_manager.verify_solution('xxxxx'), [(letter, LetterStates.WRONG) for letter in 'xxxxx'])
        self.assertEqual(self.game_manager.verify_solution('rpase'), [(letter, LetterStates.MISPLACED) for letter in 'rpase'])
        self.assertEqual(self.game_manager.verify_solution('sapew'), [
            ('s', LetterStates.MISPLACED),
            ('a', LetterStates.PROPER),
            ('p', LetterStates.MISPLACED),
            ('e', LetterStates.PROPER),
            ('w', LetterStates.WRONG)])
        self.assertEqual(self.game_manager.verify_solution('pypaa'), [
            ('p', LetterStates.PROPER),
            ('y', LetterStates.WRONG),
            ('p', LetterStates.WRONG),
            ('a', LetterStates.MISPLACED),
            ('a', LetterStates.WRONG)])
        self.assertEqual(self.game_manager.verify_solution('aaaaa'), [
            ('a', LetterStates.WRONG),
            ('a', LetterStates.PROPER),
            ('a', LetterStates.WRONG),
            ('a', LetterStates.WRONG),
            ('a', LetterStates.WRONG)])


if __name__ == '__main__':
    unittest.main()
