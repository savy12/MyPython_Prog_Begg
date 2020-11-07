from tkinter import *
root = Tk()
def mmm():
    a = v.get()
    if(a==1):
        a1 = Tk()
        a1.title('r1')
        l1 = Label(a1,text='welcome to r1',font=('roman',23,'italic')).pack()
    elif(a==2):
        a1 = Tk()
        a1.title('r2')
        l1 = Label(a1,text='welcome to r2',font=('roman',23,'italic')).pack()
    elif(a==3):
        a1 = Tk()
        a1.title('r3')
        l1 = Label(a1,text='welcome to r3 ',font=('roman',23,'italic')).pack()
    elif(a==4):
        a1 = Tk()
        a1.title('r4')
        l1 = Label(a1,text='welcome to r4',font=('roman',23,'italic')).pack()
    

root.title("radio")

v=IntVar()
v.set(1)
languages = [('r1',1),('r2',2),('r3',3),('r4',4)]
Label(root,text="Choose Progg language",padx=25,justify=RIGHT).pack(anchor=W)
for txt, val in languages:
    Radiobutton(root,text=txt,padx=40,indicatoron =0,width = 15,variable=v,value=val,command=mmm).pack(anchor=W)
root.mainloop()
