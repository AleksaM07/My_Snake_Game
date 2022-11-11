from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):

    def __init__(self, score):
        super().__init__()
        #self.score = 0
        self.refresh(score)

    def refresh(self, score):
        self.clear()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(f"Score: {score}", move=False, align=ALIGMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGMENT, font=FONT)


