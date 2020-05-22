import math
import turtle

turtle.shape('turtle')
turtle.speed('fastest')
big_radius = 50
small_radius = big_radius / 5
num_of_springs = 5
circle_edges = 180
circle_angle = 90


def spring(edges, rad, clockwise=True, solid=True):
    turtle.pendown()
    nn = 1
    while nn <= edges / 2:
        if not solid:
            turtle.dot(2, "blue")
            turtle.penup()

        turtle.forward(2 * rad * math.sin(math.pi / (edges - 1)))
        turtle.pendown()

        if clockwise:
            turtle.right(360 / edges)
        else:
            turtle.left(360 / edges)

        nn += 1


turtle.back((2 * big_radius - small_radius) * num_of_springs / 2 - small_radius)
turtle.setheading(circle_angle)

for n in range(num_of_springs):
    spring(circle_edges, big_radius)
    if n != num_of_springs - 1:
        spring(circle_edges, small_radius)
