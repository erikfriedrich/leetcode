# Given an integer n, return any array containing n unique integers such that they add up to 0.

class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        arr = []
        ind = 1 
        
        # using round() improves Speed and Memory; I suppose it's because Python doesn't get "confused" if n is odd and n/2 ends with .5
        
        for i in range(round(int(n/2))): # since we always add two numbers, we only need to do it n/2 times
            arr.append(ind)
            arr.append(-ind) # together they add 0 to the sum
            ind += 1 # get new integer
        
        if n % 2 != 0: # using the for-loop above we get an array of even-length; if n is odd we need to add one element, that doesn't change the sum (-> 0)
            arr.append(0)
            
        return arr
