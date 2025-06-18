from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 1000,height = 800)
user_guess =screen.textinput(title = "Play the prediction game : ",
                 prompt = "Which turtle will win the race? Enter a color:")
colors = ["red", "Orange","blue", "green", "yellow", "purple"]

y_size = [-200, -120, -40, 40, 120, 200]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-490, y= y_size[turtle_index])
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 465:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_guess:
                print(f"You've won.The {winner_color} Turtle wins!")
            else:
                print(f"You've lost.The {winner_color} Turtle wins!")
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()