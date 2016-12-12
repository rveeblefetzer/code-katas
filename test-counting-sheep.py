array1 = [True,  True,  True,  False,
              True,  True,  True,  True ,
              True,  False, True,  False,
              True,  False, False, True ,
              True,  True,  True,  True ,
              False, False, True,  True ]
              
array2 = []
array2.extend([True] * 500)
array2.extend([None] * 5)
array2.extend([False] * 100)

array3 = []
 

test.assert_equals(count_sheeps(array1), 17, "There are 17 sheeps in total, not %s" % count_sheeps(array1))
test.assert_equals(count_sheeps(array2), 500, "There are 500 sheeps in total, not %s" % count_sheeps(array2))
test.assert_equals(count_sheeps(array3), 0, "There are no sheeps at all, you counted %s" % count_sheeps(array3))
