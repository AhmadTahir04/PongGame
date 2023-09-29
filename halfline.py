from turtle import *

class Half(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=0.2)
        self.color("white")
        self.penup()
        self.goto(position)