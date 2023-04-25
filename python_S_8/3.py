from tkinter import *
def double_click(event):
    global a
    a = listbox.curselection()
    if a == (0,):
        a = "rose"
    elif a == (1,):
        a = "lilly"
    elif a == (2,):
        a = "pansy"
    elif a == (3,):
        a = "sunflower"
    lbl['text'] = a
    lbl.text = a
a = ''
win = Tk()
flower = ["rose", "lilly", "pansy", "sunflower"]
listbox = Listbox(win)
lbl = Label(win, text = 'asdfgasdhf;tgahsiugrasiug   ', width = 50, height = 1)
for i in range(4):
    listbox.insert(i, flower[i])
listbox.bind("<Double-Button-1>", double_click)
lbl.pack()
listbox.pack()
win.mainloop()