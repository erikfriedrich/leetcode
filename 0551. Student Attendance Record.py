# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.

class Solution:
    def checkRecord(self, s: str) -> bool:
      
        # it would've been smarter just to check if "LLL" is in s
        
        # counts the days absent
        absent = s.count("A")
        
        # make a counter to count consecutive times missing
        count = 0
        s = list(s)
        days_late = [0]
        
        for i in range(1, len(s)):
            if s[i] == s[i-1] == "L":
                count += 1
                days_late.append(count)
            else:
                count = 0

        late = max(days_late)
        
        # two days late is enough in this case because we don't count the last time the L appears
        return absent < 2 and late < 2
  
