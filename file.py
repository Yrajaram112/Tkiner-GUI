from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

root=Tk()
root.title("Open a file")
root.iconbitmap("D:/python/GUI/nana.ico")

root.filename=filedialog.askopenfilename(initialdir="E:\download",title="Select a file",filetypes=(("jpg files","*.jpg"),("Allfiles","*.*")))


root.mainloop()
