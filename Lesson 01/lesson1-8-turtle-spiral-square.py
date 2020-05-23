import turtle

turtle.shape('turtle')

width = 6
side = 12
for i in range(10):
    for j in range(4):
        turtle.forward(side * (i + 1) + width * j/2)
        turtle.left(90)