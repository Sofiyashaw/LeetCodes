# -*- coding: utf-8 -*-
"""
Created on Wed May  8 19:45:04 2024

@author: jacin
"""

class Solution(object):
    def reverse(self, x):
       int_min , int_max = -2**31 , 2**31 -1
       sign = -1 if x < 0 else 1
       x = abs(x)
       rev = 0

       while x!= 0:
         pop = x%10
         x //= 10
         rev = rev * 10 + pop
       rev = rev * sign

       if rev < int_min or rev > int_max:
         return 0
       return rev

x =  123
sol = Solution()
sol.reverse(x)        

    