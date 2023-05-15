# Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.

# An English letter b is greater than another letter a if b appears after a in the English alphabet.

class Solution:
    def greatestLetter(self, s: str) -> str:

        letters = [] # collect letters that are present both lower and upper case
        
        # check if a letter ist there both upper and lowercase
        for letter in s:
            if letter.upper() in s and letter.lower() in s:
                letters.append(letter.upper()) # if so, we add it to letters
        
        # if there is no letter in letters we return ""
        if len(letters) == 0:
            return ""
        
        # returns the maximum letter following the tasks logic
        return max(letters)
