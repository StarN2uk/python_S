from tkinter import *
win = Tk()
def message(event):
    global c
    c = int(entry.get()) * 0.39
    lbl['text'] = c
entry = Entry(win)
entry.bind("<Return>", message)
entry.pack()
c = 0
lbl = Label(win, text = "")
lbl.pack()
win.mainloop()