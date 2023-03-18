# here is a function signFunc(x) that returns:

# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.

# Return signFunc(product).

class Solution:
    def arraySign(self, nums: List[int]) -> int:
      
        product = 1 # initiate our product as 1
        
        for number in nums: # goes trough all numbers in nums and multiplies them together
            product = product * number
            
        if product > 0: # just 'applies' the signFunc() to our product
            return 1
        elif product == 0:
            return 0
        else:
            return -1
