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
https://www.codewars.com/kata/vowel-count/train/python

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

