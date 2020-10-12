from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Checkboxes")
root.iconbitmap("nana.ico")
root.geometry("400x400")

def show():
    mylbl=Label(root,text=Cy.get()).pack()
#Cy=IntVar()
Cy=StringVar()

c=Checkbutton(root,text="Tick it for fun",variable=Cy,onvalue="You have clicked it damn",offvalue="Dekh kya rahe hoo")
c.deselect()
c.pack()
mybut=Button(root,text="Show me value bro",command=show).pack()

root.mainloop()
