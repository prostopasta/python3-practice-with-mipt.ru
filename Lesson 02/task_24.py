#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    color_plus(3)
    move_up()

def color_plus(size=3):
    move_right(size//2 + 1)
    color_plus_side(size)
    move_right(size//2 + 1)
    move_up(size//2)
    color_plus_side(size, False)


def color_plus_side(size=3, down=True):
    for n in range(size):
        if down:
            move_down()
        else:
            move_left()
        fill_cell()


if __name__ == '__main__':
    run_tasks()
