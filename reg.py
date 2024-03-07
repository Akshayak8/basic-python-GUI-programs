from tkinter import*
from tkinter import messagebox
a=Tk()
a.title("reg")
a.configure(bg="yellow")
lb=Label(a,text="regestration",bg="yellow",font=("Arial bold",20))
lb.grid(column=1,row=0)
lb1=Label(a,text="name",bg="yellow")
lb1.grid(column=0,row=1)
lb2=Label(a,text="roll no",bg="yellow")
lb2.grid(column=0,row=2)
e1=Entry(a,width=15)
e1.grid(column=1,row=1)
e2=Entry(a,width=15)
e2.grid(column=1,row=2)
def click():
    #messagebox.showinfo("","done")
    import login
b1=Button(a,text="submit",bg="yellow",command=click)
b1.grid(column=1,row=3)
a.mainloop()
