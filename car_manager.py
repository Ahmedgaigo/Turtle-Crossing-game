from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = r.randint(1, 6)
        if chance == 1:
            car = Turtle()
            car.pu()
            self.hideturtle()
            car.shape("square")
            car.color(r.choice(COLORS))
            car.shapesize(1, 2)
            car.y_value = r.randint(-250, 250)
            car.goto(300, car.y_value)
            self.all_cars.append(car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def move(self):
        for car in self.all_cars:
            car.bk(self.car_speed)
