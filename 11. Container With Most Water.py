# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 17:24:03 2024

@author: jacin
"""

class Solution(object):
    def maxArea(self, height):
        #Initialize the result
        res = 0
        #Have left pointer at the beginning 
        l = 0
        #Have right pointer at the end 
        r =len(height) - 1
        # Condition when left pointer is less than right pointer
        while l < r:
            # Calculate the area 
            # (r-l) is the width on x axis and min(height[l],height[r]) is the height on y axis
            area = (r - l) * min(height[l],height[r])
            # Store the max value in the result
            res = max(res,area)

            #These are some conditions to to it quick
            # We need max height
            # If right height is great advance the left pointer
            if height[l] < height[r]:
                l += 1
            #If left height is great advance the right pointer    
            elif height[r] > height[l]:
                r -= 1
            # If both the values of left and right pointer ( Their heights are same)  you can advance            any one   
            else:
                r -= 1
        #Return the result        
        return res                
