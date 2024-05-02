# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:18:17 2024

@author: jacin
"""

class Solution(object):
  def lengthOfLongestSubstring(self, s):
    left = 0
    right = 0
    max_len = 0
    seen = set()

    while right < len(s):
        if s[right] not in seen:
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1
        else:
            seen.remove(s[left])
            left += 1
    return max_len
s="abcabcbb"        
sol =  Solution()
sol.lengthOfLongestSubstring(s)