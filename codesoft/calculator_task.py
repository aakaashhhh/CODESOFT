import tkinter as t
# Window Creating
window = t.Tk()
window.geometry("300x300")
window.title("Calculator")
window.configure(bg='cyan2')

l1 = t.Label(window, text=" Num1 ",width=5,bg='mistyrose3', font=("Arial",14))
l2 = t.Label(window, text=" Num2 ",width=5,bg='mistyrose3', font=("Arial",14))
l3 = t.Label(window, text="Result",width=5,bg='mistyrose3', font=("Arial",14))
e1 = t.Entry(window, bg='antiquewhite',font=("Arial", 14))
e2 = t.Entry(window, bg='antiquewhite',font=("Arial", 14))
e3 = t.Entry(window, bg='antiquewhite',font=("Arial", 14))
l1.grid(row=0, column=0,pady=2)
l2.grid(row=1, column=0,pady=2)
l3.grid(row=2, column=0,pady=2)
e1.grid(row=0, column=1,columnspan=3,pady=2)
e2.grid(row=1, column=1,columnspan=3,pady=2)
e3.grid(row=2, column=1,columnspan=3,pady=2)

def digit(num):
    current_text = e1.get() if e1.focus_get() == e1 else e2.get()
    current_text += str(num)
    if e1.focus_get() == e1:
        e1.delete(0, t.END)
        e1.insert(0, current_text)
    else:
        e2.delete(0, t.END)
        e2.insert(0, current_text)
        
def add():
    try:
        value1 = float(e1.get())
        value2 = float(e2.get())
        result = value1 + value2
        e3.delete(0, t.END)
        e3.insert(0, str(result))
    except ValueError:
        e3.delete(0, t.END)
        e3.insert(0, "Error")       
def sub():
    try:
        value1 = float(e1.get())
        value2 = float(e2.get())
        result = value1 - value2
        e3.delete(0, t.END)
        e3.insert(0, str(result))
    except ValueError:
        e3.delete(0, t.END)
        e3.insert(0, "Error")      
def multiply():
    try:
        value1 = float(e1.get())
        value2 = float(e2.get())
        result = value1 * value2
        e3.delete(0, t.END)
        e3.insert(0, str(result))
    except ValueError:
        e3.delete(0, t.END)
        e3.insert(0, "Error")      
def div():
    try:
        value1 = float(e1.get())
        value2 = float(e2.get())
        if value2 == 0:
            raise ZeroDivisionError
        result = value1 / value2
        e3.delete(0, t.END)
        e3.insert(0, str(result))
    except ValueError:
        e3.delete(0, t.END)
        e3.insert(0, "Error")
    except ZeroDivisionError:
        e3.delete(0, t.END)
        e3.insert(0, "Can't divide by 0")        
def clear():
    e1.delete(0, t.END)
    e2.delete(0, t.END)
    e3.delete(0, t.END)

# Button Creation
b1=t.Button(window, text='7',bg='lightgray',font=("Arial",14),width=5,command=lambda: digit('7'))
b2=t.Button(window, text='8',bg='lightgray',font=("Arial",14),width=5,command=lambda: digit('8'))
b3=t.Button(window, text='9',bg='lightgray',font=("Arial",14),width=5,command=lambda: digit('9'))
b4=t.Button(window, text='4',bg='lightgray',font=("Arial",14),width=5,command=lambda: digit('4'))
b5=t.Button(window, text='5',bg='lightgray',font=("Arial",14),width=5,command=lambda: digit('5'))
b6=t.Button(window, text='6',bg='lightgray',font=("Arial",14),width=5,command=lambda: digit('6'))
b7=t.Button(window, text='1',bg='lightgray',font=("Arial",14),width=5,command=lambda: digit('1'))
b8=t.Button(window, text='2',bg='lightgray',font=("Arial",14),width=5,command=lambda: digit('2'))
b9=t.Button(window, text='3',bg='lightgray',font=("Arial",14),width=5,command=lambda: digit('3'))
b10=t.Button(window, text='0',bg='lightgray',font=("Arial",14),width=5,command=lambda: digit('0'))
b11=t.Button(window, text=" + ",bg='gold',font=("Arial",14),width=5,command=add)
b12=t.Button(window, text=" - ",bg='gold',font=("Arial",14),width=5,command=sub)
b13=t.Button(window, text=" * ",bg='gold',font=("Arial",14),width=5,command=multiply)
b14=t.Button(window, text=" / ",bg='gold',font=("Arial",14),width=5,command=div)
b15=t.Button(window, text="Clear",bg='red',fg='white',font=("Arial",14),width=5,command=clear)
b1.grid(row=3,column=0,pady=5)
b2.grid(row=3,column=1,pady=5)
b3.grid(row=3,column=2,pady=5)
b4.grid(row=4,column=0,pady=5)
b5.grid(row=4,column=1,pady=5)
b6.grid(row=4,column=2,pady=5)
b7.grid(row=5,column=0,pady=5)
b8.grid(row=5,column=1,pady=5)
b9.grid(row=5,column=2,pady=5)
b10.grid(row=6,column=1,pady=5)
b11.grid(row=3,column=3,pady=5)
b12.grid(row=4,column=3,pady=5)
b13.grid(row=5,column=3,pady=5)
b14.grid(row=6, column=3,pady=5)
b15.grid(row=6,column=2,pady=5)
window.mainloop()