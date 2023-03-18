#  Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

# V1
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
      
        nums.sort() # sorts nums in ascending order
        
        while len(nums) >= 3: # if len(nums) < 3 we would not have enough sides to form a triangle
            if (nums[-3] + nums[-2]) > nums[-1]: # checks if the second and third longest sides (the cathetus) are longer than the hypotenuse ( required to form a triangle)
                return nums[-3] + nums[-2] + nums[-1] # returns perimiter
              
            else:
                nums = nums[:-1] # if we can't form a triangle with the longest side, we remove it from nums and then try again
                
                if len(nums) == 3 and (nums[-3] + nums[-2]) <= nums[-1]: # if we only have three nums left and can't form a triangle we have to return 0
                    return 0
                  
#V2 

# sort in  descending order and then use for i in range(len(nums)-2) ...

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort(reverse = True)

        for i in range(len(nums)-2):
            if nums[i] < (nums[i+1] + nums[i+2]):
                return nums[i] + nums[i+1] + nums[i+2]
        
        return 0
