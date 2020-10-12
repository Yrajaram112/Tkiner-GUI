from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt

root=Tk()
root.title("Plotting graphs")
root.iconbitmap("nana.ico")
root.geometry("400x200")

def graph():
    house_prices=np.random.normal(200000,25000,5000)
    plt.hist(house_prices,10)
    #plt.pie(house_prices)
    plt.show()

mybut=Button(root,text="Graph It!",command=graph)
mybut.pack()

root.mainloop()
