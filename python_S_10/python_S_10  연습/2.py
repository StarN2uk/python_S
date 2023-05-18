from tkinter import *
pen_color = "black"
s = ''
wt = 3
def shape1():
    global s
    s = 'oval'
def shape2():
    global s
    s = 'rectangle'
def shape3():
    global s
    s = 'polygon'
def Shape(event):
    global s
    x1, y1 = event.x, event.y
    x2, y2 = x1 + 50, y1 + 50
    x3, y3 = event.x, event.y
    x4, y4 = x3 + 25, y3 + 50
    x5, y5 = x3 - 25, y3 + 50
    if s == 'oval':
        canvas.create_oval(x1, y1, x2, y2, fill = pen_color)
    elif s == 'rectangle':
        canvas.create_rectangle(x1, y1, x2, y2, fill = pen_color)
    elif s == 'polygon':
        canvas.create_polygon(x3, y3, x4, y4, x5, y5, fill = pen_color)
def paint(event):
    global pen_color
    global wt
    x1, y1 = event.x, event.y
    x2, y2 = x1 + 4, y1 + 4
    if wt <= 0:
        wt = 0
    canvas.create_line(x1, y1, x2, y2, width = wt, fill = pen_color)
def change_color1():
    global pen_color
    pen_color = "white"
def change_color2():
    global pen_color
    pen_color = "black"
def change_color3():
    global pen_color
    pen_color = "blue"
def change_color4():
    global pen_color
    pen_color = "green"
def change_color5():
    global pen_color
    pen_color = "yellow"
def change_color6():
    global pen_color
    pen_color = "red"
def change_width1():
    global wt
    wt += 1
    paint(wt)
def change_width2():
    global wt
    wt -= 1
    paint(wt)
def clear_color():
    canvas.delete("all")
win = Tk()
canvas = Canvas(win, bg = "white", width = 500, height = 200)
btn1 = Button(win, text = "canvas color", bg = "white")
btn2 = Button(win, text = "black", bg = "black", command = change_color2)
btn3 = Button(win, text = "blue", bg = "blue", command = change_color3)
btn4 = Button(win, text = "green", bg = "green", command = change_color4)
btn5 = Button(win, text = "+", bg = "white", command = change_width1)
btn6 = Button(win, text = "pen color", bg = "white")
btn7 = Button(win, text = "white", bg = "white", command = change_color1)
btn8 = Button(win, text = "red", bg = "red", command = change_color6)
btn9 = Button(win, text = "yellow", bg = "yellow", command = change_color5)
btn10 = Button(win, text = "-", bg = "white", command = change_width2)
btn11 = Button(win, text = "fill color", bg = "white")
btn12 = Button(win, text = "●", bg = "white", command = shape1)
btn13 = Button(win, text = "■", bg = "white", command = shape2)
btn14 = Button(win, text = "▲", bg = "white", command = shape3)
btn15 = Button(win, text = "clear", bg = "white", command = clear_color)
canvas.grid(row =  0, column = 0, columnspan = 5)
btn1.grid(row = 1, column = 0)
btn2.grid(row = 1, column = 1)
btn3.grid(row = 1, column = 2)
btn4.grid(row = 1, column = 3)
btn5.grid(row = 1, column = 4)
btn6.grid(row  = 2, column = 0)
btn7.grid(row = 2, column = 1)
btn8.grid(row = 2, column = 2)
btn9.grid(row = 2, column = 3)
btn10.grid(row = 2, column = 4)
btn11.grid(row = 3, column = 0)
btn12.grid(row = 3, column = 1)
btn13.grid(row = 3, column = 2)
btn14.grid(row = 3, column = 3)
btn15.grid(row = 3, column = 4)
win.bind("<B1-Motion>", paint)
win.bind("<Double-Button-1>", Shape)
win.mainloop()