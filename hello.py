from tkinter import *

root = Tk()
def myclick():
    mylabel= Label(root,text="I am nitish gadhaa")
    mylabel.pack()
def mycli():
    mylabel1=Label(root,text="I am malik ghuskol").pack()
def mu():
    mylabel=Label(root,text="Kon aaya bahubali raja aaya mai hoon hero smart genius")
    mylabel.pack()
mylabel2=Button(root,text="Click me!",padx=10,pady=10,command=myclick,fg="Blue",bg="Red").pack()
mylabel3=Button(root,text="Click me!",padx=10,pady=10,command=mycli,fg="Green",bg="Pink").pack()
mylabel4=Button(root,text="Click me!",padx=10,pady=10,command=mu,fg="White",bg="Black").pack()

root.mainloop()


