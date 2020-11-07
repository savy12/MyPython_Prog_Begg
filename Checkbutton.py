from tkinter import *
root = Tk()
def mget():
    print(var1.get(),var2.get(),var3.get(),var4.get())

var1 = IntVar()
Checkbutton(root,text='CB1',width=20,indicatoron=0,variable=var1).grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(root,text='CB2',width=20,indicatoron=0,variable=var2).grid(row=1,sticky=W)
var3=IntVar()
Checkbutton(root,text='CB3',width=20,indicatoron=0,variable=var3).grid(row=2,sticky=W)
var4=IntVar()
Checkbutton(root,text='CB4',width=20,variable=var4,indicatoron=0).grid(row=3,sticky=W)
print(var1.get(),var2.get(),var3.get(),var4.get())
button=Button(root,text='get val',width=20,command=mget).grid(row=4,sticky=W)
but=Button(root,text='quit',width = 20,command=root.destroy).grid(row=5,sticky=W)
root.mainloop()
