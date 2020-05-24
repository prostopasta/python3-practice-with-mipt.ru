#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():

    for i in range(13):
        move_down()
        posx = 0

        while posx <= (i):
            move_right()
            fill_cell()
            posx += 1

        move_left(posx)

    move_down()
    move_right()


if __name__ == '__main__':
    run_tasks()
