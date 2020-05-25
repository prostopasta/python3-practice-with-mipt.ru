#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    size = 3
    for n in range(5):
        color_plus(size)
        if n != 4:
            move_up(size // 2 + 1)
            move_right(size + size // 2)
        else:
            move_up(size // 2)


def color_plus(size=3):
    move_right(size // 2)
    color_plus_side(size)
    move_right(size // 2)
    move_up(size // 2)
    color_plus_side(size, False)


def color_plus_side(size=3, down=True):
    for nn in range(size):
        if down:
            move_down()
            fill_cell()
        else:
            fill_cell()
            if nn != size - 1:
                move_left()


if __name__ == '__main__':
    run_tasks()
