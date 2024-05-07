# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 14:23:10 2024

@author: jacin
"""

#Write a python program to calculate factorial using recursion
                                                                                    

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
num=int(input("Enter a number"))  
print("The factorial",num,"is",factorial(num))  




#normal method

def factorial(n):
     result=1
     for i in range(1,n+1):
            result *=i
            return result
     
num = int(input("Enter a number:"))  
print("Factorial of num is",factorial(num))      