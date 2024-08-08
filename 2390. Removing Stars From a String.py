# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 17:43:04 2024

@author: jacin
"""

class Solution(object):
    def removeStars(self, s):
      # Initialize a stack ( list of strings)
      stack = []
      
      # iterate through the string
      for i in s:
        # If the element is * pop the last element from the stack
        # In Python, the expression stack and stack.pop() is a shorthand way of conditionally executing the stack.pop() method only if stack is not empty. 
        if i == "*":
            stack and  stack.pop()
        # Else append the current letter to the stack    
        else:
            stack.append(i)
      
      # Finally we now have a list of elements , so use the join method to convert the list of iterables into a string , so that we can output it 
      return "".join(stack)          




