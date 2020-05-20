import math
import turtle

turtle.shape('turtle')
side = 200
num = 10


def n_side(n):
    if n == 3:
        return side
    else:
        return 2 * n_radius(n - 1) * math.sin(math.pi / n) / math.cos(math.pi / n)


def n_radius(n):
    return n_side(n) / math.sin(math.pi / n) / 2


turtle.penup()
for i in range(3, num + 1):
    n_angle = 90 - 180 / i
    turtle.forward(n_radius(i))
    turtle.pendown()
    for j in range(i):
        if j == 0:
            turtle.left(180 - n_angle)
        else:
            turtle.left(180 - 2 * n_angle)
        turtle.forward(n_side(i))
    turtle.penup()
    turtle.home()
