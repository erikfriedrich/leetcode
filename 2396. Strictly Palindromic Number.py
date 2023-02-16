# An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.
# Given an integer n, return true if n is strictly palindromic and false otherwise.

# tricky question, since there is no number that satisfies this condition
# n in base n-2: n = 1 * (n-2) ^ 1 + 2 * (n-2) ^ 0 = 1 * (n-2) + 2 * 1 = n - 2 + 2 = n 

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False
