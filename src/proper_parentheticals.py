"""A linked list to verify parenthetical pairs."""


class Node(object):
    """Create class to represent individual node elements in data structure."""

    def __init__(self, data, next_node=None):
        """Something."""
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    """Create linked lists."""

    def __init__(self, iterable=None):
        """Instantiate linked-list object with optional iterable."""
        self.head = None
        if iterable and hasattr(iterable, "__iter__"):
            for value in iterable:
                self.push(value)
        # for py27
        elif iterable and isinstance(iterable, str):
            for char in iterable:
                self.push(char)
        elif iterable:
            raise TypeError

    def push(self, val):
        """Push elements into list."""
        node = Node(val)
        node.next_node = self.head
        self.head = node

    def pop(self):
        """Remove head element and return value."""
        temp_data = self.head.data
        self.head = self.head.next_node
        return temp_data

    def size(self):
        """Return length of list."""
        count = 0
        current = self.head
        if self.head is None:
            return 0
        while current.next_node is not None:
            count += 1
            current = current.next_node
        return count + 1

    def search(self, val):
        """Return node with data value of val."""
        current = self.head
        # import pdb; pdb.set_trace()
        while current is not None:
            if current.data == val:
                return current
            current = current.next_node
        return None

    def remove(self, node):
        """Remove given node from list."""
        current = self.head
        if current.data == node.data:
            self.head = current.next_node
            return True
        while current.next_node is not None:
            if current.next.data == node.data:
                current.next_node = current.next_node.next_node
                return True
            current = current.next_node
        raise ValueError("Node not in list.")

    def display(self):
        """Display all elements in a linked list."""
        current = self.head
        result = "("
        while current is not None:
            if isinstance(current.data, str):
                result = result + "'" + current.data + "'"
            else:
                result = result + str(current.data)
            if current.next_node is not None:
                result += ", "
            current = current.next_node
        result += ')'
        print(result)
        return result


def parentheses_check(string):
    """Check if parentheticals close."""
    parens = []
    for char in string:
        if char == '(' or char == ')':
            parens.append(char)
    rev_parens = parens[::-1]
    parens_check = LinkedList(rev_parens)
    state = 0
    current = parens_check.head
    while current is not None:
        if current.data == '(':
            state += 1
        else:
            state -= 1
        if state < 0:
            return -1
        current = current.next_node
    if state > 0:
        return 1
    return 0
