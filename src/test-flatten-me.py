from random import choice, randint
from string import printable


def random_element():
    """ Returns a single random element
    Choices are an ASCII string character, boolean or a random integer
    """
    return choice((
        choice(printable), choice((True, False)), randint(0, 1000)
    ))


def random_sequence():
    """ Returns a list with a maximum of one level of nesting """
    return [choice((
        random_element(), [random_element() for _ in range(randint(1, 9))]
    )) for _ in range(randint(5, 30))]


def solution(lst):
    result = []
    for a in lst:
        try:
            result.extend(a)
        except TypeError:
            result.append(a)
    return result


Test.describe('Basic Tests')
Test.assert_equals(flatten_me([1, [2, 3], 4]), [1, 2, 3, 4])
Test.assert_equals(flatten_me([['a', 'b'], 'c', ['d']]), ['a', 'b', 'c', 'd'])
Test.assert_equals(flatten_me(['!', '?']), ['!', '?'])
Test.assert_equals(
    flatten_me([[True, False], ['!'], ['?'], [71, '@']]),
    [True, False, '!', '?', 71, '@']
)

Test.describe('Random Tests')
for _ in range(100):
    random_seq = random_sequence()
    Test.assert_equals(solution(random_seq), flatten_me(random_seq))
