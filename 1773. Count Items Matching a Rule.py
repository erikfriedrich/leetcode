# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

# The ith item is said to match the rule if one of the following is true:

# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.class Solution:

def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        count = 0
          
        # match ruleKey to specific cases
        match ruleKey:
            case 'type':
                j = 0
            case 'color':
                j = 1
            case "name":
                j = 2
        
        # check if the Value at the specified position (by the Key) is equal to our Rule
        for i in range(len(items)):
            if items[i][j] == ruleValue:
                count += 1

        return count
