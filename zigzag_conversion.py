# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:58:14 2024

@author: jacin
"""

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or  numRows >= len(s):
            return s

        rows = [''] * numRows
        index , step = 0,1

        for char in s:
            rows[index] += char
            if index == 0:           # Specifying the direction
                step = 1
            elif index == numRows - 1:
                step = -1
            index = index + step
        return ''.join(rows)

s = "PAYPALISHIRING"
numRows = 3
sol = Solution()
sol.convert(s, numRows)
