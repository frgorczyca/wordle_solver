from statistical_search import get_letter_frequency, get_missing_letters_amount, get_statistical_solution
from wordbank_manager import WordbankManager
import unittest
from game_manager import GameManager, LetterStates

class StatisticalSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wordbank_manager = WordbankManager('mock_word_bank.txt')

    def test_verify_solution(self):
        result = [LetterStates.PROPER for i in range(5)]
        print(result)

        self.assertEqual(get_missing_letters_amount([(letter, LetterStates.PROPER) for letter in 'paser']), 0)
        self.assertEqual(get_missing_letters_amount([(letter, LetterStates.WRONG) for letter in 'paser']), 0)

if __name__ == '__main__':
    unittest.main()
