# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:44:57 2024

@author: jacin
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
       merged = sorted(nums1 + nums2)
       n = len(merged)
       if n % 2 == 0:
           return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
       else:
           return merged[n // 2]  

nums1 = [1,3]            
nums2 = [2]
sol = Solution()
sol.findMedianSortedArrays(nums1,nums2)
