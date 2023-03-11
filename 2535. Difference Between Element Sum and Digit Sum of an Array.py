# You are given a positive integer array nums.

# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.

# Note that the absolute difference between two integers x and y is defined as |x - y|.

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
      
        element_sum = sum(nums) # sum of all integers in the list
        
        digit_sum = sum(map(lambda elements: sum(int(sub) for sub in str(elements)), nums))
        
        # sum(int(sub) for sub in str(elements)
        # sums up the values of each digit that make up one integer in the list of nums
          # has to turn them into an integer before
        # map() applies the lamba function to nums
        # sum() then adds all those values together
        
        return element_sum - digit_sum
