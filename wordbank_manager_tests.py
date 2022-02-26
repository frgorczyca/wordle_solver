import unittest
from wordbank_manager import WordbankManager

class WordbankManagerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wordbank_manager = WordbankManager('mock_word_bank.txt')

    def test_does_word_exists(self):
        self.assertTrue(self.wordbank_manager.does_word_exist('topaz'))
        self.assertFalse(self.wordbank_manager.does_word_exist('aaaaa'))
    
    def test_get_words_without_letters(self):
        self.assertEqual(self.wordbank_manager.get_words_without_letters(['a','z','b']), ['omlet', 'xxxxx'])
        self.assertEqual(self.wordbank_manager.get_words_without_letters('pwxbm'), ['flota'])
        self.assertFalse('pazur' in self.wordbank_manager.get_words_without_letters('a'))
        self.assertEqual(self.wordbank_manager.get_words_without_letters([]), [])

    def test_get_words_with_all_letters(self):
        self.assertEqual(self.wordbank_manager.get_words_with_all_letters(['l','o']), ['flota', 'omlet'])
        self.assertEqual(self.wordbank_manager.get_words_with_all_letters('a'), ['pazur','flota', 'wydra', 'topaz', 'saper'])
        self.assertFalse('xxxxx' in self.wordbank_manager.get_words_with_all_letters('b'))
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
        
if __name__ == '__main__':
    unittest.main()
