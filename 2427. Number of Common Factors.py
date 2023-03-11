# Given two positive integers a and b, return the number of common factors of a and b.

# An integer x is a common factor of a and b if x divides both a and b.

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        n = 1
        common_factors = 0
        
        while n <= a or n <= b: # loop stops when n reaches a or b, since this is the greatest possible common divisor
            if a % n == 0 and b % n == 0:
                common_factors += 1 # if n divides a and b we have found a new common_factor and add it to our total
            n += 1 # "go to the next n"
            
        return common_factors
