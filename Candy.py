# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:32:59 2024

@author: jacin
"""

class Solution(object):
    def candy(self, ratings):
      n = len(ratings)
      if n== 0:
        return 0

      left = [1] * n
      right = [1] * n

      for i in range(1,n):
        if ratings[i] > ratings[i-1]:
            left[i] = left[i-1] + 1

      for i in range(n-2,-1,-1):
        if ratings[i] > ratings[i+1]:
            right[i] = right[i-1] + 1

      total_candies = 0
      for i in range(n):
        total_candies += max(left[i],right[i])
      return total_candies

ratings = [1,0,2]
sol=Solution()
sol.candy(ratings)                   
