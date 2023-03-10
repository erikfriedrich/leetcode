# You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.
# Return true if the square is white, and false if the square is black.
# The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
      
        column = ord(coordinates[0]) - 96 # ord() returns integer representing the letter: -96 to get a => 1, b => 2 etc.
        row = int(coordinates[1]) # row is the second entry of the list as an integer
        
        return (column+row) % 2 == 1 # when you analyse the chessboard you'll find that all the sum of the column and the row of the white squares is always odd
