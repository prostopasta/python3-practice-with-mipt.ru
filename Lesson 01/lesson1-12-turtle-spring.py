import math
import turtle

turtle.shape('turtle')
turtle.speed('fastest')
big_radius = 60
small_radius = big_radius / 5
num_of_springs = 5
circle_edges = 10     # Должно быть четным!
start_angle = 90
angle = 360 / circle_edges


def spring(edges, rad, clockwise=True, solid=True):
    turtle.pendown()
    nn = 1

    while nn <= edges / 2:
        if not solid:
            turtle.dot(2, "blue")
            turtle.penup()

        distance = 2 * rad * math.sin(math.pi / edges)
#        print('start(', nn, ') : pos=', turtle.position(), ', dist=', distance, ', ang=', turtle.heading())

        turtle.forward(distance)

        if clockwise:
            turtle.right(angle)
        else:
            turtle.left(angle)

#        print('end(', nn, ') : pos=', turtle.position(), ', dist=', distance, ', ang=', turtle.heading())

        turtle.pendown()
        nn += 1


turtle.forward(((big_radius - small_radius) * num_of_springs + small_radius))
turtle.back(2 * ((big_radius - small_radius) * num_of_springs + small_radius))
turtle.setheading(90 - angle / 2)
#print('start: pos=', turtle.position(), ", ang=", turtle.heading())

for n in range(num_of_springs):
    spring(circle_edges, big_radius)
#    print('big: end pos=', turtle.position(), ", ang=", turtle.heading())

    if n != num_of_springs - 1:
        spring(circle_edges, small_radius)
#        print('small: end pos=', turtle.position(), ", ang=", turtle.heading())

turtle.home()
