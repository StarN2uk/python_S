from tkinter import *
from random import *
def draw_shape(event):
    color = ["black", "white", "blue", "red", "green", "yellow"]
    x1, y1 = event.x - 25, event.y
    x2, y2 = x1 + 50, y1 + 50
    a = randint(0, 1)
    if a == 0:
        canvas.create_oval(x1, y1, x2, y2, fill = color[randint(0, 5)])
    elif a == 1:
        canvas.create_rectangle(x1, y1, x2, y2, fill = color[randint(0, 5)])
def change_tool(n):
    global button1, button6, button11
    if n == 1:
        button1 = Button(win, text = "canvas color", bg = "black")
        button6 = Button(win, text = "pen color", bg = "white")
        button11 = Button(win, text = "fill color", bg = "white")
        print(3)
    elif n == 2:
        button1 = Button(win, text = "canvas color", bg = "white")
        button6 = Button(win, text = "pen color", bg = "black")
        button11 = Button(win, text = "fill color", bg = "white")
        print(1234)
    elif n == 3:
        button1 = Button(win, text = "canvas color", bg = "white")
        button6 = Button(win, text = "pen color", bg = "white")
        button11 = Button(win, text = "fill color", bg = "black")
        print(312353214)
win = Tk()
button1 = Button(win, text = "canvas color", bg = "white", command = change_tool(1))
button2 = Button(win, text = "black", bg = "black")
button3 = Button(win, text = "blue", bg = "blue")
button4 = Button(win, text = "green", bg = "green")
button5 = Button(win, text = "+", bg = "white")
button6 = Button(win, text = "pen color", bg = "white", command = change_tool(2))
button7 = Button(win, text = "white", bg = "white")
button8 = Button(win, text = "red", bg = "red")
button9 = Button(win, text = "yellow", bg = "yellow")
button10 = Button(win, text = "-", bg = "white")
button11 = Button(win, text = "fill color", bg = "white", command = change_tool(3))
button12 = Button(win, text = "●", bg = "white")
button13 = Button(win, text = "■", bg = "white")
button14 = Button(win, text = "▲", bg = "white")
button15 = Button(win, text = "clear", bg = "white")
canvas = Canvas(win, width = 500, height = 500, bg = "white")
canvas.grid(row = 0, column = 0, columnspan = 5)
button1.grid(row = 1, column = 0)
button2.grid(row = 1, column = 1)
button3.grid(row = 1, column = 2)
button4.grid(row = 1, column = 3)
button5.grid(row = 1, column = 4)
button6.grid(row = 2, column = 0)
button7.grid(row = 2, column = 1)
button8.grid(row = 2, column = 2)
button9.grid(row = 2, column = 3)
button10.grid(row = 2, column = 4)
button11.grid(row = 3, column = 0)
button12.grid(row = 3, column = 1)
button13.grid(row = 3, column = 2)
button14.grid(row = 3, column = 3)
button15.grid(row = 3, column = 4)
canvas.bind("<Double-Button-1>", draw_shape)
win.mainloop()