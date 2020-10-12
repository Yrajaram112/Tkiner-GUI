from tkinter import *

root=Tk()

phot=PhotoImage(file="try1.png")
w=Label(root,image=phot,height=1000,width=1000)
w.pack()

m=Label(w,text="I am A hero",bg="yellow",height=2,width=4)
m.grid(row=0)
x=Entry(w)
x.grid(row=2)
root.mainloop()
