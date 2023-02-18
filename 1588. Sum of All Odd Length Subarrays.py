# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        count = 0
        
        # creates all subarrays of odd-length and adds their sum together
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1, 2): # "+1" ensures that arr containing only one number can exist, ", 2" -> only subbarrays of odd-length

                count += sum(arr[i:j])

        return count
