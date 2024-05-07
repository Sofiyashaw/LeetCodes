# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 16:30:48 2024

@author: jacin
"""

#Write a Python program to check leap year

def leap_year(Year):
    if((Year%400==0)or
       (Year%100!=0)and
       (Year%4==0)):
        print("The year is leap year")
    else:
        print("The year is not a leap year")
        
year=int(input("Enter a year"))

leap_year(year)      