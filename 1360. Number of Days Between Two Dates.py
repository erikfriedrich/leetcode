# Write a program to count the number of days between two dates.

# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

from datetime import datetime, timedelta

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:

        date_format = "%Y-%m-%d" # setting the format, struggled a little bit with the uppercase Y (-> YYYY), I had lowercase first which menas (YY)
        
        # turn strings into date objects so we can work with it
        date1 = datetime.strptime(date1, date_format)
        date2 = datetime.strptime(date2, date_format)
        
        # calculates the delta between the two days and the return the absolute value of the delta in days
         # abs() is nessecary because if date1 is before date2 the delta would be negative
        delta = date1 - date2

        return abs(delta.days)
