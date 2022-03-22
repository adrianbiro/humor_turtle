#!/usr/bin/python3
import turtle

ob = turtle.Turtle()
ob.speed(10)
ob.color("black")
ob.goto(0, 0)



while True:
    ob.forward(200)
    ob.left(170)
    for i in range(100):
        if (i % 2) == 0:
            ob.forward(100)
            ob.right(90)
        else:
            ob.forward(i / 2)
            ob.right(i * 2)



turtle.done()
