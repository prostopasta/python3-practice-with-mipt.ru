#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    i = 0
    exit = False
    move_right()
    while not exit:
        for j in range(i):
            if wall_is_on_the_right():
                exit = True
                break
            move_right()
        i += 1
        if not exit:
            fill_cell()


if __name__ == '__main__':
    run_tasks()
