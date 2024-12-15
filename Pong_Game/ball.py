from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slow")
        self.x_move = 3
        self.y_move = 3

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def wall_bounce(self):
        self.y_move *= -1
    def paddle_bounce(self):
        self.x_move *= -1

    def ball_reset(self):
        self.home()
        self.paddle_bounce()

