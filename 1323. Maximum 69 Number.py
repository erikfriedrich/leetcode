# You are given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

# I'm stupid - coud've just used replace()

class Solution:
    def maximum69Number (self, num: int) -> int:

       # turn num (integer) into str 
        res = [int(x) for x in str(num)]

        # change first res[i] that is equal to six into a nine
        for i in range(len(res)):
            if res[i] == 6:
                res[i] = 9
                break

        # turn list into integer again
        num = int(''.join(map(str, res)))
        return num
