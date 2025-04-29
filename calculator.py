import tkinter as tk
window=tk.Tk()
window.geometry("500x500")
window.title("Calculator")

num1=tk.Label(text="Enter num 1 : ",font=("Arial",20))
num1val=tk.Entry(window,font=("Arial",20,"bold"))
num1.pack()
num1val.pack()

num2=tk.Label(text="Enter num 2 : ",font=("Arial",20))
num2val=tk.Entry(window,font=("Arial",20,"bold"))
num2.pack()
num2val.pack()
def sum():
    n1=int(num1val.get())
    n2=int(num2val.get())
    result=n1+n2
    ans1.config(text=f"Addition value is : {result}")
def sub():
    n1=int(num1val.get())
    n2=int(num2val.get())
    result=n1-n2
    ans2.config(text=f"Subtraction value is : {result}")
def div():
    n1=int(num1val.get())
    n2=int(num2val.get())
    result=n1/n2
    ans3.config(text=f"Division value is : {result}")
def mul():
    n1=int(num1val.get())
    n2=int(num2val.get())
    result=n1*n2
    ans4.config(text=f"Multiplication value is : {result}")
def concat():
    n1=str(num1val.get())
    n2=str(num2val.get())
    result=n1+n2
    ans5.config(text=f"Value is concatinated : {result}")


btn1=tk.Button(window,text="Addition",font=("Arial",20,"italic"),fg="pink",bg="black",command=sum)
btn1.pack()
btn2=tk.Button(window,text="Subtraction",font=("Arial",20,"italic"),fg="pink",bg="black",command=sub)
btn2.pack()
btn3=tk.Button(window,text="Divide",font=("Arial",20,"italic"),fg="pink",bg="black",command=div)
btn3.pack()
btn4=tk.Button(window,text="Multiply",font=("Arial",20,"italic"),fg="pink",bg="black",command=mul)
btn4.pack()
btn5=tk.Button(window,text="Concatination",font=("Arial",20,"italic"),fg="pink",bg="black",command=concat)
btn5.pack()

ans1=tk.Label(text="",font=("Arial",20,"italic"))
ans1.pack()
ans2=tk.Label(text="",font=("Arial",20,"italic"))
ans2.pack()
ans3=tk.Label(text="",font=("Arial",20,"italic"))
ans3.pack()
ans4=tk.Label(text="",font=("Arial",20,"italic"))
ans4.pack()
ans5=tk.Label(text="",font=("Arial",20,"italic"))
ans5.pack()
window.mainloop()