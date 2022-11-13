import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
GAME_SPEED = {
    "Hard": 0.04,
    "Normal": 0.08}


screen = t.Screen()
#Asking a user for the game mode they want, on hard mode snake will be faster
game_mode = screen.textinput("Game mode", "Hard or Normal").title()

screen.setup(width=600, height=600)
t.bgpic('slika.png')
screen.title("My Snake Game")

screen.setup(width=600, height=600)
#screen.bgcolor("black")
#adding my own bacground for visuly dividing the screen
t.bgpic('slika.png')
screen.title("Snake game")
screen.tracer(0)

zmijic = Snake()
food = Food()
scoreboard = Scoreboard()

#zmijic = little snake in serbian
zmijic = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(zmijic.up, "Up")
screen.onkey(zmijic.down, "Down")
screen.onkey(zmijic.left, "Left")
screen.onkey(zmijic.right, "Right")

while True:
    screen.update()
    # delay for a sec and then refresh the screen
    time.sleep(GAME_SPEED[game_mode])
    zmijic.move()

    #Detect collision with food.
    for seg in zmijic.segments:
        if seg.distance(food) < 16:
            food.refresh()
            zmijic.extend()
            scoreboard.increase_score()

    #Detect collision with wall.
    if zmijic.head.xcor() > 280 or zmijic.head.xcor() < -280 or zmijic.head.ycor() > 237 or zmijic.head.ycor() < -280:
        scoreboard.reset()
        zmijic.reset()

    #Detect collision with tail.
    for segment in zmijic.segments:
        if segment == zmijic.head:
            pass
        elif zmijic.head.distance(segment) < 10:
            scoreboard.reset()
            zmijic.reset()

screen.exitonclick()
