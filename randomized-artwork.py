import turtle
from turtle import Turtle, Screen
import random

# import colorgram
# colors = colorgram.extract('image.jpg', 30)
# color_list = []
# for color_number in range(30):
#     color_tuple = colors[color_number]
#     color = tuple(color_tuple.rgb)
#     color_list.append(color)
# print(color_list)

colors = [(34, 108, 167), (223, 229, 235), (245, 77, 36), (112, 163, 211), (153, 57, 85), (219, 156, 94), (201, 60, 27),
 (24, 133, 55), (246, 204, 84), (190, 151, 47), (225, 119, 152), (46, 53, 121), (221, 68, 97), (113, 199, 156),
 (147, 37, 30), (253, 202, 0), (91, 113, 192), (74, 40, 32), (248, 153, 143), (111, 41, 49), (155, 212, 203),
 (53, 174, 163), (38, 31, 67), (154, 210, 219), (43, 33, 45), (35, 55, 46), (99, 93, 2)]


tim = Turtle()
tim.shape("circle")
# tim.pensize(20)
# tim.resizemode("auto")
screen = Screen()
turtle.colormode(255)
circle_color = random.choice(colors)
starting_position = (-250, -250)

def random_color():
    color = (random.choice(colors))
    r = color[0]
    g = color[1]
    b = color[2]
    return (r, g, b)


def new_row(position):
    tim.hideturtle()
    tim.penup()






def run_row(number_circles):
    for _ in range(number_circles):
        tim.color(random_color())
        tim.stamp()
        tim.penup()
        tim.forward(50)



tim.hideturtle()
tim.penup()
tim.goto(starting_position)
run_row(10)


screen.exitonclick()




