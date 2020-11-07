from tkinter import *
from tkinter import colorchooser
from tkinter.colorchooser import askcolor
from tkinter import filedialog
root=Tk()
def mcolor():
    color = colorchooser.askcolor()
    label = Label(text = "               ",bg=color[1]).pack()
def mfile():
    file1 = filedialog.askopenfile()
    label = Label(text = file1,font=('roman',30,'italic')).pack()
    file2 = file1.name
    f = open(file2)
    label2=Label(text=f.read(),font=('arial',24,'bold')).pack()
    

button = Button(text='choose color',width = 40,command = mcolor).pack()
button = Button(text='open file',command = mfile).pack()
root.mainloop()
