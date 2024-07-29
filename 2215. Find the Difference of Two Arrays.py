# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 18:48:22 2024

@author: jacin
"""

class Solution(object):
    def findDifference(self, nums1, nums2):
       nums1Set , nums2Set = set(nums1) , set(nums2)
       res1 , res2 = set() , set()

       for n in nums1:
        if n not in nums2:
            res1.add(n)

       for n in nums2:
        if n not in nums1:
            res2.add(n)

       return[list(res1),list(res2)]   
nums1 = [1,2,3]
nums2 = [2,4,6]
sol = Solution()
sol.findDifference(nums1, nums2)       
