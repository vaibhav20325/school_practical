# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 13:19:52 2018

@author: amity
"""

m=int(input("Enter the number "))
n=int(input("Enter the number "))
sum=0
if m>n:
    n=m+n
    m=n-m
    n=n-m
for i in range(m+1,n,1):
    if i%3==0:
        continue
    else:
        sum=sum+i
print(sum)