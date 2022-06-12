from turtle import Screen
from turtlecreation import TurtleCreation
from block import Block
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

turtle = TurtleCreation()
block = Block()
block.hideturtle()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=turtle.go_up)

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    block.create_block()
    block.move_block()

    # Detect the collision of turtle with any block and make the game over
    for seg in block.blocks:
        if turtle.distance(seg) < 20:
            is_game_on = False
            scoreboard.game_over()

    # If turtle reach the other side successfully, start the next level
    if turtle.finished_crossing():
        turtle.reset_player()
        scoreboard.refresh()
        block.increase_block_speed()

screen.exitonclick()
