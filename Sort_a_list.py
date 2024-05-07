#Write a sort function to sort the elements in the list
l=[2,89,67,54,87]
l.sort()
print(l)

#descending order
l=[2,89,67,54,87]
l.sort(reverse=True)
print(l)


#Write a sorting function without using the list.sort function(descending order) 
data_list=[67,85,46,34,12,89]
new_list=[]

while data_list:
    minimum=data_list[0]
    for x in data_list:
        if x>minimum:
            minimum=x
    new_list.append(minimum)   
    data_list.remove(minimum)
print(new_list)    