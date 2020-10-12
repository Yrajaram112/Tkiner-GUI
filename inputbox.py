from tkinter import *

root=Tk()
e=Entry(root)
e.grid(row=0)
e.insert(0,"Whats your name")
def don1():
    mylabe=Label(root,text=e.get())
    mylabe.grid(row=3)
    e.delete(0,END)

label1=Label(root,text="Hero")
but=Button(root,text="Press",command=don1)
label1.grid(row=2)
but.grid(row=1)
root.mainloop()
