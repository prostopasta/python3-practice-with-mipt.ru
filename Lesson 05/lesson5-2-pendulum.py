# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab5.html#id23

import graphics as gr
import math

SIZE_X = 800
SIZE_Y = 800
window = gr.GraphWin("Pendulum", SIZE_X, SIZE_Y)

SIZE = 30
LENGTH = SIZE_Y / 2
ANGLE = math.pi / 4    # Начальный угол отклонения маятника
G = 9.81
AMPLITUDE = LENGTH * math.sin(ANGLE)
TIME = 2 * math.pi * (LENGTH / G) ** 0.5
TIME_STEP = TIME / 100

mountpoint = gr.Point(SIZE_X // 2, SIZE_Y // 2)       # Точка крепления нити маятника
coordinates = gr.Point(mountpoint.x + AMPLITUDE, mountpoint.y)    # Начальное положение маятника


# Обьекты создаются здесь ОДИН лишь раз
rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
rectangle.setFill('yellow')
rectangle.draw(window)

mount = gr.Circle(mountpoint, SIZE // 10)
mount.setFill('black')
mount.draw(window)

rope = gr.Line(mountpoint, coordinates)
rope.setFill('black')
rope.draw(window)

pendulum = gr.Circle(coordinates, SIZE)
pendulum.setFill('blue')
pendulum.draw(window)


def update_coordinates(_coordinates, _time):
    current_angle = ANGLE + _time * (G / LENGTH) ** 0.5
#    if _time % math.pi < TIME_STEP:
    new_coordinates = gr.Point(mountpoint.x + AMPLITUDE * math.sin(current_angle),
                               mountpoint.y - AMPLITUDE * math.cos(current_angle))
#    else:
#        new_coordinates = gr.Point(mountpoint.x - AMPLITUDE * math.sin(current_angle),
#                                   mountpoint.y - AMPLITUDE * math.cos(current_angle))
    return new_coordinates


def draw_rope(_new_coordinates):
    global rope
    rope.undraw()
    rope.setFill('yellow')
    rope.draw(window)
    rope = gr.Line(mountpoint, _new_coordinates)
    rope.setFill('black')
    rope.draw(window)
    mount.undraw()
    mount.draw(window)


def draw_pendulum(_previous_coordinates, _new_coordinates):
    pendulum.move(_new_coordinates.x - _previous_coordinates.x, _new_coordinates.y - _previous_coordinates.y)
    draw_rope(_new_coordinates)


previous_coordinates = coordinates
t = 0
while t <= 10 * TIME:
    draw_pendulum(previous_coordinates, coordinates)
    previous_coordinates = coordinates
    coordinates = update_coordinates(previous_coordinates, t)
    t += TIME_STEP
    gr.time.sleep(0.02)

#  Ожидание нажатия кнопки мыши по окну.
window.getMouse()

#  После того как мы выполнили все нужные операции, окно следует закрыть.
window.close()