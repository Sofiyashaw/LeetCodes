# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 17:22:21 2024

@author: jacin
"""

class Solution(object):
    def moveZeroes(self, nums):
        # start position left pointer
        l = 0
        # right pointer (iterate through the array)
        for r in range(len(nums)):
            # When r is 0 pass
            if nums[r]==0:
                pass
            # When r is a non-zero value 
            else:
            #Swap both the values 
               nums[l],nums[r] = nums[r],nums[l]
            # Advance the left pointer
               l+=1
        return nums



