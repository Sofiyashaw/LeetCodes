# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:28:47 2024

@author: jacin
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Initialize a listnode
        dummy = ListNode()
        # Assign curr as dummy
        curr = dummy
        # Initialize carry value as 0
        carry = 0
        # While there are elements in lisnode 1 , listnode 2 and carry has some elements
        while l1 or l2 or carry:
            # Let us now calculate value 1 from the listnode1
            v1 = l1.val if l1 else 0 
            # Let us now calculate value 2 from listnode2
            v2 = l2.val if l2 else 0
           
            # Calculate the first addition

            val = v1 + v2 + carry
            #val = 2 + 5 + 0
            #val = 7

            #Calculate carry by using floor division
            # carry = 7 // 10
            # carry = 0 (Because we cant divide 7/10)
            # It divides two numbers and returns the largest integer less than or equal to the result.
            carry = val // 10
            # Then calculate the value
            # val = 7 % 10
            # val = 7
            val = val % 10
            
            #curr.next = ListNode(val) sets the next pointer of the current node (curr) to this new node.
            # This is for setting the pointer
            # Initially
            # dummy -> None
            # After the first iteration
            # dummy -> 7 -> None
            curr.next = ListNode(val)
            

            # Current State Before the Step:
            # curr is pointing to the current node in the linked list.
            # curr.next is pointing to the next node in the linked list.
            # After Executing curr = curr.next:
            # The curr pointer is updated to point to the next node in the list.
            # That means initially dummy to next node
            # Now list node 7 to next node
            curr = curr.next


            # This line updates the pointer l1 to the next node in the linked list it currently refers to.
            l1 = l1.next if l1 else None

            # This line updates the pointer l2 to the next node in the linked list it currently refers to.
            l2 = l2.next if l2 else None

        # Remember we want only the output node , but we have created it along with dummy , so
        # return dummy.next that is only the output value to be returned , dummy.next = 7 starting from that
        # return the listnode    
        return dummy.next