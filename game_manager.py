from random import randint
from enum import Enum
from random import randint

class LetterStates(Enum):
        PROPER = 1,
        MISPLACED = 2,
        WRONG = 3

class GameManager():
    """
    Class managing single instance of Worlde game.

    Attributes:
        five_letter_words: contains all five letter words as a wordbank for the game. 
        password: Current correct anwser to game instance. Can be generated via generate_password() method.
    """
    def __init__(self):
        self.__password = ''
    
    def set_password(self, password):
        """Set a new, random password as a solution to the GameManager object."""
        self.__password = password

    def get_password(self):
        """Returns literal password. Should only be used to compare result to exit loops and compare results."""
        return self.__password
    
    def verify_solution(self, word):
        """Compare letters and their placement to correct answer"""
        letter_states = []
        
        for (index, letter) in enumerate(word):
            if(self.__password[index] == letter):
                letter_states.append((letter, LetterStates.PROPER))
            elif(letter in self.__password):
                letter_states.append((letter, LetterStates.MISPLACED))
            else:
                letter_states.append((letter, LetterStates.WRONG))
        
        return letter_states
            
