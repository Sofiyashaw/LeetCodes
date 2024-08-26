# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 23:43:48 2024

@author: jacin
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Iinitialize 2 pointers one to 1 and another to max(piles) in ex-1 11
        l , r = 1, max(piles)
        # let res be the max(piles) as that is the max possible value of k
        # We need to find the minimum one  
        res = r
        
        # While both the pointers don't cross each other
        while l <= r:
            # Take he value at l and r add them up and divide it by 2
            k = (l + r)//2
            # Start with hours as 0
            hours = 0

            # Iterate through piles
            for p in piles:
                # ceil
                # ceil(4.2) becomes 5
                # ceil(7.8) becomes 8
                hours += math.ceil(p / k)
                
            # Checking if the hours we calculated is less than the actual hours
            if hours <= h:
                res = min(res , k)
                # If the hours <= h try for lesser values of k
                # Update the pointer
                r = k -1
            # If hours>= h then it means the value of k we are taking is too small so advance it the 2nd half of the
            # piles array for bigger values of k
            else:    
                # 2nd half of piles
                l = k + 1
        return res        
