# You are given an integer n, the number of teams in a tournament that has strange rules:

# If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
# If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
# Return the number of matches played in the tournament until a winner is decided.

# visualize the conditions -> you should recognize a pattern
  # you can simplify it into the following
    # every game that is played, one team loses and is eliminated 
      # if we have n teams, n-1 games have to be played to get the winner
      
class Solution:
   def numberOfMatches(self, n: int) -> int:
       return n-1
