import turtle as t
import numpy as np

def regpol(n, a):
    t.left(90 + 180/n)
    for i in range(n):
        t.forward(a)
        t.left(360/n)
    t.right(90 + 190/n)
    

t.shape('turtle')
t.speed(1)
k = int(input())
t.penup()
t.forward(20)
t.pendown()
for i in range(3, k+1):
    a = 2*(20 + 20*(i-3))*np.sin((np.pi/i))
    regpol(i, a)
    t.penup()
    t.forward(20)
    t.pendown()
