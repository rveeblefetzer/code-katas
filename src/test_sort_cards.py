from random import randint, choice

SORTED_CARDS = 'A23456789TJQK'
TEST_CARDS = (
    'A', '3', 'T', 'T824Q', 'QKJ6932', 'J69327A8', 'J679J7327A8',
    'TA8AAA24AQA', 'AAAAAAAAAAAAA', '39A5T824Q7J6K', 'Q286JK395A47T',
    '54TQKJ69327A8', 'Q286JK395A47TQ286JK395A47T',
    'Q286JKKKKK395AAA47TQ286JK395A47T',
    'AAAAAAAAAAAAAQ286JK395A47TQ286JK395A47T'
)


def solution(cards):
    return sorted(cards, key='A23456789TJQK'.index)


Test.it('Basic Tests')
for cards_str in TEST_CARDS:
    cards = list(cards_str)
    Test.it(repr(cards))
    Test.assert_equals(sort_cards(cards), solution(cards))

Test.it('Random Tests')
for _ in range(100):
    random_cards = [choice(SORTED_CARDS) for i in range(randint(1, 100))]
    Test.it(repr(random_cards))
    Test.assert_equals(sort_cards(random_cards), solution(random_cards))