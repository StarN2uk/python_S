from tkinter import *
win = Tk()
canvas = Canvas(win, bg = "white", width = 480, height = 480)
canvas.pack()
for i in range(10, 500, 50):
    x1, y1 = 10, i
    x2, y2 = 460, y1
    canvas.create_line(x1, y1, x2, y2, fill = "blue", width = 3)
    canvas.create_line(y1, x1, y2, x2, fill = "red", width = 3)
win.mainloop()