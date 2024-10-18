# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:47:40 2024

@author: jacin
"""

class Solution:
    def twoSum(self,nums,target):
        hashmap = {}

        for i,num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [i,hashmap[complement]]
            hashmap[num] = i
            