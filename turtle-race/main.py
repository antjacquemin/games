from random import randint
from turtle import Turtle, Screen, exitonclick

font = ("Courier", 28, "bold")
screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic("img/road.gif")

turtles = []
ypos = [-260, -172, -85, 2, 85, 172, 260]
colors = ["red", "pink", "orange", "yellow", "green", "blue", "purple"]
nbWinners = 0

selectedTurtle = ""
while (not selectedTurtle in colors):
    selectedTurtle = screen.textinput("Choose your turtle", prompt="Select which color: " + ", ".join(colors))

for i in range(7):
    turtle = Turtle("turtle")
    turtle.shapesize(2)
    turtle.speed("fastest")
    turtle.penup()
    turtle.goto(-350, ypos[i])
    turtle.color(colors[i])
    turtles.append(turtle)

race = True
win = False
while race:
    for turtle in turtles:
        turtle.forward(randint(1,10)) #(10) # To test dead heat 
        if turtle.xcor() > 330:
            race = False
            nbWinners += 1
            turtle.write(f"The {turtle.pencolor()} turtle wins! ", align="right", font=font)
            if selectedTurtle == turtle.pencolor():
                win = True

scoreTurtle = Turtle("classic")
scoreTurtle.penup()
scoreTurtle.color("white")
scoreTurtle.goto(-350, 45)
if nbWinners > 1:
    scoreTurtle.write("Dead heat", align="left", font=font)
scoreTurtle.goto(-350, -20)
if win:
    scoreTurtle.write("You WIN", align="left", font=font)
else:
    scoreTurtle.write("You LOSE", align="left", font=font)  

screen.exitonclick()