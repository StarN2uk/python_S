from tkinter import *
class Court:
    def __init__(self, window, width, height, img):
        self.canvas = Canvas(window, width = width, height = height)
        self.img = PhotoImage(file = img)
        self.canvas.create_image(width/2, height/2, image = self.img)
        self.width = width
        self.height = height
        self.canvas.pack()
w, h = 745, 374
win = Tk()
canvas = Canvas(win, width = w, height = h)
img = PhotoImage(file = "court.png")
canvas.create_image(w/2, h/2, image = img)
canvas.pack()
win.mainloop()