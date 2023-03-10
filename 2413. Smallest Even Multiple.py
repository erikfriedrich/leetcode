# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
# => return n if even (can be written as 2 * m, satisfying our conditions) and 
# => n*2 if odd (divisible by n and two since they're it's factors [trivial that they're the smallest])

# the proof for all this was part of Analysis B

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n*2
