# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 20:27:00 2024

@author: jacin
"""

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total_poisoned_time = 0
        
        for i in range(1, len(timeSeries)):
            # The poison duration is either the full 'duration' or the time between two attacks, whichever is smaller.
            total_poisoned_time += min(timeSeries[i] - timeSeries[i-1], duration)
        
        # Add the poison time from the last attack.
        total_poisoned_time += duration
        
        return total_poisoned_time
