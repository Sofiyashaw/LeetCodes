# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:21:40 2024

@author: jacin
"""

class Solution(object):
    def findMin(self,nums):
        res = nums[0]
        l , r = 0 , len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res , nums[l])
                break
            m = (l+r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
               l = m + 1
            else:
               r = m - 1    
        return res
nums = [3,4,5,1,2]   
sol = Solution()
sol.findMin(nums)     