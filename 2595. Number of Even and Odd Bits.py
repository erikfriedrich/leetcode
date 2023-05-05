# You are given a positive integer n.

# Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.

# Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.

# Return an integer array answer where answer = [even, odd].


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
      
        binary = list(format(n, 'b')) # turns n into a list of it's binary representation
        binary.reverse() # reverses it's order, so the loops start if a the right place (1 -> 2 -> 4 ....) instead of starting with the highest
        
        even, odd = 0, 0
        
        # goes trough all even and odd indexes and checks for a "1" (because truning each element into ints would waste time)
        
        for i in range(0, len(binary), 2):
            if binary[i] == "1":
                even += 1
        for i in range(1, len(binary), 2):
            if binary[i] == "1":
                odd += 1
                
        return [even, odd]
