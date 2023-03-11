# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums. 

# Note: Subsets with the same elements should be counted multiple times.

# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
      
        bits = 0
        
        for i in range(len(nums)):
            bits |= nums[i] # |= it just performes the bitwise OR operation between the bit and the next entry in the list
        
        # My first intution was to make a list of nums that contains all possible sublist and then do the XOR
        # this seemed way to inefficient to me so I looked up a faster way to do it
        # this logic behind it goes the following:
            # sketch a tree with all possible sublist of some given nums
            # you'll find that every bit appears 2 ^ (n -1) times
            
        ans = bits * pow(2, len(nums)-1) #
        
        return ans
