from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Use of frame in GUI")
root.iconbitmap("pycharm.ico")

frame=LabelFrame(root,text="This is my frame",padx=100,pady=100)
frame.grid(padx=20,pady=20)


my_label1=Button(root,text="Don't Click here!",borderwidth=4)
my_label2=Button(frame,text="Nor Here",borderwidth=3,command=root.destroy)

my_label1.grid(row=3,column=1)
my_label2.grid(row=5,column=3)
root.mainloop()
