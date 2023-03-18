# Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

# Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

class Solution:
    def averageValue(self, nums: List[int]) -> int:

        div6 = [] # list that will store all integers in nums that are divisible by 6 (even and dibisible by three)

        for number in nums: # goes trough all integers in nums
            if number % 6 == 0: # appends the number to our list if it's divisible by 6
                div6.append(number)

        if len(div6) == 0: # if there is no element in div6 we have to return zero, otherwise we would get an error with the average
            return 0

        avg = sum(div6) / len(div6) # compute a the average of the numbers divisible by 6
        
        return int(avg)
