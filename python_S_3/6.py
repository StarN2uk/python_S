from tkinter import *
win = Tk()
img = PhotoImage(file = 'pizza.gif')
label = Label(win, image = img)
label1 = Label(win, text = 'pizza', bg = 'yellow', fg = 'red')
label.pack()
label1.pack()
win.mainloop()