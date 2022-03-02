from solvers.statistical_search import worlde_statistical_search
from solvers.wordbank_manager import WordbankManager
from solvers.game_manager import GameManager


wordbank_manager = WordbankManager('eng_five_letter_words.txt')

game_manager = GameManager()

statistical_iterations = []

for i in range (10):
    game_manager.set_password(wordbank_manager.get_random_word())
    statistical_iterations.append(worlde_statistical_search(game_manager, wordbank_manager, wordbank_manager.get_random_word())[1])

print(sum(statistical_iterations)/10)
