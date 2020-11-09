from tkinter import *
from tkinter import DISABLED
root=Tk()
var1 = IntVar()
var5=IntVar()
def cal():
    var2 = var1.get()
    var3 = var2*3.785
    e2.insert(0,var3)
def cal1():
    var6 = var5.get()
    var7 = var6/3.785
    e1.insert(0,var7)
def mclear():
    e1.delete(0,END)
    e1.insert(0,0)
    e2.delete(0,END)
    e2.insert(0,0)

n = 'arial',14,'italic'
Label(root,text='gallons',padx=25,font=(n)).grid(row=0,sticky=W)
Label(root,text='liters',padx=25,font=(n)).grid(row=1,sticky=W)
e1=Entry(root,width=25,textvariable=var1)
e1.grid(row=0,column=1)
e2=Entry(root,textvariable=var5,width=25)
e2.grid(row=1,column=1)
Button(root,text='cacl gal to lts',command=cal,font=(n),width=20).grid(row=2)
Button(root,text='cacl lts to gal',command=cal1,font=(n),width=20).grid(row=2,column=1)
Button(root,text='clear',command=mclear,font=(n),width=20).grid(row=3)
Button(root,text='exit',command = root.destroy,font=(n),width=20).grid(row=3,column=1)


root.mainloop()
