from tkinter import *
root=Tk()
Label(root,text="first name").grid(row=0)
Label(root,text="last name").grid(row=1)
Label(root,text="E-mail").grid(row=2)
Label(root,text="Country").grid(row=3)
def mentry():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
e1=Entry(root)
e1.grid(row=0,column=1)
e1.insert(0,'peter')
e2=Entry(root)
e2.grid(row=1,column=1)
e2.insert(0,'jha')
e3=Entry(root)
e3.grid(row=2,column=1)
e3.insert(0,'sjksadj@gm.com')
e4=Entry(root)
e4.grid(row=3,column=1)
e4.insert(0,'INDIA')
butt=Button(root,text='New Entries',command=mentry).grid(row=4,column=1)
root.mainloop()