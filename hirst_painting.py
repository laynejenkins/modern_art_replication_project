# import colorgram

# colors = colorgram.extract("spot_image.jpg", 30)
# rgb_color_list = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     extracted_color = (r, g, b)
#     rgb_color_list.append(extracted_color)

import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

usable_color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32),
                     (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dots in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(usable_color_list))
    timmy.forward(50)

    if dots % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
