from tkinter import *
from random import *
def draw_shape(event):
    color = ["black", "white", "blue", "red", "green", "yellow"]
    x1, y1 = event.x, event.y
    x2, y2 = x1 + randint(10, 70), y1 + randint(10, 70)
    canvas.create_rectangle(x1, y1, x2, y2, fill = color[randint(0, 5)])
win = Tk()
canvas = Canvas(win, width = 300, height = 300, bg = "white")
canvas.pack()
canvas.bind("<Double-Button-1>", draw_shape)
win.mainloop()