# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

# Stragety


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        ans = [] # make empty list that will be returned later

        x = 1 # first number that will appear in list

        while x <= n: # till x = n, because n will be the last possible number that appears in the list
     
# we start with the case that x is divisible by 15
  # if we would start with 3 or 4 we would have to check that it's not divisible by the other (case divisible by 15)
    # this would low down the code
    
            if x % 15 == 0: 
                ans.append("FizzBuzz")
            elif x % 3 == 0:
                ans.append('Fizz')
            elif x % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(x))

            x += 1 # 'go to next integer'
            
        return ans 
