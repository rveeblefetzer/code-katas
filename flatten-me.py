#!/usr/bin/env python
"""Flatten a list of strings and lists into a new list of discrete elements."""


def flatten_me(lst):
    """Parse elements in a list and append a new list to return."""
    idx = 0
    new_list = []
    while idx < len(lst):
        if type(lst[idx]) == list:
            j = 0
            while j < len(lst[idx]):
                new_list.append(lst[idx][j])
                j += 1
        else:
            new_list.append(lst[idx])
        idx += 1
    return new_list
