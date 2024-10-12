# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:37:48 2024

@author: jacin
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and i < 0 < stack[-1]:
                if stack[-1] < abs(i):
                    stack.pop()
                    continue
                elif stack[-1] == abs(i):
                     stack.pop()
                break
            else:
                stack.append(i)
        return stack
               