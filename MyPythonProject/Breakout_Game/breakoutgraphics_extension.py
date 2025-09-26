"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Provide a :class:`BreakoutGraphics` that supports users to create a breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gimage import GImage
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self._paddle = GRect(paddle_width, paddle_height)
        self._paddle.filled = True
        self.window.add(self._paddle, x=(window_width-paddle_width)//2, y=window_height-paddle_offset)
        # Center a filled ball in the graphical window
        self._ball = GOval(ball_radius*2, ball_radius*2)
        self._ball.filled = True
        self.window.add(self._ball, x=window_width//2-ball_radius, y=window_height//2-ball_radius)
        # Default initial velocity for the ball
        self.__vx = 0
        self.__vy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.game_start)
        onmousemoved(self.paddle_move)
        # Draw bricks
        self.brick_set = set()
        self.draw_bricks(brick_width, brick_height, brick_rows, brick_cols, brick_spacing, brick_offset)

        # Draw lives
        self.lives = 3
        self.heart_lst = []
        for i in range(1, self.lives+1):
            self.heart = GImage('small_heart.jpg')
            self.window.add(self.heart, x=window_width-self.heart.width*i, y=window_height-self.heart.height)
            self.heart_lst.append(self.heart)

        # Label
        self.victory_w = GLabel('You won!')
        self.loss_w = GLabel('Game over')

    def draw_bricks(self, width, height, rows, cols, space, offset):
        """In this method, it draws all the bricks."""
        for i in range(rows):
            for j in range(cols):
                if i < 2:
                    color = 'red'
                elif 2 <= i < 4:
                    color = 'orange'
                elif 4 <= i < 6:
                    color = 'yellow'
                elif 6 <= i < 8:
                    color = 'green'
                else:
                    color = 'blue'
                brick = GRect(width, height)
                brick.filled = True
                brick.fill_color = color
                brick.color = color
                self.brick_set.add(brick)
                self.window.add(brick, x=j*(width+space), y=i*(height+space)+offset)

    def paddle_move(self, mouse):
        """This method is to make the paddle follow the mouse, and the paddle position
        is always within the boundary of the Canvas."""
        if mouse.x < self._paddle.width//2:
            self._paddle.x = 0
        elif mouse.x > self.window.width-self._paddle.width//2:
            self._paddle.x = self.window.width-self._paddle.width
        else:
            self._paddle.x = mouse.x - self._paddle.width//2

    def game_start(self, mouse):
        """
        In this method, as the ball is still, it randomly generates velocity x and y for ball
        when user click the mouse.
        """
        if self.__vx == 0 and self.__vy == 0:
            self.__vx = random.randint(1, MAX_X_SPEED)
            self.__vy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__vx = -self.__vx

    def reset_ball(self):
        """This method reset the ball to its initial position"""
        self.__vx = 0
        self.__vy = 0
        self._ball.x = self.window.width // 2 - BALL_RADIUS
        self._ball.y = self.window.height // 2 - BALL_RADIUS

    def get_paddle(self):
        return self._paddle

    def get_ball(self):
        return self._ball

    def get_vx(self):
        return self.__vx

    def get_vy(self):
        return self.__vy

    def set_lives(self):
        self.window.remove(self.heart_lst[-1])
        self.heart_lst.pop(-1)

    def get_brick_num(self):
        return len(self.brick_set)

    def victory(self):
        self.victory_w.font = '-30'
        self.victory_w.color = 'red'
        self.window.add(self.victory_w, x=(self.window.width-self.victory_w.width)//2,
                        y=(self.window.height+self.victory_w.height)//2)

    def loss(self):
        self.loss_w.font = '-30'
        self.loss_w.color = 'red'
        self.window.add(self.loss_w, x=(self.window.width-self.loss_w.width)//2,
                        y=(self.window.height+self.loss_w.height)//2)




