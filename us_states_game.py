import turtle
import pandas

screen = turtle.Screen()
screen.title('                                                                     U.S.States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
tim = turtle.Turtle()

tim.penup()
tim.hideturtle()


def write_states(name_of_state, x_cord, y_cord):
    tim.goto(x_cord, y_cord)
    tim.write(name_of_state, align='center', font=('Arial', 7, 'normal'))


states = pandas.read_csv('50_states.csv')
state_in_us_list = states.state.to_list()
correct_guess = []
while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f'{len(correct_guess)}/50. Guess the state',
                                    prompt="What's another state name?").title()
    if answer_state in correct_guess:
        pass
    elif answer_state == 'Exit':
        break
    else:
        for state in state_in_us_list:
            if answer_state == state:
                correct_guess.append(answer_state)
                cord = states[states.state == answer_state]
                write_states(answer_state, int(cord.x), int(cord.y))


for state in state_in_us_list:
    if state not in correct_guess:
        print(state)
