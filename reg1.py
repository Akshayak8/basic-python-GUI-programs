from tkinter import*
from tkinter import messagebox
a=Tk()
lb1=Label(a,text="Name :")
lb1.grid(column=0,row=1)
lb2=Label(a,text="Gender :")
lb2.grid(column=0,row=2)
lb3=Label(a,text="Fav PL :")
lb3.grid(column=0,row=3)
lb4=Label(a,text="Branch :")
lb4.grid(column=0,row=4)
e1=Entry(a,width=20)
e1.grid(column=1,row=1)
v=IntVar()
r1=Radiobutton(a,text="Male",variable=v,value=1)
r1.grid(column=1,row=2)
r2=Radiobutton(a,text="Female",variable=v,value=2)
r2.grid(column=2,row=2)
v1=IntVar()
v2=IntVar()
v3=IntVar()
c1=Checkbutton(a,text="c",variable=v1,onvalue=1,offvalue=0)
c1.grid(column=1,row=3)
c2=Checkbutton(a,text="python",variable=v2,onvalue=1,offvalue=0)
c2.grid(column=2,row=3)
c3=Checkbutton(a,text="java",variable=v3,onvalue=1,offvalue=0)
c3.grid(column=3,row=3)
options=["CSE","DS","CS","IT"]
v4=StringVar()
d1=OptionMenu(a,v4,*options)
d1.grid(column=1,row=4)
def click():
    name=e1.get()
    messagebox.showinfo("","Hello "+name+"\n your registration done")
b=Button(a,text="submit",command=click)
b.grid(column=1,row=5)
a.mainloop()
