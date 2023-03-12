# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

# I tought that also ment for example using n**0.5 (which is equivalent to the sqrt())
  # but turns out this was a false assumption (after looking at the fastest solution)\
  
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        n = 0 

        while n <= num: # sqrt of num can never be bigger than num itself (if integer ofc)
          
            if num == n*n: # case perfect square
                return True
            if num < n*n: # perfect square won't be reached
                return False
            n += 1 # get to next possible n
