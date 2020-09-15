import turtle as t
import numpy as np

def circl(a):
    t.speed(0)
    for i in range(120):
        t.forward(a)
        t.left(3)

def circr(a):
    t.speed(0)
    for i in range(120):
        t.forward(a)
        t.right(3)
    

t.shape('turtle')
t.speed(0)
k = int(input())
t.left(90)
for i in range(k):
    circl(5 + i)
    circr(5 + i)
