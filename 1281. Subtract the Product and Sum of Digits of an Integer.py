# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        product = 1
        sum = 0
        
        # turns n into a string, and goes trough every digit in the list
        for i in str(n):
          
            product = product * int(i) # multiplies the old product with the next digit
            sum = sum + int(i) # adds the next digit to the sum // if you want to be fancy, you could also use sum += int(i) but it's actually slower
            
        return product - sum
