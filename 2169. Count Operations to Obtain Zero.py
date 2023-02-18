# You are given two non-negative integers num1 and num2.
# In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.
# Return the number of operations required to make either num1 = 0 or num2 = 0.

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:

        n = 0

        while num1 != 0 and num2 != 0:
            if num1 > num2: # not ">=" like the description, because if num1 = num2 it doesn't matter which one is subtracted
                num1 -= num2
            else:
                num2 -= num1
            n += 1
            
        return n
