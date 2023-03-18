# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      
        x = 0 # start with the power 0
        
        while 2 ** x <= n: # while n could be a power of two
            if 2 ** x == n: # returns true if n is a power of two
                return True
              
            x += 1 # go to next bigger x, if n was not a power of two yet
            
        return False # if n can't be a power of two return false
