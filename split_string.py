# -*- coding: utf-8 -*-


#Write a python program to split strings using newline delimiter

ini_str = " This is a test program "

print("Initial String",ini_str)

res_list= (ini_str.rstrip().split(' '))

print("Resultant prefix",str(res_list))