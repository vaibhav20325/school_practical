# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:19:58 2019

@author: RajeevKumar
"""

from tkinter import*
from tkinter import messagebox  


import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                   database='q5',
                                   user='root',
                                   password='abcd')

cursor = connection.cursor()
x=(0)
window=Tk()
window.geometry('240x310')
Label(window,text='BUS').grid(column=0,row=0)
a=('1','','','','')  
b=IntVar()
r=IntVar()
k=IntVar()
o=StringVar()
d=StringVar()
Label(window,text='Enter BusNo').grid(column=0,row=1)
Entry(window,width=10,textvariable=b).grid(column=1,row=1)
Label(window,text='Enter Origin').grid(column=0,row=2)
Entry(window,width=10,textvariable=o).grid(column=1,row=2)
Label(window,text='Enter Dest').grid(column=0,row=3)
Entry(window,width=10,textvariable=d).grid(column=1,row=3)
Label(window,text='Enter Rate').grid(column=0,row=4)
Entry(window,width=10,textvariable=r).grid(column=1,row=4)
Label(window,text='Enter Km').grid(column=0,row=5)
Entry(window,width=10,textvariable=k).grid(column=1,row=5)
def insert_click():
    global b,o,d,r,k
    b,o,d,r,k=(b.get(),o.get(),d.get(),r.get(),k.get())
    query = "INSERT INTO BUS values('%d', '%s', '%s', '%d', '%d');" % (b,o,d,r,k)
    cursor.execute(query)
    connection.commit()
n=1
def display():
    global a,n
    if n==1:
        query = "Select * from BUS;"
        cursor.execute(query)
    n=n+1
    a=cursor.fetchone()
    Label(window,text='BusNo: ').grid(column=0,row=11)
    l1=Label(window,text=str(a[0])).grid(column=1,row=11)
    Label(window,text='Origin: ').grid(column=0,row=12)
    l2=Label(window,text=str(a[1])).grid(column=1,row=12)
    Label(window,text='Dest: ').grid(column=0,row=13)
    l3=Label(window,text=str(a[2])).grid(column=1,row=13)
    Label(window,text='Rate: ').grid(column=0,row=14)
    l4=Label(window,text=str(a[3])).grid(column=1,row=14)
    Label(window,text='Km: ').grid(column=0,row=15)
    l5=Label(window,text=str(a[4])).grid(column=1,row=15)

Button(window,text='Create New Record', command = insert_click).grid(column=0,row=8)
Button(window,text='Show Next Record', command = display).grid(column=0 , row=17)
Button(window,text='Exit', command = window.destroy).grid(column=1 , row=17)

window.mainloop()
