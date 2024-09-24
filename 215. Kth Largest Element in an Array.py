# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:43:24 2024

@author: jacin
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # k = index of the value we are trying to find when the array is sorted , it will be sorted
        # quick select
        k = len(nums) - k 

        # RECURSIVE QUICK SELECT ALGORITHM
        # Everytime the subarray we are looking for changes we pass in 2 parameters l & r pointers
        def quickselect(l,r):
            # pivot is the value at nums[r]
            # p pointer is at the left
            pivot , p = nums[r] , l
            
            # iterate through the array except the last element r 
            # cus we are doing it keeping in mind that the last element is pivot 
            # cuz its easier that way
            for i in range(l,r):
                # If the element at i is less than or equal to pivot
                # swap it with the leftmost value 
                if nums[i] <= pivot:
                    nums[i] , nums[p] = nums[p] , nums[i]
                    # increment the p pointer
                    p += 1
            # after getting all the elements less than pivot on the left side
            # swap the pivot ele (nums[r]) with the nums[p]
            nums[p] , nums[r] = nums[r] , nums[p]
            # now nums[p] is the pivot


            # Now 1st set of sorting is over
            # Recursively call the quickselect for each subarray 
            # When k is less than p , run quickselect on the first half of the array
            if k < p : return quickselect( l , p - 1)
            # When k is greater than p , run quickselect on the second half of the array
            elif k > p : return quickselect( p+1 , r)
            # when the k and pivot are same
            else : return nums[p]
            
        # Now call the function with values of l and right pointer
        # return the output of the quickselect function
        return quickselect(0,len(nums)-1)