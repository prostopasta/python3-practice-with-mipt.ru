#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():

    for i in range(2):
        move_right()
        move_down()
    fill_cell()

    move_right()
    move_down()
    move_right()

if __name__ == '__main__':
    run_tasks()
