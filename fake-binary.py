def fake_bin(x):
    """Replace numbers in string with 0 for -lt 5 or 1 for -ge 5."""
    new = []
    divvied = list(x)
    idx = 0
    while idx < len(divvied):
        if int(divvied[idx]) < 5:
            new.append("0")
        else:
            new.append("1")
        idx += 1
    return "".join(new)
