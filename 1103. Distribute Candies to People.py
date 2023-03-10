# We distribute some number of candies, to a row of n = num_people people in the following way:
# We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.
# Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.
# This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).
# Return an array (of length num_people and sum candies) that represents the final distribution of candies.

# Goal: return a list with the number of candies everyone gets

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
      
        # make an empty list that we'll than add the amounts to
        amount = []
        n = 1
        
        # set the number of candies that everyone has to 0 
        for i in range(0, num_people):
            amount.append(0)
        
        # while we still can distribute candies 
        while candies > 0:
            
            # goes trough all the people if the number of candies left is more or equal to the amount that they would get
              # else: we add the remaining amount of candies to the last person and return the list "amount"
                # while candies > 0: if we've reached the last person, we'll start again at the front
              
            for i in range(0, num_people):
                if candies >= n:
                    amount[i] = amount[i] + n # add the number of candies the person should receive to the amount of candies the person already has
                    candies -= n # reduce the amount of candies by the number of candies that we've given the last person
                    n += 1 # to go the the next person
                else:
                    amount[i] = amount[i] + candies
                    candies = 0
        return amount
