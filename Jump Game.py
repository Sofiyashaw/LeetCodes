# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:51:01 2024

@author: jacin
"""

class Solution(object):
    def canJump(self, nums):
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest , i+nums[i])   

            if farthest >= len(nums) - 1:
                return True

        return False
nums = [2,3,1,1,4]
sol = Solution()
sol.canJump(nums)                