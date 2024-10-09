# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 06:43:52 2024

@author: jacin
"""

class Solution(object):
    def longestOnes(self, nums, k):
        #Variable to store zero_count
        zero_count = 0
        # Initialize start pointer
        start = 0

        # Variable to store max_ones
        max_ones = 0
        

        #Sliding window
        # Iterate through the array
        for i in range(len(nums)):
            # If you find a 0 increment the zero_count
            if nums[i] == 0:
                zero_count += 1  

            
            # When the zero_count value gets greater than k
            while zero_count > k:   
                # Check if the start index is 0  if thats so reduce the zero_count
                # If the start index is not 0 then advance the start pointer until you find a zero and  decrement the zero count
                if nums[start] == 0:
                    zero_count -= 1  
                elif nums[start] == 1:
                    pass
                start += 1
             
            # We calculate the number of ones by subtracting the start - end and then add one because if you have to find the value as 6(we subtract the i-start+1 (5-0+1) think)
            max_ones = max(max_ones, i - start + 1)  
            

        return max_ones


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
sol = Solution()
print(sol.longestOnes(nums, k))  
