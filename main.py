import turtle as t
import time
import snake as s
import food as f
from scoreboard import Scoreboard
GAME_SPEED = {
    "Hard": 0.04,
    "Normal": 0.08}

screen = t.Screen()
#Asking a user for the game mode they want, on hard mode snake will be faster
game_mode = screen.textinput("Game mode", "Hard or Normal").title()

screen.setup(width=600, height=600)
#screen.bgcolor("black")
#adding my own bacground for visuly dividing the screen
t.bgpic('slika.png')
screen.tracer(0)
score = 0

#zmijic = little snake in serbian
zmijic = s.Snake()
food = f.Food()
scoreboard = Scoreboard(score)

screen.listen()
screen.onkey(zmijic.up, "Up")
screen.onkey(zmijic.down, "Down")
screen.onkey(zmijic.left, "Left")
screen.onkey(zmijic.right, "Right")

game_is_in = True
while game_is_in:
    screen.update()
    # delay for a sec and then refresh the screen
    time.sleep(GAME_SPEED[game_mode])
    zmijic.move_snake()

    #detect collision with food
    if zmijic.head.distance(food) < 16:
        food.refresh()
        score += 1
        zmijic.extend()
        scoreboard.refresh(score)

    #detect collision with wall
    if zmijic.head.xcor() > 280 or zmijic.head.xcor() < -280 or zmijic.head.ycor() > 237 or zmijic.head.ycor() < -280:
        game_is_in = False
        scoreboard.game_over()

    #detect collision with tail
    for segment in zmijic.segments[1:]:
        if zmijic.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
