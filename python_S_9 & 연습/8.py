from tkinter import *
pen_color = "black"
def paint(event):
    global pen_color
    global wt
    x1, y1 = event.x, event.y
    x2, y2 = x1 + 5, y1 + 5
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
wt = 3
canvas = Canvas(win, bg = "white", width = 500, height = 200)
btn = Button(win, text = "white", bg = "white", command = change_color1)
btn1 = Button(win, text = "black", bg = "black", command = change_color2)
btn2 = Button(win, text = "blue", bg = "blue", command = change_color3)
btn3 = Button(win, text = "green", bg = "green", command = change_color4)
btn4 = Button(win, text = "yellow", bg = "yellow", command = change_color5)
btn5 = Button(win, text = "red", bg = "red", command = change_color6)
btn6 = Button(win, text = "+", bg = "white", command = change_width1)
btn7 = Button(win, text = "-", bg = "white", command = change_width2)
btn8 = Button(win, text = "clear", bg = "white", command = clear_color)
canvas.pack()
btn.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()
btn7.pack()
btn8.pack()
win.bind("<B1-Motion>", paint)
win.mainloop()