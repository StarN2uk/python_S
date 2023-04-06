from tkinter import *
from tkinter import messagebox

def save() :
    data = txt['text']
    file_name = entry.get()
    f = open(file_name, 'w')
    f.write(data)
    messagebox.showinfo("save", "Save Complete")
def clear():
    txt['text'] = ''
    entry.delete(0, END)
    ans = messagebox.showinfo("clear", "Delete Complete")
win = Tk()
win.title("My Notepad")
win.geometry("1000x1000")
lbl = Label(win, text = "File name : ")
entry = Entry(win)
txt = Text(win, text = '')
btn_save = Button(text = 'save', command = save)
btn_clear = Button(text = 'clear', command = clear)
txt.grid(row = 0, column = 0, columnspan = 3)
lbl.grid(row = 1, column = 1)
entry.grid(row = 1, column = 2)
btn_save.grid(row = 1, column = 3)
btn_clear.grid(row = 2, column = 3)
win.mainloop()