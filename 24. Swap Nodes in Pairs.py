# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:21:04 2024

@author: jacin
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        # Base case: if the list is empty or has only one node, no swap is possible
        if not head or not head.next:
            return head  # Return the node itself, not None

        # Identify the first and second nodes to swap
        firstnode = head
        secondnode = head.next

        # Recursive call to swap the remaining pairs of the list
        firstnode.next = self.swapPairs(secondnode.next)

        # Swap the two nodes
        secondnode.next = firstnode 

        # Return the new head (second node)
        return secondnode
