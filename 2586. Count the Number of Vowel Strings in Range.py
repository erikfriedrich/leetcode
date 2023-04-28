# You are given a 0-indexed array of string words and two integers left and right.

# A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.

# Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        
        vowels = "aeiou"
        counter = 0
        
        # goes trough every item in words that i within range and cheks if the first value and the second are in vowels -> that increase counter
        for i in range(left, right + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                counter += 1
        
        return counter
