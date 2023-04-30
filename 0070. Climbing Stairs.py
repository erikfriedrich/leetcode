# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:

        n1, n2 = 0, 1

        counter = 0

        while counter < n:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            counter += 1

        return n2
