# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 22:03:38 2024

@author: jacin
"""

class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i],dp[i-coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1   

coins = [1,2,5]
amount = 11
sol = Solution()
sol.coinChange(coins, amount)
