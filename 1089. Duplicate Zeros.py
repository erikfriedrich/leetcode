# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        #"""
        #Do not return anything, modify arr in-place instead.
        #"""
        indices = []

        length = int(len(arr))

        for ind, val in enumerate(arr):
            if val == 0:
                indices.append(ind)

        n = 0

        for i in indices:
            arr.insert(i+n, 0)
            n += 1
        
        while len(arr) > length:
            arr.pop(-1)
