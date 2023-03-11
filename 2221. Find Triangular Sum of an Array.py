# You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

# The triangular sum of nums is the value of the only element present in nums after the following process terminates:

# Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
# For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
# Replace the array nums with newNums.
# Repeat the entire process starting from step 1.
# Return the triangular sum of nums.

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
      
            while len(nums) > 1: # stops when len(nums) = 1, meaning that nums[0] = triangular sum of nums
          
                for i in range(len(nums)-1): # for every integer in nums, except the last one
                    nums[i] = (nums[i] + nums[i+1]) % 10 # from the description of the task
                
                nums = nums[:-1] # cut the last character of the list -> process then starts again
                
            return nums[0] # to get return type integer
