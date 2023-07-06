from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.pu()
        self.hideturtle()
        self.goto(-280, 260)
        self.increase_level()

    def increase_level(self):
        self.level += 1
        self.write(f"level: {self.level}", False, "left", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, "left", FONT)

