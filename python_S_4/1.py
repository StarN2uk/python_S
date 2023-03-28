from tkinter import *

def Click(n):
    if n == 1:
        lbl['text'] = "First button clicked."
    elif n == 2:
        lbl['text'] = "Second button clicked."
    else:
        lbl['text'] = "Third button clicked."
win = Tk()
lbl = Label(win, text = "BUTTON")
btn1 = Button(win, text = "First", command = lambda : Click(1))
btn2 = Button(win, text = "Second", command = lambda : Click(2))
btn3 = Button(win, text = "Third", command = lambda : Click(3))
lbl.grid(row = 0, column = 0, columnspan = 3)
btn1.grid(row = 1, column = 0)
btn2.grid(row = 1, column = 1)
btn3.grid(row = 1, column = 2)
win.mainloop()