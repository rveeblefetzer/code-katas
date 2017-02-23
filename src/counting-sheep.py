def count_sheeps(arrayOfSheeps):
    """With True meaning sheep present, count the number of sheep in a list."""
    count = 0
    for i in arrayOfSheeps:
    if i == True:
        count += 1
    return count
