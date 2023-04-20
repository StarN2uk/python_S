from tkinter import *
class action:
    def __init__(self, AC):
        self.AC = AC
    def info(self):
        print()
def Click1(n):
    global user_image
    if n == 1:
        user_image = PhotoImage(file = "alien.png")
    elif n == 2:
        user_image = PhotoImage(file = "alien2.jpg")
    lbl_alien['image'] = user_image
    lbl_alien.image = user_image
def Click2(n):
    global user_image
    if n == 1:
        user_image = PhotoImage(file = "Frank.png")
    elif n == 2:
        user_image = PhotoImage(file = "Frank2.jpg")
    lbl_Frank['image'] = user_image
    lbl_Frank.image = user_image
win = Tk()
user_image = PhotoImage()
win.title("tk")
lbl_alien = Label(win, width = 100, height = 50)
lbl_Frank = Label(win, image = '')
btn_alien1 = Button(win, text = "Action1", width = 30, height = 2, bg = 'red', command = lambda : Click1(1))
btn_alien2 = Button(win, text = 'Action2', width = 30, height = 2, bg = 'blue', command = lambda : Click1(2))
btn_Frank1 = Button(win, text = "Action1", width = 30, height = 2, bg = 'red', command = lambda : Click2(1))
btn_Frank2= Button(win, text = 'Action2', width = 30, height = 2, bg = 'blue', command = lambda : Click2(2))
action1 = action(1)
lbl_alien.grid(row = 0, column = 0)
lbl_Frank.grid(row = 0, column = 1)
btn_alien1.grid(row = 1, column = 0)
btn_alien2.grid(row = 1, column = 1)
btn_Frank1.grid(row = 1, column = 2)
btn_Frank2.grid(row = 1, column = 3)
win.mainloop()