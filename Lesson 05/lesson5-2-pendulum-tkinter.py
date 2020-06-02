import time
import math
from tkinter import *


class Ball:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


root = Tk()
C = Canvas(root, width='1000', height='200')
C.grid()
graph = Canvas(root, bg='white', width='1000', height='100')
graph.grid()
graph.create_line(0, 50, 1000, 50)
ball = Ball(650, 0, 20)
x1 = int(C['width']) / 2
L = math.sqrt((ball.x - x1) ** 2 + ball.y ** 2)

old_x = ball.x
old_y = ball.y
acc = 1500  # pixels per s^2
then = time.time()
t = 0
# t1=0
# T = 2*math.pi*math.sqrt(L/acc)
# j=0
delay = time.time()
while True:
    now = time.time()
    n_dt = round((now - then) / 0.016)
    then = now
    if time.time() - delay > 5:
        for i in range(n_dt):
            prev_x = ball.x
            prev_y = ball.y
            ball.x += ball.x - old_x
            ball.y += ball.y - old_y + acc * 0.016 * 0.016

            l_x = x1 - ball.x
            l_y = -ball.y
            l = math.sqrt(l_x ** 2 + l_y ** 2)
            if l > L:
                ball.x += l_x * ((l - L) / l)
                ball.y += l_y * ((l - L) / l)
            old_x = prev_x
            old_y = prev_y

        all = C.find_all()
        for i in all:
            C.delete(i)
        C.create_line(x1, 0, ball.x, ball.y)
        C.create_oval(ball.x - ball.r, ball.y - ball.r, ball.x + ball.r, ball.y + ball.r, fill='blue')
        # t1+=1
        # if(t1*0.016 > T):
        #    graph.create_oval(t-5, 50+(500-ball.x)*50/250-5, t+5, 50+(500-ball.x)*50/250+5, fill = 'orange')
        #   t1=0
        # else:
        graph.create_oval(t, 50 + (500 - ball.x) * 50 / 250, t, 50 + (500 - ball.x) * 50 / 250, outline='green')
        # v = math.sqrt((ball.x-old_x)**2 + (ball.y-old_y)**2)
        v = ball.x - old_x
        graph.create_oval(t, 50 + (v / 10) * 50, t, 50 + (v / 10) * 50, outline='red')
        t += 1

        C.create_oval(ball.x - ball.r - 5, ball.y - ball.r - 5, ball.x + ball.r + 5, ball.y + ball.r + 5, outline='')
        C.create_oval(ball.x - ball.r - 10, ball.y - ball.r - 10, ball.x + ball.r + 10, ball.y + ball.r + 10,
                      outline='')

        # graph.create_text(70, 10, text="T = " + T)
    C.update()
    time.sleep(0.016)  # - time.time() + now)
