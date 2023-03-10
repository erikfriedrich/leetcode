# Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
# The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.
# Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.
# Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

# basically Alice always wins, try finding a counter example if you have to much freetime
# explanation: https://leetcode.com/problems/stone-game/solutions/154610/dp-or-just-return-true/?orderBy=most_votes
# I came up with the solution myself but don't have a way of explaining it easily

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
      
 
