# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

# Return the positive integer k. If there is no such integer, return -1.

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
      
        nums = list(set(nums)) # this deletes all duplicates, using the code below you could run into a problem, where 30 would be returned but there was 30 and 30 in the list of -30 and -30, AND NOT -30 and 30
        nums = [abs(ele) for ele in nums] # converts everything to it's absolute value           
        nums.sort(reverse=True) # sort in descending order -> possible max will be found earlier
        
        # checks if an element in the list is equal to the following element -> we have -k and k in the list -> return k
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
        
        # otherwise we return -1
        return -1
