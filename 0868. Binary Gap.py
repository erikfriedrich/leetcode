# Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

# Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.

class Solution:
    def binaryGap(self, n: int) -> int:
        
        n = list('{0:0b}'.format(n)) # turn n into list of it's binary representation

        indexes = [i for i, e in enumerate(n) if e == "1"] # get all the indexes of the One's
        
        maxd = 0 # set our maximum index distance to 0
        
        # go trough indexes and checks if the absolute difference between adjacent elements is greater than our max
         # if so, we make it our new maximum
        for i in range(len(indexes)-1):
            if abs(indexes[i]-indexes[i+1]) > maxd:
                maxd = abs(indexes[i]-indexes[i+1])
        
        return maxd
