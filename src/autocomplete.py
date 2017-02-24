"""Attempt at creating an autocomplete class."""

from trie import Node, Trie


class Autocomplete(object):
    """Given a word list, enable autocomplete for new words."""

    def __init__(self, vocabulary, max_completions=5):
        """Set up trie for autocomplete."""
        self._trie = Trie()
        self.vocabulary = vocabulary
        self.max_completions = max_completions
        self._stored_vocab = Trie()
        self.word_list = []
        for word in self.vocabulary:
            self._trie.insert(word)

    def autocomplete(self, word):
        """Autocomplete a word based on self.vocab."""
        self.word_list = []
        current = self._trie.root
        if word:
            for letter in word:
                if letter in current.children:
                    current = current.children[letter]
                else:
                    return
        self._autocomplete(current)
        return self.word_list[:self.max_completions]

    def _autocomplete(self, node):
        """Traverse trie."""
        if not node.children:
            return node
        for key, value in node.children.items():
            if key == '$':
                if value not in self.word_list:
                    self.word_list.append(value)
                else:
                    continue
            else:
                self._autocomplete(value)
        return self.word_list
