

#Write a Python Program to print set of duplicates in a list

def find_duplicates(lst):
    seen=set()
    duplicates=set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
            
    return duplicates

lst=[1,2,3,4,3,2,1,3,4,3,5,6,7,8,7,6,7,8,9]
print("Set of duplicates:", find_duplicates(lst))     
    