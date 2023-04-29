# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

class Solution:
    def tribonacci(self, n: int) -> int:
        
        # weird case
        if n == 0:
            return 0

        n1, n2, n3 = 0, 1, 1
        count = 0

        while count < n-2:
            nth = n1 + n2 + n3
            n1, n2 = n2, n3
            n3 = nth
            count += 1

        return n3
