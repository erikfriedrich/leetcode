# You are playing the following Nim Game with your friend:
# Initially, there is a heap of stones on the table.
# You and your friend will alternate taking turns, and you go first.
# On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
# The one who removes the last stone is the winner.
# Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

# say n = 4: 
# the one that starts will aways lose, no matter what is choosen, the other can always make a move so the number of removed stones equals 4 (and he ends up removing the last stone)
# if n is not a multiple of 4 you can always force the other into this situation and end up winning
# if n is a multiple of 4 you will always lose

# V1 
class Solution:
    def canWinNim(self, n: int) -> bool:
        return True if n % 4 != 0 else False
      
# V2

# the most efficient solution would be:
  # return n % 4 != 0 
  # because they expect the function to return a boolean value
