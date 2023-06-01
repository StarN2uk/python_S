from tkinter import *
def move_up(event):
    global x, y
    y -= 65
    canvas.coords(racket, x, y)
def move_down(event):
    global x, y
    y += 65
    canvas.coords(racket, x, y)
def move_up2(event):
    global x2, y2
    y2 -= 65
    canvas.coords(racket2, x2, y2)
def move_down2(event):
    global x2, y2
    y2 += 65
    canvas.coords(racket2, x2, y2)
x, y = 400, 235
x2, y2 = 100, 235
win = Tk()
canvas = Canvas(win, width = 500, height = 500, bg = "white")
img = PhotoImage(file = "red_racket.png")
img2 = PhotoImage(file = "green_racket.png")
racket = canvas.create_image(x, y, image = img)
racket2 = canvas.create_image(x2, y2, image = img2)
canvas.pack()
win.bind("<Up>", move_up)
win.bind("<Down>", move_down)
win.bind("<w>", move_up2)
win.bind("<s>", move_down2)
win.mainloop()