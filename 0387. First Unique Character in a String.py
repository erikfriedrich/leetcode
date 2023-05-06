# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:

        checked = [] # to keep track of already checked chars
      
        for char in s:
            if char not in checked:
                checked.append(char)
                if s.count(char) == 1:
                    return s.index(char)

        return -1
