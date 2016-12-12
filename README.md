# code-katas
My solutions to katas on [Code Wars](https://www.codewars.com)

## Flatten Me
* **Module:** flatten-me.py
* **Tests:** test-flatten-me.py
* **Link:** https://www.codewars.com/kata/55a5bef147d6be698b0000cd

Code Wars' most clever solution:
```python
def flatten_me(lst):
    return [v for sub in [e if type(e) == list else [e] for e in lst] for v in sub]
 ```
