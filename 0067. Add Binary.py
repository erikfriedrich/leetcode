# Given two binary strings a and b, return their sum as a binary string.

# we'll solve this by using the built in function int(x, 2) [=> with base two] and bin()

class Solution:
    def addBinary(self, a: str, b: str) -> str:
      
        return bin(int(a, 2) + int(b, 2))[2:] # [2:] slices off the binary string prefix
