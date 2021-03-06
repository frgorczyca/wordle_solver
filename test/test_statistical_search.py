import unittest, os
from solvers.game_manager import LetterStates
from solvers.statistical_search import get_letter_frequency, get_missing_letters_number, get_statistical_solution
from solvers.wordbank_manager import WordbankManager

class StatisticalSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_dir = os.path.dirname(__file__)
        rel_path = 'mock_word_bank.txt'
        cls.wordbank_manager = WordbankManager(os.path.join(test_dir, rel_path))

    def test_get_letter_frequency(self):
        word_set = ['abc', 'abd', 'aee']
        frequency = ['a','b','e','c','d']
        self.assertEqual(get_letter_frequency(word_set), frequency)
    
    def test_get_missing_letters_number(self):
        self.assertEqual(get_missing_letters_number([(letter, LetterStates.PROPER) for letter in 'paser']), 0)
        self.assertEqual(get_missing_letters_number([(letter, LetterStates.MISPLACED) for letter in 'paser']), 0)
        self.assertEqual(get_missing_letters_number([(letter, LetterStates.WRONG) for letter in 'paser']), 5)
        with self.assertRaises(ValueError):
            get_missing_letters_number([])

    def test_get_statistical_solution(self):
        self.assertEqual(get_statistical_solution([], 0, ['solution']), 'solution')

        frequency = ['a','e','c','d']
        word_set = ['aecd', 'sbd', 'ae']
        self.assertEqual(get_statistical_solution(frequency,4,word_set),'aecd')
        self.assertTrue(get_statistical_solution(frequency,2,word_set) in ['aecd','ae'])
    

if __name__ == '__main__':
    unittest.main()
