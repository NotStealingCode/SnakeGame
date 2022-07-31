from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.goto(0, 300)
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align=ALIGNMENT, font=FONT)
