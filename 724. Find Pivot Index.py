# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 18:47:45 2024

@author: jacin
"""

class Solution(object):
    def pivotIndex(self, nums):
        #Calculate the total sum
        total_sum = sum(nums)
        # Initialize the left_sum variable to 0
        left_sum = 0

        #Iterate through the array
        for i in range(len(nums)):
            # Calculate the right_sum
            right_sum = total_sum - left_sum - nums[i]

            # If left_sum and right_sum are equal return the index
            if left_sum == right_sum:
                return i

            # Keep updating the left sum for each i value
            left_sum += nums[i]
        # If right and left sum never equals return -1
        return -1      