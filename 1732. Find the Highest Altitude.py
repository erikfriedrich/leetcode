# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        maxx, curr_alt = 0, 0 # set max altitude and current altitude to 0

        # goes trough every reached altitude and updates the max
        for i in range(len(gain)):
            
            curr_alt += gain[i] 
            maxx = max(maxx, curr_alt)
            
        return maxx
