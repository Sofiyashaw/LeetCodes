# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:57:59 2024

@author: jacin
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        trimmed = s.strip()
        words = trimmed.split()
        last_word = words[-1]
        return len(last_word)

s = "Hello World"
sol=Solution()
sol.lengthOfLastWord(s)

