from tkinter import *
win = Tk()
canvas = Canvas(win, width = 100, height = 100, bg = "white")
canvas.pack()
canvas.create_polygon(20, 10, 20, 90, 80, 90, fill = "red", outline = "black")
win.mainloop()