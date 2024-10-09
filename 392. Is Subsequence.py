# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 17:23:02 2024

@author: jacin
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize 2 pointers i and j
        i = 0
        j = 0
        # While both i and j are less than len(str)
        while i < len(s) and j < len(t):
            # If both the characters are equal then advance both the array
            if s[i]==t[j]:
                i += 1
                j += 1
            # If its not equal only advance j pointer    
            else:    
                j+=1

        # If the end of array is reached return True else return False
        return True if i == len(s) else False       
