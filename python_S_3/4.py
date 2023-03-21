from tkinter import *
win = Tk()
List = ["info", "warning", "error", "question", "questhead", "hourglass", "gray12", "gray25", "gray50", "gray75"]
for i in range(10):
    lbl = Label(win, bitmap = List[i])
    lbl.pack(side = 'left')
win.mainloop()