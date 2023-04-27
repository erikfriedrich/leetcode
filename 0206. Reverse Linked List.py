# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        prev, curr = None, head # initialize pointers as None and head
        
        # run until curr points to None
        while curr:
            next = curr.next # next ponter is pointer after curr
            curr.next = prev # assign prev pointer as curr's next pointer
            prev, curr = curr, next # assign curr to prev pointer and next to curr # like shifting everything by one
            
        return prev # returns reverse linked list
