import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)

# creating player object
player = Player()

# creating car object
car = CarManager()

level = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    # Detect collision of player with the cars
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            level.game_over()
            game_is_on = False

    # Turtle reaches end of screen
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        level.clear()
        level.increase_level()


screen.exitonclick()
