from random import choice
from game_manager import GameManager, LetterStates
from wordbank_manager import WordbankManager

def update_taboo_list(result_list, taboo_list):
    """Add letters that do not exist in solution to taboo list"""
    for result in result_list:
        if result[1] == LetterStates.WRONG and result[0] not in taboo_list:
            taboo_list.append(result[0])

    return taboo_list

def update_correct_list(result_list, correct_list):
    """Add letters that exist in solution to correct list"""
    for (index, result) in enumerate(result_list):
        if result[1] == LetterStates.PROPER and (index, result[0]) not in correct_list:
            correct_list.append((index, result[0]))

    return correct_list

def update_misplaced_list(result_list, misplaced_list):
    """Add letters that do not exist in solution to taboo list"""
    for result in result_list:
        if result[1] == LetterStates.MISPLACED and result[0] not in misplaced_list:
            misplaced_list.append(result[0])

    return misplaced_list

def worlde_humanilike_search(game_manager,wordbank_manager, solution):
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
        misplaced_words = wordbank_manager.get_words_with_letters(misplaced_list)

        solution = choice([word for word in allowed_words if (word in correct_words or not correct_words) and (word in misplaced_words or not misplaced_words)])
    
    return (solution, iterations)

taboo_wordbank_manager = WordbankManager('eng_five_letter_words.txt')
taboo_game_manager = GameManager()

taboo_game_manager.set_password(taboo_wordbank_manager.get_random_word())

res = worlde_humanilike_search(taboo_game_manager, taboo_wordbank_manager, 'soare')
print(res, taboo_game_manager.get_password())