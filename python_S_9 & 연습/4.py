from tkinter import *
win = Tk()
canvas = Canvas(win, bg = "white", width = 500, height = 100)
canvas.pack()
x1, y1 = 0, 0
x2, y2 = 500, 0
for i in range(3):
    y1 += 30
    y2 = y1
    canvas.create_line(x1, y1, x2, y2, fill = "red", width = 3)
win.mainloop()