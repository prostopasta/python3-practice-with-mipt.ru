import turtle, math

turtle.shape('turtle')
a = 2.5
b = -1
t = 0
turtle.right(90)
while t <= 21*math.pi:
    x = (a + b*t) * math.cos(t)
    y = (a + b*t) * math.sin(t)
    turtle.left(360/2/math.pi/5)
    turtle.goto(x,y)
    t += 0.2