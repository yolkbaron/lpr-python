from turtle import *
from numpy import *

def addnum(num:int):
    if num == 0:
        pendown()
        forward(100)
        right(90)
        forward(50)
        right(90)
        forward(100)
        right(90)
        forward(50)
        penup()
        right(90)
        goto(xcor()+70, ycor())
        pendown()
    if num == 1:
        penup()
        forward(50)
        pendown()
        right(45)
        forward(50*sqrt(2))
        right(135)
        forward(100)
        penup()
        left(180)
        goto(xcor()+20, ycor())
        pendown()
    if num == 2:
        penup()
        forward(100)
        right(90)
        pendown()
        forward(50)
        right(90)
        forward(50)
        right(45)
        forward(50*sqrt(2))
        left(135)
        forward(50)
        penup()
        left(90)
        goto(xcor()+20, ycor())
        pendown()
    if num == 3:
        penup()
        forward(100)
        right(90)
        pendown()
        forward(50)
        right(135)
        forward(50*sqrt(2))
        left(135)
        forward(50)
        right(135)
        forward(50*sqrt(2))
        penup()
        right(135)
        goto(xcor()+70, ycor())
        pendown()
    if num == 4:
        penup()
        forward(100)
        pendown()
        left(180)
        forward(50)
        left(90)
        forward(50)
        left(90)
        forward(50)
        left(180)
        penup()
        forward(50)
        pendown()
        forward(50)
        penup()
        left(180)
        goto(xcor()+20, ycor())
        pendown()
    if num == 5:
        pendown()
        right(90)
        forward(50)
        left(90)
        forward(50)
        left(90)
        forward(50)
        right(90)
        forward(50)
        right(90)
        forward(50)
        penup()
        left(90)
        goto(xcor()+20, ycor()-100)
        pendown()
    if num == 6:
        penup()
        forward(50)
        pendown()
        right(90)
        forward(50)
        right(90)
        forward(50)
        right(90)
        forward(50)
        right(90)
        forward(50)
        right(45)
        forward(50*sqrt(2))
        penup()
        left(45)
        goto(xcor()+20, ycor()-100)
        pendown()
    if num == 7:
        pendown()
        forward(50)
        right(45)
        forward(50*sqrt(2))
        left(135)
        forward(50)
        penup()
        right(90)
        goto(xcor()+70, ycor()-100)
        pendown()
    if num == 8:
        pendown()
        forward(100)
        right(90)
        forward(50)
        right(90)
        forward(50)
        right(90)
        forward(50)
        penup()
        left(90)
        forward(50)
        left(90)
        pendown()
        forward(50)
        left(90)
        forward(50)
        penup()
        goto(xcor()+20, ycor()-50)
        pendown()
    if num == 9:
        pendown()
        right(45)
        forward(50*sqrt(2))
        left(45)
        forward(50)
        left(90)
        forward(50)
        left(90)
        forward(50)
        left(90)
        forward(50)
        penup()
        left(90)
        goto(xcor()+20, ycor()-50)
        pendown()


def drawindex(index:float):
    for num in index:
        addnum(int(num))


shape('turtle')
speed(8)
color('blue','blue')
width(3)
left(90)
index = '141700'
drawindex(index) 
done()
