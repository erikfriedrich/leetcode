# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

class Solution:
    def arrangeCoins(self, n: int) -> int:

        count = 0
        i = 1
        
        # i = number of elements for each row, takes i of n and adds one to the counter ( while the're is still enough left to fill the row)
        while n >= i:
            n -= i
            i += 1
            count += 1

        return count
