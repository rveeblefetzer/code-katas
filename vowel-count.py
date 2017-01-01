def getCount(inputStr):
    """Count the number of lowercase vowels in a string."""
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for c in list(inputStr):
        if c in vowels: num_vowels+=1
    return num_vowels
