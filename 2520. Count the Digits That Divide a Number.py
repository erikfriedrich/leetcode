# Given an integer num, return the number of digits in num that divide num.

# An integer val divides nums if nums % val == 0.

class Solution:
    def countDigits(self, num: int) -> int:
      
        divisors = 0
        possible_divisors = [int(i) for i in str(num)] # turn num into a string consisting of all its digits
        
        for i in possible_divisors: # go trough all digits in our list of possible divisors
            if num % i == 0:
                divisors += 1 # if i is a divisors, we add 1 to our counter
                
        return divisors
