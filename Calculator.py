from tkinter import *
win=Tk()
win.title("Calculator")
win.configure(bg="black")
win.geometry("350x520")

#define entry field

e1=Entry(win,width=15,font="Ariel 28 bold",borderwidth=5,bg="grey")
e1.place(x=10,y=20)

# define button_click function

def number_click(number):
    current=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(current)+str(number))

def clear():
    e1.delete(0,END)

def add():
    first_number=e1.get()
    global f_num,operation
    f_num=int(first_number)
    operation="addition"
    e1.delete(0,END)

def sub():
    first_number=e1.get()
    global f_num,operation
    f_num=int(first_number)
    operation="subtraction"
    e1.delete(0,END)

def mul():
    first_number=e1.get()
    global f_num,operation
    f_num=int(first_number)
    operation="multiplication"
    e1.delete(0,END)

def div():
    first_number=e1.get()
    global f_num,operation
    f_num=int(first_number)
    operation="division"
    e1.delete(0,END)

def equal():
    result=0
    second_number=e1.get()
    e1.delete(0,END)
    if operation=="addition":
        result=f_num+int(second_number)
    if operation=="multiplication":
        result=f_num*int(second_number)
    if operation=="subtraction":
        result=f_num-int(second_number)
    if operation=="division":
        result=f_num/int(second_number)
    e1.insert(0,str(round(result,12)))
# defining buttons

btn1=Button(win,text="1",width=5,font="Ariel 22 bold",bg="gray",command=lambda:number_click(1))
btn2=Button(win,text="2",width=5,font="Ariel 22 bold",bg="gray",command=lambda:number_click(2))
btn3=Button(win,text="3",width=5,font="Ariel 22 bold",bg="gray",command=lambda:number_click(3))
btn4=Button(win,text="4",width=5,font="Ariel 22 bold",bg="gray",command=lambda:number_click(4))
btn5=Button(win,text="5",width=5,font="Ariel 22 bold",bg="gray",command=lambda:number_click(5))
btn6=Button(win,text="6",width=5,font="Ariel 22 bold",bg="gray",command=lambda:number_click(6))
btn7=Button(win,text="7",width=5,font="Ariel 22 bold",bg="gray",command=lambda:number_click(7))
btn8=Button(win,text="8",width=5,font="Ariel 22 bold",bg="gray",command=lambda:number_click(8))
btn9=Button(win,text="9",width=5,font="Ariel 22 bold",bg="gray",command=lambda:number_click(9))
btn0=Button(win,text="0",width=5,font="Ariel 22 bold",bg="gray",command=lambda:number_click(0))

btn_add=Button(win,text="+",width=5,font="Ariel 22 bold",bg="gray",command=add)
btn_sub=Button(win,text="-",width=5,font="Ariel 22 bold",bg="gray",command=sub)
btn_mul=Button(win,text="x",width=5,font="Ariel 22 bold",bg="gray",command=mul)
btn_div=Button(win,text="/",width=5,font="Ariel 22 bold",bg="gray",command=div)

btn_equals=Button(win,text="=",width=11,font="Ariel 22 bold",bg="gray",command=equal)
btn_clear=Button(win,text="Clear",width=11,font="Ariel 22 bold",bg="gray",command=clear)

# putting  buttons on the screen

btn7.place(x=10,y=100)
btn8.place(x=122,y=100)
btn9.place(x=234,y=100)

btn4.place(x=10,y=170)
btn5.place(x=122,y=170)
btn6.place(x=234,y=170)

btn1.place(x=10,y=240)
btn2.place(x=122,y=240)
btn3.place(x=234,y=240)

btn0.place(x=10,y=310)
btn_sub.place(x=122,y=310)
btn_div.place(x=234,y=310)

btn_add.place(x=10,y=380)
btn_clear.place(x=122,y=380)

btn_mul.place(x=10,y=450)
btn_equals.place(x=122,y=450)


win.mainloop()