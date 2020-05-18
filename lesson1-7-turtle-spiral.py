import turtle, math

a = 1.5
b = -2.4
t = 0
while t <= 11*math.pi:
    x = (a + b*t) * math.cos(t)
    y = (a + b*t) * math.sin(t)
    turtle.goto(x,y)
    t += 0.1