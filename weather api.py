from tkinter import *
from PIL import ImageTk,Image
import requests
import json  

root=Tk()

root.title("Building weather app")
root.iconbitmap("nan.ico")
#root.geometry("400x50")

def show():
    print(eat.get())
    #m=Label(root,text=e.get())
    #m.grid(row=3,column=0)
    try:
        api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + eat.get() + "&distance=25&API_KEY=141F2493-2679-41F1-B357-4D4DF0AD0B00")
        api=json.loads(api_request.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        category=api[0]['Category']['Name']

        if category=="Good":
            color="green"
        elif category=="Moderate":
            color="yellow"
        elif category=="Unhealthy for Sensitive Groups":
            color="orange"
        elif category=="Unhealthy":
            color="red"
        elif category=="Very Unhealthy":
            color="purple"
        elif category=="Hazardous":
            color="maroon"
        mylab=Label(root,text=city+'\n'+category+'\n'+str(quality),font=('Helvetica',20),bg=color)
        mylab.grid(row=4,column=0)
        root.configure(background=color)
    except Exception as e:
        api="Error..."
        
eat=Entry(root)
eat.grid(row=0,column=1,padx=10,pady=5)
b=Label(root,text="Enter the zipcode")
b.grid(row=0,column=0,padx=10,pady=10)
c=Button(root,text="Show AQI",command=show)
c.grid(row=1,column=0,columnspan=2,ipadx=50)





root.mainloop()
