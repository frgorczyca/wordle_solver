from random import choice
from itertools import combinations
from solvers.game_manager import LetterStates
from solvers.result_list_helpers import update_taboo_list, update_correct_list, update_misplaced_list

def get_letter_frequency(word_set):
    """Get most frequent letters in set of words"""
    letters_frequency = {}

    for word in word_set:
        for letter in word:
            if letter not in letters_frequency:
                letters_frequency[letter] = 1
            else:
                letters_frequency[letter] += 1

    return [x[0] for x in sorted(letters_frequency.items(), reverse=True, key=lambda item: item[1])]

def get_missing_letters_number(result_list):
    """Get number of letters that are neither correct nor misplaced"""
    if not result_list: 
        raise ValueError('result_list cannot be empty')

    missing_letters_amount = 0

    for result in result_list:
        if result[1] == LetterStates.WRONG:
            missing_letters_amount+=1

    return missing_letters_amount

def get_statistical_solution(letters_frequency, missing_letters_amount, allowed_words):
    """Get frequency based solution from avaiable word list"""
    if missing_letters_amount == 0:
        return choice(allowed_words)
    
    # In very rare cases there are fewer letters to choose from than missing slots (words with multiple duplicated letters)
    if (len(letters_frequency) < missing_letters_amount):
        missing_letters_amount = len(letters_frequency)

    words = allowed_words
    for combination in combinations(letters_frequency, missing_letters_amount):
        for letter in combination:
            words = list(filter(lambda word: letter in word, words))

        if words:
            return choice(words)

    for combination in combinations(letters_frequency, missing_letters_amount):
        words = []
        for letter in combination:
            words = words + list(filter(lambda word: letter in word, allowed_words))

        if words:
            return choice(words)
        
def worlde_statistical_search(game_manager, wordbank_manager, solution):
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
        misplaced_words = wordbank_manager.get_words_with_letter_not_on_index(misplaced_list)

        matching_words = [word for word in allowed_words if (word in correct_words or not correct_words) and (word in misplaced_words or not misplaced_words)]
        solution =  get_statistical_solution(get_letter_frequency(matching_words), get_missing_letters_number(result_list), matching_words)
    
    return (solution, iterations)
    



