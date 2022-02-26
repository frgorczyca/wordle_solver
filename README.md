This is a simple worlde game, along with basic mechanisms to help get it solved.

# Implementations
Current implementations:
- Taboo Search - simple taboo search with basic taboo list
- Humanlike Search - algorithm imitating human approach that takes all words with already guessed letters along with disqualifying banned letters and randomly pickes a word out of that set.
- Statistical Search - improved Humanlike Search that also takes into consideration frequency of letters avaiable in the set and tries to pick a word that will include most popular letters

# Wordbanks
This repo includes a couple of word lists:
- five_letter_words - list of all polish five letter words
- eng_five_letter_words - list of all words used by worlde (in English)
- mock_word_bank - simple list for unit testing
