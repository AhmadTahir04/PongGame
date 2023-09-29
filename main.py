from turtle import *
from paddle import *
from ball import *
import time
from scoreboard import *
from halfline import *

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
half_line = Half((0, 0))
half_line1 = Half((0, 300))
half_line2 = Half((0,-300))
half_line3 = Half((0, 150))
half_line4 = Half((0, -150))





screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.r_point()

    # Detect when L paddle misses
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.l_point()


screen.exitonclick()