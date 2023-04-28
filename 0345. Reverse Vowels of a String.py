# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once

class Solution:
    def reverseVowels(self, s: str) -> str:
      
        vowels = "aeiouAEIOU" # string containing all possible vowels
        
        s  = list(s) # turn s into list to iterate trough
        
        i, j = 0, len(s)-1 # make two pointers, one at the start, one a the end
        
        while i < j:
            if s[i] in vowels and s[j] in vowels: # if the values match, we swap their places
                s[i], s[j] = s[j], s[i]
                j -= 1 # next j
                i += 1 # next i
            elif s[i] in vowels: # if s[i] in vowels, s[j] not in vowels, so we go to the next one
                j -= 1
            else: # s[j] in vowels, but s[i] not -> go to next i
                i += 1
        return "".join(s)
