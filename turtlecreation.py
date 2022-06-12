from turtle import Turtle

STARTING_POSITION = (0, -280)


class TurtleCreation(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.speed("fastest")

    def go_up(self):
        self.forward(20)

    def reset_player(self):
        self.goto(STARTING_POSITION)

    def finished_crossing(self):
        if self.ycor() > 280:
            return True
        else:
            return False

