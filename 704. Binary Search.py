# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 14:17:16 2024

@author: jacin
"""

class Solution(object):
    def search(self, nums, target):
        l , r = 0  , len(nums) - 1
        # we are giving l + to find the next next middle values
        # First value l = 0 but for consecutive middle values we need to add up l
        
        while l <= r:
           m =  l + ((r-l)// 2)
           if target > nums[m]:
              l = m + 1
           elif target < nums[m]:
              r = m -1 
           else:
              return m
        return -1   

