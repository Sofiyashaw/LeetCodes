# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 14:17:45 2024

@author: jacin
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
       #  Rows = 3           Because there are 3 lists (rows) in the matrix
       #  Columns = 4        Because there are 4 elements in the first row of the matrix.
        ROWS, COLS = len(matrix) , len(matrix[0])
       
       # top index = 0
       # bottom index = rows - 1 (as it is index)
        top , bot = 0 , ROWS - 1

       # while top <= bot iterate 
        while top <= bot:
            # The row is like mid in binary search 
             row = (top+bot) // 2
             # matrix[row][-1] refers to the last element of the current row.
             # If the target is greater than that , it has to be in the next rows , so advance top
             if target > matrix[row][-1]:
                top = row + 1
             # matrix[row][0] refers to the first element of the current row.
             # If the target is less than that then it has to be previous rows , so advance the bottom 
             elif target < matrix[row][0]:
                bot = row - 1
             # If neither is neither then the target is in that row so break the loop
             # We can do the condition for it laterin the program   
             else:
                break

        # After the while loop, if top exceeds bot, it means no row contains the target, 
        # so the function returns False.        
        if not(top <= bot):
            return False

        # If it is in that row do these calculations like a simple binary search
        # A simple binary search is  performed    
        row =  (top + bot) // 2
        l , r = 0,COLS -1
        while l <= r:
            m = (l+r) // 2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True   
        return False                               