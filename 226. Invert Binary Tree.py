# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 08:51:14 2024

@author: jacin
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self,root):
        # If there is no root , root is null return None
        # The base case if not root: simply checks if the current node (root) is None. 
        # This condition becomes True when:
        # The function is called on a None node, which means there’s no left or right child
        # for the current node.
        if not root:
            return None
        
        # If not swap the first row of elements
        # tmp = 2 , root.left = 7 , root.right = 2
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        # We are calling the function again as it is a recursion to perform on the next set of rows in
        # the tree
        # It swaps the next set of elements and returns the root value
        # 
        self.invertTree(root.left)
        self.invertTree(root.right)    
        return root