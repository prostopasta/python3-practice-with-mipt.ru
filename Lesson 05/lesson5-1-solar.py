# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab5.html#id14

import graphics as gr

SIZE_X = 1600
SIZE_Y = 1000
window = gr.GraphWin("Solar System", SIZE_X, SIZE_Y)

PLANET_SIZE = 20
SUN_SIZE = 100

coordinates = gr.Point(SIZE_X // 2, 3 * SIZE_Y // 4)    # Начальное положение планеты
velocity = gr.Point(3, 0)           # Скорость
acceleration = gr.Point(0, 0)       # Центральная сила тяжести

# Обьекты солнечной системы создаются здесь ОДИН лишь раз
rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
rectangle.setFill('black')
rectangle.draw(window)

sun = gr.Circle(gr.Point(SIZE_X // 2, SIZE_Y // 2), SUN_SIZE)
sun.setFill('yellow')
sun.draw(window)

planet = gr.Circle(coordinates, PLANET_SIZE)
planet.setFill('red')
planet.draw(window)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)
    return new_point


def sub(point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)
    return new_point


def draw_planet(_previous_coordinate, _new_coordinate):
    planet.move(_new_coordinate.x - _previous_coordinate.x, _new_coordinate.y - _previous_coordinate.y)


def check_coordinates(_coordinate, _velocity):
    if _coordinate.y < PLANET_SIZE or _coordinate.y > SIZE_Y - PLANET_SIZE:
        _velocity.y = -_velocity.y
    if _coordinate.x < PLANET_SIZE or _coordinate.x > SIZE_X - PLANET_SIZE:
        _velocity.x = -_velocity.x


def update_coordinates(_coordinate, _velocity):
    return add(_coordinate, _velocity)


def update_velocity(_velocity, _acceleration):
    return add(_velocity, _acceleration)


def update_acceleration(_coordinate, _sun_coordinate):
    G = 2500
    diff = sub(_coordinate, _sun_coordinate)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)
    return gr.Point(-diff.x * G/distance_2, -diff.y * G/distance_2)


previous_coordinates = coordinates

while True:
    draw_planet(previous_coordinates, coordinates)
    acceleration = update_acceleration(coordinates, gr.Point(SIZE_X // 2, SIZE_Y // 2))
    previous_coordinates = coordinates
    coordinates = add(previous_coordinates, velocity)
    velocity = update_velocity(velocity, acceleration)
#    check_coordinates(coordinates, velocity)
    gr.time.sleep(0.005)
