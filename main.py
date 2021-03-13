from turtle import Turtle, Screen
import pandas
import turtle

# Here i create my screen and set the background image
my_screen = Screen()
my_screen.tracer(0)
my_screen.title("States in Nigeria")
my_screen.setup(width=580, height=480)
image = "map_of_nigeria.gif"
my_screen.addshape(image)
my_turtle = Turtle()
my_turtle.goto(0, 20)
my_turtle.shape(image)
my_screen.update()

# here i use pandas to format my states csv and bring out a list of states in the csv
states_and_coordinate = pandas.read_csv("36_states.csv")
states_only = states_and_coordinate["state"].to_list()

score = 0
text_question = True
gotten_states = []
learn_states = []
while text_question:
    if score == 0:
        user_input = my_screen.textinput("States in Nigeria", "Guess a state in Nigeria").title()
    else:
        user_input = my_screen.textinput(f"{score}/37 States correct", "Guess a state in Nigeria").title()
    if user_input == "Exit":
        for items in states_only:
            if items not in gotten_states:
                learn_states.append(items)
        learn_states_dataframe = pandas.DataFrame(learn_states)
        learn_states_csv = learn_states_dataframe.to_csv("States_to_learn.csv")
        break
    if user_input in states_only:
        state_row = states_and_coordinate[states_and_coordinate["state"] == user_input]
        xcor = int(state_row["x"])
        ycor = int(state_row["y"])
        writing_turtle = Turtle()
        writing_turtle.penup()
        writing_turtle.hideturtle()
        writing_turtle.color("black")
        writing_turtle.goto(xcor, ycor)
        writing_turtle.write(user_input, False, "left", ("arial", 9, "bold"))
        score += 1
        gotten_states.append(user_input)
    if score == 37:
        finished_turtle = Turtle()
        finished_turtle.penup()
        finished_turtle.hideturtle()
        finished_turtle.color("red")
        finished_turtle.goto(-175, -227)
        finished_turtle.write("CONGRATULATIONS YOU NOW KNOW ALL THE STATES IN NIGERIA", False, "left", ("arial", 9,
                                                                                                        "bold"))
        text_question = False
my_screen.exitonclick()

