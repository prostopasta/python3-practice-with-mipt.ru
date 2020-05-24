#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():

    go_right = True

    for i in range(12):
        for j in range(28):
            to_fill = True
            if go_right:
                if not wall_is_on_the_right():
                    move_right()

                if wall_is_on_the_right():
                    to_fill = False
                    go_right = False
                    move_down()
            else:
                if not wall_is_on_the_left():
                    move_left()

                if wall_is_on_the_left():
                    to_fill = False
                    go_right = True
                    move_down()

            if to_fill:
                fill_cell()

    move_right()

if __name__ == '__main__':
    run_tasks()
