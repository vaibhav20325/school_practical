# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

f=open('text.txt','w')
f.write('Neither apple nor pine are in pineapple. Boxing rings are square. \nWriters write, but fingers don\'t fing. Overlook and oversee are opposites.\nA house can burn up as it burns down. An alarm goes ogg by going on.\n')
f.close()
f=open('text.txt','r')
print(f.read()[::-1])
f.close()

f=open('text.txt','a+')
f.write('This is question one.')
f.seek(0)
l=f.readlines()

for i in range(len(l)):
    print(i+1,l[i])
print('Last line is :',l[-1])

f.seek(10,0)
print(f.readline())

line_no=int(input('Enter Line No :'))
print(l[line_no-1])

f.seek(0,0)
words=f.read().lower().split()
letter=[x[0] for x in words]
d={}
for i in letter:
    if i.isalpha:
        d[i]=letter.count(i)

for i in d:
    print('Words beginning with ',i,':',d[i])

    