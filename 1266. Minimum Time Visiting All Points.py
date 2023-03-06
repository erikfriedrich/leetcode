#On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

#You can move according to these rules:

  #In 1 second, you can either:
    #move vertically by one unit,
    #move horizontally by one unit, or
    #move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
    
  #You have to visit the points in the same order as they appear in the array.
  #You are allowed to pass through points that appear later in the order, but these do not count as visits.

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
      
        time = 0
        
        # loop goes trough all points and their "successor" (except for the last point, because there is no successor)
        # it checks wether the (absolute) difference of the x- or y- cordinates it greater, and adds bigger one to the time
        # why does this work?
          # this is how a king moves on a chess board (if you want to go the fastest) - Chebyshev distance
        
        for i in range(len(points)-1):        
            time += max(abs(points[i+1][0] - points[i][0]), abs(points[i+1][1] - points[i][1]))
            
        return time
