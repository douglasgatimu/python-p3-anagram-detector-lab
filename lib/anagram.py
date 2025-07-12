# your code goes here!
from collections import Counter
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        return [word_ for word_ in word_list if Counter(self.word) == Counter(word_)]



