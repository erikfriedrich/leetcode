class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        maxx, curr_alt = 0, 0

        for i in range(len(gain)):
            
            curr_alt += gain[i]
            maxx = max(maxx, curr_alt)
            
        return maxx
