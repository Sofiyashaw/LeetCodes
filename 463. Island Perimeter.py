# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:25:40 2024

@author: jacin
"""

class Solution(object):
    def islandPerimeter(self, grid):
      
      # A set named visit is initialized. 
      # It will be used to keep track of the coordinates (cells) 
      # that have already been visited during the depth-first search (DFS) traversal. 
      # This prevents counting the perimeter of the same land cell multiple times.
      visit = set()
      
      
      # This defines a nested helper function dfs(i, j) that performs 
      # a depth-first search starting from the cell at position (i, j)
      def dfs(i,j):
        
        
        # This checks whether the current cell (i, j) is out of bounds (i.e., it's outside the grid) or if it is water (grid[i][j] == 0).
        # If so, it means the current cell contributes 1 to the perimeter of the island, and the function returns 1.
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return 1
        
        
        # This checks if the cell (i, j) has already been visited. 
        # If so, it returns 0 because visiting the same land cell again does not add to the perimeter.    
        if (i,j) in visit:
            return 0
        
        
        # The current cell (i, j) is added to the visit set to mark it as visited. 
        # This ensures we don't process it again in future DFS calls.    
        visit.add((i,j))

        perim = 0

        # These lines perform DFS in all four possible directions: right, down, up, and left. 
        # For each neighboring cell, the perimeter contribution is added to perim. 
        # The dfs function is called recursively for each neighbor.
        #dfs(i, j + 1) explores the cell to the right.
        #dfs(i + 1, j) explores the cell below.
        #dfs(i - 1, j) explores the cell above.
        #dfs(i, j - 1) explores the cell to the left.
        perim += dfs(i , j+1)
        perim += dfs(i+1 , j)
        perim += dfs(i-1 , j)
        perim += dfs(i , j-1)

        # After exploring all neighboring cells, the total perimeter calculated for the current cell is returned.
        return perim

      # These lines iterate over each cell in the grid using a nested loop.
      # The outer loop iterates over the rows (i).
      # The inner loop iterates over the columns (j).
      # When a land cell (grid[i][j] == 1) is found, the DFS function is called starting from that cell. 
      # The function then returns the perimeter of the island.  
      for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return dfs(i,j)       