# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        n = 0
        
        # Strategy: go trough all number in the list, if the number is equal to it's index, we go to the next n 
                  # if n is equal to the length of the list (meaning we're at the end) we just return n
                  # if the number is unequal to it's index, we return n
            
        for n in range(len(nums)):
            if nums[n] == n:
                n += 1
                if n == len(nums):
                    return n
            else:
                return n
