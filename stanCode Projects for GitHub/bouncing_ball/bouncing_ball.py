"""
File: bouncing_ball.py
Name: Tiffany Lin
-------------------------
stanCode SC101 May2020
Assignment 1- Problem 3
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 100

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True

# This helps restrict mouse clicks for actions while ball is bouncing
mouse_lock = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball, START_X, START_Y)
    onmouseclicked(activate)


def activate(event):
    if mouse_lock == 0:
        ball_bouncing()
    else:
        nothing = GOval(5, 5)
        nothing.color = 'white'
        window.add(nothing, event.x, event.y)


def ball_bouncing():
    bounce_x = VX
    bounce_y = GRAVITY
    fall = 0
    count = 0
    global mouse_lock
    mouse_lock = 1
    while True:
        if ball.x <= window.width and ball.y + bounce_y < window.height:
            ball.move(bounce_x, bounce_y)
            pause(DELAY)
            fall += bounce_y
            bounce_y += GRAVITY
        elif ball.y + bounce_y >= window.height:
            bounce_y = - bounce_y
            bounce_y *= REDUCE
            ball.move(bounce_x, bounce_y)
            pause(DELAY)
            bounce_y += GRAVITY
        elif ball.x >= window.width:
            window.remove(ball)
            window.add(ball, START_X, START_Y)
            count += 1
            if count == 3:
                count = 0
                mouse_lock = 0
                break


if __name__ == "__main__":
    main()
