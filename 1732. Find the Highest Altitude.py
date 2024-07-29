# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 18:47:08 2024

@author: jacin
"""
class Solution(object):
    def largestAltitude(self, gain):
        
        current_altitude = 0
        highest_altitude = 0
    
        for g in gain:
            current_altitude += g

            if current_altitude > highest_altitude:
               highest_altitude = current_altitude
        return highest_altitude

