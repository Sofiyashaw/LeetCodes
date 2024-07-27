# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 06:44:52 2024

@author: jacin
"""

class Solution(object):
    def longestSubarray(self, nums):
        #Initialize the start pointer
        start = 0
        # Variable to store the max_length to return it
        max_length = 0
        # Counting the zeros that we are deleting
        zeros_count = 0
        #Iterate through the array
        for i in range(len(nums)):
           # If the value equals zero increment the zero count ( we have to delete one element that should be zero)
           # Let us say we are going to delete it or just not consider it ( remember we are not going to change it we are going to advance the pointer if zero_count is greater than 1)
            if nums[i] == 0:
                zeros_count += 1

                #When zero count is greater than 1 if the starting is 0 , we do zero_count -=1 and advance the start pointer 
            while zeros_count > 1:
                if nums[start] == 0:
                    zeros_count -= 1
                start += 1
                # Update the max_length     
            max_length = max(max_length , i - start + 1)
        # We are doing max_length - 1 because we need to return the output after deleting one element but the array consists of that one_element to be deleted also , so max_length - 1        
        return max_length - 1

nums = [1,1,0,1]
sol = Solution()
sol.longestSubarray(nums)

