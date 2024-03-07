from tkinter import*
from tkinter import messagebox
a=Tk()
a.title("log")
a.configure(bg="lightgreen")
lb=Label(a,text="login",bg="lightgreen",font=("Arial bold",30))
lb.grid(column=1,row=0)
lb1=Label(a,text="user name",bg="green")
lb1.grid(column=0,row=1)
lb2=Label(a,text="password",bg="green")
lb2.grid(column=0,row=2)
e1=Entry(a,width=25)
e1.grid(column=1,row=1)
e2=Entry(a,width=25,show="*")
e2.grid(column=1,row=2)
def click():
    un=e1.get()
    ps=e2.get()
    if un=="akshay" and ps=="1234":
        messagebox.showinfo("","Logindone")
    else:
        messagebox.showerror("","Invalid")
b=Button(a,text="signin",command=click)
b.grid(column=1,row=3)     
a.mainloop()
