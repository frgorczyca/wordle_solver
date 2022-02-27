from random import choice
from result_list_helpers import update_taboo_list

def worlde_taboo_search(game_manager, wordbank_manager, solution):
    """Get solution to worlde problem and number of iterations"""
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