from tkinter import *
from math import *
def calculate():
    input= int(entry.get())
    output = round(input/1.609, 2)
    result.config(text=output)

window = Tk()
window.geometry('300x300')
window.title('Km to Mile')

entry = Entry()
entry.grid(column=1, row=0)

km = Label(text='Km')
km.grid(column=2,row=0)

equal = Label(text='is equal to')
equal.grid(column=0,row=1)

result = Label(text=0)
result.grid(column=1,row=1)

miles = Label(text='Miles')
miles.grid(column=2,row=1)

calculate = Button(text='Calculate',command=calculate)
calculate.grid(column=1,row=2)


window.mainloop()