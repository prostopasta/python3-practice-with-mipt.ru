#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():

    goright = True
    while goright:
        while wall_is_beneath():
            if goright:
                if not wall_is_on_the_right():
                    move_right()
                else:
                    goright = False
            elif not goright:
                if wall_is_on_the_left():
                    if wall_is_beneath():
                        return
                else:
                    move_left()

        if not wall_is_beneath():
            move_down()
            goright = True


if __name__ == '__main__':
    run_tasks()
