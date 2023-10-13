from turtle import Screen
import time
from snake import Snake
from scorecard import Scorecard
from food import Food

screen = Screen()
screen.setup(750, 750, 0, 0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

score_card = Scorecard()
food = Food()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.075)
    snake.move()

screen.mainloop()
