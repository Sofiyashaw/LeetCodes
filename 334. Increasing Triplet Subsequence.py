# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:21:39 2024

@author: jacin
"""

class Solution(object):
    def increasingTriplet(self, nums):
        # Initialize first and second to a large value
        first = second = float('inf')
        #Iterate through he array
        for n in nums:
            # The first value will be default stored in first
            if n<= first:
                first = n
            # Here comes second if the second is greater than one it gets stored here    
            elif n<= second:
                second = n
            # If a number greater than both first and second then return True    
            else:
                return True

        # If there is no such triplet return False
        return False        
