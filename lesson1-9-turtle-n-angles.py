import math
import turtle

turtle.shape('turtle')
side = 100
num = 10


def ext_radius(n=3):
    if n == 3:
        return side / math.sin(math.pi / n) / 2
    else:
        return ext_radius(n-1) / math.cos(math.pi / n)


turtle.penup()
for i in range(3, num + 1):
    n_angle = 90 - 180 / i
    turtle.forward(ext_radius(i))
    turtle.pendown()
    for j in range(i):
        if j == 0:
            turtle.left(180 - n_angle)
        else:
            turtle.left(180 - 2 * n_angle)
        turtle.forward(side)
    turtle.penup()
    turtle.home()
