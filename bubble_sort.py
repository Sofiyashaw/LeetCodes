# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:51:37 2024

@author: jacin
"""


#Write a program to execute the bubble sort algorithm.
'''Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. '''

def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
arr=[78,56,34,67,23,89]   
bubble_sort(arr) 
print("Sorted array is",arr)            