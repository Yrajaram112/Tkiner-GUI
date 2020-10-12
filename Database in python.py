from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title("Using databases creating datas")
root.iconbitmap("pycharm.ico")

#create table
'''c.execute("""CREATE TABLE addresses(
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )""")
'''
#create function to delete
def delete():
    #Create database or connect
    conn=sqlite3.connect('address_book.db')
    
    #Create a cursor
    c=conn.cursor()

    #delete
    c.execute("DELETE from addresses WHERE oid="+deletebox.get())
    
    #commit changes
    conn.commit()
    conn.close()

def update():
    #Create database or connect
    conn=sqlite3.connect('address_book.db')
    
    #Create a cursor
    c=conn.cursor()

    record_id=deletebox.get()

    c.execute("""UPDATE addresses SET
        first_name=:first,
        last_name=:last,
        address=:address,
        city=:city,
        state=:state,
        zipcode=:zipcode

        WHERE oid=:oid""",
        {'first':f_name.get(),
         'last':l_name.get(),
         'address':address.get(),
         'city':city.get(),
         'state':state.get(),
         'zipcode':zipcode.get(),
         'oid':record_id    
            }
              )

    #commit changes
    conn.commit()
    conn.close()
    editor.destroy()
    

def edit():
    global editor
    editor=Tk()
    editor.title("Update a record")
    editor.iconbitmap("nana.ico")
    editor.geometry("280x240")

    #Create database or connect
    conn=sqlite3.connect('address_book.db')
    
    #Create a cursor
    c=conn.cursor()

    record_id=deletebox.get()

    c.execute("SELECT * FROM addresses WHERE oid="+record_id)
    v=c.fetchall()

    #create global
    global f_name
    global l_name
    global address
    global city
    global state
    global zipcode
    
    f_name=Entry(editor,width=30)
    f_name.grid(row=0,column=1,padx=20,pady=(10,0))
    l_name=Entry(editor,width=30)
    l_name.grid(row=1,column=1)
    address=Entry(editor,width=30)
    address.grid(row=2,column=1)
    city=Entry(editor,width=30)
    city.grid(row=3,column=1)
    state=Entry(editor,width=30)
    state.grid(row=4,column=1)
    zipcode=Entry(editor,width=30)
    zipcode.grid(row=5,column=1)

    flabe=Label(editor,text="First name")
    flabe.grid(row=0,column=0,pady=(10,0))
    llabe=Label(editor,text="Last name")
    llabe.grid(row=1,column=0)
    addres=Label(editor,text="Address")
    addres.grid(row=2,column=0)
    ci=Label(editor,text="City")
    ci.grid(row=3,column=0)
    fx=Label(editor,text="State")
    fx.grid(row=4,column=0)
    fz=Label(editor,text="Zipcode")
    fz.grid(row=5,column=0)

    #loop through records
    for record in v:
        print(record)
        f_name.insert(0,v[0][0])
        l_name.insert(0,record[1])
        address.insert(0,record[2])
        city.insert(0,record[3])
        state.insert(0,record[4])
        zipcode.insert(0,record[5])

    savebut=Button(editor,text="Save",command=update)
    savebut.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=100)
    
def submit():
    #Create database or connect
    conn=sqlite3.connect('address_book.db')
    
    #Create a cursor
    c=conn.cursor()
    #Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name1.get(),
                'l_name': l_name1.get(),
                'address':address1.get(),
                'city':city1.get(),
                'state':state1.get(),
                'zipcode':zipcode1.get()
        })
    

    #commit changes
    conn.commit()
    conn.close()


    
    #clear text boxes
    f_name1.delete(0,END)
    l_name1.delete(0,END)
    address1.delete(0,END)
    city1.delete(0,END)
    state1.delete(0,END)
    zipcode1.delete(0,END)

def query():
    #Create database or connect
    conn=sqlite3.connect('address_book.db')
    
    #Create a cursor
    c=conn.cursor()

    c.execute("SELECT *,oid FROM addresses")
    v=c.fetchall()
    #print(v)

    xv=''
    for reco in v:
        for recor in reco:
            xv+=str(recor)+"\n"
    querylabel=Label(root,text=xv)
    querylabel.grid(row=12,column=0,columnspan=2)

    
    #commit changes
    conn.commit()
    conn.close()

f_name1=Entry(root,width=30)
f_name1.grid(row=0,column=1,padx=20,pady=(10,0))
l_name1=Entry(root,width=30)
l_name1.grid(row=1,column=1)
address1=Entry(root,width=30)
address1.grid(row=2,column=1)
city1=Entry(root,width=30)
city1.grid(row=3,column=1)
state1=Entry(root,width=30)
state1.grid(row=4,column=1)
zipcode1=Entry(root,width=30)
zipcode1.grid(row=5,column=1)

deletebox=Entry(root,width=30)
deletebox.grid(row=9,column=1)

flabe=Label(root,text="First name")
flabe.grid(row=0,column=0,pady=(10,0))
llabe=Label(root,text="Last name")
llabe.grid(row=1,column=0)
addres=Label(root,text="Address")
addres.grid(row=2,column=0)
ci=Label(root,text="City")
ci.grid(row=3,column=0)
fx=Label(root,text="State")
fx.grid(row=4,column=0)
fz=Label(root,text="Zipcode")
fz.grid(row=5,column=0)
dellabel=Label(root,text="Select ID")
dellabel.grid(row=9,column=0)

but1=Button(root,text="Submit your data",command=submit)
but1.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
#Query button
que=Button(root,text="Show records",command=query)
que.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=110)

delbut=Button(root,text="Delete records",command=delete)
delbut.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=110)
editbut=Button(root,text="Edit record",command=edit)
editbut.grid(row=11,column=0,columnspan=2,pady=5,ipadx=118)

root.mainloop()
