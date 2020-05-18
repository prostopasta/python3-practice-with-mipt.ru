import turtle

turtle.shape('turtle')

width = 20
for i in range(10):
    for j in range(4):
        turtle.forward(width*(i+1))
        turtle.left(90)
    turtle.right(135)
    turtle.penup()
    turtle.forward((2*width**2)**0.5/2)
    turtle.left(135)
    turtle.pendown()