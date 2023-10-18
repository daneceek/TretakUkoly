from turtle import Turtle, Screen
import random
tomas = Turtle()
tomas.shape("turtle")
def barva():
    colors = ["red", "blue", "yellow", "green"]
    return random.choice(colors)
def uhel_strana():
    x = ["vpravo", "vlevo"]
    return random.choice(x)
size = 1

while True:
    tomas.color(barva())
    if uhel_strana() == "vpravo":
        tomas.right(90)
        tomas.forward(50)
    else:
        tomas.left(90)
        tomas.forward(50)
    tomas.pensize(size)
    size += 1
    if size > 10:
        size = 10

# for i in range(4):
#     tomas.forward(20)
#     tomas.right(90)
# for i in range(10):
#     tomas.forward(10)
#     tomas.penup()
#     tomas.forward(10)
#     tomas.pendown()
# print(f"šířka : {my_screen.canvwidth}")
# print(f"výška : {my_screen.canvheight}")

trojuhelnik()
ctverec_a_uhly()

my_screen = Screen()
my_screen.bgcolor("white")
my_screen.exitonclick()

