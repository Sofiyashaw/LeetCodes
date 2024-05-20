# -*- coding: utf-8 -*-
"""
Created on Tue May 21 00:30:17 2024

@author: jacin
"""

class Solution(object):
    def majorityElement(self, nums):
       candidate=None
       count=0

       for num in nums:
         if count==0:
            candidate=num
            count=1
         elif num==candidate:
            count+=1
         else:
            count-=1

       count=0
       for num in nums:
            if num==candidate:
                count+=1
       return candidate

sol=Solution()
nums = [3,2,3]                           
sol.majorityElement(nums)        