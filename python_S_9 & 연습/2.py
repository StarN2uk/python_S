from tkinter import *
win = Tk()
wetpoop = Canvas(win, bg = "white", width = 500, height = 100)
wetpoop.create_line(0, 50, 500, 50, fill = "blue", width = 5)
wetpoop.pack()
win.mainloop()