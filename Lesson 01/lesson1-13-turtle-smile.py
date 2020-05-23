import math
import turtle

turtle.shape('turtle')
turtle.speed('slow')
face_radius = 200
eye_radius = face_radius / 5
smile_radius = face_radius / 2
circle_edges = 18  # Должно быть четным!
start_angle = 90
angle = 360 / circle_edges
face_side = 2 * face_radius * math.sin(math.pi / circle_edges)
eye_side = 2 * eye_radius * math.sin(math.pi / circle_edges)


def circle(edges, rad, ang, clockwise=False, solid=True):
    turtle.pendown()

    for nn in range(edges):
        if not solid:
            turtle.dot(2, "blue")
            turtle.penup()

        distance = 2 * rad * math.sin(math.pi / edges)
        turtle.forward(distance)
        print('n(', nn, '): pos=', turtle.position(), ", ang=", turtle.heading())

        if clockwise:
            turtle.right(angle)
        else:
            turtle.left(angle)

        turtle.pendown()


def spring(edges, rad, clockwise=True, solid=True):
    turtle.pendown()
    nn = 1

    while nn <= edges / 2:
        if not solid:
            turtle.dot(2, "blue")
            turtle.penup()

        distance = 2 * rad * math.sin(math.pi / edges)
        turtle.forward(distance)

        if clockwise:
            turtle.right(angle)
        else:
            turtle.left(angle)

        turtle.pendown()
        nn += 1


turtle.home()
turtle.penup()
turtle.forward(face_radius)
turtle.setheading(start_angle + angle / 2)
print('face: pos=', turtle.position(), ", ang=", turtle.heading())
turtle.fillcolor("yellow")
turtle.begin_fill()
circle(circle_edges, face_radius, angle)  # рисуем голову
turtle.end_fill()

turtle.penup()
turtle.setheading(start_angle + angle / 2)
turtle.goto(eye_radius - face_radius / 2, face_radius / 2)
print('right: pos=', turtle.position(), ", ang=", turtle.heading())
turtle.fillcolor("blue")
turtle.begin_fill()
circle(circle_edges, eye_radius, angle)  # рисуем правый глаз
turtle.end_fill()

turtle.penup()
turtle.setheading(start_angle + angle / 2)
turtle.goto(eye_radius + face_radius / 2, face_radius / 2)
print('left: pos=', turtle.position(), ", ang=", turtle.heading())
turtle.fillcolor("blue")
turtle.begin_fill()
circle(circle_edges, eye_radius, angle)  # рисуем левый глаз
turtle.end_fill()

turtle.penup()
turtle.goto(0, face_radius / 4)
turtle.pendown()
turtle.setheading(270)
turtle.color("black")
turtle.pensize(face_radius // 10)
turtle.forward(face_radius / 2)         # рисуем нос

turtle.penup()
turtle.setheading(360 - start_angle - angle / 2)
turtle.goto(face_radius / 2, - face_radius / 4)
print('smile: pos=', turtle.position(), ", ang=", turtle.heading())
turtle.color("red")
spring(circle_edges, smile_radius)      # рисуем улыбку
