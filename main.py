from tkinter import *
from btn_widget import Btn

win = Tk()
win.title("Calculator")
win.geometry("1000x500")

def enter(val):
    entry.insert(END, val)

def equel():
    try:
        el = entry.get()
        result = eval(el)
        entry.delete(0,END)
        entry.insert(0, result)
    except:
        entry.delete(0,END)
        entry.insert(0, 'Math error')

def clear():
    entry.delete(0,END)

entry = Entry(win, width=30, font=("Times 22"))
entry.grid(row=0, column=1)

# Placing buttons in a grid layout
buttons = [
    (1, 1, 0), (2, 1, 1), (3, 1, 2),
    (4, 2, 0), (5, 2, 1), (6, 2, 2),
    (7, 3, 0), (8, 3, 1), (9, 3, 2),
    (0, 4, 1)
]

for (num, row, col) in buttons:
    Btn(label=num, name=f'btn_{num}', screen=win, func=enter, row=row, column=col, special=False)

Btn(label='CL', name=f'btn_plus', screen=win, func=clear, row=0, column=3, special=True)

Btn(label='+', name=f'btn_plus', screen=win, func=enter, row=1, column=3, special=False)
Btn(label='-', name=f'btn_minus', screen=win, func=enter, row=2, column=3, special=False)
Btn(label='*', name=f'btn_astrisk', screen=win, func=enter, row=3, column=3, special=False)
Btn(label='/', name=f'btn_dev', screen=win, func=enter, row=4, column=2, special=False)

Btn(label='=', name=f'btn_equel', screen=win, func=equel, row=4, column=3, special=True)


win.mainloop()
