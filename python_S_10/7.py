from tkinter import *
from random import *
def draw_shape(event):
    color = ["black", "white", "blue", "red", "green", "yellow"]
    x1, y1 = event.x - 25, event.y
    x2, y2 = x1 + 50, y1 + 50
    a = randint(0, 1)
    if a == 0:
        canvas.create_oval(x1, y1, x2, y2, fill = color[randint(0, 5)])
    elif a == 1:
        canvas.create_rectangle(x1, y1, x2, y2, fill = color[randint(0, 5)])
win = Tk()
canvas = Canvas(win, width = 300, height = 300, bg = "white")
canvas.pack()
canvas.bind("<Double-Button-1>", draw_shape)
win.mainloop()