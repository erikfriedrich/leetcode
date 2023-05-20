# You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).

# The valid times are those inclusively between 00:00 and 23:59.

# Return the latest valid time you can get from time by replacing the hidden digits.

class Solution:
    def maximumTime(self, time: str) -> str:

        time = list(time)
        
        for i in range(5):
            if time[i] == '?':
                if i == 0:
                    if time[1] == "?":
                        time[0] = 2
                    elif int(time[1]) > 3:
                        time[0] = 1
                    else:
                        time[0] = 2
                if i == 1:
                    if int(time[0]) == 1 or int(time[0]) == 0:
                        time[1] = 9
                    else:
                        time[1] = 3
                if i == 3:
                    time[3] = 5
                if i == 4:
                    time[4] = 9
        
        return "".join(str(e) for e in time)
