from tkinter import *
win = Tk()
def message(event):
    lbl['text'] = entry.get()
entry = Entry(win)
entry.bind("<Return>", message)
entry.pack()
lbl = Label(win, text = "")
lbl.pack()
win.mainloop()