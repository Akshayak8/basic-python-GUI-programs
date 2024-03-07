from tkinter import*
from tkinter import messagebox
a=Tk()
lb1=Label(a,text="BOOK MY SHOW",font=("Arial bold",20))
lb1.grid(column=0,row=0)
lb2=Label(a,text="NAME")
lb2.grid(column=0,row=1)
lb3=Label(a,text="MOVIE NAME")
lb3.grid(column=0,row=2)
lb4=Label(a,text="TICKETS")
lb4.grid(column=0,row=3)
e1=Entry(a,width=15)
e1.grid(column=1,row=1)
m=["RRR","KGF","PUSPHA"]
v1=StringVar()
d1=OptionMenu(a,v1,*m)
d1.grid(column=1,row=2)
tickets=[1,2,3,4,5]
v2=IntVar()
d2=OptionMenu(a,v2,*tickets)
d2.grid(column=1,row=3)
def b():
    sm=v1.get()
    st=v2.get()
    bill=0
    if sm=="RRR":
        bill=st*400
    elif sm=="KGF":
        bill=st*150
    elif sm=="PUSPHA":
        bill=st*120
    else:
        bill=0
    messagebox.showinfo("","Hello "+e1.get()+"\n movie :"+sm+"\n Tickets :"+str(st)+"\n your bill :"+str(bill))
b=Button(a,text="Book",command=b)
b.grid(column=1,row=4)
a.mainloop()

          
