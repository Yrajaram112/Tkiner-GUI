from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Dropdown boxes")
root.iconbitmap("pycharm.ico")
root.geometry("400x400")

 #Drop Down Boxes
def show():
    my=Label(root,text=e.get()).pack()

lis=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July"
]
e=StringVar()
e.set("January")
drop=OptionMenu(root,e,*lis)
drop.pack()

mybutton=Button(root,text="Show me selection",command=show).pack()

root.mainloop()
