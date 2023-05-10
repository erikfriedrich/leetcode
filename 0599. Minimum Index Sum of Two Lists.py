# Given two arrays of strings list1 and list2, find the common strings with the least index sum.

# A common string is a string that appeared in both list1 and list2.

# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

# Return all the common strings with the least index sum. Return the answer in any order.




class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        ind_sum = []
        comm = []
        
        # find every common word
        for word in list1:
            if word in list2:
                comm.append(word)
        
        # if there is only one common word we can just return it
        if len(comm) == 0:
            return comm
        
        # get the index sum of every common word
        for word in comm:
            i = list1.index(word)
            j = list2.index(word)
            ind_sum.append(i+j)
        
        # get the minimum index sum
        k = min(ind_sum)
        # number of common words -> "0-indexed"
        i = len(comm)-1
        
        # go trough every common word, from the top, and then pop it if it's index sum is not equal to the minimum
          # with a for-loop the next index would be out of range 
        while i >= 0:
            if ind_sum[i] > k:
                comm.pop(i)
            i -= 1

        return comm
