"""Thests for the string pyramid kata."""


def test_from_side_given_example():
    """Test the basic given case for side view."""
    from string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side('abc') == "  c  \n bbb \naaaaa"


def test_from_side_two_chars():
    """Test passing in two characters."""
    from string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side('ab') == ' b \naaa'


def test_from_side_three_of_same_char():
    """Test passing in three of same character."""
    from string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side('aaa') == '  a  \n aaa \naaaaa'


def test_from_top_two_chars():
    """Test passing in 2 characters to top view."""
    from string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above('ab') == 'aaa\naba\naaa'


def test_from_top_given_example():
    """Test the basic given case for top view."""
    from string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above('abc') == "aaaaa\nabbba\nabcba\nabbba\naaaaa"


def test_count_visible_characters_given_example():
    """Test the basic given case for counting visible characters."""
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid('abc') == 25


def test_count_all_characters_given_example():
    """Test the basic given case for counting all characters."""
    from string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid('abc') == 35
