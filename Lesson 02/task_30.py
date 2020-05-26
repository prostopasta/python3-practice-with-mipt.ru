#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    size = 1
    while not wall_is_on_the_right():
        move_right()
        size += 1

    for y in range(size):
        if (y + 1) % 2 == 0:
            goRight = True
        else:
            goRight = False

        for x in range(size):
            if (x == y) or (size - x == y + 1):
                pass
            else:
                fill_cell()

            if goRight:
                if not wall_is_on_the_right():
                    move_right()
            else:
                if not wall_is_on_the_left():
                    move_left()
        if not wall_is_beneath():
            move_down()


if __name__ == '__main__':
    run_tasks()
