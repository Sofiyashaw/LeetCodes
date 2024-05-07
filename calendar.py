# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 08:45:10 2024

@author: jacin
"""

#Write a python program to display the calendar

import calendar

year=int(input("Enter the year: "))
month=int(input("Enter the month: "))

print(calendar.month(year,month))