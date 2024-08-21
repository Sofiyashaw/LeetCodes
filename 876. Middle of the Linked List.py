# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 17:57:21 2024

@author: jacin
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        # Initialize 2 pointers to head
        slow , fast = head , head
        # While both fast and fast.next is not null
        while fast and fast.next:
            # Advance slow pointer by one step
            slow = slow.next
            # Advance fast pointer by 2 step
            fast = fast.next.next
        # Return the slow pointer
        # Middle node of the linked list    
        return slow     