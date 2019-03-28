# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:00:05 2019

@author: SCL
"""

def isvowel(file1):
    f1=open(file1,'r')
    f2=open('file2.txt','w')
    f2.write('')
    f2.close()
    f2=open('file2.txt','a+')

    for i in f1.read().split():
        if i[0].lower() not in ['a','e','i','o','u']:
            f2.write(i)
            f2.write(' ')
    f2.seek(0)
    return(f2.read())
    f1.close()
    f2.close()

print(isvowel('text.txt'))


