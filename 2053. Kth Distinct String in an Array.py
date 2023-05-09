# A distinct string is a string that is present only once in an array.

# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

# Note that the strings are considered in the order in which they appear in the array.

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        distinct = []
        
        # add every distinct string in arr to a new list
        for string in arr:
            if arr.count(string) == 1:
                distinct.append(string)
            if len(distinct) >= k: # we can stop collecting distinct integers if we have more than k
                break
        
        # if there are less than k integers, we return an empty string
          # else we return k (k-1 becaus 0-indexed)
        if len(distinct) < k:
            return ""
        else:
            return distinct[k-1]
