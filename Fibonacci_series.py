#Write a Python Program to print Fibonacci Series
"0,1,1,2,3,5,8,13,21,34"

def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)

for i in range(12):
   print(f(i))    