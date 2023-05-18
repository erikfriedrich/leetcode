# You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

# Return the maximum total number of units that can be put on the truck.

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True) # sorts the boxes by the number of items that are in the box

        n_boxes = truckSize
        units = 0
       
        for i in range(len(boxTypes)):
            if n_boxes == 0: # if we have no box left to fill, we can just stop the loop
                break
            elif boxTypes[i][0] <= n_boxes: # if we can put all our boxes (of one kind) into the truck, we can just add the product of the number of boxes and the amount of items to our units
                units += boxTypes[i][0] * boxTypes[i][1]
                n_boxes -= boxTypes[i][0]
            else: # if we have more boxes of one kind than we have boxes left to fill, we just fill all boxes left with the number of products in the box we're looking at 
                units += n_boxes  * boxTypes[i][1]
                break
        
        return units
