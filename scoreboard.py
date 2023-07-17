from turtle import Turtle
SCORE_ALIGNMENT = "center"
FONT = "courier"
FONT_SIZE = 15
FONT_STYLE = "normal"
class ScoreBoard(Turtle):

    def __init__(self,):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        file = open("data.txt")
        self.high_score = int(file.read())
        file.close()
        self.pencolor("white")
        self.write(f"Your score: {self.score} highscore: {self.high_score}", align=SCORE_ALIGNMENT, font=(FONT, FONT_SIZE, FONT_STYLE))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!!", align=SCORE_ALIGNMENT, font=(FONT, 25, "bold"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Your score: {self.score} highscore: {self.high_score}", align="center",
                   font=('Arial', 15, 'normal'))

    def score_increase(self):
        self.score += 1
        self.update_scoreboard()

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
