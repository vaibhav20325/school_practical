from tkinter import*
from tkinter import messagebox

window=Tk()
p=IntVar()
r=IntVar()
t=IntVar()

window.geometry('210x110')

Label(window,text='Simple Interest Calculator').grid(column=0,row=0)
Label(window,text='Enter Principle').grid(column=0,row=1)
Entry(window,width=10,textvariable=p).grid(column=1,row=1)

Label(window,text='Enter Rate').grid(column=0,row=2)
Entry(window,width=10,textvariable=r).grid(column=1,row=2)

Label(window,text='Enter Time').grid(column=0,row=3)
Entry(window,width=10,textvariable=t).grid(column=1,row=3)

def clicked():
    global p,r,t
    interest = p.get()*r.get()*t.get()/100
    messagebox.showinfo('Simple Interest','Interest is : '+ str(interest))
    
Button(window,text='Calculate', command = clicked).grid(column=0,row=4)

Button(window,text='Exit', command = window.destroy).grid(column=1 , row=4)

window.mainloop()
