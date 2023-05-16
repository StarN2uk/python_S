from tkinter import *
win = Tk()
canvas = Canvas(win, width = 100, height = 100, bg = "white")
canvas.pack()
canvas.create_oval(20, 20, 80, 80, fill = "blue", outline = "black")
win.mainloop()