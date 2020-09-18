"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao
-----------------------------------------
SC101 - Assignment 2
File: breakout.py
Name: Tiffany Lin
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3            # Number of times the ball can hit bottom wall before the game ends.


def main():
    """
    This program creates the Breakout Game.
    A ball will be bouncing around the GWindow and
    bounce back if it hits the walls, paddles or the bricks.
    Bricks are removed if hit by the ball.
    Player can use the paddle to prevent ball from falling out of
    the bottom window by moving the mouse.
    The game ends if all the bricks are removed or
    the ball falls out of the bottom wall for over NUM_LIVES.
    """
    graphics = BreakoutGraphics()

    # Add animation loop here!
    lives = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        while graphics.mouse_lock is True:
            if graphics.ball_out():
                lives -= 1
                if lives > 0:
                    graphics.reset_ball()
                    break
                elif lives <= 0:
                    break
            if graphics.brick_left == 0:
                break
            graphics.move_ball()
            graphics.handle_collision()
            pause(FRAME_RATE)
        if graphics.brick_left == 0:
            break


if __name__ == '__main__':
    main()
