from tkinter import *
win = Tk()
wetpoop = Canvas(win, bg = "white", width = 100, height = 300)
wetpoop.create_line(50, 0, 50, 300, fill = "red", width = 5)
wetpoop.pack()
win.mainloop()