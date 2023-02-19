# Reversing an integer means to reverse all its digits.
# For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
# Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.

# since 0 are not retained -> the only case in which reversed2 doesn't equal num is when num divisible by ten
# 0 itself being the exception; if num == 0, true has to be returned

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return True if num % 10 != 0 or num == 0 else False
