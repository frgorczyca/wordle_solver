from enum import Enum

class LetterStates(Enum):
        PROPER = 1,
        MISPLACED = 2,
        WRONG = 3

class GameManager():
    """
    Class managing single instance of Worlde game.

    Attributes:
        __password: Current correct anwser to game instance. Can be generated via generate_password() method.
    """
    def __init__(self):
        self.__password = ''
        self.__password_stats = {}


    def set_password(self, password):
        """Set a new, random password as a solution to the GameManager object."""
        self.__password = password
        self.__password_stats = {}
        for (index, letter) in enumerate(password):
            if letter not in self.__password_stats:
                self.__password_stats[letter] = [index]
            else:
                self.__password_stats[letter].append(index)
        

    def get_password(self):
        """Returns literal password. Should only be used to compare result to exit loops and compare results."""
        return self.__password
    
    def verify_solution(self, word):
        """Compare letters and their placement to correct answer"""
        letter_states = [0] * len(word)
        word_stats = {}

        for (index, letter) in enumerate(word):
            if letter not in word_stats:
                word_stats[letter] = [index]
            else:
                word_stats[letter].append(index)

        for letter in word_stats.keys():
            for index, instance in enumerate(word_stats[letter]):
                if letter in self.__password_stats.keys() and instance in self.__password_stats[letter]:
                    letter_states[instance] = ((letter, LetterStates.PROPER))
                elif letter in self.__password_stats.keys() and set(self.__password_stats[letter]).isdisjoint(word_stats[letter]) and index <= len(self.__password_stats[letter])-1:
                    letter_states[instance] = ((letter, LetterStates.MISPLACED))
                else: 
                    letter_states[instance] = ((letter, LetterStates.WRONG))
            

        return letter_states

