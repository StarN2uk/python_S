from tkinter import *
win = Tk()
def click():
    if btn['text'] == 'hello':
        btn['text'] = 'python'
        btn['bg'] = 'green'
    else:
        btn['text'] = 'hello'
        btn['bg' ] = 'orange'
btn = Label(win, text = '', bg = 'white')
i = Button(win, text = 'button', fg = 'black', bg = 'white', command = click)
btn.pack()
i.pack()
win.mainloop()