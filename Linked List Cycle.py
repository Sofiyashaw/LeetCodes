# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 13:56:49 2024

@author: jacin
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):   
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

def createLinkedList(arr, pos):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    cycle_node = None
    
    if pos == 0:
        cycle_node = head
    
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
        if i == pos:
            cycle_node = current
    
    if pos != -1:
        current.next = cycle_node
    
    return head

# Example inputs
head = [3, 2, 0, -4]
pos = 1

# Create the linked list with a cycle
linked_list_head = createLinkedList(head, pos)

# Test the hasCycle function
sol = Solution()
print(sol.hasCycle(linked_list_head))  # Expected output: True
