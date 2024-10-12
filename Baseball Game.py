# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:37:29 2024

@author: jacin
"""

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for op in operations:  # Use the correct variable name
            if op == "C":
                if stack:  # Check if stack is not empty
                    stack.pop()  # Invalidate the last score
            elif op == "D":
                if stack:  # Check if stack is not empty
                    stack.append(stack[-1] * 2)  # Double the last score
            elif op == "+":
                if len(stack) >= 2:  # Ensure there are at least two scores
                    stack.append(stack[-1] + stack[-2])  # Sum the last two scores
            else:
                stack.append(int(op))  # Convert the score to an integer
        
        return sum(stack)  # Return the sum of all scores

# Example usage
ops = ["5","2","C","D","+"]
sol = Solution()
print(sol.calPoints(ops))  # Output: 30
