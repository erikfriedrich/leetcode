# Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

# V1 - stupid solution, because I didn't know python had a gcd function 
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        nums.sort()
        
        small_num = nums[0]
        big_num = nums[-1]
        
        div = 1
        divisors = []
        
        # to take some complexity from it
        if big_num == small_num or small_num == 1:
            return small_num
        
        # goes trough all possible divisors from 1 
          # [has to be included otherwise divisors[-1] doesn't work if there's only one common divisor greater than one] 
            # to the biggest_num (technically it never goes beyond big_num-1, because the case big_num = gcd if caught by the if before
            
        for div in range(1, big_num):
            if small_num % div == 0 and big_num % div == 0:
                divisors.append(div) # in case it is a divisor it gets added to the list of divisors
            div += 1
        return divisors[-1] # returns the last number in the list of divisors
    
# V2 - if was smart
class Solution:
    def findGCD(self, nums: List[int]) -> int:
      
        minimum = min(nums)
        maximum = max(nums)
        
        return gcd(minimum, maximum)
