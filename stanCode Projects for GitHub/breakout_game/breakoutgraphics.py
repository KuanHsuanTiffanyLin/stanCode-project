"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
-----------------------------------------
SC101 - Assignment 2
File: breakoutgraphics.py
Name: Tiffany Lin
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    # Constructor
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-self.paddle.width)/2, y=window_height-paddle_offset)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width-ball_radius)/2, y=(window_height-ball_radius)/2)

        # Default initial velocity for the ball.
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners.
        onmouseclicked(self.game_start)  # Todo: Need fixing!!!
        self.mouse_lock = False
        onmousemoved(self.paddle_move)

        # Draw bricks.
        for i in range(brick_rows):
            self.brick_x = 0
            self.brick_y = brick_offset
            self.brick_y += (brick_height+brick_spacing)*i
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick_color(i)
                self.window.add(self.brick, x=self.brick_x, y=self.brick_y)
                self.brick_x += (brick_width+brick_spacing)
        self.brick_left = brick_rows*brick_cols

        # For detecting whether ball hit objects.
        self.obj = 0

    # Methods
    def game_start(self, event):  # Todo: Need fixing!!
        """
        To detect whether the game has started or not.
                If not, the game will start and turns the mouse lock on (True).
                If yes, further mouse clicks should have no effects.
        """
        self.mouse_lock = True

    def move_ball(self):
        """
        Ball move by the velocity of __dx and __dy as defined in the constructor.
        """
        self.ball.move(self.__dx, self.__dy)

    def reset_ball(self):
        """
        Reset the ball back to its initial position.
        Mouse lock off (False).
        """
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.mouse_lock = False

    def handle_collision(self):
        """
        Updates __dx and __dy depending on whether or not ball has hit a wall, the paddle or bricks.
        """
        # Hit left/right wall
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball.width:
            self.__dx = -self.__dx
        # Hit top/bottom wall
        if self.ball.y <= 0 or self.ball.y >= self.window.height - self.ball.height:
            self.__dy = -self.__dy

        # Hit paddles/bricks
        self.detect_obj()
        self.hit_paddle_or_bricks()

    def detect_obj(self):
        """
        Detect if the ball hit any objects.
        """
        self.obj = self.window.get_object_at(self.ball.x, self.ball.y)
        if self.obj is not None:
            return self.obj
        else:
            self.obj = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.width)
            if self.obj is not None:
                return self.obj
            else:
                self.obj = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
                if self.obj is not None:
                    return self.obj
                else:
                    self.obj = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y+ + self.ball.width)
                    if self.obj is not None:
                        return self.obj
                    else:
                        return None

    def hit_paddle_or_bricks(self):
        """
        Identify whether the object(s) hit is the paddle or brick.
        """
        if self.obj == self.paddle:
            self.__dy = -self.__dy
        elif self.obj is not None and self.obj is not self.paddle:
            self.__dy = -self.__dy
            self.window.remove(self.obj)
            self.brick_left -= 1

    def ball_out(self):
        """
        Return whether or not the ball has fallen below the paddle/bottom wall.
        """
        is_ball_out = self.ball.y >= self.window.height - self.ball.height
        return is_ball_out

    def paddle_move(self, event):
        """
        Sync the center of the paddle and the location of the mouse while moving.
        """
        if event.x - self.paddle.width/2 <= 0:
            self.paddle.x = 0
        elif self.window.width - event.x <= self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width/2

    def brick_color(self, i):
        """
        Sets the bricks in color designated in the handout.
        """
        if i <= 1:
            self.brick.fill_color = 'red'
        elif 1 < i <= 3:
            self.brick.fill_color = 'orange'
        elif 3 < i <= 5:
            self.brick.fill_color = 'yellow'
        elif 5 < i <= 7:
            self.brick.fill_color = 'green'
        elif 7 < i <= 9:
            self.brick.fill_color = 'blue'
        else:
            pass


"""
Ideas for extensions:
- ENTER USER NAME
- CHOOSE MODE
- BRICKS' COLOR VARIETY                        
- CHOOSE WHERE TO DROP THE BALL
- PADDLE LENGTHEN/SHORTEN
- GAIN LIVES
- IMPORT IMAGE FOR BACKGROUND
- PADDLE LOWER ON CLICKS
"""