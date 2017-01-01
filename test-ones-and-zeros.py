import random

Test.describe("Example tests")
Test.assert_equals(binary_array_to_number([0,0,0,1]), 1)
Test.assert_equals(binary_array_to_number([0,0,1,0]), 2)
Test.assert_equals(binary_array_to_number([1,1,1,1]), 15)
Test.assert_equals(binary_array_to_number([0,1,1,0]), 6)

Test.describe("Random tests")
for _ in range(50):
    n = random.randint(0, 1000)
    array = [int(x) for x in bin(n)[2:]]
    Test.it("Tests %s ==> %s" % (array, n))
    Test.assert_equals(binary_array_to_number(array), n,"It should work for random inputs too") 
