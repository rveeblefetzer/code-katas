"""Tests for proper_parenthetics."""

import pytest

PARENS_TABLE = [
    [")))(((", -1],
    ['instantfail)', -1],
    ['(evens out)(but order bad))(', -1],
    ["from my .emacs file (add-hook 'org-mode-hook(lambda () (add-hook 'before-save-hook 'my/org-add-ids-to-headlines-in-file nil 'local)))", 0],
    ['(((one not closed))', 1],
    ['()', 0],
    ['(()())', 0]
]


@pytest.mark.parametrize("string, result", PARENS_TABLE)
def test_parens_ispaired(string, result):
    """Test if string of parentheses all close."""
    from proper_parentheticals import parentheses_check
    assert parentheses_check(string) == result
