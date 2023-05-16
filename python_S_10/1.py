from tkinter import *
win = Tk()
canvas = Canvas(win, width = 200, height = 100, bg = "white")
canvas.pack()
canvas.create_oval(10, 10, 60, 60, fill = "blue")
canvas.create_rectangle(100, 10, 160, 60, fill = "yellow", outline = "red")
win.mainloop()