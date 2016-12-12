
def reverseAndMirror(s1,s2):
    """S2 reverse and swapcase, concatenate with separator and s1 reverse, swapcase and mirrored."""
    return s2[::-1].swapcase() + "@@@" + s1[::-1].swapcase() + s1.swapcase()
