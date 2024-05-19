# -*- coding: utf-8 -*-
"""
Created on Sun May 19 22:46:20 2024

@author: jacin
"""
class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i] = nums[j]
                i += 1
        return i

nums = [3,2,2,3]
val = 3   
sol = Solution()    
sol.removeElement(nums, val)  
