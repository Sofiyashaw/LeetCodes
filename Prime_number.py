#Write a Python Program to print Prime Numbers Between 100 and 200
n=int(input("Enter the prime no range"))
for num in range(n):
    if all( num%i!=0  for i in range(2,num)):
        print(num)
    


 # Syntax :     if all(condition for item in iterable):
    
