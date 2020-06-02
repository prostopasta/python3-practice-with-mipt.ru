# http://judge.mipt.ru/mipt_cs_on_python3/code/lab5/
import graphics as gr

SIZE_X = 400
SIZE_Y = 400
BALL_SIZE = 20
coordinates = gr.Point(SIZE_X // 2, SIZE_Y // 2)    #  Начальное положение шарика
velocity = gr.Point(2, 0)       #  Скорость
acceleration = gr.Point(0, 0.1)     #  Равномерная сила тяжести
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)
    return new_point


def draw_circle(_coordinate):
    circle = gr.Circle(_coordinate, BALL_SIZE)
    circle.setFill('blue')
    circle.draw(window)


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('yellow')
    rectangle.draw(window)


def check_coordinates(_coordinate, _velocity):
    if _coordinate.y < BALL_SIZE or _coordinate.y > SIZE_Y - BALL_SIZE:
        _velocity.y = -_velocity.y
    if _coordinate.x < BALL_SIZE or _coordinate.x > SIZE_X - BALL_SIZE:
        _velocity.x = -_velocity.x


def update_velocity(_velocity, _acceleration):
    return add(_velocity, _acceleration)


while True:
    clear_window()
    draw_circle(coordinates)
    coordinates = add(coordinates, velocity)
    velocity = update_velocity(velocity, acceleration)
    check_coordinates(coordinates, velocity)
#    gr.time.sleep(0.01)
