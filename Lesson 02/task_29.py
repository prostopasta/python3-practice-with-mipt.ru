#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    x = 0
    while True:
        if (x < 3) and not wall_is_on_the_right():
            move_right()
        else:
            break

        if cell_is_filled():
            x += 1
        else:
            x = 0


if __name__ == '__main__':
    run_tasks()
