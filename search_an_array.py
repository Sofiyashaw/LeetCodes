

#Given an array arr[] of n elements , write a Python function to search a given element x

def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return True  # Return True if element found
    print("Not Present in the list")  # Print message if element not found
    return False  # Return False if element not found

l = [2, 3, 4, 5, 2, 3, 4]
print(search(l, 2))  # Output: True


