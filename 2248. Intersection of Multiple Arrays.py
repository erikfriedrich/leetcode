# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
      
        res = []
        
        # length is equal to the amount of sublist and if an element occurs the same amount of times, it's present in every sublist
          # this works because the elements in each sublist are distinct
          
        length = len(nums) 
        flatList = [element for innerList in nums for element in innerList] # got this from geeksforgeeks, this flattens the list, so we don't have any sublists 
        
        # goes trough each element in the first sublist and checks if that element occurs in flatlist the same amount of times as we have sublists in total
          # if so, it gets added to res
        for number in nums[0]:
            if flatList.count(number) == length:
                res.append(number)
         
        # return sorted res
        res.sort() 
        return res
