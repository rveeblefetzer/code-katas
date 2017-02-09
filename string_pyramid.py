#!usr/bin/env Python
"""Solutions to a code kata on Code Wars:

http://www.codewars.com/kata/string-pyramid
"""

def watch_pyramid_from_the_side(characters):
    """Build a pyramid with the given string, with the base as the first character,
    and layering upwards and return the view from one side."""
    if characters:
        white_space = 0
        count = len(characters)
        result = ""
        for char in characters:
            result += " " * white_space + char * (2 * count - 1) +\
                          " " * white_space + "\n"
            count -= 1
            white_space += 1
        return result[-2::-1]
    else:
        return characters


def watch_pyramid_from_above(characters):
    """Build a pyramid with the given string, with the base as the first character,
    and layering each character upwards and return the view from above."""
    if characters:
        view = []
        for char in range(len(characters)):
            view.append(characters[:char] + characters[char] * len(characters[char:]))
        for row in range(len(characters)):
            view[row] += view[row][-2::-1]
        for row_to_copy in range(len(characters) - 2, -1, -1):
            view.append(view[row_to_copy])
        return "\n".join(view)
    else:
        return characters


def count_visible_characters_of_the_pyramid(characters):
    """Tally the number of pyramid stones that can be seen."""
    if characters:
        visible_chars = watch_pyramid_from_above(characters)
        return len(''.join(visible_chars.split()))
    else:
        return -1

def count_all_characters_of_the_pyramid(characters):
    """Tally the total number of stones in the pyramid."""
    if characters:
        total = 0
        for char in range(len(characters)):
            total += count_visible_characters_of_the_pyramid(characters[char:])
        return total
    else:
        return -1
