# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 12:47:20 2019

@author: amity
"""
d={'rose':('red','black','pink'),'lily':('violet','white','pink')}
a=()
for i in d.values():
    a+=i
maxcol=0
maxcolour=''
for i in a:
    if a.count(i)>maxcol:
        maxcol=a.count(i)
        maxcolour=i
print('Flower in max colours is ', max(d.items())[0])
print('Colour in which max flowers are presnt ',maxcolour)

