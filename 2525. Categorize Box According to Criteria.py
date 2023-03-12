# Given four integers length, width, height, and mass, representing the dimensions and mass of a box, respectively, return a string representing the category of the box.

# The box is "Bulky" if:
# Any of the dimensions of the box is greater or equal to 104.
# Or, the volume of the box is greater or equal to 109.
# If the mass of the box is greater or equal to 100, it is "Heavy".
# If the box is both "Bulky" and "Heavy", then its category is "Both".
# If the box is neither "Bulky" nor "Heavy", then its category is "Neither".
# If the box is "Bulky" but not "Heavy", then its category is "Bulky".
# If the box is "Heavy" but not "Bulky", then its category is "Heavy".
# Note that the volume of the box is the product of its length, width and height.

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        
        # this is a simpler form of assigning bulky and weight boolean values
            # using boolean would save some 0.2 MB of Memory and maybe a few milliseconds of runtime
        
        greatest_dimension = max(length, width, height) # to check if any dimension is greater that 10^4
        volume = length*width*height # calculates volume
       
        bulky = 0 
        weight = 0

        if greatest_dimension >= 10**4 or volume >= 10**9:
            bulky += 1
        if mass >= 100:
            weight += 1 
        # give back the categories depending on the values of bulky and weight
        
        if bulky == weight == 1:
            return "Both"
        if bulky == weight == 0:
            return "Neither"
        if bulky == 1 and weight == 0:
            return "Bulky"
        if bulky == 0 and weight == 1:
            return "Heavy"
