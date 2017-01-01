#!/usr/bin/env python
def sort_cards(deck):
    """Sort a set of playing cards by rank."""
    suit = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    sort_order = list(map(lambda given_order: suit.index(given_order), deck))
    print(list(map(lambda card: suit[card], sorted(sort_order))))
