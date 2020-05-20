import math
import turtle

turtle.shape('turtle')
side3 = 36
num = 10
circle_edges = 36
adjust = side3 / 3


def side(n):
    if n == 3:
        return side3
    else:
#        return 2 * (radius(n-1)) * math.sin(math.pi / n) / math.cos(math.pi / n)  # высчитывать сторону на основе радиуса вписанной окружности
        return 2 * (radius(n)) * math.sin(math.pi / n)


def radius(n):
    if n == 3:
        return side(n) / math.sin(math.pi / n) / 2
    else:
        return radius(3) + (n - 3) * adjust


def circle(n, r, solid=True):
    turtle.penup()
    turtle.home()
    turtle.forward(r)
    turtle.setheading(90)
    turtle.pendown()
    for i in range(n):
        if not solid:
            turtle.dot(2, "blue")
            turtle.penup()
        turtle.forward(2 * r * math.sin(math.pi / n))
        turtle.pendown()
        turtle.left(360 / n)


turtle.penup()
for i in range(3, num + 3):
    n_angle = 90 - 180 / i
    n_radius = radius(i)
    n_side = side(i)
    turtle.forward(radius(3) + (i - 3) * adjust)
    turtle.pendown()
    for j in range(i):
        if j == 0:
            turtle.left(180 - n_angle)
        else:
            turtle.left(180 - 2 * n_angle)
        turtle.forward(n_side)
#    circle(circle_edges, n_radius, False)  # рисовать описанную вокруг текущего многоугольника окружность
    turtle.penup()
    turtle.home()
