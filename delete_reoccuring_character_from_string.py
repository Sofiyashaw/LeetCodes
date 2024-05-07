# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 12:58:42 2024

@author: jacin
"""

#Given a string as your input , delete any reoccuring character and return the new string

def duplicate_string(input_string):
    seen=set()
    result=''
    
    for char in input_string:
        if char not in seen:
            result+=char
            seen.add(char)
    return result

input_str="hellogorg"
result_str=duplicate_string(input_str)
print(result_str)