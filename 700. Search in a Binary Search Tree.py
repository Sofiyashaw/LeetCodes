# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 08:58:40 2024

@author: jacin
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        # If the value we are trying to search is the root then return it 
        # In a binary tree, each node points to its left and right subtrees. 
        # So, when you return a node (in this case, root), 
        # you are returning that node along with all of its descendants 
        # (its entire left and right subtrees).
        # Base case , whenener the value equals then it returns the root along with its subtrees
        if root is None or root.val == val:
            return root
        
        # If the value we are trying to search is greater then call the function recursively using
        # root.right
        elif root.val < val:
            return self.searchBST(root.right,val) 

        # else search in the left
        else:
            return self.searchBST(root.left,val)      



