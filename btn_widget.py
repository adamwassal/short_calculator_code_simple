from tkinter import *

class Btn:
    def __init__(self, name, screen, label, func, row, column, special):
        if bool(special) == False:
            self.button = Button(screen, text=label, command=lambda: func(label), width=10, height=2, font=('Times 19'))
            self.button.grid(row=row, column=column, pady=10, padx=5)
        else:
            self.button = Button(screen, text=label, command=lambda: func(), width=10, height=2, font=('Times 19'))
            self.button.grid(row=row, column=column, pady=10, padx=5)

# You can optionally store `name` as an attribute if you plan to use it later
# for example: self.name = name
