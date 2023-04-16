#Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

#A substring is a contiguous sequence of characters within a string.

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
      
        count = 0
        
        # this creates a list containing all sub_strings of word
          # it adds word[i:j] to the list
            # for i in range of the length of the word
            # and for every j that comes after i
          
        res = [word[i: j] for i in range(len(word)) for j in range(i + 1, len(word) + 1)]
        
        # goes trough each pattern in patterns
          # and every sub_string of word (that is contained in res)
            # and checks if the pattern in question is equal to one of the substrings
            # if this is the case, we add one to our counter and break, otherwise we could be counting the appearence of "a" in "aaa" multiple times
        
        for pattern in patterns:
            for j in range(len(res)):
                if pattern == res[j]:
                    count += 1
                    break
                    
        return count
      
 # this solution is quite in efficent since the same result could have been achieved by 
 
  return sum(p in word for p in patterns)
