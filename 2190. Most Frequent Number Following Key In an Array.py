# You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.

# For every unique integer target in nums, count the number of times target immediately follows an occurrence of key in nums. In other words, count the number of indices i such that:

# 0 <= i <= nums.length - 2,
# nums[i] == key and,
# nums[i + 1] == target.
# Return the target with the maximum count. The test cases will be generated such that the target with maximum count is unique.

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        
        # make dict where we will store target and it's count
        occ = {}
        
        # add every value after our key value to our dict and increment it's occurence by one
        for i in range(len(nums)-1):
            if nums[i] == key:
                try:
                    occ[nums[i+1]] += 1
                except KeyError:
                    occ[nums[i+1]] = 1
        
        # return key with maximum occurence
        return max(occ, key=occ.get)
