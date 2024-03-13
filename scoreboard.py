from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            contents = file.read()
        self.score = 0
        self.high_score = int(contents)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.show()

    def add_point(self):
        self.score += 1
        self.show()

    def show(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.show()
