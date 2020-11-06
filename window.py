from tkinter import *
from tkinter import messagebox
root = Tk()
ss=Tk()
def hello():
    b=a.get()
    label12 = Label(text = b,fg="red",bg="yellow",font = 10).pack()
def newfi():
    label123 = Label(text = "new file created",font = ('roman',34,'italic')).pack()
def mbox():
    messagebox.showinfo('hi','hsjhfshjadasdas')
def mquit():
    mess=messagebox.askyesno('quit','are you sure you want to quit')
    if mess==1:
        root.destroy()
def mbut():
    label12312 = Label(text='bro').pack()
    

a=StringVar()
root.title("1st")
root.geometry("300x300+150+150")
ss.title("2nd")
ss.geometry("300x300+150+150")

label = Button(text = "sd",fg="black",bg="white",font = ('arial',24,'italic'),command=hello).pack()
label = Button(text = "biro",fg="black",bg="white",font = ('palatino',24,'bold'),command=hello).pack()
text = Entry(textvariable = a).pack()
mbutton = Button(text = 'hsjhs',fg='black',bg='green',font=('roman',23,'italic'),command=mbut).pack()


can = Canvas(ss,bg='blue',height=250,width=300)
line = can.create_line(108,120,320,40,fill='red')
arc=can.create_arc(180,150,80,210,fill='yellow')
oval = can.create_oval(80,30,140,150,fill='green')
polygon=can.create_rectangle(120,140,160,180,fill='red')
can.pack()








menu1 = Menu()

listone=Menu()
listone.add_command(label="new file",command=newfi)
listone.add_command(label="open")
listone.add_command(label="save",command=mbox)
listone.add_command(label="quit",command=mquit)


menu1.add_cascade(label="file",menu=listone)
menu1.add_cascade(label="edit")
menu1.add_cascade(label="format")
menu1.add_cascade(label="run")
root.config(menu = menu1)
root.mainloop()
