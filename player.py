from turtle import Turtle, Screen


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.left(90)
        self.shape("turtle")
        self.go_to_start()
        self.screen = Screen()
        self.screen.listen()
        self.screen.onkeypress(self.move_up, "Up")

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.fd(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

