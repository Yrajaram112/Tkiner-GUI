from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("Using databases")
root.iconbitmap("pycharm.ico")
root.geometry("400x400")

#Database

#Create table
'''c.execute("""CREATE TABLE address (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)""")
'''

def submit():
    #Create a database or connect to one
    conn=sqlite3.connect('address_book.db')
    #create cursor
    c=conn.cursor()    
    #Insert into table
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'city':city.get(),
                'state':state.get(),
                'zipcode':zipcode.get()              
            })
    conn.commit()

    conn.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1)
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)
address=Entry(root,width=30)
address.grid(row=2,column=1)
city=Entry(root,width=30)
city.grid(row=3,column=1)
state=Entry(root,width=30)
state.grid(row=4,column=1)
zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1)

flabel=Label(root,text="First name",padx=10).grid(row=0,column=0)
llabel=Label(root,text="Last name",padx=10).grid(row=1,column=0)
add=Label(root,text="Address",padx=10).grid(row=2,column=0)
cit=Label(root,text="City",padx=10).grid(row=3,column=0)
stat=Label(root,text="State",padx=10).grid(row=4,column=0)
zipc=Label(root,text="Zipcode",pady=15).grid(row=5,column=0)

submitbutton=Button(root,text="Submit",comman=submit)
submitbutton.grid(row=7,column=1,columnspan=2)

root.mainloop()
