# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 13:01:07 2018

@author: amity
"""

s=input("Enter String ")
cnt=0
s=" "+s+" "
for i in range(len(s)-1):
    if s[i]==" ":
        if s[i+1] in "AEIOUaeiou":
            while s[i+1]!=" ":
                i=i+1
            cnt=cnt+1
print (cnt, "words")