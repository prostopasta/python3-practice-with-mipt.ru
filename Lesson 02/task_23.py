#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():

    x = 0
    y = 0

    while not wall_is_on_the_right():
        move_right()
        x += 1

        while not wall_is_above():
            move_up()
            fill_cell()
            y += 1

        if (y > 0):
            move_down(y)
            y = 0

    move_left(x)


if __name__ == '__main__':
    run_tasks()
