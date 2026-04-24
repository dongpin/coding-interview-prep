
from collections import defaultdict


class Trie:
    def __init__(self):
        self.words = defaultdict(Trie)
        self.end = False

    def add(self, word):
        trie = self
        while word:
            trie = trie.words[word[0]]
            word = word[1:]
        trie.end = True

    def search(self, word):
        trie = self
        while word:
            if word[0] in trie.words:
                trie = trie.words[word[0]]
                word = word[1:]
            else:
                return False
        return trie.end

    def build_trie(self, words):
        for word in words:
            self.add(word)
