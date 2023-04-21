# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
      
        Dict = {} # make an empty dict
        
        # strategy:
        # go trough all characters in the string and add count their occurences using a dict
        
        for character in s:
            occ = Dict.get(character, 0) # gets the number of occurences for a given character, 0 in case the character is not in the list yet
            Dict[character] = occ + 1 # adds one to the counter and automatically adds any new character that were not in the list yet
        
        # get test value to compare all other values to
        test = list(Dict.values())[0] # turns the values of the dict into a list and grabs the first element
        
        # goes trough all characters in the dict and checks if their occurences is equal to the test value or not
        for character in Dict:
            if Dict[character] != test:
                return False
        return True
