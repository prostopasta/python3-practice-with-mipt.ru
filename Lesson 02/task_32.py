#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    x = 0
    y = 0
    before_colored = 0

    while wall_is_beneath():
        x += 1

        while not wall_is_above():
            move_up()
            if cell_is_filled():
                before_colored += 1
            else:
                fill_cell()
            y += 1

        if y > 0:
            move_down(y)
            y = 0

        if wall_is_above() and wall_is_beneath():
            fill_cell()

        move_right()

    mov('ax', before_colored)


if __name__ == '__main__':
    run_tasks()
