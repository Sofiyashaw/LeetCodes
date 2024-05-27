# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:26:49 2024

@author: jacin
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        start_station = 0
        total_tank = 0
        curr_tank = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                start_station = i+1
                curr_tank = 0

        return start_station if total_tank >= 0 else -1

gas = [1,2,3,4,5] 
cost = [3,4,5,1,2]   
sol = Solution()
sol.canCompleteCircuit(gas, cost)             
