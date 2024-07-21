# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:18:43 2024

@author: jacin
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Always ensure that str1 should be greater if not swap
        if len(str2) > len(str1):
            str1 , str2 = str2 , str1
        # if both strings are equal then return one string
        #Base case in recursion (If base case is reached recursion stops)   
        if str1 == str2:
            return str1
        #if str2 is not a substring of the first part of string1 then return ""    
        if str1[:len(str2)] != str2:
            return ""


        #str1[len(str2):] takes the substring of str1 starting from the index len(str2) to the end of str1.
        #This effectively removes the prefix of str1 that matches str2.
        #The function then calls itself with this new substring of str1 and the original str2
        #Recursion
        return self.gcdOfStrings(str1[len(str2):],str2) 


        #self. is used as we are defining the method inside the class and python needs tto know it


        