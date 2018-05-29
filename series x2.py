# -*- coding: utf-8 -*-
"""
Created on Tue May 22 08:29:47 2018

@author: amity
"""

a=int(input("Enter number of numbers "))
x=int(input("Enter first number "))
sum=0
for i in range (1,a+1,1):
    sum = sum + (x**i)/i
print (sum)
