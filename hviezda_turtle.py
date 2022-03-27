#!/usr/bin/python3
import turtle

hv = turtle.Turtle()
sc = turtle.Screen()
sc.bgcolor("black")
hv.pencolor("red")

a = 0
b = 0
hv.speed(0)
hv.penup()
hv.goto(0, 200)
hv.pendown()
while True:
    hv.forward(a)
    hv.right(b)
    a += 3
    b += 1
    if b == 210:
        break
    hv.hideturtle()
turtle.done()
