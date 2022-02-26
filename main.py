from statistical_search import worlde_statistical_search
from humanlike_search import worlde_humanilike_search
from taboo_search import worlde_taboo_search
from wordbank_manager import WordbankManager
from game_manager import GameManager

wordbank_manager = WordbankManager('wordbanks/eng_five_letter_words.txt')
game_manager = GameManager()

game_manager.set_password(wordbank_manager.get_random_word())
print(worlde_taboo_search(game_manager, wordbank_manager, wordbank_manager.get_random_word()))
print(worlde_humanilike_search(game_manager, wordbank_manager, wordbank_manager.get_random_word()))
print(worlde_statistical_search(game_manager, wordbank_manager, wordbank_manager.get_random_word()))