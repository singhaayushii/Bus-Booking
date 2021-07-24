from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter.ttk import Combobox
import splash


root= Tk()
root.title("Bus Booking Service")
root.geometry("500x400")





def addmore():
    Label(text="Operator").grid(row=6,column=1)
    Entry().grid(row=6,column=2)
    Label(text="Bus Type").grid(row=7,column=1)
    Entry().grid(row=7,column=2)
    Label(text="From").grid(row=8,column=1)
    Entry().grid(row=8,column=2)
    Label(text="To").grid(row=9,column=1)
    Entry().grid(row=9,column=2)
    Label(text="Date").grid(row=10,column=1)
    Entry().grid(row=10,column=2)
    Label(text="Departure Time").grid(row=11,column=1)
    Entry().grid(row=11,column=2)
    Label(text="Arrival Time").grid(row=12,column=1)
    Entry().grid(row=12,column=2)
    Label(text="Fair").grid(row=13,column=1)
    Entry().grid(row=13,column=2)
    Label(text="Seats").grid(row=14,column=1)
    Entry().grid(row=14,column=2)
    Button(text="Save",command=save).grid(row=15,column=1,columnspan=5)
def ask():
    s=messagebox.askyesno(title="yes or no",message="Do you want to go back")
    if s== True:
        main()
def ask2():
    s=messagebox.askyesno(title="yes or no",message="Do you want to go back")
    if s== True:
        main()
def save():
    m=messagebox.showinfo(message="Information saved")
    
        


def add():
    f=Frame()
    f.place(x=0,y=0,width=500,height=400)
    Button(text="<-",command=ask).grid(row=0,column=0,rowspan=2)
    Label(f,text="Bus Booking Service",font=("Berlin Sans FB Demi",20),fg="purple",bg="pink").grid(row=0,column=0,columnspan=5,padx=100)
    Label(f,text="Add Bus",fg="red",font=("Berlin Sans FB Demi",15)).grid(row=1,column=1,columnspan=2,padx=10)
    Label(f,text="Full Name").grid(row=2,column=1,padx=50)
    Entry(f).grid(row=2,column=2)
    Label(f,text="Contact").grid(row=3,column=1)
    Entry(f).grid(row=3,column=2)
    Label(f,text="Address").grid(row=4,column=1)
    Entry(f).grid(row=4,column=2)
    Button(f,text="Add more details",activebackground="cyan",command=addmore).grid(row=5,column=2)

def addmore():
    ff=Frame()
    ff.place(x=0,y=0,width=500,height=400)
    Label(ff,text="Bus Booking Service",font=("Berlin Sans FB Demi",20),fg="purple",bg="pink").grid(row=0,column=0,columnspan=5,padx=100,)
    Label(ff,text="Operator").grid(row=1,column=1,padx=50)
    Entry(ff).grid(row=1,column=2)
    Label(ff,text="Bus Type").grid(row=2,column=1)
    Entry(ff).grid(row=2,column=2)
    Label(ff,text="From").grid(row=3,column=1)
    Entry(ff).grid(row=3,column=2)
    Label(ff,text="To").grid(row=4,column=1)
    Entry(ff).grid(row=4,column=2)
    Label(ff,text="Date").grid(row=5,column=1)
    Entry(ff).grid(row=5,column=2)
    Label(ff,text="Departure Time").grid(row=6,column=1)
    Entry(ff).grid(row=6,column=2)
    Label(ff,text="Arrival Time").grid(row=7,column=1)
    Entry(ff).grid(row=7,column=2)
    Label(ff,text="Fair").grid(row=8,column=1)
    Entry(ff).grid(row=8,column=2)
    Label(ff,text="Seats").grid(row=9,column=1)
    Entry(ff).grid(row=9,column=2)
    Button(ff,text="Save",command=main).grid(row=10,column=1,columnspan=5)
    
def search():
    f1=Frame()
    f1.place(x=0,y=0,width=500,height=400)
    Label(f1,text="Bus Booking Service",font=("Berlin Sans FB Demi",20),fg="purple",bg="pink").grid(row=0,column=0,columnspan=5,padx=100)
    Label(f1,text="Add Bus",fg="red",font=("Berlin Sans FB Demi",15)).grid(row=1,column=1,columnspan=2,padx=10)
    Label(f1,text="Bus type").grid(row=2,column=1)
    Combobox(f1,values=['AC','Non-AC','AC sleeper','Non-AC sleeper']).grid(row=2,column=2)
    Label(f1,text="From").grid(row=3,column=1)
    Entry(f1).grid(row=3,column=2)
    Label(f1,text="To").grid(row=4,column=1)
    Entry(f1).grid(row=4,column=2)
    Label(f1,text="Date").grid(row=5,column=1)
    Entry(f1).grid(row=5,column=2)
    Button(text="<-",command=ask2).grid(row=0,column=0,columnspan=5)
    Button(f1,text="search",activebackground="cyan").grid(row=7,column=1,rowspan=5)
def main():
    f=Frame()
    f.place(x=0,y=0,width=700,height=700)
    photo=PhotoImage(file='C:\\Users\\hp\\Desktop\\projeccttt\\bus (4).png')
    Label(f,image=photo).grid(row=1,column=3)
    Label(f,text="Bus Booking Service",font=("Berlin Sans FB Demi",20),fg="purple",bg="pink").grid(row=0,column=0,columnspan=5,padx=100)
    b1=Button(f,text="Add Bus",font=("Arial",10),command=add)
    b1.grid(row=2,column=1,pady=100)
    b2=Button(f,text="Search Bus",font=("Arial",10),command=search)
    b2.grid(row=2,column=3)
main()
    

