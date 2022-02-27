from random import choice

class WordbankManager():
    """
    Class managining set of all words valid as game solutions. 

    Attributes:
        wordbank: Contains all letters valid as answers for the game. 
    """
    def __init__(self, wordbank):
        with open(wordbank, 'r') as words_file:
            self.wordbank = words_file.read().splitlines()

    def get_random_word(self):
        """Get a random word from the wordbank"""
        return choice(self.wordbank)

    def does_word_exist(self, word):
        """Verify if the word exists in the wordbank"""
        return word in self.wordbank

    def get_words_without_letters(self, forbidden_letters):
        """Returns all words without provided letters"""   
        if not forbidden_letters:
            return self.wordbank

        allowed = self.wordbank
        for letter in forbidden_letters:
            allowed = list(filter(lambda word: letter not in word, allowed))

        return allowed

    def get_words_with_all_letters(self, required_letters):
        """Returns all words containing all provided letters"""
        if not required_letters:
            return []

        allowed = self.wordbank
        for letter in required_letters:
            allowed = list(filter(lambda word: letter in word and word.count(letter) >= required_letters.count(letter), allowed))

        return allowed

    def get_words_with_letters(self, required_letters):
        """Returns all words containing at least one of provided letters"""
        if not required_letters:
            return []

        allowed = []
        for letter in required_letters:
            allowed = allowed + list(filter(lambda word: letter in word, self.wordbank))

        return list(dict.fromkeys(allowed))

    def get_words_with_letters_on_index(self, indexed_letters):
        """Given tuple with letter and index returns all words with exact indexes"""
        if not indexed_letters: 
            return []

        allowed = self.wordbank 
        for index, letter in indexed_letters:
            allowed = list(filter(lambda word: word[index] == letter, allowed))

        return allowed

    