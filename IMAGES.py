from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Use of images exit")
root.iconbitmap('D:/Python/GUI/pycharm.ico')

my_img=ImageTk.PhotoImage(Image.open("try1.png"))
#my_label=Label(image=my_img,height=600,width=500)
#my_label.pack()
root.configure(bg=my_img)



buttonqit=Button(root,text='Close window',command=root.destroy)
buttonqit.pack()
root.mainloop()
