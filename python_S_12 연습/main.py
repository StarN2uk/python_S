from tkinter import *
from court import *
from ball import *
from racket import *
width, height = 745, 374
win = Tk()
canvas = Canvas(win, width = width, height = height)
win.title("Tennis Game")
win.geometry("745x374+150+150")
win.resizable(False, False)
img = PhotoImage(file = "red_racket.png")
img2 = PhotoImage(file = "green_racket.png")
img3 = PhotoImage(file = "court.png")
a, b = 645, 187
a2, b2 = 100, 187
court = Court(win, width, height, "court.png")
racket = canvas.create_image(a, b, image = img)
racket2 = canvas.create_image(a2, b2, image = img2)
x1, y1 = width / 2, height / 2
x2, y2 = x1 + 30, y1 + 30
canvas.pack()
ball = Ball(court, x1, y1, x2, y2)
def play_game():
    ball.move_ball()
    win.after(50, play_game)
    if ball.x1 <= 5:
        winner = "green"
        ball.stop_ball()
    if ball.x1 + ball.width >= court.width - 5:
        winner = "red"
        ball.stop_ball()
def score():
        global green_score
        global red_score
        global winner
        if winner == "red":
            red_score += 1
            winner = ''
        elif winner == "green":
            green_score += 1
            winner = ''
        court.draw_score(red_score, green_score)
play_game()
win.mainloop()