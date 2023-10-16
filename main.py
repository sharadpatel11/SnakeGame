from turtle import Screen
import time
from snake import Snake
from scorecard import Scorecard
from food import Food

screen = Screen()
screen.setup(600, 600, 0, 0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scorecard = Scorecard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scorecard.increase_score()
        snake.increase_body()

    snake.check_bound()

    for seg in snake.body:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            game_is_on = False
            scorecard.game_over()


screen.exitonclick()
