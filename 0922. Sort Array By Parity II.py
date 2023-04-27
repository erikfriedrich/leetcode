# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

 #Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

# Return any answer array that satisfies this condition.

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        # make empty list for even and odd numbers in nums
        res_even = []
        res_odd = []
        
        # append all odd numbers to res_odd and all even number to res_even
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                res_even.append(nums[i])
            else:
                res_odd.append(nums[i])
                
        n = 1
        # insert an odd number after every even number (at a odd-index)
        for i in range(len(res_odd)):
            res_even.insert(n, res_odd[i])
            n += 2
          
        return res_even
