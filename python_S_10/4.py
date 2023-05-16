from tkinter import *
win = Tk()
canvas = Canvas(win, width = 100, height = 100, bg = "white")
canvas.pack()
canvas.create_polygon(50, 10, 10, 90, 90, 90, fill = "red", outline = "black")
win.mainloop()