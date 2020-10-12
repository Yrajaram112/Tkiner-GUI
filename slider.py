from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("This is slider")
root.iconbitmap("D:/python/GUI/nana.ico")

def slide(var):
    root.geometry("800x"+(str(verticle.get()))

verticle1=Scale(root,from_=0, to=800,command=slide)
verticle1.pack()


root.mainloop()