"""Tests for forbes_filter() function."""
from forbes_filter import forbes_filter

def test_returns_dict():
    assert type(forbes_filter()) == dict


def test_returned_dict_has_old_billionaire():
    assert 'oldest_billionaire_under_80' in forbes_filter().keys()


def test_old_billionaire_key_has_name():
    assert forbes_filter()['oldest_billionaire_under_80'][0] == 'Phil Knight'


def test_old_billionaire_key_has_net_worth():
    assert forbes_filter()['oldest_billionaire_under_80'][1] == 24400000000


def test_old_billionaire_key_has_money_source():
    assert forbes_filter()['oldest_billionaire_under_80'][2] == "Nike"


def test_returned_dict_has_youngest_billionaire():
    assert 'youngest_billionaire' in forbes_filter().keys()


def test_youngest_billionaire_key_has_name():
    assert forbes_filter()['youngest_billionaire'][0] == 'Mark Zuckerberg'


def test_youngest_billionaire_key_has_net_worth():
    assert forbes_filter()['youngest_billionaire'][1] == 44600000000


def test_youngest_billionaire_key_has_money_source():
    assert forbes_filter()['youngest_billionaire'][2] == "Facebook"
