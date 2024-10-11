# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:54:08 2024

@author: jacin
"""

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to act as the starting point of the merged list
        dummy = ListNode(0)
        # `current` pointer to keep track of the last node in the merged list
        current = dummy
        
        # Loop until either list1 or list2 is exhausted
        while list1 and list2:
            # Compare the values of the current nodes of list1 and list2
            if list1.val <= list2.val:
                # If the current node in list1 has a larger value,
                # append it to the merged list
                current.next = list1
                # Move to the next node in list1
                list1 = list1.next
            else:
                # Otherwise, append the current node in list2 to the merged list
                current.next = list2
                # Move to the next node in list2
                list2 = list2.next
            # Move the current pointer to the last node in the merged list
            current = current.next
        
        # If there are remaining nodes in either list1 or list2, append them
        if list1:
            current.next = list1  # Attach the remaining nodes from list1
        elif list2:
            current.next = list2  # Attach the remaining nodes from list2
        
        # Return the head of the merged list, which starts after the dummy node
        return dummy.next
