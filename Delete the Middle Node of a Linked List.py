# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:53:36 2024

@author: jacin
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        # Edge case: if the list is empty or has only one node, return None (since the middle would be the only node)
        if not head or not head.next:
            return None

        # Initialize slow and fast pointers at the head
        slow = head  # Slow pointer moves one step at a time
        fast = head  # Fast pointer moves two steps at a time
        prev = None  # This will track the node before the middle node

        # Traverse the list using two pointers: fast moves 2 steps, slow moves 1 step
        while fast and fast.next:
            prev = slow          # Keep track of the node before the middle node
            slow = slow.next     # Move slow pointer by one step
            fast = fast.next.next  # Move fast pointer by two steps

        # At this point, 'slow' is at the middle node, and 'prev' is at the node before the middle
        # Remove the middle node by linking 'prev.next' to the node after 'slow'
        prev.next = slow.next

        # Return the head of the modified list
        return head
