from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()

root.title("Message")
root.iconbitmap("nana.ico")
#showinfo,showwarning,showerror,askquestion,askokcancel,askyesno


def popup():
    response=messagebox.showwarning("This is an error","Please turn off your computer")
    Label(root,text=response).pack()
    #if response=='yes':
     #   Label(root,text="You clickes Yes!").pack()
    #else:
     #   Label(root,text="You clicked No!").pack()


mybutton=Button(root,text="Click to scan",command=popup)
mybutton.pack()
