from tkinter import *
from random import *
def Click(n):
    if n == 1:
        user_image = PhotoImage(file = "scissor.png")
    elif n == 2:
        user_image = PhotoImage(file = "rock.png")
    else:
        user_image = PhotoImage(file = "paper.png")
    lbl_user['image'] = user_image
    lbl_user.image = user_image
win = Tk()
user_image = PhotoImage()
win.title("Rock Paper Scissors Game")
basic_img = PhotoImage()
lbl_com = Label(win, text = 'ready?', width = 50, height = 50)
lbl_user = Label(win, text = 'ready?', width = 100, height = 50)
lbl_res = Label(win, text = '')
lbl_name1 = Label(win, text = 'Computer')
lbl_name2 = Label(win, text = 'User')
btn_scissor = Button(win, text = "scissor", width = 30, height = 2, bg = 'red', command = lambda : Click(1))
btn_rock = Button(win, text = 'rock', width = 30, height = 2, bg = 'blue', command = lambda : Click(2))
btn_paper = Button(win, text = 'paper', width = 30, height = 2, bg = 'green', command = lambda : Click(3))
lbl_com.grid(row = 0, column = 0)
lbl_user.grid(row = 1, column = 0)
lbl_com.grid(row = 1, column = 2)
lbl_name2.grid(row = 2, column = 0)
lbl_name1.grid(row = 2, column = 2)
btn_scissor.grid(row = 3, column = 0)
btn_rock.grid(row = 3, column = 1)
btn_paper.grid(row = 3, column = 2)
win.mainloop()