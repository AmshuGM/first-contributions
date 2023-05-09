from tkinter import *
import time

t=Tk()

t.geometry("450x150")
t.title("clock")


def clock():
    h=time.strftime("%I")
    m=time.strftime("%M")
    s=time.strftime("%S")
    a=time.strftime("%p")
    label.config(text=h+':'+m+':'+s+' '+a)
    label.after(1000,clock)
    
label=Label(t,text="",background="black",font=("Helvetica",60),fg="red")
label.pack(pady="20",fill=BOTH)
clock()
t.mainloop()



