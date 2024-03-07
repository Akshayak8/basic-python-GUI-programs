from tkinter import*
import webbrowser
a=Tk()
a.title("NEWS")
def m():
    url1="https://www.sakshi.com/"
    webbrowser.open(url1)
b1=Button(a,text="TELUGU",command=m)
b1.grid(column=0,row=1)
lb1=Label(a,text="")
lb1.grid(column=0,row=2)
def n():
    url2="https://www.indiatimes.com"
    webbrowser.open(url2)
b1=Button(a,text="ENGLISH",command=n)
b1.grid(column=0,row=3)
lb2=Label(a,text="")
lb2.grid(column=0,row=4)
def o():
    url3="https://www.bbc.com/hindi"
    webbrowser.open(url3)
b1=Button(a,text="HINDI",command=o)
b1.grid(column=0,row=5)
a.mainloop()
