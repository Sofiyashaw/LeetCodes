# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:25:17 2024

@author: jacin
"""

class Solution(object):
    def maxProfit(self, prices):
       min_price=float('inf')
       max_profit=0
       for price in prices:
         if price<min_price:
            min_price = price
         elif  price-min_price > max_profit:
            max_profit = price-min_price
       return max_profit
prices = [7,1,5,3,6,4]        
sol=Solution()      
sol.maxProfit(prices)      
        