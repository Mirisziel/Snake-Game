from turtle import Turtle
ways = [270, 180, 90, 0]
class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.pensize(10)
        self.penup()
        self.goto(300, 300)
        self.create_wall()
    def create_wall(self):
        for direction in ways:
            self.setheading(direction)
            self.pendown()
            self.forward(600)
