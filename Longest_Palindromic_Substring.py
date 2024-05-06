# -*- coding: utf-8 -*-
"""
Created on Mon May  6 22:35:27 2024

@author: jacin
"""

class Solution(object):
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s

        Max_len = 1
        Max_str = s[0]    
        for i in range(len(s)-1):
            for j  in range(i+1,len(s)):
                if j-i+1 > Max_len and s[i:j+1]==s[i:j+1][::-1]:
                    Max_len = j-i+1
                    Max_str = s[i:j+1]
        return Max_str
s="babad"        
sol = Solution()
sol.longestPalindrome(s)     

