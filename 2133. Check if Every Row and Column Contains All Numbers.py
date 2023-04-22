# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
      
        n = len(matrix)
        matrix_row = matrix
        # this transposes the matrix ( I now know that this could've been done using zip )
        matrix_column = [] 
        
        for i in range(n):
            for j in range(n):
                matrix_column.append(matrix[j][i])
                
        matrix_column = [matrix_column[x:x+n] for x in range(0, len(matrix_column), n)]
        
        # checks if the length of a the set of each row/ column differs from the lenght of the row/ column -> if so there has to be a duplicate -> return False
        for i in range(n):
            if len(set(matrix_row[i])) != n:
                return False
                break
            if len(set(matrix_column[i])) != n:
                return False
              
                break
        return True
