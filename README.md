# code-katas
My solutions to katas on [Code Wars](https://www.codewars.com)

## Flatten Me (7 kyu)
* **Module:** flatten-me.py
* **Tests:** test-flatten-me.py
* **Link:** https://www.codewars.com/kata/55a5bef147d6be698b0000cd

Code Wars' most clever solution:
```python
def flatten_me(lst):
    return [v for sub in [e if type(e) == list else [e] for e in lst] for v in sub]
 ```

## Ones and Zeros
* **Module:**: ones-and-zeros.py
* **Tests:** test-ones-and-zeros.py
* **Link:** https://www.codewars.com/kata/ones-and-zeros/train/python

Good solution on Code Wars:
```python
def binary_array_to_number(arr):
  return int("".join(map(str, arr)), 2)
```

## Vowel Count (7 kyu)
* **Module:** vowel-count.py
* **Tests:** test-vowel-count.py
* **Link:** https://www.codewars.com/kata/vowel-count/train/python

Good solution on Code Wars:
```
def getCount(s):
    return sum(c in 'aeiou' for c in s)
```

## String Reversing, Changing case, etc. (7 kyu)
* **Module:** string-reversing-changing-case-etc.py
* **Tests:** test-string-reversing-changing-case-etc.py
* **Link:** https://www.codewars.com/kata/string-reversing-changing-case-etc/python

Interesting solution using string interpolation:
```
def reverse_and_mirror(s1, s2):
    swap = s1.swapcase()
    return '{}@@@{}{}'.format(s2[::-1].swapcase(), swap[::-1], swap)
```

## Even or Odd 
* **Module:** even-or-odd.py
* **Tests:** test-even-or-odd.py
* **Link:** https://www.codewars.com/kata/even-or-odd/python

From Code Wars' best solutions, I liked this one's use of Boolean in a one-liner:
```python
def even_or_odd(number):
  return 'Odd' if number % 2 else 'Even'
```

## Find the next perfect square! (7 kyu)
* **Module:** next-perfect-square.py
* **Tests:** test-next-perfect-square.py
* **Link:** https://www.codewars.com/kata/find-the-next-perfect-square/python

From best solutions, one that doesn't import sqrt from math:
```
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1
```

## Counting sheep...
* **Module:** counting-sheep.py
* **Tests:** test-counting-sheep.py
* **Link:** https://www.codewars.com/kata/counting-sheep-dot-dot-dot/python

From best solutions, a one-liner using .count()
```
def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)
```

## Fake Binary
* **Module:** fake-binary.py
* **Tests:** test-fake-binary.py
* **Link:** https://www.codewars.com/kata/fake-binary/python

Nice one-liner from best solutions:
```
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
```

## Sum of positive
* **Module:** sum-of-positive.py
* **Tests:** test-sum-of-positive.py
* **Link:** https://www.codewars.com/kata/sum-of-positive/python

Clear one-liner from best solutions:
```
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
```

## Convert a string to an array
* **Module:** string-to-array.py
* **Tests:** test-string-to-array.py
* **Link:** https://www.codewars.com/kata/convert-a-string-to-an-array/python

I was close to the top clever solution, though I added in a case of empty string, which it turns out I didn't need to do:
```
def string_to_array(string):
    return string.split(" ")
```

## Opposite number
* **Module:** opposite-number.py
* **Tests:** test-opposite-number.py
* **Link:** https://www.codewars.com/kata/opposite-number/python

From clever solutions, looks like I didn't need the parens:
```
def opposite(number):
    return -number
```

