import turtle as t
import numpy as np

def halfcircr(a):
    for j in range(45):
        t.forward(a)
        t.right(4)

t.shape('turtle')
t.speed(1)
k = int(input())
t.left(90)
for i in range(k):
    halfcircr(5)
    halfcircr(1)
