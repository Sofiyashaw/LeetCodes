# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:23:43 2024

@author: jacin
"""

#Python program to find area of circle

def circ_area(rad):
    pi=3.142
    return pi*(rad*rad)

rad=float(input("Enter the radius of circle:"))
print("Area of circle is",circ_area(rad))

