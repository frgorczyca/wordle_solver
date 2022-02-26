from random import choice
from game_manager import GameManager
from wordbank_manager import WordbankManager
from result_list_helpers import update_taboo_list, update_correct_list, update_misplaced_list

def worlde_humanilike_search(game_manager, wordbank_manager, solution):
    """Get solution to worlde problem and number of iterations"""
    taboo_list = []
    correct_list = []
    misplaced_list = []
    iterations = 0
    
    while solution != game_manager.get_password():
        if solution == game_manager.get_password():
            break

        iterations+=1
        result_list = game_manager.verify_solution(solution)

        taboo_list = update_taboo_list(result_list, taboo_list)
        allowed_words = wordbank_manager.get_words_without_letters(taboo_list)

        correct_list = update_correct_list(result_list, correct_list)
        correct_words = wordbank_manager.get_words_with_letters_on_index(correct_list)

        misplaced_list = update_misplaced_list(result_list, misplaced_list)
        misplaced_words = wordbank_manager.get_words_with_all_letters(misplaced_list)

        solution = choice([word for word in allowed_words if (word in correct_words or not correct_words) and (word in misplaced_words or not misplaced_words)])
    
    return (solution, iterations)