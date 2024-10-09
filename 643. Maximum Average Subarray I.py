# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 06:42:23 2024

@author: jacin
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        # Calculate the sum of first k elements
        sum_vals = sum(nums[:k])
        # Store it in the max sum
        max_sum = sum_vals
        
        # Initialize pointers
        start_index = 0
        end_index = k

        # while end_index < len(nums)
        while end_index < len(nums):
            
            # Sliding window starts here
            # Subtract the previous value
            sum_vals = sum_vals - nums[start_index]
            # Advance the pointer
            start_index = start_index + 1
            
            # Add the next value
            sum_vals = sum_vals + nums[end_index]
            #Advance the pointer
            end_index = end_index + 1

            max_sum = max(max_sum, sum_vals)
        
        
        return float(max_sum) / k

nums = [1, 12, -5, -6, 50, 3]
k = 4
sol = Solution()
print(sol.findMaxAverage(nums, k))  
