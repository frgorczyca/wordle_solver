from random import choice
from game_manager import GameManager, LetterStates
from wordbank_manager import WordbankManager

def update_taboo_list(result_list, taboo_list):
    """Add letters that do not exist in solution to taboo list"""
    for result in result_list:
        if result[1] == LetterStates.WRONG and result[0] not in taboo_list:
            taboo_list.append(result[0])

    return taboo_list

def worlde_taboo_search(game_manager,wordbank_manager, solution):
    taboo_list = []
    iterations = 0
    
    while solution != game_manager.get_password():
        if solution == game_manager.get_password():
            break

        iterations+=1
        result_list = game_manager.verify_solution(solution)
        taboo_list = update_taboo_list(result_list, taboo_list)

        solution = choice(wordbank_manager.get_words_without_letters(taboo_list))
    
    return (solution, iterations)

taboo_wordbank_manager = WordbankManager('eng_five_letter_words.txt')
taboo_game_manager = GameManager()

taboo_game_manager.set_password(taboo_wordbank_manager.get_random_word())

res = worlde_taboo_search(taboo_game_manager, taboo_wordbank_manager, taboo_wordbank_manager.get_random_word())
print(res, taboo_game_manager.get_password())