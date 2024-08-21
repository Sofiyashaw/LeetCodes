# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 17:51:23 2024

@author: jacin
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        # Initialize slow and fast to the head
        slow,fast = head,head
        # Set the prev as None
        prev =  None
        
        # Step 1: Reverse the first half of the linked list using slow pointer
        while fast and fast.next:
            # Advance two steps 
            # Move fast two steps forward (fast now points to 2).
             fast = fast.next.next

             # tmp = slow.next holds the pointer to the node 4 from (as slow points to the head)
             tmp = slow.next
             # slow.next pointer points to None , in this case reversed
             slow.next = prev

             # Now advance the prev from None to slow(5)(slow initially pointed to head)
             prev = slow
             # slow(5) to tmp(tmp is already slow.next)
             slow = tmp
             # Continue to do it until the fast and fast.null doesn't equal to null
             # If it goes out then exit the loop


        # Calculate the result value     
        res = 0
        # Continue until slow doesn't become null
        while slow:
            # prev.val is the left part and slow.val is the right part
            # prev.val = 4 and slow.val = 2
            res = max(res,prev.val+slow.val)
            # now as the first half is reveresed when you do prev.next it goes in the opp direction
            # and chooses the first node in this case 5
            prev = prev.next
            # slow.next points to 1 here
            slow = slow.next
        # return the result    
        return res
        