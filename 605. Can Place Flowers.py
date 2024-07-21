# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:19:53 2024

@author: jacin
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True

        planted = 0

        for i in range(len(flowerbed)):
            leftisempty = (i==0) or flowerbed[i-1]==0
            rightisempty = i==len(flowerbed)-1  or flowerbed[i+1]==0

            if flowerbed[i]==0 and leftisempty and rightisempty:
               flowerbed[i]=1
               planted +=1

               if(planted==n):
                    return True
                
        
