from tkinter import *
win = Tk()
listbox = Listbox(win)
for i in range(10) :
    listbox.insert(i, str(i))
print(listbox.curselection())
print(listbox.get(0, 9))
listbox.pack()
win.mainloop()