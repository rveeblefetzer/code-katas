from math import sqrt 
def find_next_square(sq):
    """If sq is perfect square, return next; -1 otherwise."""
    if sqrt(sq) % 1 > 0:
        return -1
    else:
        return (sqrt(sq) + 1) ** 2
