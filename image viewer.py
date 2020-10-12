from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Use of images exit")
root.iconbitmap('D:/Python/GUI/pycharm.ico')

my_img1=ImageTk.PhotoImage(Image.open("images/image1.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("images/image2.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("images/me1.png"))
my_img4=ImageTk.PhotoImage(Image.open("images/me2.jpg"))
my_img5=ImageTk.PhotoImage(Image.open("images/me3.jpg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]

status=Label(root,text="Image 1 of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
status.grid(row=3,column=0,columnspan=3,sticky=W+E)

my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forwarder(imnum):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=image_list[imnum-1])
    a="Image " +str(imnum)+" of "+str(len(image_list))
    status=Label(root,text=a,anchor=W)
    status.grid(row=3,column=2,sticky=W+E)
    button_forward=Button(root,text=">>",command=lambda:forwarder(imnum+1))
    button_back=Button(root,text="<<",command=lambda:backer(imnum-1))

    if imnum==5:
        button_forward=Button(root,text=">>",state=DISABLED)

    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    my_label.grid(row=0,column=0,columnspan=3)

def backer(imnum):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=image_list[imnum-1])
    a="Image " +str(imnum)+" of "+str(len(image_list))
    status=Label(root,text=a)
    status.grid(row=3,column=2,sticky=W+E)
    button_forward=Button(root,text=">>",command=lambda:forwarder(imnum+1))
    button_back=Button(root,text="<<",command=lambda:backer(imnum-1))

    if imnum==1:
        button_back=Button(root,text="<<",state=DISABLED)

    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    my_label.grid(row=0,column=0,columnspan=3)

quit1=Button(root,text='Close window',command=root.quit)
back=Button(root,text="<<",state=DISABLED)
forward=Button(root,text=">>",command=lambda:forwarder(2))

back.grid(row=1,column=0)
forward.grid(row=1,column=2)
quit1.grid(row=1,column=1)

root.mainloop()
