from tkinter import Button, Entry, Label
from tkiner import *

window = Tk()
window.title("Area claculator")
window.geometry('800x400')

label1= Label(window,text ='Length:',font=('arial',30,'bold'))
label1.pack(pady=(50,6))
tb1=Entry(window,font=('arial',30,'bold'))
tb1.pack(pady=6)

label2= Label(window,text ='Breath:',font=('arial',30,'bold'))
label2.pack(pady=(50,6))
tb2=Entry(window,font=('arial',30,'bold'))
tb2.pack(pady=6)

button= Button(window,font=('arial',30,'bold'))
button.pack(pady=6)

window.mainloop()