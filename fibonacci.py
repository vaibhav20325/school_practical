# -*- coding: utf-8 -*-
"""
Created on Tue May 29 08:49:48 2018

@author: amity
"""

n=int(input("Enter number of numbers "))
a=0
b=1
for i in range(1,n+1,1):
   print(a,end=" ")
   a=a+b
   b=a-b
   