import graphics as gr
import math as m

SIZE_X = 1000
SIZE_Y = 1000
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)
# Начальные условия
l = 300  # длина маятника
w0 = m.sqrt(9.81 / l)  # круговая (собственная) частота колебаний
Ax = 20  # амплитуда колебаний по Х
fi0 = m.pi  # начальная фаза.
fi = 0  # угол отклонения маятника
t = 0  # начальный момент времени
coords = gr.Point(500, 500)  # начальные координаты маятника в пикселях
x0 = 500
y0 = 500


def get_fi(t):
    """ Вычисляем угол fi отклонение маятника"""
    return Ax * m.sin(w0 * t + fi0)


def new_coords(t):
    """ Вычисляем текущие координаты точки """
    x = l * m.sin(get_fi(t)) + x0  # координата по Х
    y = l * m.cos(get_fi(t)) + y0  # координата по Y
    return gr.Point(x, y)


def add(point_1, point_2):
    """сумма координат точек"""

    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)
    return new_point


def sub(point_1, point_2):
    """разность координат точек"""
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)
    return new_point


# рисуем саму точку на поле с начальными координатами
circle = gr.Circle(coords, 10)
circle.setFill('red')
circle.draw(window)
# устареваем текущие координаты
pref_coords = gr.Point(coords.x, coords.y)

# запускаем сам цикл
while True:
    t += 0.1  # шаг времени
    q = add(new_coords(t), pref_coords)  # сумма координат точек
    p = sub(new_coords(t), pref_coords)  # разность координат точек
    circle.move(p.x, p.y)  # двигаемся на эту разницу
    # устареваем новые координаты
    pref_coords = gr.Point(coords.x, coords.y)
    gr.time.sleep(0.1)
