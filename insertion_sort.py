# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:13:01 2024

@author: jacin
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = [12, 11, 13, 5, 6]
print("Original array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)


'''Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It iterates over the input list and at each iteration, it removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. This process is repeated until the entire list is sorted.

Here's how insertion sort works:

Start with the second element: The first element is considered to be a sorted sublist of one element. So, the algorithm starts with the second element of the list.
Compare and insert: For each element, compare it with the elements before it in the sorted sublist. Move the larger elements one position to the right to make space for the current element. Insert the current element in the correct position in the sorted sublist.
Repeat: Repeat this process until all elements are in their correct positions, and the entire list is sorted. '''