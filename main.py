from tkinter import *
from time import strftime


# create the frame
root = Tk()
root.title("Digital Computer Clock")


# define the time function
def time():
    # fetch the system time and storing it
    string = strftime("%H:%M:%S %p") #%p is for am/pm
    # label variable displaying time retrieved 
    lbl.config(text=string)
    #return the function after 1s
    lbl.after(1000,time)
    
lbl = Label(root,font=('arial',160,"bold"),bg="black",fg="white")

lbl.pack(anchor="center",fill="both",expand=1)

time()
mainloop()

