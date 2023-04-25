from tkinter import *
def double_click(event):
    index = listbox.curselection()
    print("Today :", listbox.get(index[0]))
def left_click(event) :
    index = listbox.curselection()
    if index :
        if index[0] == 0:
            print("Yesterday :")
        else :
            print("Yesterday :", listbox.get(index[0]-1))
def right_click(event) :
    index = listbox.curselection()
    if index :
        if index[0] == 6:
            print("Tomorrow : Mon")
        else :
            print("Tomorrow :", listbox.get(index[0] + 1))
day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
win = Tk()
listbox = Listbox(win)
for i in range(7):
    listbox.insert(i, day[i])
listbox.bind("<Double-Button-1>", double_click)
listbox.bind("<Button-1>", left_click)
listbox.bind("<Button-3>", right_click)
listbox.pack()
win.mainloop()