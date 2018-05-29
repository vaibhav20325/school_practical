# -*- coding: utf-8 -*-
"""
Created on Tue May 29 08:30:19 2018

@author: amity
"""

n=int(input("Enter the number:"))
a=n
arm=0
while a>0:
    d=a%10
    a=a//10
    arm=arm+d**3
if arm==n:
    print ("The nummber is an armstrong")
else:
    print ("The number is not an armstrong")