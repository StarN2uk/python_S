from tkinter import *
def get_click() :
    lbl2['text'] = txt_box.get(1.0, END)
def ins_click() :
    txt_box.insert(1.0, lbl2['text'])
def del_click() :
    txt_box.delete(1.0, END)
win = Tk()
txt_box = Text(win, width = 40, height = 5)
lbl1 = Label(win, text = "CLick the 'insert' button to insert this string.", width = 40, height = 5, bg = "skyblue")
lbl2 = Label(win, text = "Click the 'get' button to import textbox strings/ninto this label.", width = 40, height = 5, bg = "pink")
btn_get = Button(win, text = "get", width = 10, command = get_click)
btn_ins = Button(win, text = "insert", width = 10, command = ins_click)
btn_del = Button(win, text = "delete", width = 10, command = del_click)
txt_box.grid(row = 0, column = 0, columnspan = 3)
lbl1.grid(row = 1, column = 0, columnspan = 3)
lbl2.grid(row = 2, column = 0, columnspan = 3)
btn_get.grid(row = 3, column = 0)
btn_ins.grid(row = 3, column = 1)
btn_del.grid(row = 3, column = 2)
win.mainloop()