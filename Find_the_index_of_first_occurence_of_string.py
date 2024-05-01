# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:33:24 2024

@author: jacin
"""

class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)-len(needle)+1):
           if haystack[i:i+len(needle)]==needle:
            return i
        return -1    
sol = Solution()
haystack = "sadbutsad"
needle = "sad"
sol.strStr(haystack,needle)    
            