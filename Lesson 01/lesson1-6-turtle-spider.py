import turtle

turtle.shape('turtle')

legs = 12
length = 100
for i in range(legs):
    turtle.forward(length)
    turtle.stamp()
    turtle.back(length)
    turtle.right(360/legs)
