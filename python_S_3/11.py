from tkinter import *
win = Tk()
win.title("grid")
label1 = Label(win, width = 10, height = 5, bg = "red")
label2 = Label(win, width = 10, height = 5, bg = "orange")
label3 = Label(win, width = 10, height = 5, bg = "yellow")
label4 = Label(win, width = 10, height = 5, bg = "green")
label5 = Label(win, width = 10, height = 5, bg = "blue")
label6 = Label(win, width = 10, height = 5, bg = "purple")
label1.grid(row = 0, column = 0)
label2.grid(row = 0, column = 1)
label3.grid(row = 0, column = 2)
label4.grid(row = 1, column = 0)
label5.grid(row = 1, column = 1)
label6.grid(row = 1, column = 2)
win.mainloop()