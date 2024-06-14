# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 18:37:47 2024

@author: jacin
"""

class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2

        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        
        return ways[n]

# Example usage
n = 5
sol = Solution()
print(sol.climbStairs(n))  # Output should be 8
