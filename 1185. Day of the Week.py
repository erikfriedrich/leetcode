# Given a date, return the corresponding day of the week for that date.

# The input is given as three integers representing the day, month and year respectively.

# Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

from datetime import datetime # import datetime to convert the integers into a weekday

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date = datetime(year=year, month=month, day=day)
        return date.strftime('%A') # "%A" retuns the weekday -> look into datetime documentation for other ones
