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
for i in range(k):
    circl(5)
    t.left(360/k)
t.done()
