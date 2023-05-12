# You are given a positive integer n. Each digit of n has a sign according to the following rules:

# The most significant digit is assigned a positive sign.
# Each other digit has an opposite sign to its adjacent digits.
# Return the sum of all digits with their corresponding sign.

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        # turn n into a list of integers
        n = [int(i) for i in str(n)]
        
        # every second number has to be negative
        for i in range(1, len(n), 2):
            n[i] = -n[i]
        
        # returns sum of n
        return sum(n)
