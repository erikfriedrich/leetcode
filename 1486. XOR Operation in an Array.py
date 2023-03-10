# You are given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
      
        nums = []
        index = 0
        
        # Applying: Define an array...
        for index in range(n):
            nums.append(start + 2 * index)
            index += 1
        
        
        res = reduce(lambda x, y,: x ^ y, nums) # reduce(): reduces our list back into one integer
                                                # lambda... x ^ y ...: takes the bitwise XOR of all elements in nums
        
        return res
