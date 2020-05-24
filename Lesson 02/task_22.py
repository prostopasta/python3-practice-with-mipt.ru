#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():

    size_x = 1
    size_y = 1

    while not wall_is_on_the_right():
        move_right()
        size_x += 1

    while not wall_is_beneath():
        move_down()
        size_y += 1

    if size_y > 1:
        move_up(size_y-1)

    if size_x == size_y == 1:
        fill_cell()
        return

    for x in range(size_x):
        for y in range(size_y-1):
            fill_cell()
            move_down()

        fill_cell()
        if x != size_x-1:
            move_up(size_y-1)
            move_left()


if __name__ == '__main__':
    run_tasks()
