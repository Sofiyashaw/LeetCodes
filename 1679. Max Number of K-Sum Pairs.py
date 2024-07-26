# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 17:24:40 2024

@author: jacin
"""

class Solution(object):
    def maxOperations(self, nums, k):
        #Initialize left pointer
        left = 0
        #Initialize right pointer
        right = len(nums) - 1
        #Initialize n to store the number of operations performed
        n = 0
        #Sort the array
        nums.sort()
        # While left pointer is less than right pointer
        while left < right:
            # When sum of left and right element is equal to k
            if nums[left] + nums[right] == k:
                #Advance the left pointer
                left += 1
                #Advance the right pointer
                right -= 1
                # Increment the value of n
                n += 1
            # If the k value is greater advance the right pointer    
            elif nums[left] + nums[right] > k:
                right -= 1
            # Else advance the left pointer    
            else:
                left += 1
        return n                

        