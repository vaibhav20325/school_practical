# -*- coding: utf-8 -*-
"""
Created on Thu May 10 13:01:29 2018

@author: amity
"""

s=int(input("Enter Speed:"))
a=str(input("Is today your birthday? (yes/no) "))
if a=="yes":
    if s<=65:
        t=0
    elif s<=85:
        t=1
    else :
        t=2
elif a=="no":
    if s<=60:
        t=0
    elif s<=80:
        t=1
    else :
        t=2
else: t="error"
print ("The ticket number is ",t )