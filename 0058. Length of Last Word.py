# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      
        s = s[::-1]
        s = s.split(" ")

        while 0 < 1: 
            if s[0] == "":
                s.pop(0)
            else:
                break
                
        return len(s[0])
