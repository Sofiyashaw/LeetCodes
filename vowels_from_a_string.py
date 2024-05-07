# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 08:59:46 2024

@author: jacin
"""

#Write a Python Program to find vowels from a string

def get_vowels(string):
    return[each for each in string if each in "aeiou"]

get_string="hello"

print("The vowels are",get_vowels(get_string))
        