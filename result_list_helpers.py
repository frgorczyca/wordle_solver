from game_manager import LetterStates

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
    """Add letters that exists in solution on a different index to misplaced list"""
    for result in result_list:
        if result[1] == LetterStates.MISPLACED and result[0] not in misplaced_list:
            misplaced_list.append(result[0])

    return misplaced_list