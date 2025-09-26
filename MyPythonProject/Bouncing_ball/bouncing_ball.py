"""
File: bouncing_ball.py
Name: Shane
-------------------------
This program simulates a bouncing ball at (START_X, START_Y) that has VX as x velocity and 0 as y velocity.
Each bounce reduces y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True
dropping = False
counts = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global counts, dropping
    # milestone1 create a ball and move the ball when clicked the mouse
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(ball_move)

    while True:
        pause(DELAY)
        # milestone2  ball falls and bounces
        vy = 0  # The initial velocity
        if dropping and counts != 3:
            while ball.x < window.width:
                ball.move(VX, vy)
                vy += GRAVITY
                if ball.y >= window.height - SIZE:  # Ball hits the ground
                    vy *= REDUCE
                    vy = -vy
                pause(DELAY)
            # milestone3 recording the click times
            counts += 1
            # after ball goes out of window.width, create a new ball at the initial position
            window.add(ball, x=START_X, y=START_Y)
            dropping = False    # Turning back to False, wait for the next click


def ball_move(mouse):
    global dropping
    dropping = True


if __name__ == "__main__":
    main()
