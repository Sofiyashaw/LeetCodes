# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:59:21 2024

@author: jacin
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self,root):
        res = []
        stack = []
        # Initialize current node to the root node
        # This is a pointer
        cur = root
        
    # while the pointer is not null or til the stack is non emmpty continue to do execute the   loop
        while cur or stack:
            # While cur is not null
            while cur:
                # Append the node to the stack 
                stack.append(cur)
                # Initially just go left according to the algorithm given below
                cur = cur.left
            # When the cur is null
            # Pop from the stack and pointer cur points to the popped node
            cur = stack.pop()
            # Append the popped value to res 
            res.append(cur.val)
            # Once a value is popped (since we have aldready gone completely left noe check right)
            cur = cur.right
        return res    


# The algo is simiar to a in-order traversal , except we go left completey in the beginning and then we go to root and then go right
# In-order traversal = left -> root -> right
# Algorithm
# In - order traversal we are doing it iteratively hence we are using a pointer and a stack
# Stack and one pointer approach
# 1) Whenever a pointer points to a node add it to the stack    
# 2) Go towards the left till there is no node on the left
# 3) When there is no node on the left , then pop one node from the stack and add it the res and the pointer points to the popped node
# 4) After popping a node from the stack now check the right node to the current node which the pointer points to     
# 5) If the right node is there then add it to the stack if not pop another node from the stack ( always pop the top of the stack)
# 6) Continue this process untill all the nodes have been traversed