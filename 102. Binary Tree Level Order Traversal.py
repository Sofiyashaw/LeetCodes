# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 08:53:56 2024

@author: jacin
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self,root):
        # final list
        res = []
        
        # Initialize queue in python
        q = collections.deque()
        # Appends one element to the queue , adds root value 3
        q.append(root)

        # While q is non empty
        while q:
            # Get the length of the queue (number of nodes at the current level)
            qLen = len(q)
            # Appends the value in level for each row
            level = []
            # Iterating through elements in a complete row/level
            for i in range(qLen):
                # This means pop the leftmost element of the queue and store it in node
                node = q.popleft()
                # When the node is not null
                if node:
                    # Add that popped value to the level
                    level.append(node.val)
                    # After popping a element of q from the left add its children to the queue
                    q.append(node.left)
                    q.append(node.right)
            # Finally when the level's are not null        
            if level:
                # Add all the sublevels (separate lists) to a single list
                res.append(level)
        return res       

 # Algorithm
 # Add a ele to the queue and calculate the length
 # for every ele in that level , pop the leftmost ele , and add it to the level , if the ele has children add them to the queue
 # continue to do it for all the ele in the level (only 2) as its a binary tree
 # finally combine all the levels(single lists) into the list res 
 # return the final list of lists


