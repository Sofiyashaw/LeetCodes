

#Write a Python program to implement a Binary Searh

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [2, 3, 2, 1, 4, 5, 3, 6]
x = 6
        
result = binary_search(arr, x)
if result != -1:
    print(f"The element {x} has been found at position {result}")
else:
    print(f"The element {x} is not present in the array")
 


































'''Binary search is an efficient algorithm used to search for a specific element in a sorted array or list. It works by repeatedly dividing the search interval in half and comparing the target value with the middle element of the array.
Here's how it works:

Compare the target value with the middle element of the array.
1.If the target value matches the middle element, the search is successful.
2.If the target value is greater than the middle element, the search continues in the upper half of the array.
3.If the target value is less than the middle element, the search continues in the lower half of the array.
Repeat the process until the target value is found or the search interval becomes empty.'''


