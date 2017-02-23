def series_sum(n):
    """Return series sum up to nth term in which denominator increments by 3."""
    denominator = 1
    total = 0
    if n == 0:
        return "0.00"
    else:
        for i in range(n):
            total += eval("1/" + str(denominator))
            denominator += 3
    return str(format(total, '.2f'))
