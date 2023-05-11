from tkinter import *
def paint(event):
    x1, y1 = event.x, event.y
    x2, y2 = x1 + 5, y1 + 5
    canvas.create_line(x1, y1, x2, y2, width = 3)
win= Tk()
canvas = Canvas(win, bg = "white", width = 500, height = 200)
canvas.pack()
win.bind("<B1-Motion>", paint)
win.mainloop()