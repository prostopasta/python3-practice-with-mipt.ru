import math
import turtle

turtle.shape('turtle')
turtle.speed('fastest')
radius = 100
num = 6
circle_edges = 90
circle_angle = 360 / num


def circle(edges, rad, angle, clockwise=False, solid=True):
    turtle.home()
    turtle.setheading(angle)
    turtle.pendown()
    for nn in range(edges):
        if not solid:
            turtle.dot(2, "blue")
            turtle.penup()

        turtle.forward(2 * rad * math.sin(math.pi / (edges - 1)))
        turtle.pendown()

        if clockwise:
            turtle.right(360 / edges)
        else:
            turtle.left(360 / edges)


n = 1
while n <= int(num / 2):
    circle(circle_edges, radius, circle_angle * (n - 1))
    circle(circle_edges, radius, circle_angle * (n - 1), clockwise=True)
    n += 1
