import turtle
import time
from turtle import *
from numpy import *


turtle.shape("circle")
color('green')
speed(0)
begin_fill()
goto(1000, 0)
goto(1000, -1000)
goto(-1000, -1000)
goto(-1000, 0)
goto(0, 0)
end_fill()
penup()
goto(0, 10)
turtle.shapesize(1, 1, 1)
color('black')
pendown()
x = 0.0
y = 10.0
vx = 0
vy = 50
seconds = 60
pendown()
for tick in range(seconds*20):
    timecheck = time.time() + 1/20
    x += vx/20
    y += vy/20
    if y <= 10:
        y = y - vy/20
        vy = -vy
    else:
        vy += -9.8/20
    goto(x, y)
    while timecheck > time.time():
        pass
done()
