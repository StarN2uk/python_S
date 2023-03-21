from tkinter import *
win = Tk()
lbl1 = Label(win, text = "orange", width = 20, height = 3, relief = "solid")
lbl2= Label(win, text = "banana", font = ("Elephant", 20), bg = "yellow")
lbl3 = Label(win, text = "apple", fg = "red")
lbl1.pack()
lbl2.pack()
lbl3.pack()
win.mainloop()