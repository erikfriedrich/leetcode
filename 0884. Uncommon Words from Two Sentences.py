# A sentence is a string of single-space separated words where each word consists only of lowercase letters.

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
      
      # split the strings at the spaces
        s1 = s1.split(" ")
        s2 = s2.split(" ")
      
      # empty list, where we'll store all uncommon words
        uncommon = []
      
      # find all uncommon words in s1 and 2
        # they have to appear once in in their respected strings and not in the other one
        for word in s1:
            if s1.count(word) == 1 and word not in s2:
                uncommon.append(word)

        for word in s2:
            if s2.count(word) == 1 and word not in s1:
                uncommon.append(word)
                
        return uncommon
