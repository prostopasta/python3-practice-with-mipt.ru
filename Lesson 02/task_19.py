#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    stop_flag = False

    while True:
        while not wall_is_on_the_left():
            move_left()

        if not wall_is_above():
            break

        while not wall_is_on_the_right():
            move_right()

        if wall_is_above():
            stop_flag = True

        break

    if stop_flag:
        return

    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
