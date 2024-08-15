# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:03:55 2024

@author: jacin
"""

class Solution(object):
    def decodeString(self, s):
        #Initialize a stack
        stack = []
        
        # Iterate through the string s
        for i in range(len(s)):
            # Add elements from string s to stack until you find a ] 
            if s[i] != "]":
                stack.append(s[i])
            # When you encounter a ]     
            else:
                # Create a substr
                substr = ""
                # This means when you find a ] when the top of stack not equal to [
                # You are basically poping all the elements in between those 2 brackets
                while stack[-1] != "[":
                    # Add the popped elements to the substr
                    substr = stack.pop() + substr
                # Now after adding the popped element to the substr also pop [ 
                stack.pop()
                
                # Now initialize a string k for storing the number
                k = ""
                # while stack has elements and the top of the stack is a digit
                while stack and stack[-1].isdigit():
                    # Pop the digit and add it to k
                    k = stack.pop() + k
                # Now we multiply the substr by k times and add it back to the stack
                # Adding back to the stack is done for nested brackets, so that it gets multipled by the parent bracket too(only in case of nested)   
                stack.append(int(k) * substr) 
        # The output is needed as a string , so conver the stack to a string and return it
        return "".join(stack)   


