from tkinter import *
win = Tk()
def message(event):
    global count
    count = count + int(entry.get())
    lbl['text'] = count
def Click():
    lbl['text'] = 0
count = 0
entry = Entry(win)
entry.bind("<Return>", message)
entry.pack()
lbl = Label(win, text = "")
lbl1 = Button(win, text = "clear", fg = 'black', bg = 'white', command = Click)
lbl.pack()
lbl1.pack()
win.mainloop()