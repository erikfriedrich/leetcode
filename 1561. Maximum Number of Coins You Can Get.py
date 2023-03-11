# There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

# In each step, you will choose any 3 piles of coins (not necessarily consecutive).
# Of your choice, Alice will pick the pile with the maximum number of coins.
# You will pick the next pile with the maximum number of coins.
# Your friend Bob will pick the last pile.
# Repeat until there are no more piles of coins.
# Given an array of integers piles where piles[i] is the number of coins in the ith pile.

# Return the maximum number of coins that you can have.

class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort() # sort piles from smallest to biggest

        n = int(len(piles) / 3) # get number of pair of three's that can be made

        piles = piles[n:] # if n = 6: it will cut-off the first two lowest numbers, because they will always go to Bob

        my_piles = piles[0::2] # since we choose the piles of coins, we can ensure that we always get the second biggest from any slice
                                # this starts from the lowest and goes up in steps of two
                                
        return sum(my_piles)
