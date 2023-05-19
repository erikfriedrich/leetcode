# # You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.

# Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.

# Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:

        dictt = {}

        for i in range(lowLimit, highLimit+1):
            
            # get the digit sum of each integer between the lowLimit and the highLimit
            summ = 0
            for digit in str(i): 
                summ += int(digit)      
            
            # update counter in dict for the specific sum
            dictt[summ] = dictt.get(summ, 0) + 1
        
        # return max value
        return max(dictt.values())
