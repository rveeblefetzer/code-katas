"""Test autocomplete engine kata."""

import pytest

TEST_WORDLIST = ['pizza', 'pizazz', 'piezo', 'pizzicato', 'pizzeria']


@pytest.fixture
def pizza_set():
    """Set up a test trie for autocomplete."""
    from autocomplete import Autocomplete
    return Autocomplete(TEST_WORDLIST)


def test_init():
    """Test autocomplete instantiation with vocabulary."""
    from autocomplete import Autocomplete
    test_autocomplete = Autocomplete(TEST_WORDLIST)
    for word in TEST_WORDLIST:
        assert word in test_autocomplete.vocabulary


def test_autocomplete(pizza_set):
    """Test complete_me method of autocomplete."""
    assert pizza_set.autocomplete('piz') == ['pizza', 'pizzicato',
                                             'pizzeria', 'pizazz']


def test_set_completions():
    """Test that reduced max completions limit returns."""
    from autocomplete import Autocomplete
    comp = Autocomplete(TEST_WORDLIST, 3)
    assert comp.autocomplete('p') == ['pizza', 'pizzicato', 'pizzeria']
