# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 09:12:02 2024

@author: jacin
"""

class Solution(object):
    def equalPairs(self, grid):
        
        # from collections import defaultdict
        # Create a dictionary for all the rows in the grid
        row_counts = defaultdict(int)
        
        # Initialize the count as 0
        count = 0
        
        # For each row in grid
        for row in grid:
        
        
        # If we have to initialize a value in dictionary , first we need the name of dictionary i,e      row_counts . Convert the list in grid to tuple as only tuple value can be added to dictionary and not a list . Convert the grid values to tuple and accoding to the number of times they appear , change the value part in the dictionary.'''
        # row_counts = defaultdict(int, { (3, 2, 1): 1, (1, 7, 6): 1, (2, 7, 7): 1 }) '''
            row_counts[tuple(row)] += 1

        
        # zip(*grid) transposes the matrix 
        for column in zip(*grid): 



         # For column (3, 1, 2)
         # count: 0 + row_counts[(3, 1, 2)] -> 0 + 0 = 0
    
         # For column (2, 7, 7)
         # count: 0 + row_counts[(2, 7, 7)] -> 0 + 1 = 1
    
         # For column (1, 6, 7)
         # count: 1 + row_counts[(1, 6, 7)] -> 1 + 0 = 1
            count += row_counts[column]  

        # Return the count    
        return count

grid = [[3,2,1],[1,7,6],[2,7,7]] 
sol = Solution()
sol.equalPairs(grid)  
