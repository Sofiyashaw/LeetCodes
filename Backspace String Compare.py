# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:36:19 2024

@author: jacin
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stack1 = []
        for i in s:
            if i == "#":
               stack and stack.pop()
            else:
                stack.append(i)
        result = "".join(stack)
        for i in t:
            if i == "#":
                stack1 and stack1.pop()
            else:
                stack1.append(i)
        result1 = "".join(stack1)

        if result == result1:
            return True
        else:
            return False