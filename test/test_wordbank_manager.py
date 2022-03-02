import unittest, os
from solvers.wordbank_manager import WordbankManager

class WordbankManagerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_dir = os.path.dirname(__file__)
        rel_path = 'mock_word_bank.txt'
        cls.wordbank_manager = WordbankManager(os.path.join(test_dir, rel_path))
    
    def test_get_words_without_letters(self):
        self.assertEqual(self.wordbank_manager.get_words_without_letters(['a','z','b']), ['omlet', 'xxxxx','mimic'])
        self.assertEqual(self.wordbank_manager.get_words_without_letters('pwxbm'), ['flota'])
        self.assertFalse('pazur' in self.wordbank_manager.get_words_without_letters('a'))
        self.assertEqual(self.wordbank_manager.get_words_without_letters([]), self.wordbank_manager.wordbank)

    def test_get_words_with_all_letters(self):
        self.assertEqual(self.wordbank_manager.get_words_with_all_letters(['l','o']), ['flota', 'omlet'])
        self.assertEqual(self.wordbank_manager.get_words_with_all_letters('a'), ['pazur','flota', 'wydra', 'topaz', 'saper'])
        self.assertEqual(self.wordbank_manager.get_words_with_all_letters('ar'), ['pazur', 'wydra', 'saper'])
        self.assertEqual(self.wordbank_manager.get_words_with_all_letters('ii'), ['mimic'])
        self.assertFalse('xxxxx' in self.wordbank_manager.get_words_with_all_letters('b'))
        self.assertFalse('topaz' in self.wordbank_manager.get_words_with_all_letters('oo'))
        self.assertEqual(self.wordbank_manager.get_words_with_all_letters([]), [])

    def test_get_words_with_letters_on_index(self):
        self.assertEqual(self.wordbank_manager.get_words_with_letters_on_index([(4, 'a')]), ['flota', 'wydra'])
        self.assertEqual(self.wordbank_manager.get_words_with_letters_on_index([(1, 'a'), (4,'r')]), ['pazur', 'saper'])
        self.assertFalse('czaju' in self.wordbank_manager.get_words_with_letters_on_index([(2, 'f')]))
        self.assertEqual(self.wordbank_manager.get_words_with_letters_on_index([]), [])

    def test_get_words_with_letters(self):
        self.assertEqual(self.wordbank_manager.get_words_with_letters(['l','o']), ['flota', 'omlet', 'topaz'])
        self.assertEqual(self.wordbank_manager.get_words_with_letters('ax'), ['pazur','flota', 'wydra', 'topaz', 'saper','xxxxx'])
        self.assertEqual(self.wordbank_manager.get_words_with_letters('b'), ['bbbbb'])
        self.assertFalse('xxxxx' in self.wordbank_manager.get_words_with_letters('bca'))
        self.assertEqual(self.wordbank_manager.get_words_with_letters([]), [])

    def test_get_words_with_letters_not_on_index(self):
        self.assertEqual(self.wordbank_manager.get_words_with_letter_not_on_index([(4, 'a')]), ['pazur', 'topaz', 'saper'])
        self.assertEqual(self.wordbank_manager.get_words_with_letter_not_on_index([(1, 't'), (2,'o')]), ['omlet', 'topaz'])
        self.assertFalse('xxxxx' in self.wordbank_manager.get_words_with_letter_not_on_index([(2, 'x')]))
        self.assertEqual(self.wordbank_manager.get_words_with_letter_not_on_index([]), [])
        
if __name__ == '__main__':
    unittest.main()
