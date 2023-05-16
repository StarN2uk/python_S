from tkinter import *
win = Tk()
canvas = Canvas(win, width = 100, height = 100, bg = "white")
canvas.pack()
canvas.create_oval(30, 30, 70, 50, fill = "blue", outline = "black")
win.mainloop()