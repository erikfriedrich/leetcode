# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # if x is negative it's not possible to be a Palindrome
        if x < 0:
            return False
          
        # reverse x 
        reverse = int(str(x)[::-1])
        
        # check if reverse is equal to x
        if x == reverse:
            return True
          
# best would be to make x into a string and check if it's equal to it reversed
