import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor('black')

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

colors = ["red", "blue", "lime", "yellow", "cyan", "magenta", "orange", "pink"]

scale = 15
steps = 120
for i in range(steps):
    t.penup()
    t.goto(0, 40)
    angle = i * (2 * math.pi) / steps
    # Parametric heart-like curve (scaled)
    x = 16 * (math.sin(angle) ** 3) * scale
    y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * scale
    c = random.choice(colors)
    t.color(c)
    t.pendown()
    t.goto(x, y)
    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

turtle.done()
