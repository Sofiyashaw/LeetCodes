# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:20:17 2024

@author: jacin
"""

class Solution(object):
    def reverseVowels(self, s):
          # Two Pointers
          # Create a set as it uses O(1) complexity
          vowels = set("aeiouAEIOU")
          #Convert string to list as it is mutable
          s = list(s)
          #Initialize pointer 1
          left = 0
          #Initialize pointer 2
          right = len(s)-1
          
          #Continue as long as the two pointers dont cross each other, if they do come out of the loop
          while left < right:
            if s[left] not in vowels:
                left+=1
            elif s[right] not in vowels:
                right-=1
            
            #If both are vowels swap
            else:
                s[right],s[left] = s[left],s[right]
                left +=1
                right -=1
          # Return as a string as it is asked in the output      
          return "".join(s)

s = "hello"
sol=Solution()
sol.reverseVowels(s)


