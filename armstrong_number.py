# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:43:24 2024

@author: jacin
"""

#Write a Python program to check Armstrong’s number.

'''The armstrong number can be defined as n-digit numbers equal to the sum of the nth powers of their digits are called armstrong numbers.
Armstrong Number Example:

153 is a armstrong number.
n=3

1^3+5^3+3^3 = (1*1*1)+(5*5*5)+(3*3*3) =153 '''


num = int(input("Enter a number to check for armstrong"))

arms=num
n= len(str(num))
sum1=0

while num!=0:
    rem=num%10
    sum1+=rem**n
    num = num//10
    
if arms==sum1:
    print("The given number is a armstrong number" ,arms)
else:
    print("The given number is not a armstrong number" ,arms)    
    
    
