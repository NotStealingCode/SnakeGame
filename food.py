from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        random_x = random.randint(-620, 620)
        random_y = random.randint(-330, 330)
        self.goto(random_x, random_y)
