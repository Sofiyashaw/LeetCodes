# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 00:26:57 2024

@author: jacin
"""

class Solution:
    def lengthOfLongestSubstring(self,s):
        myset = set()
        start = 0
        maxlength = 0
        for char in range(len(s)):
            while s[char] in myset:
                myset.remove(s[start])
                start += 1
            myset.add(s[char])
            maxlength = max(maxlength , char - start + 1 )
        return maxlength

        