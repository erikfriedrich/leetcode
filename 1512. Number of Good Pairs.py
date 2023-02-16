# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        counter = 0 # set sum to zero

        # loop that goes through all num[i], except the last one, and checks, wether there exists a num[j] in front of it (with len(nums) >= j >= i +1)
        # if so the counter goes up by one

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    counter += 1
        return counter
