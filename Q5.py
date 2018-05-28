# -*- coding: utf-8 -*-
"""
Created on Fri May  4 13:34:43 2018

@author: amity
"""

m=int(input("Enter the amount of money "))
a=int(m/1000)
x=m%1000
b=int(x/500)
x=m%500
c=int(x/100)
x=m%100
d=int(x/50)
x=m%50
e=int(x/10)
x=m%10
f=int(x/5)
x=m%5
g=int(x/2)
x=m%2
h=x
print ("You have :",a,"Rs 1000 notes",b,"Rs 500 notes",c,"Rs 100 notes"
       ,d,"Rs 50 notes",e,"Rs 10 notes",f,"Rs 5 notes",g,"Rs 2 notes"
       ,h,"Rs 1 notes")