from tkinter import *
from random import *
def change_shape(event):
    global a
    p = randint(0, 5)
    if p == 0:
        canvas.itemconfigure(board, text = "I hate Thanos poop")
    elif p == 1:
        canvas.itemconfigure(board, text = 'I am Ironman')
    elif p == 2:
        canvas.itemconfigure(board, text = "I am Docter Strange")
    elif p == 3:
        canvas.itemconfigure(board, text = "I am Hulk")
    elif p == 4:
        canvas.itemconfigure(board, text = "I am Star road")
    elif p == 5:
        canvas.itemconfigure(board, text = "I am Gamora")
    elif p == 6:
        canvas.itemconfigure(board, text = "I am groot")
    a += 1
def change_color(event):
    global color
    canvas.itemconfigure(board, fill = color[randint(0, 6)])
a = 0
color = ['blue', 'yellow', 'green', 'red', 'orange', 'purple', 'pink']
my_font = ("consolas", 20)
win = Tk()
win.title("Tennis Game")
canvas = Canvas(win, width = 1000, height = 500, bg = "white")
board = canvas.create_text(500, 250, font = my_font, fill = "green", text = "I hate you")
canvas.pack()
win.bind("<Button-1>", change_shape)
win.bind("<Button-3>", change_color)
win.mainloop()