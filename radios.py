from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Examples of radio ")
root.iconbitmap("nana.ico")

#r=IntVar()
#r.set("2")

Actors=[
    ("Robert Downey Jr.","Iron Man,Avengers"),
    ("Tom Cruise","Mission Impossible"),
    ("Yash","KGF"),
    ("Chris Evans","Thor"),
    ("Prabhas","Bahubali")
]
action=StringVar()
action.set("Iron Man,Avengers")
for actor,movies in Actors:
    Radiobutton(root,text=actor,variable=action,value=movies).pack(anchor=W)
def clicked(value):
    myLabel=Label(root,text=value)
    myLabel.pack()

#Radiobutton(root,text="Open Facebook",variable=r,value=1,command=lambda:clicked(r.get())).pack()
#Radiobutton(root,text="Open Google",variable=r,value=2,command=lambda:clicked(r.get())).pack()

myButton=Button(root,text="Movies",command=lambda:clicked(action.get()))
myButton.pack()

myLabel=Label(root,text=action.get())
myLabel.pack()


root.mainloop()
