# You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.
# For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
# Return the minimum possible sum of new1 and new2.

# Strategy: to get the smallest number possible, new1 and new2 they have to start with the smallest and second smallest digit (and then the third and forth largest)

class Solution:
    def minimumSum(self, num: int) -> int:
      
      # turns the given number into a string and puts every digit into a list
      my_list = [int(n) for n in str(num)]
      my_list.sort() #sorts the list from smallest to biggest
      
      # creates the new number explained in the strategy  
      new1 = int(str(my_list[0]) + str(my_list[2])) # since list are indexed at 0, to get the first element you use my_list[0]
      new2 = int(str(my_list[1]) + str(my_list[3]))
      
      # trivial
      sum = new1 + new2 
        
      return sum
