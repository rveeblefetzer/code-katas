Test.describe("positive_sum")

Test.it("works for some examples")
Test.assert_equals(positive_sum([1,2,3,4,5]),15)
Test.assert_equals(positive_sum([1,-2,3,4,5]),13)
Test.assert_equals(positive_sum([-1,2,3,4,-5]),9)

Test.it("returns 0 when array is empty")
Test.assert_equals(positive_sum([]),0)

Test.it("returns 0 when all elements are negative")
Test.assert_equals(positive_sum([-1,-2,-3,-4,-5]),0)

Test.it("works for random arrays")
from random import randint

def randarr(l):
    return [randint(-100, 100) for _ in xrange(l)]

def solution(arr):
    return sum(x for x in arr if x > 0)

for _ in xrange(40):
    arr = randarr(randint(5, 120))
    Test.assert_equals(positive_sum(arr[:]), solution(arr[:]), "Failed when arr = {}".format(arr))
