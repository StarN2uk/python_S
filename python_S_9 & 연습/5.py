from tkinter import *
win = Tk()
canvas = Canvas(win, bg = "white", width = 500, height = 100)
canvas.pack()
x1, y1 = 0, 0
x2, y2 = 0, 100
for i in range(10):
    x1 += 45
    x2 = x1
    canvas.create_line(x1, y1, x2, y2, fill = "red", width = 3)
win.mainloop()