from tkinter import *

def update_add():
    update("add")

def update_sub():
    update("sub")

def update_reset():
    update("reset")

window=Tk()
total=0
sum=Label(window)
sum.grid(row=0,column=1,columnspan=2)

l1=Label(window,text="현재 합계:")
l1.grid(row=0,column=0)

e1=Entry(window)
e1.grid(row=1,column=0,columnspan=3)

add_button=Button(window,text="더하기(+)",command=update_add)
sub_button=Button(window,text="빼기(-)",command=update_sub)
reset_button=Button(window,text="초기화",command=update_reset)

add_button.grid(row=2,column=0)
sub_button.grid(row=2,column=1)
reset_button.grid(row=2,column=2)

def update(method):
    global total
    if method=="add":
        total+=int(e1.get())
    elif method == "sub":
        total-=int(e1.get())
    else:
        total=0
    sum['text']=str(total)
    e1.delete(0,END)

window.mainloop()