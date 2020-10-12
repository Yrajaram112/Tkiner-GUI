from tkinter import *
root=Tk()
root.title("Simple Calculator")

e=Entry(width=40,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_ad(number):
    curr=e.get()
    e.delete(0,END)
    e.insert(0,str(curr)+str(number))

def buton_cl():
    e.delete(0,END)
def button_add():
    firstnum=e.get()
    global fnum
    global math
    math="add"
    fnum=int(firstnum)
    e.delete(0,END)
def button_sub():
    firstnum=e.get()
    global fnum
    global math
    math="sub"
    fnum=int(firstnum)
    e.delete(0,END)
def button_mul():
    firstnum=e.get()
    global fnum
    global math
    math="mul"
    fnum=int(firstnum)
    e.delete(0,END)
def button_div():
    firstnum=e.get()
    global fnum
    global math
    math="div"
    fnum=int(firstnum)
    e.delete(0,END)

def button_eq():
    secondnumber=e.get()
    e.delete(0,END)
    if math=="add":
        result=fnum+int(secondnumber)
    elif math=="sub":
        result=fnum-int(secondnumber)
    elif math=="mul":
        result=fnum*int(secondnumber)
    elif math=="div":
        result=fnum/int(secondnumber)
    e.insert(0,result) 

button1=Button(root,text="1",padx=30,pady=40,command=lambda:button_ad(1))
button2=Button(root,text="2",padx=30,pady=40,command=lambda: button_ad(2))
button3=Button(root,text="3",padx=30,pady=40,command=lambda: button_ad(3))
button4=Button(root,text="4",padx=30,pady=40,command=lambda: button_ad(4))
button5=Button(root,text="5",padx=30,pady=40,command=lambda: button_ad(5))
button6=Button(root,text="6",padx=30,pady=40,command=lambda: button_ad(6))
button7=Button(root,text="7",padx=30,pady=40,command=lambda: button_ad(7))
button8=Button(root,text="8",padx=30,pady=40,command=lambda: button_ad(8))
button9=Button(root,text="9",padx=30,pady=40,command=lambda: button_ad(9))
button0=Button(root,text="0",padx=30,pady=40,command=lambda: button_ad(0))

buttonad=Button(root,text="+",padx=30,pady=40,command=button_add)
buttonsub=Button(root,text="-",padx=30,pady=40,command=button_sub)
buttonmul=Button(root,text="*",padx=30,pady=40,command=button_mul)
buttondiv=Button(root,text="/",padx=30,pady=40,command=button_div)

buttoneq=Button(root,text="=",padx=90,pady=30,command=button_eq)
buttoncl=Button(root,text="CA",padx=30,pady=40,command=lambda: buton_cl())

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)

buttonad.grid(row=4,column=1)
buttonsub.grid(row=6,column=0)
buttonmul.grid(row=6,column=1)
buttondiv.grid(row=6,column=2)
buttoneq.grid(row=5,column=0,columnspan=3)
buttoncl.grid(row=4,column=2)
root.mainloop()
