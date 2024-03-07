from tkinter import *
from tkinter import messagebox

a = Tk()
a.title("CALCULATOR")

lb = Label(a, text="           ")
lb.grid(column=0, row=6)

v = ''

def f1():
    global v
    v = v + '1'
    lb.configure(text=v)

def f2():
    global v
    v = v + '2'
    lb.configure(text=v)

def f3():
    global v
    v = v + '3'
    lb.configure(text=v)

def f4():
    global v
    v = v + '+'
    lb.configure(text=v)

def f5():
    global v
    v = v + '4'
    lb.configure(text=v)

def f6():
    global v
    v = v + '5'
    lb.configure(text=v)

def f7():
    global v
    v = v + '6'
    lb.configure(text=v)

def f8():
    global v
    v = v + '-'
    lb.configure(text=v)

def f9():
    global v
    v = v + '7'
    lb.configure(text=v)

def f10():
    global v
    v = v + '8'
    lb.configure(text=v)

def f11():
    global v
    v = v + '9'
    lb.configure(text=v)

def f12():
    global v
    v = v + '*'
    lb.configure(text=v)

def f13():
    global v
    v = v + '.'
    lb.configure(text=v)

def f14():
    global v
    v = v + '0'
    lb.configure(text=v)

def f15():
    global v
    v = v + '/'
    lb.configure(text=v)

def f16():
    global v
    print(v)
    a = eval(v)
    lb.configure(text=v+' = '+str(a))

b1 = Button(a, text="1", bg="white", fg="black", font=("arial bold", 15), command=f1)
b1.grid(column=0, row=1)
lb1 = Label(a, text="")
lb1.grid(column=1, row=1)

b2 = Button(a, text="2", bg="white", fg="black", font=("arial bold", 15), command=f2)
b2.grid(column=2, row=1)
lb2 = Label(a, text="")
lb2.grid(column=3, row=1)

b3 = Button(a, text="3", bg="white", fg="black", font=("arial bold", 15), command=f3)
b3.grid(column=4, row=1)
lb3 = Label(a, text="")
lb3.grid(column=5, row=1)

b4 = Button(a, text="+", bg="white", fg="black", font=("arial bold", 15), command=f4)
b4.grid(column=6, row=1)

b5 = Button(a, text="4", bg="white", fg="black", font=("arial bold", 15), command=f5)
b5.grid(column=0, row=2)
lb4 = Label(a, text="")
lb4.grid(column=1, row=2)

b6 = Button(a, text="5", bg="white", fg="black", font=("arial bold", 15), command=f6)
b6.grid(column=2, row=2)
lb5 = Label(a, text="")
lb5.grid(column=3, row=2)

b7 = Button(a, text="6", bg="white", fg="black", font=("arial bold", 15), command=f7)
b7.grid(column=4, row=2)
lb6 = Label(a, text="")
lb6.grid(column=5, row=2)

b8 = Button(a, text="-", bg="white", fg="black", font=("arial bold", 15), command=f8)
b8.grid(column=6, row=2)

b9 = Button(a, text="7", bg="white", fg="black", font=("arial bold", 15), command=f9)
b9.grid(column=0, row=3)
lb7 = Label(a, text="")
lb7.grid(column=1, row=3)

b10 = Button(a, text="8", bg="white", fg="black", font=("arial bold", 15), command=f10)
b10.grid(column=2, row=3)
lb8 = Label(a, text="")
lb8.grid(column=3, row=3)

b11 = Button(a, text="9", bg="white", fg="black", font=("arial bold", 15), command=f11)
b11.grid(column=4, row=3)
lb9 = Label(a, text="")
lb9.grid(column=5, row=3)

b12 = Button(a, text="*", bg="white", fg="black", font=("arial bold", 15), command=f12)
b12.grid(column=6, row=3)

b13 = Button(a, text=".", bg="white", fg="black", font=("arial bold", 15), command=f13)
b13.grid(column=0, row=4)
lb10 = Label(a, text="")
lb10.grid(column=1, row=4)

b14 = Button(a, text="0", bg="white", fg="black", font=("arial bold", 15), command=f14)
b14.grid(column=2, row=4)
lb11 = Label(a, text="")
lb11.grid(column=3, row=4)

b15 = Button(a, text="/", bg="white", fg="black", font=("arial bold", 15), command=f15)
b15.grid(column=4, row=4)
lb12 = Label(a, text="")
lb12.grid(column=5, row=4)

b16 = Button(a, text="=", bg="white", fg="black", font=("arial bold", 15), command=f16)
b16.grid(column=6, row=4)
a.mainloop()
