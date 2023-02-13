# Task
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
#Return the decimal value of the number in the linked list.
#The most significant bit is at the head of the linked list.


# Definition for singly-linked list. 
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        # turn singly-linked list into array
        # reasoning: I'm more familiar to working with arrays

        arr = [] # creating array

        current = head # setting variable "current" to the head of the linked list

        # loop that appends the value of a node to the array, moves trough all nodes and stops at the end (when the current node has no value anymore)
        while(current != None):
            arr.append(current.val)
            current = current.next
        
        counter = len(arr) - 1 # setting counter 
        sum = 0 # setting sum to zero

        # loop that goes trough array; if value of i is one it adds the decimal value of the binary to the sum; else the counter is just lowered by one to "skip" the zeros. In the end the desired sum is returned
        for i in range(len(arr)):
            if arr[i] == 1:
                sum = sum + 2 ** counter
                counter -= 1
            else:
                counter -= 1

        return sum
