from turtle import *

size = 150


def star(n, col='red'):
    coord = xcor()
    color(col)
    begin_fill()
    if n % 2 != 0:
        ang = 180 - 360 / n / 2
    else:
        ang = 180 - 360 / n
    while True:
        forward(size)
        left(ang)
        if abs(abs(coord) - abs(xcor())) < 1:
            break
    end_fill()

home()
back(size)
star(5)

penup()
home()
forward(size * 0.5)
pendown()
star(11, 'blue')
done()
