from turtle import Turtle, Screen
import random

t_race = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Enter a color: ")
colors = ["orange", "purple","red", "blue"]
y_pos = [-90, -30, 30, 90]
all_t = []

for t_index in range(0,4):
    new_t = Turtle(shape="turtle")
    new_t.color(colors[t_index])
    new_t.penup()
    new_t.goto(x=-240, y=y_pos[t_index])
    all_t.append(new_t)

if user_bet:
    t_race =True

while t_race:

    for t in all_t:
        if t.xcor() > 230:
            t_race = False
            win_color = t.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} turtle is the winner!")
            else:
                print(f"You've lost! The {win_color} turtle is the winner!")

        rand_dist = random.randint(0, 10)
        t.fd(rand_dist)


screen.mainloop()