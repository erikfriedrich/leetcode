# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

# Given the string command, return the Goal Parser's interpretation of command.

class Solution:
    def interpret(self, command: str) -> str:
      
        out = []
        n = 0
        
        while n < len(command):
            if command[n] == "G":
                out.append("G")
                n += 1
            elif command[n] == "(" and command[n+1] == ")":
                out.append("o")
                n += 2
            else:
                out.append("al")
                n += 4
                
        return ''.join(out)
      
 # more elegant would have been just to use replace()
