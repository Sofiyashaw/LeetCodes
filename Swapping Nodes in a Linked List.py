# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:52:47 2024

@author: jacin
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # This holds the value of the node
        self.next = next  # This is a pointer to the next node

class Solution:
    def swapNodes(self, head, k):
        cur = head  # Step 1: Initialize cur to point to the head of the linked list
        
        # Step 2: Traverse to the k-th node from the beginning
        for i in range(k - 1):  # Move to the (k-1)th node
            cur = cur.next  # Move cur to the next node
        
        left = cur  # Step 3: left now points to the k-th node from the start
        right = head  # Step 4: Initialize right to point to the head
        
        # Step 5: Move both pointers until cur reaches the end
        while cur.next:  # Continue until cur is at the last node
            cur = cur.next  # Move cur to the next node
            right = right.next  # Move right to the next node
        
        # Step 6: Swap the values of left and right nodes
        left.val, right.val = right.val, left.val  # Swap values
        
        return head  # Return the modified list starting from head
