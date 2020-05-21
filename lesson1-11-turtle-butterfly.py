import math
import turtle

turtle.shape('turtle')
turtle.speed('fastest')
first_radius = 50
num_of_circles = 10
circle_edges = 90
circle_angle = 90


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


for n in range(num_of_circles):
    circle(circle_edges, first_radius * (1 + n / 5), circle_angle)
    circle(circle_edges, first_radius * (1 + n / 5), circle_angle, clockwise=True)
