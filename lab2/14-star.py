from turtle import *
from numpy import tan, pi


def star(n):
    if n%2 == 1:
        for i in range(n):
            forward(200)
            right(180 - 180/n)
    if n%4 == 2:
        for i in range(n//2):
            forward(200)
            right(180 - 360/n)
        penup()
        goto(200*tan(pi/n), 0)
        pendown()
        for i in range(n//2):
            forward(200)
            left(180 - 360/n)
    elif n%2 == 0:
        for i in range(n):
            forward(200)
            right(180 - 360/n)

left(90)
star(5)
penup()
goto(-200, 0)
pendown()
star(11)
done()
