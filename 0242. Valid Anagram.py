# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # make empty dicts
        dict_s = {}
        dict_t = {}
        
        # count the occurences of every letter in s and t 
        for letter in s:
                dict_s[letter] = dict_s.get(letter, 0) + 1
        for letter in t:
                dict_t[letter] = dict_t.get(letter, 0) + 1
        
        # check if they're equal -> every letter occurs the same amount of times
        return dict_t == dict_s
