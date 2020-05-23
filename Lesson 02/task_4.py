#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():

    if not wall_is_on_the_right():
        move_right()
    elif not wall_is_above():
        move_up()
    elif not wall_is_on_the_left():
        move_left()
    else:
        move_down()


if __name__ == '__main__':
    run_tasks()
