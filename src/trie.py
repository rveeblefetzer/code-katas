"""A trie tree to help the accompanying autocomplete module."""

from collections import OrderedDict


class Node(object):
    """Node object to build a trie."""

    def __init__(self, value=None):
        """Create node to push into Doubly link list."""
        self.value = value
        self.children = OrderedDict()


class Trie(object):
    """
    Implementation of the trie tree.

    Methods include:
    insert(string): Add a string to the trie.
    contains(string): Return true if string is in trie, else false.
    size(): Return the number of words in the trie. 0 if empty.
    traversal(self, start): Traverse the graph from start.
    """

    def __init__(self):
        """Initialize the Trie class."""
        self.root = Node()
        self._size = 0

    def insert(self, string):
        """Insert string into the trie."""
        if not isinstance(string, str):
            raise TypeError("Please input a string")
        string = string.lower()
        current_node = self.root
        for letter in string:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                current_node.children[letter] = Node(letter)
                current_node = current_node.children[letter]
        if '$' not in current_node.children:
            current_node.children['$'] = string
            self._size += 1

    def contains(self, string):
        """Return true or false whether string is in trie."""
        if not isinstance(string, str):
            raise TypeError("I can only search for a string")
        current_node = self.root
        for letter in string:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                return False
        if current_node.children['$']:
                return True

    def size(self):
        """Return the number of words/strings in the trie."""
        return self._size

    def __len__(self):
        """Allow use of len() function."""
        return self.size()

    def traversal(self, start=None):
        """Return a generator yielding words emanating from start."""
        start_node = self.root
        if start is not None:
            for letter in start:
                if letter in start_node.children:
                    start_node = start_node.children[letter]
                else:
                    raise ValueError("String is not in trie.")
        result = self._traversal(current_node, True)
        for val in result:
            yield val.value

    def _traversal(self, node, first=False):
        if not first:
            yield node
        for child in node.children:
            if child == '$':
                continue
            for val in self._traversal(node.children[child]):
                yield val
