from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()
root.title("Create new windows")
root.iconbitmap("nana.ico")

def open():
    global my_img,my_lbl
    top=Toplevel()
    lbl=Label(top,text="I am new window!   plzz welcome me").pack()
    my_img=ImageTk.PhotoImage(Image.open("images\me2.jpg"))
    my_lbl=Label(top,image=my_img).pack()
    btn2=Button(top,text="Close window",command=top.destroy).pack()
mybutton=Button(root,text="New window",command=open).pack()


mbr=Button(root,text="Kill this window",command=root.destroy).pack()
mainloop()
