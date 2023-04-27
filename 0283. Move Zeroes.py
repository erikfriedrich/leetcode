# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # collect all the indixes of the zeros in nums
        indexes = [i for i, e in enumerate(nums) if e == 0]
        
        # we reverse indexes and go trough each index, delete the 0 there and add one back at the end of nums
          # if we wouldn't reverse it the following problem would arise
            # suppose the zeros are at [0,2]
              # we first delete the zero at i=0
                # the second zero is now at i=1 instead of i=2 and we'll delete the wrong value
                
        for index in sorted(indexes, reverse=True):
            del nums[index]
            nums.append(0)      
