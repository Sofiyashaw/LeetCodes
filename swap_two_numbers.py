# -*- coding: utf-8 -*-


#Write a Python program to swap two variables.


num1= int(input("Enter the first number"))
num2= int(input("Enter the second number"))

print("The value of variables before swapping",num1)
print("The value of variables after swapping",num2)

temp=num1
num1=num2
num2=temp

print("The value of variables after swapping",num1)
print("The value of variable after swapping",num2)