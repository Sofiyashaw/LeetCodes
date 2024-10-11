# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:51:53 2024

@author: jacin
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Create a dummy node pointing to the head of the linked list.
        # This helps handle edge cases, such as removing the head node.
        dummy = ListNode(0, head)
        
        # Initialize two pointers: left starting at dummy and right starting at head.
        left = dummy
        right = head

        # Move the right pointer n nodes ahead in the list.
        while n > 0 and right:
            right = right.next  # Move right to the next node
            n -= 1              # Decrease n by 1
        
        # Move both pointers until the right pointer reaches the end of the list.
        while right:
            left = left.next   # Move left to the next node
            right = right.next # Move right to the next node
        
        # Skip the nth node from the end by adjusting the next pointer of the left pointer.
        left.next = left.next.next

        # Return the head of the modified list, which is next of the dummy node.
        return dummy.next
