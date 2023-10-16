from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.body = []
        self.create()
        self.head = self.body[0]

    def create(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(position)
            self.body.append(new_segment)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            x = self.body[i - 1].xcor()
            y = self.body[i - 1].ycor()
            self.body[i].goto(x, y)
        self.head.forward(MOVING_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def increase_body(self):
        new_seg = Turtle("square")
        new_seg.color("green")
        new_seg.penup()
        new_seg.goto(self.body[-1].position())
        self.body.append(new_seg)

    def check_bound(self):
        self.check_x()
        self.check_y()

    def check_x(self):
        if self.head.xcor() < -290:
            self.head.goto(290, self.head.ycor())
        elif self.head.xcor() > 290:
            self.head.goto(-290, self.head.ycor())

    def check_y(self):
        if self.head.ycor() < -290:
            self.head.goto(self.head.xcor(), 290)
        elif self.head.ycor() > 290:
            self.head.goto(self.head.xcor(), -290)