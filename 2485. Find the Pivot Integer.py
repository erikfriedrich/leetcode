# Given a positive integer n, find the pivot integer x such that:
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

class Solution:
    def pivotInteger(self, n: int) -> int:
        
        # make a list from 1 to n
        
        nums = []
        
        for number in range(1, n + 1):
            nums.append(number)

        total = sum(nums)
        left_sum = 0
        
        # my first intuition was left_sum == total-left_sum, but this doesn't account for the fact that it's "inclusive", which is why you need minnus i
        
        for i in nums:
            if left_sum == (total-left_sum-i):
                return i
            else:
                left_sum += i
        return -1
