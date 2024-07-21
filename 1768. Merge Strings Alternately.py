# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:17:37 2024

@author: jacin
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""

        for w1,w2 in zip(word1,word2):
            ans = ans + w1 + w2

        if  len(word1) > len(word2):
            ans = ans + word1[len(word2):]   

        elif len(word2) > len(word1):
            ans = ans + word2[len(word1):] 

        return ans

word1 = "abc" 
word2 = "pqr"
sol = Solution()
sol.mergeAlternately(word1,word2)



