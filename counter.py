import tkinter as tk
import time
counter =0
def counter_label():
    counter=0
    def count():
        global counter
        counter +=1
        label.config(text=str(counter))
        label.after(1000,count)
    count()
def pause():
    time.sleep(5)
root = tk.Tk()
root.title("counter")
label=tk.Label(root,fg= 'green')
label.pack()
start = tk.Button(root,text='start',width = 50,command=counter_label)
start.pack()
button1 = tk.Button(root,text='pause for 5 seconds',width=40,command=pause)
button1.pack()
button = tk.Button(root,text='stop',width=40,command=root.destroy)
button.pack()
root.mainloop()
