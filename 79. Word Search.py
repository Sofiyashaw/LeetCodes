# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:22:52 2024

@author: jacin
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Gets the row and col of the board
        ROWS , COLS = len(board) , len(board[0])
        # Declare a variable path to keep track of the words we have visited
        path = set()
        

        def dfs(r,c,i):
            # After every dfs call the i when it comes to the iteration which equals the len(word) then 
            # return True
            if i == len(word):
                return True

            # 1) r<0 
            # This checks if the row index r is less than 0,
            # meaning the current search has moved above the first row of the board
            # 2) c < 0
            #  This checks if the column index c is less than 0, meaning the current search 
            # has moved left of the first column of the board.
            # 3) r >= ROWS
            #  This condition checks if the row index r is greater than or equal to ROWS, 
            # meaning the current search has moved below the last row of the board.
            # 4) c >= COLS
            # This condition checks if the column index c is greater than or equal to COLS,
            # meaning the current search has moved right of the last column of the board.
            # 5)  word[i] != board[r][c]
            # This condition checks whether the current character word[i]
            # matches the character in the board at position (r, c).
            # 6)   (r, c) in path
            # This condition checks if the current cell (r, c) has already been visited during
            # the current search. 
            # This prevents revisiting the same cell, which would lead to cycles or 
            # incorrect word matches.
            if (r < 0 or c < 0 or r >= ROWS or c>= COLS or word[i] != board[r][c] or
            (r,c) in path):
                return False
            
            # When you move to a cell (r, c), you add it to the path set to mark it as visited. 
            # This ensures that during the current DFS path, you do not revisit the same cell.
            # Revisiting cells would lead to incorrect results and infinite loops.
            path.add((r,c))
            # The res variable in the DFS function indeed only stores a boolean result,
            # indicating whether a successful path was found. However, it doesn't need to know 
            # which specific recursive call to make next; rather, 
            # it combines the results of all possible directions to decide if a valid path exists
            res = (dfs(r+1 , c , i+1) or
                   dfs(r-1 , c , i+1) or
                   dfs(r, c+1 , i+1) or
                   dfs(r , c-1 , i+1))
            

            # Backtracking
            # After exploring all possible directions from the current cell (r, c), 
            # you remove it from path. This is known as backtracking. 
            # Removing it allows the algorithm to explore new paths from previous cells
            # in future recursive calls.
            path.remove((r,c))
            return res
        
        # for r in range(ROWS):
        # This loop iterates over each row in the board. ROWS is the total number of rows in the board.
        # for c in range(COLS): 
        # Nested within the row loop, this loop iterates over each column in the current row. 
        # COLS is the total number of columns in the board.
        for r in range(ROWS):
            for c in range(COLS):
                # Calls the dfs (Depth-First Search) function starting from the cell (r, c) and 
                # initial index 0, which corresponds to the first character of the word.
                # The dfs function will attempt to find the word starting from this cell by 
                # exploring all valid paths.
                # If the dfs function returns True, it means that starting from cell (r, c), 
                # the word can be found on the board. The exist function then immediately 
                # returns True, indicating that the word exists on the board.
                if dfs(r,c,0):
                 return True
        #The exist function will then return False, indicating that the word does 
        # not exist on the board.
        return False



# Initialize Board Dimensions:
# ROWS = 3, COLS = 3

# Define DFS Function:
# dfs(r, c, i) will check if the word starting from (r, c) and index i can be formed.

# Base Cases in DFS:
# Word Found: If i equals 6 (length of "ABCCED"), return True.

# Out of Bounds or Mismatch: Return False.

#Mark the Path:
# Track cells in a set path to avoid revisiting them in the same path.

#Explore Directions:
#From (0, 0) with i = 0, explore:
#Down: dfs(1, 0, 1) (to 'S')
#Up: Out of bounds
#Right: dfs(0, 1, 1) (to 'B')
#Left: Out of bounds
#Continue DFS from valid directions:

#From (0, 1) with i = 1 (found 'B'), explore:
#Down: dfs(1, 1, 2) (to 'F')
#Right: dfs(0, 2, 2) (to 'C')
#Up: Out of bounds
#Left: Out of bounds
#Backtrack:

#After exploring all directions from a cell, remove that cell from path.
#Main Function Logic:

#Iterate over all cells:
#Start DFS from (0, 0): check if the word can be formed.
#Continue until either a valid path is found or all cells are checked.
