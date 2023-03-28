from tkinter import *

def Click(shape):
    if shape == "circle":
        img = PhotoImage(file = "circle.gif")
    elif shape == "triangle":
        img = PhotoImage(file = "triangle.gif")
    else:
        img = PhotoImage(file = "star.gif")

    lbl['image'] = img
    lbl.image = img

win = Tk()

img = PhotoImage(file = "circle.gif")
lbl = Label(win, image = img)
btn1 = Button(win, text = "circle", command = lambda : Click("circle"))
btn2 = Button(win, text = "triangle", command = lambda : Click("triangle"))
btn3 = Button(win, text = "star", command = lambda : Click("star"))
lbl.grid(row = 0, column = 0, columnspan = 3)
btn1.grid(row = 1, column = 0)
btn2.grid(row = 1, column = 1)
btn3.grid(row = 1, column = 2)
win.mainloop()