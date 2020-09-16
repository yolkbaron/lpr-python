from turtle import *
from random import *

shape('circle')
color('red', 'red')
speed(10)
for i in range(500):
    if randint(0,1):
        left(random()*180)
        forward(random()*50)
    else:
        right(random()*180)
        forward(random()*50)
done()
