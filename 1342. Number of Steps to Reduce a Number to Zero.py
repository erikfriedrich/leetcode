# Given an integer num, return the number of steps to reduce it to zero.

# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

class Solution:
    def numberOfSteps(self, num: int) -> int:
      
        counter = 0
        
       # more or less selfexplanatory
      
        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
                
            counter += 1 # counter outside of if-else, it's  faster
            
        return counter
