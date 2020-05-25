#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    size = 3
    xcol = 10
    ycol = 5

    for y in range(ycol):
        for n in range(xcol):
            color_plus(size)
            if n != xcol - 1:
                move_up(size // 2)
                move_right(size + size // 2)
            else:
                move_up(size // 2)
        if y != ycol - 1:
            move_down(2 * (size // 2) + 2)
        move_left((size + 1) * (xcol - 1))


def color_plus(size=3):
    move_right(size // 2)
    color_plus_side(size)
    move_right(size // 2)
    move_up(size // 2)
    color_plus_side(size, False)


def color_plus_side(size=3, down=True):
    for nn in range(size-1):
        fill_cell()
        if down:
            move_down()
        else:
            move_left()
    fill_cell()


if __name__ == '__main__':
    run_tasks()
