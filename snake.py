from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for snake_index in STARTING_POSITIONS:
            self.add_segment(snake_index)

    def add_segment(self, snake_index):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(snake_index)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())




    def move(self):
        for change_position in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[change_position - 1].xcor()
            new_y = self.segments[change_position - 1].ycor()
            self.segments[change_position].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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
