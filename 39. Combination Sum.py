# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:59:40 2024

@author: jacin
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize the result list to store all valid combinations.
        res = []
        
        # Define the recursive function for Depth First Search (DFS)
        # i: current index in the candidates array
        # cur: the current combination (list of numbers)
        # total: the sum of the current combination
        def dfs(i, cur, total):
            # Base case: if the sum of the current combination equals the target
            if total == target:
                # Add a copy of the current combination to the result list
                res.append(cur.copy())  # cur.copy() ensures we're appending the current state, not a reference
                return  # End this path of recursion as we found a valid combination

            # Base case: if index exceeds array length or total exceeds target, stop exploring further
            if i >= len(candidates) or total > target:
                return  # End this path of recursion because it's invalid

            # Include the current candidate in the combination and explore further
            cur.append(candidates[i])  # Add the current candidate to the combination
            dfs(i, cur, total + candidates[i])  # Recur by considering the current candidate again (allow reuse)

            # Backtrack: remove the last element to explore other combinations
            cur.pop()  # Remove the last added element to backtrack and try the next candidate

            # Exclude the current candidate and move to the next one
            dfs(i + 1, cur, total)  # Recur by moving to the next candidate without including the current one

        # Start the DFS process with the initial values (starting index, empty combination, and total sum of 0)
        dfs(0, [], 0)

        # Return the result list containing all valid combinations
        return res
