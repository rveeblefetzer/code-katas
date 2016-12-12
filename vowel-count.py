def getCount(inputStr):
    num_vowels = 0
    # your code here

    vowels = ['a', 'e', 'i', 'o', 'u']

    for c in list(inputStr):
        if c in vowels: num_vowels+=1

    return num_vowels
