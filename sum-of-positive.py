def positive_sum(arr):
    """Add all positive numbers in list."""
    if len(arr) == 0:
        return 0
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
    return sum
    
