"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program creates a breakout game. It starts with a random velocity of a bouncing ball.
To win the game, user needs to eliminate all the bricks. If the ball touches the bottom edge
of the window. The ball position will be reset to the middle of the window and user will lose
1 live out of 3. As 3 lives turn 0, user will lose the game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    ball = graphics.get_ball()
    paddle = graphics.get_paddle()
    brick_num = graphics.get_brick_num()
    lives = NUM_LIVES
    vx = 0
    vy = 0
    not_on_paddle = True

    while lives != 0 and brick_num != 0:
        if vx == 0 and vy == 0:
            # The initial velocity
            vx = graphics.get_vx()
            vy = graphics.get_vy()

        ball_corners = [graphics.window.get_object_at(ball.x, ball.y),
                        graphics.window.get_object_at(ball.x, ball.y + ball.height),
                        graphics.window.get_object_at(ball.x + ball.width, ball.y),
                        graphics.window.get_object_at(ball.x + ball.width, ball.y + ball.height)]
        # Set ball bounce
        if ball.x < 0 or ball.x+ball.width > graphics.window.width:
            vx = -vx
        if ball.y < 0:
            vy = -vy
            not_on_paddle = True
        if ball.y+ball.height >= graphics.window.height:
            # Ball is out of boundary
            lives -= 1
            vx = 0
            vy = 0
            graphics.set_lives()
            graphics.reset_ball()
            continue
        for collision in ball_corners:
            if collision:
                if collision is paddle:
                    if not_on_paddle:
                        # Collision on the paddle
                        vy = -vy
                        not_on_paddle = False
                else:
                    if ball.y < paddle.y:       # Avoid removing hearts
                        # Collision on bricks
                        vy = -vy
                        graphics.window.remove(collision)
                        graphics.brick_set.remove(collision)
                        not_on_paddle = True
                break

        # Update bricks number
        brick_num = graphics.get_brick_num()
        ball.move(vx, vy)
        pause(FRAME_RATE)
    if brick_num == 0:
        graphics.window.clear()
        graphics.victory()
    else:
        graphics.window.clear()
        graphics.loss()


if __name__ == '__main__':
    main()
