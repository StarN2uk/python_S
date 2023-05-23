from tkinter import *
from random import *
class Ball:
    def __init__(self, court, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x_dist = 10
        self.y_dist = 10
        self.width = x2 - x1
        self.height = y2 - y1
        self.court = court
        self.canvas = court.canvas
        self.ball = self.canvas.create_oval(x1, y1, x2, y2, fill = 'blue')
    def move_ball(self):
        global add
        self.x1 += self.x_dist
        self.y1 += self.y_dist
        if self.y1 <= 5:
            self.y1 = 5
            add += 1
            self.y_dist *= -1
        if self.y1 >= (self.court.height - (self.height - 5)):
            add += 1
            self.y1 = self.court.height - (self.height - 5)
            self.y_dist *= -1
        if self.x1 <= 5:
            add += 1
            self.x_dist *= -1
        if self.x1 + self.width >= self.court.width - 5:
            add += 1
            self.x_dist *= -1
        self.x1 = self.x1
        self.x2 = self.x1 + self.width
        self.y1 = self.y1
        self.y2 = self.y1 + self.height
        self.canvas.coords(self.ball, self.x1, self.y1, self.x2, self.y2)
        if add >= 5 and add <= 10:
            self.ball = self.canvas.create_oval(x1, y1, x2, y2, fill = '')
        if add >= 10:
            self.ball = self.canvas.create_oval(x1, y1, x2, y2, fill = 'blue')
win = Tk()
add = 0
x1, y1 = 10, 10
x2, y2 = x1 + 30, y1 + 30
x_dist, y_dist = 1, 1
canvas = Canvas(win, width = 1000, height = 1000, bg = "white")
ball = canvas.create_oval(x1, y1, x2, y2, fill = 'blue')
def flow():
    global x1, y1, x2, y2
    x1 += x_dist
    y1 += y_dist
    x2, y2 = x1 + 30, y1 + 30
    canvas.coords(ball, x1, y1, x2, y2)
    win.after(6, flow)
flow()
canvas.pack()
win.mainloop()